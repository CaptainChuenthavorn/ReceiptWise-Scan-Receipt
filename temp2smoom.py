import numpy as np

Input = np.array(
                   [[0, 0, 0, 0, 0],
                   [0, 2, 5, 7, 0],
                   [0, 3, 0, 4, 0],
                   [0, 0, 1, 6, 0],
                   [0, 0, 0, 0, 0]],np.int32)

Kernal = np.array(
           [[1, 2, 3, 2, 1],
    [2,4,8,4,2],
    [4,8,16,8,4],
    [2,4,8,4,2],
    [1,2,3,2,1]],np.int32)

# Get the dimensions of the input image and the kernel
Input_height, Input_width = Input.shape
Kernal_height, Kernal_width = Kernal.shape

# Calculate the output dimensions
Result_height = Input_height - Kernal_height + 1
Result_width = Input_width - Kernal_width + 1

# Initialize the output array
Result = np.zeros((Result_height, Result_width), dtype=np.int32)

# Perform convolution manually
for i in range(Result_height):
    for j in range(Result_width):
        Result[i, j] = np.sum(Input[i:i+Kernal_height, j:j+Kernal_width] * Kernal)
print("Smoothing")
print("Input\n",Input)
print("     x")
print("Kernal\n",Kernal)
print("     =")

print("Result\n",Result)
