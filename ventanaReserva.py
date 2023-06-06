import tkinter as tk
from tkinter import *
from tkinter import ttk
import customtkinter as ctk

import mysql.connector
mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hoteles"
        )
#Declaracion de variables para el combox
sel={}
seleccionado=0

def ventanaReserva():
    frmRES = tk.Toplevel(border=2,padx=15,pady=15)
    frmRES.grid()

#Primera fila Agregar el numero de havitacion    
    ttk.Label(frmRES, text="Nro Habitacion:").grid(column=0, row=0)
    EntryNro=ttk.Entry(frmRES,)
    EntryNro.grid( column=1,row=0,  padx=10, pady=10, sticky="nsew")

#Segunda fila La tabla de habitaciones 
    columns = ('tipo', 'costo')
    tablaHa = ttk.Treeview(frmRES, columns=columns, show='headings',xscrollcommand=TRUE)
    tablaHa.heading('tipo', text='Tipo de habitacion ')
    tablaHa.heading('costo', text='Costo')
    tablaHa.grid(row=2,column=0, padx=0, pady=0,columnspan=2)

#Tercera fila Dias de estadia
    ttk.Label(frmRES, text="Dias de estadia:").grid(column=0, row=3)
    EntryDias=ttk.Entry(frmRES)
    EntryDias.grid( column=1,row=3,  padx=10, pady=10, sticky="nsew")

#Cuarta y quinta fila Radio Butons

    genderVar = tk.StringVar(value="No responde")

    CreditoRadioButton = ctk.CTkRadioButton(frmRES, text="Credito",variable=genderVar, value="1")
    CreditoRadioButton.grid(row=4, column=1,  padx=20, pady=20,  sticky="ew")

    ContadoRadioButton = ctk.CTkRadioButton(frmRES, text="Contado", variable=genderVar,  value="2")
    ContadoRadioButton.grid(row=5, column=1, padx=20, pady=5, sticky="ew")

#Botones Borrar, Modificar y Cargar

    ttk.Button(frmRES, text="Cargar").grid(column=0, row=6,padx=10, pady=20, sticky="nsew")
    ttk.Button(frmRES, text="Modificar").grid(column=1, row=6,padx=10, pady=20, sticky="nsew")
    ttk.Button(frmRES, text="Elimirar").grid(column=0, row=7,padx=50, pady=20, sticky="nsew",columnspan=2)


# Tabla General de reservas
    columns = ('numero', 'tipo', 'costo','subtotal','descuento','total')
    tablaGeneral = ttk.Treeview(frmRES, columns=columns, show='headings',xscrollcommand=TRUE)
    tablaGeneral.heading('numero', text='Nro habitacion')
    tablaGeneral.heading('tipo', text='Tipo de habitacion')
    tablaGeneral.heading('subtotal', text='Sub-Totales')
    tablaGeneral.heading('descuento', text='% Descuento')
    tablaGeneral.heading('costo', text='Costo')
    tablaGeneral.grid(row=0,column=2, padx=0, pady=0,columnspan=5,rowspan=3,)