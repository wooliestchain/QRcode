from tkinter import *

window = Tk()
window.title("QRCode")
window.geometry("720x480")
window.config(background="#4065A4")

widht = 300
height = 300
image = PhotoImage(file="test3.png").zoom(8).subsample(7)
canvas = Canvas(window, width=widht, height=height, bg="#4065A4")
canvas.create_image(widht/2, height/2, image=image)
frame = Frame(window, bg='#4065A4')
right_frame = Frame(frame, bg="#4065A4")

x = Entry(right_frame, textvariable="Entrer un numéro de compte", font=("Arial",20), bg="#4065A4", fg="black")

window.mainloop()