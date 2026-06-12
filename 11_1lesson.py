import cv2

#Pfad des Bildes
image_path = "cat.jpg"

#Das Bild als Objekt speichern
image = cv2.imread(image_path)

cv2.imshow("cat", image)

cv2.waitKey()

#Erkennungsprofil einbinden
cat_face_cascade = cv2.CascadeClassifier("haarcascade_frontalcatface_extended.xml")

