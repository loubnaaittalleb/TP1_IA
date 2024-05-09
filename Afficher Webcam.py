#
# Afficher la webcam comme video
#
import cv2
import face_recognition
def dess_rectangle(image, haut_gauche, bas_droit, couleur=(255,255,255), epaisseur=1, type_ligne=cv2.LINE_AA):
    cv2.rectangle(image, haut_gauche, bas_droit, couleur, epaisseur, type_ligne)

capture = cv2.VideoCapture(0)                   # lire a partir de la camera par defaut

# configurer les propriétées de la video
# https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html#ggaeb8dd9c89c10a5c63c139bf7c4f5704dab26d2ba37086662261148e9fe93eecad
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)      # la largeur
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)     # la hauteur
capture.set(cv2.CAP_PROP_BRIGHTNESS, 180)       # la brillance
capture.set(cv2.CAP_PROP_CONTRAST, 50)          # le contraste

succes, img = capture.read()
while succes:
    visages_positions = face_recognition.face_locations(img)

    face_landmarks_list = face_recognition.face_landmarks(img)
    print(len(face_landmarks_list))
    for visage_position in visages_positions:
        haut, droit, bas, gauche = visage_position
        dess_rectangle(img,(gauche,haut),(droit,bas),couleur=(0,255,0),epaisseur=4)
    cv2.imshow("Webcam", img)
    # Taper sur la touche ESC pour stopper la boucle
    if cv2.waitKey(10) & 0xFF == 27:
        break
    succes, img = capture.read()

capture.release()
cv2.destroyWindow("Webcam")