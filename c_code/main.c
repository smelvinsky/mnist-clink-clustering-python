#include "stdio.h"
#include "stdint.h"
#include "uint28_t.h"
#include "mnist_clusters.h"

extern reference_cluster_t reference_clusters[10]; // in reference_clusters.c

void display_mnist_image(mnist_object_t mnist_object)
{
    printf("Image:\n");
    for (int column = 0; column < 28; column++)
    {
        for (int row = 0; row < 28; row++)
        {
            if ((mnist_object.image[column] & (1UL << (unsigned) row)) == 0)
            {
                printf(".");
            }
            else
            {
                printf("X");
            }
        }
        printf("\n");
    }
    printf("Label: %u\n\n", mnist_object.label);
}

int main()
{
    printf("Initializing reference clusters...");
    init_clusters();

    // display all images from reference cluster no.5
    for (int mnist_obj = 0; mnist_obj < reference_clusters[5].cluster->num_of_objects; mnist_obj++)
    {
        display_mnist_image(reference_clusters[5].cluster->mnist_objects[mnist_obj]);
    }

    return 0;
}