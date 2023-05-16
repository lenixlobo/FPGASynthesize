import numpy as np
from PIL import Image

# Load the image
b = np.array(Image.open('curved-lane.jpg'))

# The image is processed from the last row to the first
a = np.zeros((b.shape[0] * b.shape[1] * 3,), dtype=np.uint8)
k = 0
for i in range(b.shape[0]-1, -1, -1):
    for j in range(b.shape[1]):
        a[k] = b[i, j, 0]
        a[k+1] = b[i, j, 1]
        a[k+2] = b[i, j, 2]
        k += 3

# Save the output hex file
with open('road_hex_gray_1280_720.hex', 'w') as f:
    for val in a:
        f.write('{:02x}\n'.format(val))

print('Hex file successfully created.\n')