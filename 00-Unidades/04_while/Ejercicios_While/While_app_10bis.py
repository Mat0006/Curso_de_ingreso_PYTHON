import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos
    G. El máximo valor. 
    H. El mínimo valor (incluyendo en que iteracion se encontro, solo la primera)
Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        suma_ac_negativos = 0
        suma_ac_positivos = 0
        cantidad_num_negativos = 0
        cantidad_num_positivos = 0
        cantidad_ceros = 0
        dif_positivos_negativos = 0
        bandera_num = True
        contador_itera = 1
        while True:
            numero = prompt("numero", "ingrese un numero")
            if numero is None:
                break
            while numero == "":    #esto para verificar que entren solo digitos, también sirve el modulo ".isdigit()"
                numero = prompt("numero", "ingrese un numero valido")

            numero = int(numero)
            if numero > 0:
                suma_ac_positivos += numero
                cantidad_num_positivos += 1
            elif numero < 0:
                suma_ac_negativos += numero
                cantidad_num_negativos += 1
            else:
                cantidad_ceros += 1

            if bandera_num or (numero > maximo):
                maximo = numero
            if bandera_num or (numero < minimo):
                minimo = numero
                cantidad_num_negativos = contador_itera
                bandera_num = False
            contador_itera += 1
        dif_positivos_negativos = cantidad_num_negativos - cantidad_num_positivos
        if dif_positivos_negativos < 0:
            dif_positivos_negativos *= -1
            
        mensaje =  f"suma negativos : {suma_ac_negativos}\nsuma positivos: {suma_ac_positivos}\ncantidad números negativos: {cantidad_num_negativos}\ncantidad números positivos: {cantidad_num_positivos}\ncantidad de ceros: {cantidad_ceros}\nla diferencia es : {dif_positivos_negativos}\n el maximo es: {maximo}\n el minimo es: {minimo} en la iteración {cantidad_num_negativos}"
        
        alert("numeros", mensaje)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
