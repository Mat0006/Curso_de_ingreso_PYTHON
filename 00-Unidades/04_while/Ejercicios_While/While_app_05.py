import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre:
apellido:
---
Ejercicio: while_05
---
Simulacro Turno Noche

Un famoso casino de mar del plata,  requiere una app para controlar el egreso de dinero durante una jornada. Para ello se ingresa por cada ganador:
Nombre
Importe ganado (mayor o igual $1000)
Género (“Femenino”, “Masculino”, “Otro”)
Juego (Ruleta, Poker, Tragamonedas)
Necesitamos saber:
1. Nombre y género de la persona que más ganó.
2. Promedio de dinero ganado en Ruleta.
3. Porcentaje de personas que jugaron en el Tragamonedas.
4. Cuál es el juego menos elegido por los ganadores.
5. El nombre del jugador que ganó más dinero jugando Poker
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_validar_letra = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_validar_letra_on_click)
        self.btn_validar_letra.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_validar_letra_on_click(self):
        bandera = True
        contador_jugador_ruleta = 0
        contador_jugador_poker = 0
        contador_jugador_tragamonedas = 0

        acumulador_dinero = 0
        acumulador_dinero_ruleta = 0
        mayor_importe_poker = 0
        while bandera:
            nombre = prompt("nombre", "ingrese su nombre: ")
            while nombre == None or nombre == "":
                nombre = prompt("error", "reingrese su nombre: ")
            importe_ganado = prompt("importe", "ingrese su importe: ")
            importe_ganado = int(importe_ganado)
            while int(importe_ganado) < 1000:
                importe_ganado = prompt("error", "reingrese su importe: ")
            genero = prompt("genero", "ingrese su genero: ")
            while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
                genero = prompt("error", "reingrese su genero")
            juego = prompt("juego", "ingrese al juego: ")
            while juego != "Ruleta" and juego != "Poker" and juego != "Tragamonedas":
                juego = prompt("error", "reingrese el juego: ")
            acumulador_dinero += importe_ganado
            match juego:
                case "Ruleta":
                    acumulador_dinero_ruleta += importe_ganado
                    contador_jugador_ruleta += 1
                    promedio_dinero_ruleta = acumulador_dinero_ruleta / contador_jugador_ruleta
                case "Tragamonedas":
                    contador_jugador_tragamonedas += 1
                case "Poker":
                    contador_jugador_poker += 1
                    if importe_ganado > mayor_importe_poker:
                        mayor_importe_poker = importe_ganado
                        nombre_ganador = nombre

            if contador_jugador_poker < contador_jugador_ruleta and contador_jugador_poker < contador_jugador_tragamonedas:
                menor_jugado = "Poker"
            elif contador_jugador_ruleta < contador_jugador_tragamonedas:
                menor_jugado = "Ruleta"
            else:
                menor_jugado = "Tragamonedas"

            if importe_ganado > acumulador_dinero:
                acumulador_dinero = importe_ganado
                nombre_mayor_ganador = nombre
                genero_mayor_ganador = genero

            bandera = question("continuar", "¿quiere continuar?")

            total_personas = contador_jugador_poker + contador_jugador_ruleta + contador_jugador_tragamonedas
            porcentaje_personas_tragamonedas = (contador_jugador_tragamonedas * 100) / total_personas




            bandera = question("continuar", "¿quiere continuar?")
        print (f"1. el nombre de quien más ganó es {nombre_mayor_ganador} y su genero es {genero_mayor_ganador}")
        print (f"2. el promedio de dinero ganado en ruleta es : {promedio_dinero_ruleta}")
        print (f"3. el porcentaje de personas que jugaron al tragamonedas es : {porcentaje_personas_tragamonedas}%")
        print (f"4. el menos elegido es: {menor_jugado}")
        print (f"5.el nombre de quien ganó más en poker es: {nombre_ganador}")
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()