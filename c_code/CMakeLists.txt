cmake_minimum_required(VERSION 3.10)
project(c_code C)

set(CMAKE_C_STANDARD 99)

add_executable(c_code main.c uint28_t.h mnist_clusters.h mnist_clusters.c)