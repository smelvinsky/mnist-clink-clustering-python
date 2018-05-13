import mnist
import cluster

# load mnist database
mnist_data = mnist.load_training()

# show all mnist images - uncomment if you got too much time
# for i in range(0, len(mnist_data)):
#    mnist_data[i].display()

# add 2 first objects to the new cluster
mnist_cluster_1 = cluster.MnistCluster()
for i in range(0, 2):
    mnist_cluster_1.add_object(mnist_data[i])
print("Cluster 1")
mnist_cluster_1.display()

# add 3 first objects to the new cluster
mnist_cluster_2 = cluster.MnistCluster()
for i in range(2, 5):
    mnist_cluster_2.add_object(mnist_data[i])
print("Cluster 2")
mnist_cluster_2.display()

# merge clusters
merged_cluster = cluster.merge_clusters(mnist_cluster_1, mnist_cluster_2)
print("Merged Cluster")
merged_cluster.display()

# calculate distance between two first mnist images
print("Calculated distance between two first mnist images: " + str(mnist.get_distance(mnist_data[0], mnist_data[2])))

# calculate distance between two clusters created before
print("Calculated distance between two clusters: " + str(cluster.get_distance(mnist_cluster_1, mnist_cluster_2)))
