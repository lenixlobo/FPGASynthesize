#Generate 3 channel gray image
import cv2

image = cv2.imread("card-roading.jpg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_gray = cv2.cvtColor(image_gray, cv2.COLOR_GRAY2BGR)
cv2.imwrite('road_gray_560_356.bmp',image_gray)