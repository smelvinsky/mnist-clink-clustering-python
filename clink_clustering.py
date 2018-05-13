import mnist

# load mnist database
mnist_data = mnist.load_training()

# show all mnist images
for image in range(0, len(mnist_data)):
    mnist_data[image].display()


