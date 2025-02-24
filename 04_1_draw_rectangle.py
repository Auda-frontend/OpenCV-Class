import cv2  # Import OpenCV library

# Read the image 'lena.jpg'
image = cv2.imread('lena.jpg')

# Draw a green rectangle on the image
# Rectangle coordinates: top-left (750, 750), bottom-right (1500, 1500)
# Color: Green (BGR format: (0, 255, 0)), Thickness: 8 pixels

cv2.rectangle(image, (100, 100), (250, 250), (0, 255, 0), 8)

# Display the image in a new window named 'Image'
cv2.imshow('Image', image)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Save the grayscale image to a new file
cv2.imwrite('lena_shapes.jpg', image)

# Close all OpenCV windows to release resources
cv2.destroyAllWindows()