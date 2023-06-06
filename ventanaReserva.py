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



def ventanaReserva():
    frmRES = tk.Toplevel(border=2,padx=15,pady=15)
    frmRES.grid()
    
#---------------------------------------------Declaracion de funciones--------------------------------------------
    def finalizar():
        curItem = tablaGeneral.focus()
        seleccionado=tablaGeneral.item(curItem)
        cod=seleccionado['values'][0]
        mycursor = mydb.cursor()
        sql = "UPDATE reserva SET estado=1 WHERE id_reserva=%s"
        mycursor.execute(sql,[cod])
        mydb.commit()
        cargaBase()

    def FinalizarEsta(numr):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT id_reserva,numero_reserva FROM reserva WHERE estado=0")
        filas = mycursor.fetchall()
        bandera=False
        ind=0
        for fila in filas:
            if(fila[1]==numr):
                bandera=True
                ind=fila[0]
        if(bandera):
            mycursor = mydb.cursor()
            sql = "UPDATE reserva SET estado=1 WHERE id_reserva=%s"
            mycursor.execute(sql,[ind])
            mydb.commit()
        return
        
        
    def actualizar():
        curItem = tablaGeneral.focus()
        seleccionado=tablaGeneral.item(curItem)
        cod=seleccionado['values'][0]
        dias=int(EntryDias.get())
        descuento=seleccionado['values'][6]
        if(dias>10):
            descuento=descuento+2
        elif(descuento=='5' and dias<5):
            descuento=0
        subtotal=dias*seleccionado['values'][3]
        
        mycursor = mydb.cursor()
        sql = "UPDATE reserva SET dias=%s,subtotal=%s,porcentaje_descuento=%s,total=%sWHERE id_reserva=%s"
        value=[dias,subtotal,descuento,(subtotal-(subtotal*(descuento/100))),cod]
        mycursor.execute(sql,value)
        mydb.commit()
        cargaBase()

    def cargaBase():
        mycursor = mydb.cursor()
        mycursor.execute("SELECT id_reserva,numero_reserva,tipo,costo,dias,subtotal,porcentaje_descuento,total,tipo_pago FROM reserva WHERE estado=0")
        
        filas = mycursor.fetchall()
        for row in tablaGeneral.get_children():
            tablaGeneral.delete(row)
        for fila in filas:
            tablaGeneral.insert("", tk.END, values=fila)

    def cargarReser():
        numr=int(EntryNro.get())
        FinalizarEsta(numr)
        dias=int(EntryDias.get())
        option=genderVar.get()
        descuento=0.0
        curItem = tablaHa.focus()
        seleccionado=tablaHa.item(curItem)
        subtotal=(seleccionado['values'][1]*dias)
        if(option=='1' and   dias>5):
            descuento=0.05
        elif(option=='2'):
            descuento=0.1
        if(dias>10):
            descuento=descuento+0.02
        sql = 'INSERT INTO reserva(`numero_reserva`, `tipo`, `costo`, `dias`, `subtotal`, `porcentaje_descuento`, `total`,tipo_pago) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
        val = [numr,seleccionado['values'][0],seleccionado['values'][1],dias,subtotal,int(descuento*100.0),((seleccionado['values'][1]*dias)-descuento),option]
        mycursor = mydb.cursor()
        mycursor.execute(sql,val)
        mydb.commit()
        cargaBase()
        

    
    def cargaTablaTipo():
        mycursor = mydb.cursor()
        #falta cambiar el select por un select like
        mycursor.execute("SELECT tipo,costo FROM habitacion")
        filas = mycursor.fetchall()
        for row in tablaHa.get_children():
            tablaHa.delete(row)
        for fila in filas:
            tablaHa.insert("", tk.END, values=fila)

    def cargaSeleccion(element):
        curItem1 = tablaGeneral.focus()
        seleccionado1=tablaGeneral.item(curItem1)
        print(seleccionado1['values'])
        if(seleccionado1['values']):
            EntryNro.delete(0, tk.END)
            EntryDias.delete(0, tk.END)
            EntryDias.insert(0,seleccionado1['values'][4])
        else:EntryDias.delete(0, tk.END)



#---------------------------------------------Parte visual--------------------------------------------------------


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

    ttk.Button(frmRES, text="Cargar", command=cargarReser).grid(column=0, row=6,padx=10, pady=20, sticky="nsew")
    ttk.Button(frmRES, text="Modificar",command=actualizar).grid(column=1, row=6,padx=10, pady=20, sticky="nsew")
    ttk.Button(frmRES, text="Finalizar",command=finalizar).grid(column=0, row=7,padx=50, pady=20, sticky="nsew",columnspan=2)


# Tabla General de reservas
    columns = ('id_reserva','numero', 'tipo', 'costo','dias','subtotal','descuento','total','tipoPago')
    tablaGeneral = ttk.Treeview(frmRES, columns=columns, show='headings')
    tablaGeneral.heading('id_reserva', text='id_reserva')
    tablaGeneral.heading('numero', text='Nro habitacion')
    tablaGeneral.heading('tipo', text='Tipo de habitacion')
    tablaGeneral.heading('dias', text='Dias')
    tablaGeneral.heading('tipoPago', text='Tipo de pago')

    tablaGeneral.heading('subtotal', text='Sub-Totales')
    tablaGeneral.heading('descuento', text='Descuento')
    tablaGeneral.heading('costo', text='Costo')
    tablaGeneral.heading('total', text='Total')

    tablaGeneral.grid(row=0,column=2, padx=0, pady=0,columnspan=5,rowspan=3)

    tablaGeneral.column('numero', width=120)
    tablaGeneral.column('tipo', width=120)
    tablaGeneral.column('dias', width=120)
    tablaGeneral.column('subtotal', width=120)
    tablaGeneral.bind('<<TreeviewSelect>>',cargaSeleccion)


#--------------------------------------llamado a funciones iniciales------------------------------------------
    cargaTablaTipo()
    cargaBase()