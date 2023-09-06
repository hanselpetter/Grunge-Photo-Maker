import cv2
import numpy as np

# Load the image
image = cv2.imread('image1.jpeg')

# conversion code
# image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Convert the image from BGR to HSV color space
image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
  
# Adjust the hue, saturation, and value of the image
# Adjusts the hue by multiplying it by 0.7
image[:, :, 0] = image[:, :, 0] * 1
# Adjusts the saturation by multiplying it by 1.5
image[:, :, 1] = image[:, :, 1] * 0.5
# Adjusts the value by multiplying it by 0.5
image[:, :, 2] = image[:, :, 2] * 1
  
# Convert the image back to BGR color space
image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)

# define the alpha and beta
alpha = 0.5 # Contrast control
beta = -8 # Brightness control

# call convertScaleAbs function
image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)


# Generate random Gaussian noise
mean = 0
stddev = 20
noise = np.zeros(image.shape, np.uint8)
cv2.randn(noise, mean, stddev)

# Add noise to image
image = cv2.add(image, noise)


# Apply a blur to the image
image = cv2.blur(image, (6, 3))


# Convert the image back to the RGB color space
# image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)

cv2.imshow("image", image)

# Save the image
cv2.imwrite("grunge_image.jpeg", image)
cv2.waitKey(0)
cv2.destroyAllWindows()