from ultralytics import YOLO
import cv2
import time
from tkinter import *
import os
import threading

# Stile giallo per l'interfaccia
YELLOW = "#f7f5dd"

# Caricamento del modello YOLOv8
modello = YOLO('best-cls.pt')

# Inizializzazione cattura video
cap = cv2.VideoCapture(0)

window = Tk()
window.title('SMART BIN')
window.config(padx=200, pady=300, bg=YELLOW)

# Funzione per la classificazione delle immagini
def image_classification():
    start_button.config(state='disabled')
    succ, img = cap.read()
    if succ:
        # Ridimensionamento a risoluzione appropriata
        img = cv2.resize(img, (420, 420))

        # Esecuzione dell'inferenza con il modello YOLOv8
        results = modello.predict(img)
         
        # Ottenimento dell'immagine con i rilevamenti
        classification = results[0].plot()
        # Salvataggio dell'immagine risultante
        classification = cv2.resize(classification, (100, 124))
        cv2.imwrite('image.png', classification)
      
        # Creazione del canvas in Tkinter
        canvas = Canvas(width=100, height=124, highlightthickness=0)
        photo_img = PhotoImage(file='image.png')
        canvas.create_image(50, 62, image=photo_img)  # Posizionamento dell'immagine centrata
        window.update()
        canvas.grid(column=0, row=1)
        # Avvio del ciclo principale di Tkinter
        
        start_button.config(state='active')
        os.remove('image.png')
        window.mainloop()
        
    else:
        print("Access to frame failed!") 


# Pulsante per avviare la classificazione
start_button = Button(text='Start', highlightthickness=0, command=image_classification)
start_button.grid(row=2, column=0, padx=20, pady=20)
# Avvio del ciclo principale di Tkinter
window.mainloop() 

# Rilascio delle risorse
cap.release()
cv2.destroyAllWindows() 