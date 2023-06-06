import tkinter as tk
from tkinter import *
from tkinter import ttk
import ventanaAgHabitacion
import ventanaReserva
import ventanaResumenes
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Sistema Hotel").grid(column=0, row=0, columnspan=2)
ttk.Button(frm, text="Agregar Habitacion", command=lambda: ventanaAgHabitacion.ventanaAgregarHab() ).grid(column=1, row=2,padx=20, pady=20, sticky="nsew")
ttk.Button(frm, text="Agregar Reserva", command=lambda: ventanaReserva.ventanaReserva() ).grid(column=2, row=2,padx=20, pady=20, sticky="nsew")
ttk.Button(frm, text="Resumenes", command=lambda: ventanaResumenes.ventanaMostrarRes() ).grid(column=3, row=2,padx=20, pady=20, sticky="nsew")

root.mainloop()