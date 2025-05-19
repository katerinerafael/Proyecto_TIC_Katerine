import cv2

# Cargar el clasificador de rostros de OpenCV (Haar Cascade)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Iniciar la cámara (0 = webcam por defecto)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ No se pudo abrir la cámara.")
    exit()

print("📷 Presiona 'q' para salir...")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ No se pudo capturar el frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convertir a escala de grises
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # Detección de caras

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
