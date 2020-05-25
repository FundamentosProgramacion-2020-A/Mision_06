#Autor: Valeria Huerta Pedregal
#Misión 6: listas

def recortarLista(lista): #Quita el primer y último valor de la lista
    if len(lista) <= 2:
        return []
    nuevaLista = list(lista) 
    primero = nuevaLista[0]
    nuevaLista.remove(primero)
    ultimo = nuevaLista[len(nuevaLista)-1] 
    nuevaLista.remove(ultimo)
    return nuevaLista
    
def estanOrdenados(lista): #Determina si la lista está ordenada
    nuevaLista = list(lista)
    nuevaLista.sort()
    if nuevaLista == lista:
        return True
    return False

def sonAnagramas(palabra1, palabra2): #Determina si dos palabras osn anagramas
    palabra1 = palabra1.upper() 
    palabra2 = palabra2.upper()
    lista1 = list(palabra1)
    lista2 = list(palabra2) 
    lista1.sort()  
    lista2.sort()
    if lista1 == lista2:
        return True
    else:
        return False

def hayDuplicados(lista): #Determina si hay duplicados en una lista
    for valor in lista:
        if lista.count(valor)>=2:
            return True 
    return False

def borrarDuplicados(lista): #Borra los números duplicados de una lista
    while hayDuplicados(lista) == True:
        for j in range(len(lista)): 
            valor = lista[j]
            veces = lista.count(valor)
            for n in range (veces-1): 
                lista.remove(valor) 
            if veces>=2:
                break 

def main(): #Corre el programa principal
    print("Ejercicio 1.") #Ejercicio 1.
    a = [1,2,3,4,5,6,7]
    nuevaA = recortarLista(a)
    print("La lista",a,"sin el primer y último valor es", nuevaA)
    a = [1,2,3,5]
    nuevaA = recortarLista(a)
    print("La lista",a,"sin el primer y último valor es", nuevaA)
    a = [1,2,3]
    nuevaA = recortarLista(a)
    print("La lista",a,"sin el primer y último valor es", nuevaA)
    a = [1,2]
    nuevaA = recortarLista(a)
    print("La lista",a,"sin el primer y último valor es", nuevaA)
    a = []
    nuevaA = recortarLista(a)
    print("La lista",a,"sin el primer y último valor es", nuevaA)
    print("")
    
    print("Ejercicio 2.") #Ejercicio 2.
    a2 = [1,2,5,6,3,8,5]
    nuevaA2 = estanOrdenados(a2)
    if nuevaA2 == True:
        print("La lista",a2,"está ordenada.")
    else:
        print("La lista",a2,"está desordenada.")
    a2 = []
    nuevaA2 = estanOrdenados(a2)
    if nuevaA2 == True:
        print("La lista",a2,"está ordenada.")
    else:
        print("La lista",a2,"está desordenada.")
    a2 = [1,2,3,4,5,6,7,8,9]
    nuevaA2 = estanOrdenados(a2)
    if nuevaA2 == True:
        print("La lista",a2,"está ordenada.")
    else:
        print("La lista",a2,"está desordenada.")
    print("")
        
    print("Ejercicio 3.") #Ejercicio 3.
    b = "Ironicamente"
    c = "Renacimiento"
    if sonAnagramas(b,c) == True:
        print("Las palabras",b,"y",c,"son anagramas.")
    else:
        print("Las palabras",b,"y",c,"no son anagramas.")
    b = "Amar"
    c = "Trama"
    if sonAnagramas(b,c) == True:
        print("Las palabras",b,"y",c,"son anagramas.")
    else:
        print("Las palabras",b,"y",c,"no son anagramas.")
    b = "Ecuador"
    c = "Acuerdo"
    if sonAnagramas(b,c) == True:
        print("Las palabras",b,"y",c,"son anagramas.")
    else:
        print("Las palabras",b,"y",c,"no son anagramas.")
    print("")

    print("Ejercicio 4.") #Ejercicio 4.
    d = [1,2,3,4,5,4,3,2,1]
    d2 = hayDuplicados(d)
    if d2 == True:
        print("En la lista",d,"hay valores duplicados.")
    else:
        print("En la lista",d,"no hay duplicados.")
    d = [7,6,2,9,22,4,1]
    d2 = hayDuplicados(d)
    if d2 == True:
        print("En la lista",d,"hay valores duplicados.")
    else:
        print("En la lista",d,"no hay duplicados.")
    d = []
    d2 = hayDuplicados(d)
    if d2 == True:
        print("En la lista",d,"hay valores duplicados.")
    else:
        print("En la lista",d,"no hay duplicados.")
    print("")

    print("Ejercicio 5.") #Ejercicio 5.
    e = [8,2,9,4,6]
    print("La lista original es", e)
    borrarDuplicados(e)
    print("La lista queda como",e,"sin duplicados.")
    print("")
    e = [1,22,33,4,55,4]
    print("La lista original es", e)
    borrarDuplicados(e)
    print("La lista queda como",e,"sin duplicados.")
    print("")
    e = [1,1,2,2,3,3,5,6,9]
    print("La lista original es", e)
    borrarDuplicados(e)
    print("La lista queda como",e,"sin duplicados.")
    print("")
    e = []
    print("La lista original es", e)
    borrarDuplicados(e)
    print("La lista queda como",e,"sin duplicados.")
    
main()
    
    