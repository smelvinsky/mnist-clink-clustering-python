from cluster import MnistCluster
from mnist import MnistObject


class _CCodeFile:
    def __init__(self, filename: str, file_type: str):
        self.filename = filename
        if file_type == "header":
            self.file_handle = open(filename + str(".h"), mode='x')
        elif file_type == "source":
            self.file_handle = open(filename + str(".c"), mode='x')

    def add_include(self, lib_name: str):
        self.file_handle.write("#include \"" + lib_name + ".h\"\n")

    def write(self, string: str):
        self.file_handle.write(string)


class _CStructMember:
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
            code += "\n\t" + c_struct_member_tmp.get_data_type() + "\t"
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


class _CFunction:
    def __init__(self, data_type: str, name: str, code: str):
        self.data_type = data_type
        self.name = name
        self.code = code
        self.arguments = []

    def add_argument(self, argument: str, argument_data_type: str):
        self.arguments.append({"argument": argument, "argument_data_type": argument_data_type})

    def generate_code(self):
        num_of_args = len(self.arguments)
        code = self.data_type + " " + self.name + "("
        for arg_num in range(0, num_of_args):
            code += self.arguments[arg_num]["argument_data_type"] + " " + self.arguments[arg_num]["argument"]
            if arg_num != 0 and arg_num != num_of_args - 1:
                code += ", "
        code += ")\n{\n" + self.code + "\n}\n"
        return code

    def display(self):
        print("C function code:\n=================================\n"
              + self.generate_code()
              + "\n=================================\n")


def generate(clusters):
    print("Generating C code for " + str(len(clusters)) + " clusters...")

    # header file
    c_header = _CCodeFile("reference_clusters", "header")

    mnist_object_c_struct = _CStruct("mnist_object")
    mnist_object_c_struct.add_member(_CStructMember("uint8_t", "image[" + str(28*28) + "]", None))
    mnist_object_c_struct.add_member(_CStructMember("uint8_t", "label", None))

    cluster_c_struct = _CStruct("cluster")
    cluster_c_struct.add_member(_CStructMember(mnist_object_c_struct.get_name() + "*", "mnist_objects", None))
    cluster_c_struct.add_member(_CStructMember("uint8_t", "num_of_objects", None))

    c_header.add_include("stdint")
    c_header.write(mnist_object_c_struct.generate_code())
    c_header.write(cluster_c_struct.generate_code())

    # source file
    c_source = _CCodeFile("reference_clusters", "source")
    c_source.add_include("reference_clusters")
    c_source.write("\n" + cluster_c_struct.get_name() + " reference_clusters" + "[" + str(len(clusters)) + "];\n\n")

    for cluster_num in range(0, len(clusters)):
        cluster_tmp: MnistCluster = clusters[cluster_num]
        for mnist_object_num in range(0, cluster_tmp.get_num_of_objects()):
            mnist_object_tmp: MnistObject = cluster_tmp.get_object(mnist_object_num)
            mnist_object_name = "cluster_" + str(cluster_num) + "_object_" + str(mnist_object_num)
            c_source.write(mnist_object_c_struct.get_name() + " " + mnist_object_name + ";\n")
            c_source.write(mnist_object_name + ".label = " + str(mnist_object_tmp.get_label()) + ";\n")
            for pixel_num in range(0, 28*28):
                c_source.write(mnist_object_name + ".image[" + str(pixel_num) + "] = "
                               + str(mnist_object_tmp.get_image()[pixel_num]) + ";\n")

