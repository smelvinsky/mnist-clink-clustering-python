_MNIST_IMG_WIDTH = 28
_MNIST_IMG_HEIGHT = 28
_MNIST_NUMBER_OF_MNIST_OBJECTS = 60000


class MnistObject:
    def __init__(self, image, label):
        self.image = image
        self.label = label

    def display(self):
        print("Image:")
        for column in range(0, _MNIST_IMG_HEIGHT):
            for pixel_in_row in range(0, _MNIST_IMG_WIDTH):
                if self.image[pixel_in_row + column * _MNIST_IMG_HEIGHT] == 0:
                    print('.', end='')
                else:
                    print('X', end='')
            print(end="\n")
        print("Label: " + str(self.label), end="\n\n")


def _byte_swap(bytes_to_swap):
    return int.from_bytes(bytes_to_swap, byteorder="big")


def load_training():
    mnist_image_database = open("./mnist/train-images.idx3-ubyte", "rb")
    mnist_image_database.read(16)   # read and discard first 16 bytes from image set

    mnist_label_database = open("./mnist/train-labels.idx1-ubyte", "rb")
    mnist_label_database.read(8)    # read and discard first 8 bytes from label set

    mnist_objects_loaded = 0
    mnist_objects_list = []

    while mnist_objects_loaded < _MNIST_NUMBER_OF_MNIST_OBJECTS:
        image = [0 for pixel in range(0, _MNIST_IMG_WIDTH * _MNIST_IMG_HEIGHT)]
        for pixel in range(0, _MNIST_IMG_WIDTH * _MNIST_IMG_HEIGHT):
            pixel_value = _byte_swap(mnist_image_database.read(1))
            if pixel_value != 0:
                image[pixel] = 1

        label = _byte_swap(mnist_label_database.read(1))

        mnist_objects_list.append(MnistObject(image, label))
        mnist_objects_loaded += 1
        print("\rLoading images: {} out of {}".format(mnist_objects_loaded, _MNIST_NUMBER_OF_MNIST_OBJECTS), end='')
    print(end="\n")

    return mnist_objects_list


