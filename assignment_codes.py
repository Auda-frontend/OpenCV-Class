import cv2
# Read and store the assignment-001-given.jpg into the image variable
image = cv2.imread("assignment-001-given.jpg")
# Make a copy of the image 
background_label = image.copy()
# Draw a rectangle to the backgroung_label
cv2.rectangle(background_label, (800,80), (1260, 190), (0,0,0), -1)
# Blend image and background_label with same weights with the light changed on a -1 scale
blended_image = cv2.addWeighted(background_label, 0.5, image, 0.5, 0
#Draw a rectangle on the new blended image 
cv2.rectangle(blended_image, (260, 190), (995, 925), (0, 255, 0), 5)
# Adding text in this case plate number to the blended image
cv2.putText(blended_image, 'RAH972U', (820,170), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 7)
# Displaying the final image with a title of Assignment image
cv2.imshow("Assignment_image", blended_image)
# The image continues to display as long as no key is pressed 
cv2.waitKey(0)
# The image will be then saved to the assignment_result.jpg
cv2.imwrite("assignment_result.jpg", blended_image)
# All windows will then be closed when any key is pressed
cv2.destroyAllWindows()
