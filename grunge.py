import cv2
import numpy as np

# Load the image
image = cv2.imread('image1.jpeg')

# conversion code
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# define the alpha and beta
alpha = 0.5 # Contrast control
beta = -8 # Brightness control

# call convertScaleAbs function
image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)


# Generate random Gaussian noise
mean = 10
stddev = 20
noise = np.zeros(image.shape, np.uint8)
cv2.randn(noise, mean, stddev)

# Add noise to image
image = cv2.add(image, noise)


# Apply a blur to the image
image = cv2.blur(image, (6, 3))


# Convert the image back to the RGB color space
image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

cv2.imshow("image", image)

# Save the image
cv2.imwrite("grunge_image.jpeg", image)
cv2.waitKey(0)
cv2.destroyAllWindows()