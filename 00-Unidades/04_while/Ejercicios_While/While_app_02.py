import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre:
apellido:
---
Ejercicio: while_02
---
Enunciado:
UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su proximo desarrollo en python, 
que promete revolucionar el mercado. 
Las posibles aplicaciones son las siguientes: 
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA), 
# Internet de las cosas (IOT) o 


Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:

Los datos a ingresar por cada encuestado son:
    * nombre del empleado
    * edad (no menor a 18)
    * genero (Masculino - Femenino - Otro)
    * tecnologia (IA, RV/RA, IOT)   

En esta opción, se ingresaran empleados hasta que el usuario lo desee.

Una vez finalizado el ingreso, mostrar:

    #!X 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
    #!X 2) - Tecnología que mas se votó.
    #!X 3) - Porcentaje de empleados por cada genero
    #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  
    #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
    #!X 6) - Nombre y género del empleado que voto por RV/RA con menor edad.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        bandera = True
        contador_masculino_IOT_IA = 0

        contador_IA = 0
        contador_IOT = 0
        contador_RV_RA = 0

        contador_masculino = 0
        contador_femenino = 0
        contador_otros = 0

        contador_IOT_rango = 0

        contador_femenino_IA = 0
        acumulador_edad_femenino_IA = 0

        while bandera:
            #Los datos a ingresar por cada encuestado son:
            #* nombre del empleado
            #* edad (no menor a 18)
            #* genero (Masculino - Femenino - Otro)
            #* tecnologia (IA, RV/RA, IOT)
            nombre = input("ingrese nombre: ")
            edad = input("ingrese su edad: ")
            edad = int(edad)
            while edad < 18:
                edad = input("reingrese su edad: ")
                edad = int(edad)
            genero = input("ingrese su genero: ")
            while genero != "Masculino" and genero != "femenino" and genero != "Otro":
                genero = input("reingrese genero: ")
            tecnologia = input("ingrese tecnologia: ")
            while tecnologia != "IA" and tecnologia != "IOT" and tecnologia != "RV/RA":
                tecnologia = input("reingrese tecnologia: ")
            
            #!X 2) - Tecnología que mas se votó.
            match tecnologia :
                case "IA":
                    contador_IA += 1
                case "IOT":
                    contador_IOT += 1
                    #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.
                    if edad >= 18 and edad <= 25 or edad >= 33 and edad <= 42:
                        contador_IOT_rango += 1
                case "RV/RA":
                    contador_RV_RA += 1
                 #!X 6) - Nombre y género del empleado que voto por RV/RA con menor edad.
                    if contador_RV_RA == 1 or edad < edad_minima:
                        edad_minima = edad
                        genero_minimo = genero
                        nombre_minimo = nombre

            #!X 3) - Porcentaje de empleados por cada genero
            match genero:
                case "femenino":
                    contador_femenino += 1
                #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
                    if tecnologia == "IA":
                        contador_femenino_IA += 1
                        acumulador_edad_femenino_IA += edad

                case "Masculino":
                    contador_masculino += 1
                    #!X 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
                    if edad >= 25 and edad <= 50 and (tecnologia == "IOT" or tecnologia == "IA"):
                        contador_masculino_IOT_IA += 1

                case "Otro":
                    contador_otros += 1
            

            #!X 2) - Tecnología que mas se votó.
            if contador_IOT > contador_IA and contador_IOT > contador_RV_RA:
                tecnologia_mas_votada = "IOT"
            elif contador_IA > contador_RV_RA:
                tecnologia_mas_votada = "IA"
            else:
                tecnologia_mas_votada = "RV/RA"

             
            #!X 3) - Porcentaje de empleados por cada genero
            total_empleados = contador_otros + contador_femenino + contador_masculino
            porcentaje_femenino = (contador_femenino * 100) / total_empleados
            porcentaje_masculino = (contador_masculino * 100) / total_empleados
            porcentaje_otro = 100 - porcentaje_femenino - porcentaje_masculino

            #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.
            porcentaje_IOT_rango = (contador_IOT_rango * 100) / total_empleados

            #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
            if contador_femenino_IA > 0:
                promedio_edad_femenino_IA = acumulador_edad_femenino_IA / contador_femenino_IA
            else:
                promedio_edad_femenino_IA = "no se pudo calcular porque no ingreso femeninos votantes de IA"
            bandera = question("seguir", "quiere continuar?")

            print(f"1 masculinos IOT/IA en rango de edad: {contador_masculino_IOT_IA}")
            print(f"2 la tecnologias más votada es: {tecnologia_mas_votada}")
            print(f"3 porcentajes: \n\tFemenino: {porcentaje_femenino}\n\tMasculino: {porcentaje_masculino}\n\tOtro: {porcentaje_otro}")
            print(f"4 porcentaje en rango {porcentaje_IOT_rango}%")
            print(f"5 el promedio edad femenino IA es: {promedio_edad_femenino_IA}")
            if contador_RV_RA != 0:
                print(f"6 minimo: {edad_minima} -- {genero_minimo} -- {nombre_minimo}")
            else:
                print("no se encontro el minimo")
        
            
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()