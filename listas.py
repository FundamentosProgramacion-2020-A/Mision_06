# Mariana Mejía Béjar
# Se realizan diferentes funciones a partir de listas como: recortárlas, ordenarlas,
# verificar si hay duplicados, eliminar duplicados, así como comprobar si 2 palabras son anagrmas


def recortarLista(lista):                #Ejercicio 1
    if len(lista)<=2:                    #Si la lista fuera igual o menor a dos números, se regresan los corchetes [] vacíos
        return []
    
    nuevaLista = list(lista)                           #Estoy haciendo un duplicado, sobre el cual voy a hacer los cambios
    ultimo = nuevaLista[len(nuevaLista)-1]             #Len(nuevaLista)-1: es el último dato
    nuevaLista.remove(ultimo)                          #Elimina el último dato
    
    primero = nuevaLista[0]                            #Va al primer índice
    nuevaLista.remove(primero)                         #Elimina el primer dato
    return nuevaLista


def estanOrdenados(listaOriginal):         #Ejercicio 2
    
    listaNueva = list(listaOriginal)       #Duplicado, sobre el cual voy a hacer los cambios
    listaOriginal.sort()                   #Ordena la lista
    
    if listaNueva == listaOriginal:        #Compara la lista original con la lista nueva
        return True                        #Si son iguales regresa True
    
    if listaNueva == []:                   #Dice que si el corchete está vacío, la lista va a ser considerada como ordenada.
        return True
    
    else:
        return False                       #Si no son iguales regresa False
    

def sonAnagramas(cadena1, cadena2):        #Ejercicio 3 (No está en infinitivo porque regresa True or False)
    cadena1 = cadena1.upper()              #Convierte las minúsculas en mayúsculas  
    cadena2 = cadena2.upper()
    
    lista1 = list(cadena1)                 #Convierte la cadena en lista [ "A", "T", "U", "N"]
    lista2 = list(cadena2)
    
    lista1.sort()                          #Siempre los ordena de menor a mayor [ "A", "N", "T", "U"]
    lista2.sort()
    
    
    if lista1==lista2:                     #Compara la la lista 1 y la 2
        return True                        #Si tiene las mismas letras regresa True
    else: 
        return False                       #Si no, regresa False
    

def hayDuplicados(lista):                  #Ejercicio 4
    for datos in lista:
        if lista.count(datos)>=2:           #Busca si un dato se repite 2 veces o más
            return True                    #Termina y me da un resultado (porque ya se que hay un duplicado)
        
    return False                            #Termina y me da un resultado, este lo regresa en caso de no tener duplicados
    

def borrarDuplicados (lista):                #Ejercicio 5
   while hayDuplicados(lista) == True:        #Dice que sí al menos hay un dato repetido...
        for cifra in range(len(lista)):
            dato = lista[cifra]
            veces = lista.count(dato)
           
            #Elimina duplicados
           
            for numero in range (veces-1):           #Borra tantas veces menos una, como aparezca en la lista (o sea, elimina duplicados y deja solo un número de esos)
                lista.remove(dato)
            if veces >=2:                      #O sea, si sí se duplicó algún número porque aparec 2 veces o más
                break                        #Para que el ciclo de ejecución se termine
            

def main():
    
    print("Ejercicio 1: ")                   #Ejercicio 1
    
    lista = [7, 15, 19, 38, 46]
    nuevaLista = recortarLista(lista)
    print("La lista", lista, "recortada queda así: ", nuevaLista)
    
    lista2 = [15, 19, 38]
    nuevaLista = recortarLista(lista2)
    print("La lista", lista2, "recortada queda así: ", nuevaLista)
    
    lista3 = [7, 46]
    nuevaLista = recortarLista(lista3)
    print("La lista", lista3, "recortada queda así: ", nuevaLista)
    

    lista4 = []
    nuevaLista = recortarLista(lista4)
    print("La lista", lista4, "recortada queda así: ", nuevaLista)
    
    print (" ")
    
    print("Ejercicio 2: ")                   #Ejercicio 2
    
    primera = [10, 20, 20, 40, 50, 60, 70, 80, 90, 100]
    print ("La secuencia", primera)
    orden = estanOrdenados(primera)

    if orden == True:
        print ("está ordenada")
    else:
        print ("no está ordenada")
        
    print(" ")

    segunda = [10, 30, 20, 50, 40, 60, 80, 70, 100, 90]
    print ("La secuencia", segunda)
    ordenDos = estanOrdenados(segunda)

    if ordenDos == True:
        print ("está ordenada")
    else:
        print ("no está ordenada")
        
    print(" ")
        
    tercera = []
    print ("La secuencia", tercera)
    ordenTres = estanOrdenados(tercera)

    if ordenTres == True:
        print ("está ordenada")
    else:
        print ("no está ordenada")
    
    print (" ")
    
    print("Ejercicio 3: ")                   #Ejercicio 3
    
    a = "Enamoramientos"
    b = "Armoniosamente"
    
    print(a, "y", b)            
    
    if sonAnagramas(a,b)==True:
        print("Sí son anagramas")
    else:
        print("No son anagramas")
        
    print(" ")
        
    a = "Roberto"
    b = "Román"
    print(a, "y", b)
    if sonAnagramas(a,b)==True:
        print("Sí son anagramas")
    else:
        print("No son anagramas")
        
    print("     ")
    
    print("Ejercicio 4: ")                   #Ejercicio 4
    
    numeros = [10, 19, 38, 138, 19, 140]
    if hayDuplicados(numeros) == False:
        print("En la lista", numeros, "no hay duplicados")
    else:
        print("En la lista", numeros, "hay duplicados")
        
    numeros2 = [5, 10, 15, 20, 25]
    if hayDuplicados(numeros2) == False:
        print("En la lista", numeros2, "no hay duplicados")
    else:
        print("En la lista", numeros2, "hay duplicados")
    
    print (" ")
        
    print("Ejercicio 5: ")                   #Ejercicio 5
    
    secuencia = [100, 200, 200, 300, 300, 400, 500, 500, 600, 700, 800, 900, 900, 1000, 100]
    print("La lista original es: ", secuencia)
    borrarDuplicados(secuencia)
    print("Si los duplicados son eliminados, nos queda: ", secuencia)
    
    print (" ")
    
    secuencia2 = [1,2,3,4,5]
    print("La lista original es: ", secuencia2)
    borrarDuplicados(secuencia2)
    print("Si los duplicados son eliminados, nos queda: ", secuencia2)
    
    print (" ")
    
    secuencia3 = []
    print("La lista original es: ", secuencia3)
    borrarDuplicados(secuencia3)
    print("Si los duplicados son eliminados, nos queda: ", secuencia3)
     

main()