import cv2

# Read image
img = cv2.imread("rec.png")

# Check if image loaded
if img is None:
    print("Image not found")
    exit()

# -------- Rectangle 1 (First Person) --------
x1, y1, w1, h1 = 120, 80, 200, 250
cv2.rectangle(img, (x1, y1), (x1+w1, y1+h1), (255, 0, 0), 2)

roi1 = img[y1:y1+h1, x1:x1+w1]

# -------- Rectangle 2 (Second Person) --------
x2, y2, w2, h2 = 350, 80, 200, 250
cv2.rectangle(img, (x2, y2), (x2+w2, y2+h2), (255, 0, 0), 2)

roi2 = img[y2:y2+h2, x2:x2+w2]

# Show results
cv2.imshow("Image with Rectangles", img)
cv2.imshow("Extracted Object 1", roi1)
cv2.imshow("Extracted Object 2", roi2)

cv2.waitKey(0)
cv2.destroyAllWindows()
