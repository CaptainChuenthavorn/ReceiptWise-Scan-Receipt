original = [[2, 5, 7],
            [3, 0, 4],
            [0, 1, 6]]
unsharp = [[0, 0, -1, 0, 0],
           [0, -1, -2, -1, 0],
           [-1, -2, 17, -2, -1],
           [0, -1, -2, -1, 0],
           [0, 0, -1, 0, 0]]
padded_original = [[0, 0, 0, 0, 0],
                   [0, 2, 5, 7, 0],
                   [0, 3, 0, 4, 0],
                   [0, 0, 1, 6, 0],
                   [0, 0, 0, 0, 0]]
result = [[0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0]]

# Original x unsharp
for i in range(2, 7):
    for j in range(2, 7):
        # Convolution operation
        convolution_sum = 0
        for m in range(-2, 3):
            for n in range(-2, 3):
                convolution_sum += padded_original[i + m][j + n] * unsharp[m + 2][n + 2]
        result[i - 2][j - 2] = convolution_sum

# blurred
result = [[-4, -10, -9, -7, 0],
          [-4, -11, -17, -14, 0],
          [-6, -16, 25, -16, -6],
          [0, -7, -17, -10, -4],
          [0, 0, -7, -4, -4]]

# output_image = orignal + (original - blurred)
output_image = [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]
for i in range(5):
    for j in range(5):
        output_image[i][j] = original[i][j] + result[i][j]

# The final output image
output_image = [[-2, -5, -2, 0, 0],
                [-1, -11, -17, -10, 0],
                [-6, -15, 25, -16, -6],
                [0, -6, -16, -4, -4],
                [0, 0, -1, 0, 0]]
