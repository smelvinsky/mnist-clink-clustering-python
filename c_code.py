import os
import mnist
from cluster import MnistCluster
from mnist import MnistObject

_C_CODE_FILENAME = "mnist_clusters"


class _CCodeFile:
    """
    Class representing a C file source
    """
    def __init__(self, filename: str, file_type: str):
        self.filename = filename
        if file_type == "header":
            self.file_handle = open("./c_code/" + filename + ".h", mode='x')
        elif file_type == "source":
            self.file_handle = open("./c_code/" + filename + ".c", mode='x')

    def add_include(self, lib_name: str):
        self.file_handle.write("#include \"" + lib_name + ".h\"\n")

    def write(self, string: str):
        self.file_handle.write(string)

    def add_line_comment(self, comment: str):
        self.file_handle.write("// " + comment)


class _CStructMember:
    """
    Class representing a struct member in C
    """
    def __init__(self, data_type: str, member_name: str, initial_value: str = None):
        self.data_type: str = data_type
        self.member_name = member_name
        self.value = initial_value
        if self.value is None:
            self.initialized = False
        else:
            self.initialized = True

    def get_data_type(self):
        return self.data_type

    def get_member_name(self):
        return self.member_name

    def get_value(self):
        return self.value

    def is_initialized(self):
        return self.initialized


class _CStruct:
    """
    Class representing a struct in C
    """
    def __init__(self, name: str):
        self.members = []
        self.name = name
        self.num_of_numbers = 0

    def add_member(self, new_member: _CStructMember):
        self.members.append(new_member)
        self.num_of_numbers += 1

    def generate_code(self):
        code = "\ntypedef struct " + self.name + " \n{"
        for member in range(self.num_of_numbers):
            c_struct_member_tmp: _CStructMember = self.members[member]
            code += "\n\t" + c_struct_member_tmp.get_data_type() + " "
            code += c_struct_member_tmp.get_member_name()
            if c_struct_member_tmp.is_initialized():
                code += " = " + c_struct_member_tmp.get_value() + ";"
            else:
                code += ";"
        code += "\n} " + self.name + "_t;\n"
        return code

    def display(self):
        print("C structure code:\n=================================\n"
              + self.generate_code()
              + "\n=================================\n")

    def get_name(self):
        return self.name + "_t"

    def get_num_of_members(self):
        return self.num_of_numbers

    def get_member(self, index: int):
        return self.members[index]


def _generate_code_for_cluster(cluster: MnistCluster, cluster_label: int):
    """
    Generates C initialization code of given MnistCluster
    :param cluster: MnistCluster of which initialization code is being created
    :param cluster_label: label of every MnistObject stored in given MnistCluster
    :return: string containing initialization code
    """
    instance_name = "cluster_" + str(cluster_label)
    num_of_mnist_objects = cluster.get_num_of_objects()
    print("Generating code for cluster (" + instance_name + ") containing " + str(num_of_mnist_objects)
          + " MNIST objects...")

    code = "static void init_" + instance_name + "()\n{\n"
    code += "\t" + instance_name + ".num_of_objects = " + str(num_of_mnist_objects) + ";\n"

    for object_number in range(0, cluster.get_num_of_objects()):
        mnist_obj_tmp: MnistObject = cluster.get_object(object_number)
        code += "\n\t" + instance_name + "_mnist_objects[" + str(object_number) + "].label = " + str(cluster_label) \
                + ";\n"
        for pixel_column in range(0, mnist._MNIST_IMG_HEIGHT):
            code += "\tUINT28_SET(" + instance_name + "_mnist_objects[" + str(object_number) + "].image[" + str(pixel_column) \
                    + "], (uint32_t) "
            image_row = 0
            for pixel_row in range(0, mnist._MNIST_IMG_WIDTH):
                if mnist_obj_tmp.get_image()[pixel_row + pixel_column * mnist._MNIST_IMG_HEIGHT] == 1:
                    image_row = image_row | (1 << pixel_row)
            code += "0x" + format(image_row, '08X') + ");\n"

    code += "\n\t" + instance_name + ".mnist_objects = " + instance_name + "_mnist_objects;\n}\n"

    return code


def generate(clusters):
    """
    Generates C initialization code based on given clusters
    :param clusters: array of clusters to generate code from
    :return: None
    """
    print("Generating C code for " + str(len(clusters)) + " clusters:")

    # delete files if exist
    c_header_filename = "./c_code/" + _C_CODE_FILENAME + ".h"
    if os.path.isfile(c_header_filename):
        print("Removing " + c_header_filename + " file...")
        os.remove(c_header_filename)
    c_source_filename = "./c_code/" + _C_CODE_FILENAME + ".c"
    if os.path.isfile(c_source_filename):
        print("Removing " + c_source_filename + " file...")
        os.remove(c_source_filename)

    # generate header file
    c_header = _CCodeFile(_C_CODE_FILENAME, "header")

    mnist_object_c_struct = _CStruct("mnist_object")
    mnist_object_c_struct.add_member(_CStructMember("uint28_t", "image[" + str(28) + "]", None))
    mnist_object_c_struct.add_member(_CStructMember("uint8_t", "label", None))

    cluster_c_struct = _CStruct("cluster")
    cluster_c_struct.add_member(_CStructMember(mnist_object_c_struct.get_name() + "*", "mnist_objects", None))
    cluster_c_struct.add_member(_CStructMember("uint32_t", "num_of_objects", None))

    reference_cluster_c_struct = _CStruct("reference_cluster")
    reference_cluster_c_struct.add_member(_CStructMember(cluster_c_struct.get_name() + "*", "cluster", None))
    reference_cluster_c_struct.add_member(_CStructMember("uint8_t", "label", None))

    c_header.add_include("stdint")
    c_header.add_include("uint28_t")
    c_header.write(mnist_object_c_struct.generate_code())
    c_header.write(cluster_c_struct.generate_code())
    c_header.write(reference_cluster_c_struct.generate_code())

    # generate source file
    c_source = _CCodeFile(_C_CODE_FILENAME, "source")
    c_source.add_include(_C_CODE_FILENAME)
    c_source.add_include("uint28_t")
    c_source.write("\n")

    c_source.add_line_comment("array storing 10 reference clusters\n")
    c_source.write(reference_cluster_c_struct.get_name()
                   + " reference_clusters[10];\n\n")  # add array of reference clusters

    c_source.add_line_comment(str(len(clusters)) + " initial clusters:\n")
    for cluster_num in clusters:
        c_source.write("static " + cluster_c_struct.get_name() + " cluster_" + str(cluster_num) + ";\n")
        cluster_tmp: MnistCluster = clusters[cluster_num]
        code = "static " + mnist_object_c_struct.get_name() + " cluster_" + str(cluster_num) + "_mnist_objects["
        code += str(cluster_tmp.get_num_of_objects()) + "];\n\n"
        c_source.write(code)

    for cluster_num in clusters:
        c_source.write(_generate_code_for_cluster(clusters[cluster_num], cluster_num) + "\n\n")

    c_source.add_line_comment("initialize all clusters\n")
    init_all_clusters_code = "void init_clusters()\n{\n"
    for cluster_num in clusters:
        init_all_clusters_code += "\treference_clusters[" + str(cluster_num) + "].label = " + str(cluster_num) + ";\n"

    init_all_clusters_code += "\n"
    for cluster_num in clusters:
        init_all_clusters_code += "\tinit_cluster_" + str(cluster_num) + "();\n"

    init_all_clusters_code += "\n"
    for cluster_num in clusters:
        init_all_clusters_code += "\treference_clusters[" + str(cluster_num) + "].cluster = &cluster_" \
                                  + str(cluster_num) + ";\n"

    init_all_clusters_code += "}\n"

    c_source.write(init_all_clusters_code)
    c_header.write("\nvoid init_clusters(void);\n")
