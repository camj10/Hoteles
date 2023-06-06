import tkinter as tk
from tkinter import ttk, PhotoImage, Label

import ventanaAgHabitacion
import ventanaReserva
import ventanaResumenes

root = tk.Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
root.title("Kuarahy Hotel")

root.iconbitmap("sol.ico")


imagen = PhotoImage(file="fondo_inicio.png")

background = Label(root, image=imagen, text="Imagen S.O de fondo")
background.place(x=0, y=0, relwidth=1, relheight=1)

root.geometry("500x600") # Establecer el tamaño de la ventana

ttk.Label(root, text="").grid(column=0, row=1, columnspan=3 , pady=120)

# ttk.Button(root, text="Agregar Habitacion", command=lambda: ventanaAgHabitacion.ventanaAgregarHab()).grid(column=0, row=3, padx=20, pady=20, sticky="nsew")
bt_agg = PhotoImage(file="bt_agg.png")
boton = ttk.Button(root, image=bt_agg, command=lambda: ventanaAgHabitacion.ventanasecundaria(), padding=-10)
boton.grid(column=0, row=3, padx=20, pady=20, sticky="nsew")

# ttk.Button(root, text="Agregar Reserva", command=lambda: ventanaReserva.ventanaReserva()).grid(column=0, row=4, padx=20, pady=20, sticky="nsew")
bt_reserva = PhotoImage(file="bt_reserva.png")
boton = ttk.Button(root, image=bt_reserva, command=lambda: ventanaReserva.ventanaReserva(), padding=-10)
boton.grid(column=0, row=4, padx=20, pady=20, sticky="nsew")


# ttk.Button(root, text="Resumenes", command=lambda: ventanaResumenes.ventanaMostrarRes()).grid(column=0, row=5, padx=20, pady=20, sticky="nsew")
bt_resumenes = PhotoImage(file="bt_resumenes.png")
boton = ttk.Button(root, image=bt_resumenes, command=lambda: ventanaResumenes.ventanaMostrarRes(), padding=-10)
boton.grid(column=0, row=5, padx=20, pady=20, sticky="nsew")

root.grid_columnconfigure(0, weight=1) 



root.mainloop()