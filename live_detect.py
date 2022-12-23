# Importar la biblioteca OpenCV
import cv2

# Definir un objeto de captura de video
vid = cv2.VideoCapture(0)

while(True):
   
    # Capturar el video cuadro por cuadro
    ret, frame = vid.read()

    # Mostrar el cuadro resultante 
    cv2.imshow("Camara web", frame) # OpenCV no acepta caracteres especiales como el acento en "Cámara"
      
    # Salir de la ventana a través de la barra espaciadora
    if cv2.waitKey(25) == 32:
        break
  
# Después del bucle, liberar el objeto capturado
vid.release()

# Destruir todas las ventanas
cv2.destroyAllWindows()