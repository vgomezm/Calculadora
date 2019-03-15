#!/usr/bin/env python

import socket
import sys

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Crear el socket

clientsocket.connect(('10.108.33.31 ',8085)) #Se conecta al servidor (IP,puerto)

def imprime_menu():
    mensaje_menu = """    Menú.
    0. Cerrar el programa.
    1. Sumar.
    2. Restar.
    3. Multiplicar.
    4. Dividir."""
    print(mensaje_menu)

#FUNCION ELEGIR OPCION DEL MENÚ
def opcion_menu():
    a = True
    while a:
        opcion = input("Por favor, introduzca una opción válida para continuar: ")
        try:
            opcion = int(opcion)
            a = False
            print()
        except ValueError:
            print("La opción elegida no es válida.\n")
            imprime_menu()
    return opcion

#Entra en el bucle si está conectado
try:
    while 1:
        imprime_menu()
        opcion = opcion_menu()
        if opcion == 0:
            sys.exit(0)
        opcion = str(opcion)
        numero1 = str(input("Introduce un numero: "))
        numero2 = str(input("Introduce otro numero: "))
        info = (opcion,numero1,numero2)
        info =str(info)
        info = info.replace("("," ").replace(")"," ")
        info = "".join(info)
        info = str.encode(info)#Escribimos mensaje
        clientsocket.send(info)  #Se envía al servidor

        resultado = clientsocket.recv(1024).decode()  #Recibe la respuesta del servidor
        print ('El resultado de la operación es: ',resultado) #Imprime la respuesta
    clientsocket.close()  #Cierra el socket

except KeyboardInterrupt:
        print()
        print("Ejecución interrumpida por el usuario.")
        print("El programa ha finalizado.")
        clientsocket.close()
