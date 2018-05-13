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

