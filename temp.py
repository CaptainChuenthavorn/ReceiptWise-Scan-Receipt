from scipy.ndimage import convolve;
import numpy as np
F = np.array(
[[1, 2, 3, 2, 1],
[2,4,8,4,2],
[4,8,16,8,4],
[2,4,8,4,2],
[1,2,3,2,1]],np.int32)
print(F)
W = np.array(
[[2,5,7],
[3,0,4],
[0,1,6]],np.int32)
print(W)

G = convolve(F,W); 
print(G)


# [[1, 2, 3, 2, 1],
# [2,4,8,4,2],
# [4,8,16,8,4],
# [2,4,8,4,2],
# [1,2,3,2,1]]