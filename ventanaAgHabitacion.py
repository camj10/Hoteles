import tkinter as tk
from tkinter import ttk
import customtkinter
import mysql.connector
def ventanasecundaria():
    root_tk = tk.Tk()
    root_tk.geometry("1220x720")
    root_tk.title("Agregar habitacion")

    print("Ingreso en la funcion de agregar tipo de habitacion")

    datos = {}
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hoteles"
    )

    mycursor = mydb.cursor()

    def on_key_typed(event):
            for i in tree.get_children():
                tree.delete(i)
            tecla = event.char
            tecla_presionada = cajaTipoHabitacion.get()
            tecla_presionada = tecla_presionada + tecla
            print("tecla: ", tecla_presionada)
            cargar_tabla()


    def on_key_typed_2(event):
            for i in tree.get_children():
                tree.delete(i)
            tecla = event.char
            tecla_presionada = cajaTipoHabitacion.get()
            tecla_presionada = tecla_presionada + tecla
            print("tecla: ", tecla_presionada)
            cargar_tabla()


    def function_guardar():
            tipoHabitacion = str(cajaTipoHabitacion.get())
            costo = int(cajaCosto.get())
            if tipoHabitacion != '' and costo>0:
                mycursor.execute("INSERT INTO habitacion (tipo,costo) VALUES(%s,%s)",
                                (tipoHabitacion, costo))
                mydb.commit()
                print("Guardado exitosamente")
                for i in tree.get_children():
                    tree.delete(i)
                cargar_tabla()
            else: 
                print("Datos incompletos")

    def function_limpiar():
            cajaTipoHabitacion.delete(0, tk.END)
            cajaCosto.delete(0, tk.END)


    def function_borrar():
            tipoHabitacion = str(cajaTipoHabitacion.get())
            mycursor.execute("DELETE FROM habitacion WHERE tipo = %s", [tipoHabitacion])
            mydb.commit()
            print("Borrado")
            for i in tree.get_children():
                tree.delete(i)
            cargar_tabla()
    #Falta agregar el boton de editar y probar este
    # def function_editar():
    #         tipoHabitacion = str(cajaTipoHabitacion.get())
    #         costo = int(cajaCosto.get())
    #         mycursor.execute("UPDATE habitacion SET [tipo]= %s ,[costo]= %s WHERE tipo= %s",[tipoHabitacion,costo,tipoHabitacion])
    #         mydb.commit()
    #         print("Editado")
    #         for i in tree.get_children():
    #             tree.delete(i)
    #         cargar_tabla()
    def cargar_tabla():
            sql="SELECT id_habitacion,tipo,costo FROM habitacion"
            mycursor.execute(sql)
            filas = mycursor.fetchall()
            for fila in filas:
                tree.insert("", tk.END, values=(
                    fila))

    LabelTipoHabitacion=ttk.Label(root_tk, text="Tipo Habitacion").grid(column=2, row=1)
    cajaTipoHabitacion=ttk.Entry(root_tk, text="")
    cajaTipoHabitacion.grid(column=2, row=2,padx=20, pady=20, sticky="nsew")
    LabelCosto=ttk.Label(root_tk, text="Costo").grid(column=2, row=3)
    cajaCosto=ttk.Entry(root_tk, text="Costo")
    cajaCosto.grid(column=2, row=4,padx=20, pady=20, sticky="nsew")
    cajaCosto.insert(0, '0')
    buttonLimpiar = customtkinter.CTkButton(
        master=root_tk, corner_radius=10, text="Limpiar", command=function_limpiar)
    buttonLimpiar.grid(column=0, row=5, sticky="nsew")
    buttonGuardar = customtkinter.CTkButton(
        master=root_tk, corner_radius=10, text="Guardar", command=function_guardar)
    buttonGuardar.grid(column=1, row=5, sticky="nsew")
    buttonBorrar = customtkinter.CTkButton(
        master=root_tk, corner_radius=10, text="Borrar", command=function_borrar)
    buttonBorrar.grid(column=2, row=5, sticky="nsew")
    buttonSalir = customtkinter.CTkButton(
        master=root_tk, corner_radius=10, text="Salir", command=root_tk.destroy)
    buttonSalir.grid(column=3, row=5, sticky="nsew")


    columns = ('Id_habitacion', 'Tipo de habitacion', 'Costo',)
    tree = ttk.Treeview(root_tk, columns=columns, show='headings')
    tree.heading('Id_habitacion', text='id_habitacion')
    tree.heading('Tipo de habitacion', text='Tipo')
    tree.heading('Costo', text='Costo')
    tree.grid(row=6, column=0, columnspan=6, padx=10, rowspan=4, sticky="nsew")

    cargar_tabla()

    root_tk.mainloop()
