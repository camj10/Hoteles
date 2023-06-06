import tkinter as tk
from tkinter import *
from tkinter import ttk

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

def ventanaMostrarRes():
    frmRS = tk.Toplevel(border=2,padx=15,pady=15)
    frmRS.grid()
#Funciones de la ventana
    def Seleccioncombo(event):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT total,dias FROM reserva WHERE tipo=%s AND estado=1",[combobox.get()])
        filas=mycursor.fetchall()
        totald=0
        totali=0
        for row in tabla.get_children():
            tabla.delete(row)
        for fila in filas:
            totald=totald+fila[1]
            totali=totali+fila[0]
        tabla.insert("",tk.END,values=(combobox.get(),totald,totali))

    def CargarCombox():
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM habitacion")
        filas = mycursor.fetchall()
        for fila in filas:
            llave = fila[1]
            valor = fila[0]
            sel[llave] = valor
        combobox['values'] = list( sel.keys())

#Label del titulo   
    ttk.Label(frmRS, text="Resumenes",font=('Helvetica bold',34)).grid(column=2, row=0)

#Combox 
    combobox = ttk.Combobox(frmRS, state="readonly",justify='center',font=18,height=10,background='#ff6',width=10,)
    combobox.grid(column=2, row=1,padx=20, pady=20,rowspan=2, sticky="nsew")
    combobox.bind('<<ComboboxSelected>>',Seleccioncombo)
    CargarCombox()

#Tabla
    columns = ('tipo', 'dias','totalR')
    tabla = ttk.Treeview(frmRS, columns=columns, show='headings')
    tabla.heading('tipo', text='Tipo de habitacion ')
    tabla.heading('dias', text='Dias ocupados')
    tabla.heading('totalR', text='Total Ingreso')
    tabla.grid(row=3,column=0, padx=0, pady=0,columnspan=4)