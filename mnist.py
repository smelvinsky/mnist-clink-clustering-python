import math

_MNIST_IMG_WIDTH = 28
_MNIST_IMG_HEIGHT = 28
_MNIST_NUMBER_OF_TRAINING_MNIST_OBJECTS = 60000
_MNIST_NUMBER_OF_TESTING_MNIST_OBJECTS = 10000


class MnistObject:
    """
    Class of Mnist image which consists of image and label.
    """
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
        print("Label: " + str(self.label), end="\n\n", flush=True)


def _byte_swap(bytes_to_swap):
    return int.from_bytes(bytes_to_swap, byteorder="big")


def load_images(image_path, label_path, number_of_objects):
    """
    Loads mnist images.
    :param image_path: Path where images are.
    :param label_path: Path where corresponding labels are.
    :param number_of_objects: Number of images to load.
    :return: List of MnistObjects.
    """
    mnist_image_database = open(image_path, "rb")
    mnist_image_database.read(16)   # read and discard first 16 bytes from image set

    mnist_label_database = open(label_path, "rb")
    mnist_label_database.read(8)    # read and discard first 8 bytes from label set

    mnist_objects_loaded = 0
    mnist_objects_list = []

    while mnist_objects_loaded < number_of_objects:
        image = [0 for pixel in range(0, _MNIST_IMG_WIDTH * _MNIST_IMG_HEIGHT)]
        for pixel in range(0, _MNIST_IMG_WIDTH * _MNIST_IMG_HEIGHT):
            pixel_value = _byte_swap(mnist_image_database.read(1))
            if pixel_value != 0:
                image[pixel] = 1

        label = _byte_swap(mnist_label_database.read(1))

        mnist_objects_list.append(MnistObject(image, label))
        mnist_objects_loaded += 1
        print("\rLoading images: {} out of {}".format(mnist_objects_loaded, number_of_objects), end='')
    print(end="\n", flush=True)

    return mnist_objects_list


def get_distance(mnist_object_1: MnistObject, mnist_object_2: MnistObject):
    """
    Distance between MnistObjects.
    """
    distance = 0.0
    for i in range(0, _MNIST_IMG_WIDTH * _MNIST_IMG_HEIGHT):
        distance = distance + math.pow(mnist_object_1.image[i] - mnist_object_2.image[i], 2.0)
    return math.sqrt(distance)
