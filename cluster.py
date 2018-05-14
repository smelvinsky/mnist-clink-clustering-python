import mnist
from mnist import MnistObject


class MnistCluster:
    def __init__(self):
        self.__mnist_objects_list = []
        self.number_of_objects = 0

    def add_object(self, mnist_object: MnistObject):
        self.__mnist_objects_list.append(mnist_object)
        self.number_of_objects += 1

    def display(self):
        for mnist_object in range(0, self.number_of_objects):
            mnist_object_tmp: MnistObject = self.__mnist_objects_list[mnist_object]
            mnist_object_tmp.display()

    def get_object(self, index):
        return self.__mnist_objects_list[index]


def merge_clusters(cluster_1: MnistCluster, cluster_2: MnistCluster):
    output_cluster = MnistCluster()
    for i in range(0, cluster_1.number_of_objects):
        output_cluster.add_object(cluster_1.get_object(i))
    for i in range(0, cluster_2.number_of_objects):
        output_cluster.add_object(cluster_2.get_object(i))
    return output_cluster


def get_distance(cluster_1: MnistCluster, cluster_2: MnistCluster):
    max_distance = 0.0
    for o in range(0, cluster_1.number_of_objects):
        for i in range(0, cluster_2.number_of_objects):
            distance = mnist.get_distance(cluster_1.get_object(o), cluster_2.get_object(i))
            if distance > max_distance:
                max_distance = distance
    return max_distance


def create_clusters(mnist_data):
    """
    Function which creates sorted and trained clusters.
    :param mnist_data:
    :return:
    """
    reference_clusters = {i: MnistCluster() for i in range(10)}

    for i in mnist_data:
            reference_clusters[i.label].add_object(i)

    return reference_clusters


def recognize_cluster(reference_clusters, test_cluster: MnistCluster):

    results = [get_distance(reference, test_cluster) for reference in reference_clusters.values()]
    return list(index for index, value in enumerate(results) if value == min(results))
