import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("WGTA.jpg")
#convert img to a grayscale img so that the accuracy increases
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#detect the coordinates of the face(search for the cascade classifier)
faces = face_cascade.detectMultiScale(gray_image,
scaleFactor = 1.05,
minNeighbors = 10)

for x, y, height, width in faces:
    #3 for the width of the rectangle
    img = cv2.rectangle(img, (x, y), (x+width, y+height), (0, 255, 0), 3)

resized_img = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))

cv2.imshow("Face Detection", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows