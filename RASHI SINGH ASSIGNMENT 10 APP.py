
import numpy as np


# 1. Create a one-dimensional NumPy array
def create_array_from_list():
    return np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def create_array_with_arange():
    return np.arange(1, 11)


# 2. Display array properties
def describe_array(arr):
    print(f"Array            : {arr}")
    print(f"Data type (dtype): {arr.dtype}")
    print(f"Shape            : {arr.shape}")
    print(f"Number of dims   : {arr.ndim}")
    print(f"Size (elements)  : {arr.size}")


# 3. Main program
def main():
    arr1 = create_array_from_list()

    print("Array created using np.array():")
    describe_array(arr1)

    print()

    arr2 = create_array_with_arange()

    print("Array created using np.arange():")
    describe_array(arr2)

    print()

    print("Are both arrays equal?", np.array_equal(arr1, arr2))

    print("\nVectorized operations:")
    print("arr1 * 2       :", arr1 * 2)
    print("arr1 + 100     :", arr1 + 100)
    print("Sum            :", arr1.sum())
    print("Mean           :", arr1.mean())

    print("\nIndexing and slicing:")
    print("First element  :", arr1[0])
    print("Last element   :", arr1[-1])
    print("First 5 values :", arr1[:5])
    print("Every other    :", arr1[::2])


if __name__ == "__main__":
    main()
