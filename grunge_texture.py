import cv2
import numpy as np

# Load the grunge texture image
texture = cv2.imread("texture.jpg")

# Convert the image to grayscale
texture_gray = cv2.cvtColor(texture, cv2.COLOR_BGR2GRAY)

# Create a mask from the grunge texture image
mask = texture_gray > 128
mask = mask.astype(np.uint8)  # Convert the mask to uint8 data type

# Load the image to be grunged
image = cv2.imread("image.jpg")

image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
  
# Adjust the hue, saturation, and value of the image
# Adjusts the hue by multiplying it by 0.7
image[:, :, 0] = image[:, :, 0] * 0.2
# Adjusts the saturation by multiplying it by 1.5
image[:, :, 1] = image[:, :, 1] * 0.1
# Adjusts the value by multiplying it by 0.5
image[:, :, 2] = image[:, :, 2] * 1
  
# Convert the image back to BGR color space
image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)

# define the alpha and beta
alpha = 0.8 # Contrast control
beta = 5 # Brightness control

# call convertScaleAbs function
image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# Apply the mask to the image
grunge_image = cv2.bitwise_and(image, image, mask=mask)

# Save the grunge image
cv2.imwrite("grunge_image.jpg", grunge_image)