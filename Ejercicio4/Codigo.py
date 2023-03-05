#"Tabla T"
#Primero preguntamos cuantos numeros quiere ordenar
n = int(input("¿Cuantos numeros quiere ordenar? "))
#Creamos una lista vacia
lista = []
#Creamos un bucle para que el usuario introduzca los numeros
for i in range(n):
    lista.append(int(input("Introduzca un numero y tras ello pulse enter: ")))
print("La lista sin ordenar es: ", lista) #imprimimos la lista sin ordenar
#Ahora crearemos el codigo para comparar los numeros de la lista y ordenarlos
def ordenar(lista):
    for i in range(len(lista)): 
        for j in range(len(lista)): #En esta linea y la anterior, se "lee" la lista
            if lista[i] < lista[j]: #En esta linea se comparan i y j y se da una solucionpara cuando i es menor que j
                aux = lista[i] #Es la solucion de la linea anterior, donde se le da otro valor a i
                lista[i] = lista[j] 
                lista[j] = aux
 
ordenar(lista) #ejecutamos la funcion de ordenar lista definida a partir de la linea 10
print("La lista ordenada es: ", lista) #y por ultimo mprimimos la lista ordenada
