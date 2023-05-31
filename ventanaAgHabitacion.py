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
# def ventanasecundaria():
def buttonGuardar_function():
    print("Entro en funcion guardar")
    #     mycursor= mydb.cursor()
    #     nacionalidad=cajaNacionalidad.get()
    #     sql="INSERT INTO datos(nacionalidad) values (%s)"
    #     val=(nacionalidad,)
    #     mycursor.execute(sql,val)
    #     # mydb.commit()
    #     # print(mycursor.rowcount," fila insertada a Nueva nacionalidad")
    #     mycursor = mydb.cursor()
    #     filas = mycursor.fetchall()
    #     for fila in filas:
    #         tabla.insert("", tk.END, values=fila)
frm2 = tk.Toplevel()
frm2.grid()
    
LabelTipoHabitacion=ttk.Label(frm2, text="Tipo Habitacion").grid(column=2, row=1)
cajaTipoHabitacion=ttk.Entry(frm2, text="")
cajaTipoHabitacion.grid(column=2, row=2,padx=20, pady=20, sticky="nsew")
LabelCosto=ttk.Label(frm2, text="Costo").grid(column=2, row=1)
cajaCosto=ttk.Entry(frm2, text="Costo")
cajaCosto.grid(column=2, row=4,padx=20, pady=20, sticky="nsew")
ttk.Button(frm2, text="Guardar",command= buttonGuardar_function).grid(column=2, row=5,padx=20, pady=20, sticky="nsew")


    # columns = ('nacionalidad')
    # tabla = ttk.Treeview(frm2, columns=columns, show='headings')
    # tabla.heading('nacionalidad', text='Nacionalidad')

#tabla.grid(row=5,column=5, columnspan=2,padx=10, rowspan=8,pady=10, sticky="nsew")