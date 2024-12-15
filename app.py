import cv2
import sys

def detect_faces(image_path):

    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to load image at {image_path}")
        return

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Отрисовка прямоугольников
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.namedWindow("Faces Detected", cv2.WINDOW_NORMAL)
    cv2.imshow("Faces Detected", image)
    cv2.resizeWindow("Faces Detected", 800, 600)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Аргументы
    image_path = sys.argv[1] if len(sys.argv) > 1 else "default.jpg"
    detect_faces(image_path)
