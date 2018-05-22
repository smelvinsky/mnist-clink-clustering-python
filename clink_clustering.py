import mnist
import cluster
import c_code

# load mnist database
image_path = "./mnist_images/train-images.idx3-ubyte"
label_path = "./mnist_images/train-labels.idx1-ubyte"
number_of_objects = mnist._MNIST_NUMBER_OF_TRAINING_MNIST_OBJECTS
mnist_data = mnist.load_images(image_path, label_path, number_of_objects)


# show all mnist images - uncomment if you got too much time
# for i in range(0, len(mnist_data)):
#    mnist_data[i].display()

# add 2 first objects to the new cluster
# mnist_cluster_1 = cluster.MnistCluster()
# for i in range(0, 2):
#     mnist_cluster_1.add_object(mnist_data[i])
# print("Cluster 1")
# mnist_cluster_1.display()
#
# # add 3 first objects to the new cluster
# mnist_cluster_2 = cluster.MnistCluster()
# for i in range(2, 5):
#     mnist_cluster_2.add_object(mnist_data[i])
# print("Cluster 2")
# mnist_cluster_2.display()
#
# # merge clusters
# merged_cluster = cluster.merge_clusters(mnist_cluster_1, mnist_cluster_2)
# print("Merged Cluster")
# merged_cluster.display()
#
# # calculate distance between two first mnist images
# print("Calculated distance between two first mnist images: " + str(mnist.get_distance(mnist_data[0], mnist_data[2])))
#
# # calculate distance between two clusters created before
# print("Calculated distance between two clusters: " + str(cluster.get_distance(mnist_cluster_1, mnist_cluster_2)))

image_path = "./mnist_images/t10k-images.idx3-ubyte"
label_path = "./mnist_images/t10k-labels.idx1-ubyte"
number_of_objects = mnist._MNIST_NUMBER_OF_TESTING_MNIST_OBJECTS
test_data = mnist.load_images(image_path, label_path, number_of_objects)
reference = cluster.create_clusters(mnist_data)
c_code.generate(reference)

# score = 0
# maximum = 100
# for i in range(maximum):
#     print(i)
#     to_recognition = cluster.MnistCluster()
#     to_recognition.add_object(test_data[i])
#     recognition = cluster.recognize_cluster(reference, to_recognition)
#     # to_recognition.display()
#     # print("recognized: ", recognition)
#     if int(recognition[0]) == to_recognition.get_object(0).label:
#         score += 1
#     print("{} of {} tested".format(score/(i+1), i+1))



