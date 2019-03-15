#!/usr/bin/env python

import socket

serversocket    =   socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creamos socket

serversocket.bind(('10.108.33.31 ', 8085)) #Mantenemos en esucucha el puerto (8000)

serversocket.listen(1) #Mantenemos en escucha el servidor

clientsocket, clientaddress = serversocket.accept()  #Aceptamos la conexión
print ('Conexion desde: ', clientaddress)  #Imprimir la IP del clientsocket
#Entra en el bucle mientras se mantenga la conexión
try:
    while 1:
           info = clientsocket.recv(1024).decode()
           info = info.replace(" ","").replace("'","")
           info = info.split(",")
           if not info:
               serversocket.listen(1) #Mantenemos en escucha el servidor
               clientsocket, clientaddress = serversocket.accept()  #Aceptamos la conexión
               print ('Conexion desde: ', clientaddress)
           else:
               opcion = float(info[0])
               numero1 = float(info[1])
               numero2 = float(info[2])

               if opcion == 1:
                   resultado = numero1 + numero2
                   resultado = str(resultado)
                   clientsocket.send(resultado.encode())
               elif opcion == 2:
                   resultado = numero1 - numero2
                   resultado = str(resultado)
                   clientsocket.send(resultado.encode())
               elif opcion == 3:
                   resultado = numero1 * numero2
                   resultado = str(resultado)
                   clientsocket.send(resultado.encode())
               elif opcion == 4:
                   if numero2 == 0:
                       resultado = "No se puede dividir entre 0."
                   else:
                       resultado = numero1/numero2
                   resultado = str(resultado)
                   clientsocket.send(resultado.encode())
    clientsocket.close() #Cierra el socket

except KeyboardInterrupt:
        print()
        print("Ejecución interrumpida por el usuario.")
        print("El programa ha finalizado.")
        clientsocket.close()
