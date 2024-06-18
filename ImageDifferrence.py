import cv2
import numpy as np

def are_images_similar(img1_path, img2_path, threshold=30, max_diff_percentage=5):
    # Carica le immagini
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    # Controlla se le immagini hanno la stessa dimensione e numero di canali
    if img1.shape != img2.shape:
        print("Le immagini hanno dimensioni diverse.")
        return False

    # Converti le immagini in scala di grigi
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Calcola la differenza assoluta tra le immagini
    diff = cv2.absdiff(gray1, gray2)        

    # Applica una soglia per ottenere una immagine binaria delle differenze
    _, thresh = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)

    # Calcola la percentuale di pixel che differiscono
    non_zero_count = np.count_nonzero(thresh)
    total_pixels = thresh.size
    diff_percentage = (non_zero_count / total_pixels) * 100

    print(f"Percentuale di pixel diversi: {diff_percentage:.2f}%")

    # Confronta la percentuale di pixel differenti con la soglia massima consentita
    if diff_percentage > max_diff_percentage:
        return False
    else:
        return True

# Percorsi delle immagini
img1_path = "C:\\Users\\ragno\\OneDrive\\Immagini\\Rullino\\WIN_20240617_16_02_26_Pro.jpg"
img2_path = "C:\\Users\\ragno\\OneDrive\\Immagini\\Rullino\\WIN_20240617_15_58_55_Pro.jpg"
# Esegui il confronto e decidi cosa fare
if are_images_similar(img1_path, img2_path):
    print("Le immagini sono simili.")
    # Azione da eseguire se le immagini sono simili
else:
    print("Le immagini sono diverse.")
    # Azione da eseguire se le immagini sono diverse
