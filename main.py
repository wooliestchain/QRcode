#Import Library
import qrcode
import colorama
import sklearn
import random
from tkinter import *
#Generate QR Code

a=input("Entrer le nom du client: ")
b=input("Entrer le prénom du client: ")

k = int(input("ENtrer un entier: "))
if k == 100:
    print("Compte epargne en dinars")

elif k == 110:
    print("Compte epargne pour les tunisiens residents a l'etranger")

elif k == 127:
    print("aaaaa")
n=input("Nature du compte: ")
x=input("Numéro de compte: ")
c=input("Entrer date de naissance: ")
d=input("Lieu de naissance: ")
e=input("Adresse: ")
bp = ['Medh v', 'Sfax', 'Tunis centre', 'Soukra', 'Ariana','Hmmamet', 'Sousse ville', 'Sousse village', 'Le Kram', 'Beja']
bp = random.choice(bp)

dict = {"nom": a , "prenom": b, "Clé": k, "Numéro de compte": x,"Nature du compte": n, "date de naissance": c, "Lieu de naissance": d, "Adresse": e, "Bureau de poste": bp}
img=qrcode.make(dict)

img.save('test3.png')

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data("https://www.instagram.com/poste_tn/?hl=fr")
qr.make(fit=True)
img = qr.make_image(fill_color="white", back_color="blue")
img.save("medium.png")

