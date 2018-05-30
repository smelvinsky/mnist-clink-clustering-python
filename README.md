# SLINK MNIST clustering

The scope of this project is to develop a **hardware-accelerated application for recognition of handwritten digits**. Chosen target platform for firmware being created is **Zynq-7000 SoC** (by Xillinx).

The application uses a **single-linkage clustering** algorithm to group given image to one of predefined clusters storing reference digit images. Correctness verification included in behavioral model indicates that following approach is **~95% efficient**.

Reference clusters are made based on **MNIST** open-source database. (For more info about MNIST visit
http://yann.lecun.com/exdb/mnist/).

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/MnistExamples.png/220px-MnistExamples.png" width="400">)

## Behavioral model

The behavioral model is a Python application that visualises **the flow of recognition algorithm** and also generates clusters **initialization C code** for ARM processor. This script includes following steps:

1. Load **training set** from **MNIST database** (containing examples of 60 000 unique images).
2. Load **testing set** rom **MNIST database** (10 000 unique images for verification purposes).
3. Create **reference clusters** containing images from training set.
4. Group every image from testing set into one of reference clusters basing on **Euclidian distance between individual pixels** and check the correctness.
5. Generate initialization **C code** for saving previously created reference clusters into ARM processor's memory.

## Run the script

Open your ` terminal ` and ` cd ` into ` mnist-clink-clustering-python ` folder and call:
```shell
$ python3.6 clink_clustering.py
```

The execution of behavioral model correctness checking (**VERY time-consuming**) can be skipped by hitting ` CTRL+C ` (then script will jump directly to C code generation part).

After the script is done, two new files will appear in ` ./c_code ` folder: ` mnist_clusters.c ` and ` mnist_clusters.h `. Even though the size of source files reaches 131 MB, they will be compiled down to ~17 MB (e.g. using gcc). (**Most graphical text editors cannot handle files that large so it is recommended to open them with text-mode editors e.g. vim**).

## Compile and run the C code

The ` main.c ` file is provided as an example of generated C code usage. To compile the code follow the directions below:

If you haven't installed **cmake** yet type in ` terminal `:
```shell
$ sudo apt-get install cmake
```
Then, `` cd `` into `` /mnist-clink-clustering-python/c_code `` directory ( this one including  `` CMakeLists.txt `` file ) and run `cmake` to generate ` Makefile `:

```shell
$ cmake CMakeLists.txt
```
After that compile the program with:

```shell
$ make
```

Program can be executed by calling:


```shell
$ ./c_code
```
This program, as an example loads all reference clusters into memory (billion times faster than python) and prints out **all 5421 images of digit 5 stored in reference cluster no.5 : )** 
