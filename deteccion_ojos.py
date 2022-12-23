import cv2

img = cv2.imread("boy.jpg")

gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces= face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eyes= eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#Definir el objeto de la captura
vid = cv2.VideoCapture(0)

while(True):
    #Capturar el video cadro por cuadro
    ret, frame = vid.read()

    #Convertir en grises
    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #Detectar las caras, los ojos
    faces= face_cascade.detectMultiScale(gray, 1.1, 5)
    
    #Dibujar los rectangulos de la cara y ojos
    eyes= eye_cascade.detectMultiScale(gray, 1.1, 5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y), (x+w, y+h), (255, 0, 0), 2)
    for (x,y,w,h) in eyes:
        cv2.rectangle(frame,(x,y), (x+w, y+h), (255, 0, 0), 2)

    #Mostrar los rectangulos
    cv2.imshow("Fotogramas", frame)

    if cv2.waitKey(25) == 32:
        break

vid.release()

cv2.destroyAllWindows()