import cv2
from PIL import Image

# Pfad des Bildes speichern
image_path = "cat.jpg"

# Gesichtserkennung laden
cat_face_cascade = cv2.CascadeClassifier("haarcascade_frontalcatface_extended.xml")

# Bild mit OpenCV laden
image = cv2.imread(image_path)

# Katzengesicht erkennen
cat_face = cat_face_cascade.detectMultiScale(image)

# Bilder mit Pillow öffnen
cat = Image.open(image_path)
glasses = Image.open("sun-glasses.png")

# Transparenz aktivieren
cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")

# Für jedes gefundene Gesicht Brille Anpassen und aufsetzten
for (x, y, w, h) in cat_face:
    resized_glasses = glasses.resize((w, int(h / 3)))
    cat.paste(resized_glasses, (x, int(y / 4)), resized_glasses)

# Ergebnis speichern
cat.save("cat_with_glasses.png")

# Ergebnis mit OpenCV anzeigen
cat_with_glasses = cv2.imread("cat_with_glasses.png")
cv2.imshow("cool cat", cat_with_glasses)
cv2.waitKey()