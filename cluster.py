import mnist
from mnist import MnistObject


class MnistCluster:
    """
    Class which enables creating clusters using class MnistObject.
    """
    def __init__(self):
        self.__mnist_objects_list = []
        self.__number_of_objects = 0

    def add_object(self, mnist_object: MnistObject):
        self.__mnist_objects_list.append(mnist_object)
        self.__number_of_objects += 1

    def display(self):
        for mnist_object in range(0, self.__number_of_objects):
            mnist_object_tmp: MnistObject = self.__mnist_objects_list[mnist_object]
            mnist_object_tmp.display()

    def get_num_of_objects(self):
        return self.__number_of_objects

    def get_object(self, index):
        return self.__mnist_objects_list[index]


def merge_clusters(cluster_1: MnistCluster, cluster_2: MnistCluster):
    """
    Merging clusters.
    :param cluster_1: Cluster to merge.
    :param cluster_2: Cluster to merge.
    :return: Merged clusters.
    """
    output_cluster = MnistCluster()
    for i in range(0, cluster_1.number_of_objects):
        output_cluster.add_object(cluster_1.get_object(i))
    for i in range(0, cluster_2.number_of_objects):
        output_cluster.add_object(cluster_2.get_object(i))
    return output_cluster


def get_distance(cluster_1: MnistCluster, cluster_2: MnistCluster):
    """
    Function which calculates distance between two clusters.
    :param cluster_1: One of two clusters to calculate distance.
    :param cluster_2: One of two clusters to calculate distance.
    :return: Calculated distance.
    """
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
    :param mnist_data: database with training, labaled images
    :return: dictionary of 10 sorted clusters
    """
    reference_clusters = {i: MnistCluster() for i in range(10)}

    for i in mnist_data:
            reference_clusters[i.label].add_object(i)

    return reference_clusters


def recognize_cluster(reference_clusters, test_cluster: MnistCluster):
    """
    Recognizing to which cluster of reference clusters test_clusters suits the best.
    :param reference_clusters: Trained clusters.
    :param test_cluster:
    :return:
    """
    results = [get_distance(reference, test_cluster) for reference in reference_clusters.values()]
    print(results)
    return list(index for index, value in enumerate(results) if value == min(results))
