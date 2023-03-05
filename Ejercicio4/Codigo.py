#"Tabla T"
#Primero preguntamos cuantos numeros quiere ordenar
n = int(input("¿Cuantos numeros quiere ordenar? "))
#Creamos una lista vacia
lista = []
#Creamos un bucle para que el usuario introduzca los numeros
for i in range(n):
    lista.append(int(input("Introduzca un numero: ")))
#Ahora crearemos el codigo para comparar los numeros de la lista y ordenarlos