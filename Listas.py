# Autor: Sharone Márquez, A01746940
# Escribir funciones de acuerdo con el tema de listas


def recortarLista(lista): #cadena cómo parametro
    if len(lista) == 0:  #==< 2 condiciones especiales
        return []
    
    listaRecortada= list(lista)
    ultimo= listaRecortada[len(listaRecortada)-1]
    listaRecortada.remove(ultimo)
    primero= listaRecortada[0]
    listaRecortada.remove(primero)
                      
    return listaRecortada

def estanOrdenados(lista):
    listaOrdenada= list(lista)
    listaOrdenada.sort()
    
    if listaOrdenada == lista:
        return True
    return False

def sonAnagramas(cadena1, cadena2): #cadenas cómo parámetros
    cadena1= cadena1.upper()
    cadena2= cadena2.upper()
    
    lista1= list(cadena1) #convierte la cadena en lisa
    lista2= list(cadena2)
    
    lista1.sort()
    lista2.sort()
    
    if lista1 == lista2:
        return True
    return False

def hayDuplicados(lista):
    for dato in lista:
        if lista.count(dato) >= 2:
            return True   #TERMINA y me da un resultado
        
    return False

def borrarDuplicados(lista):
    while hayDuplicados(lista) == True:
        #Elimina duplicados
        for k in range(len(lista)):
            dato= lista[k]
            veces= lista.count(dato)
            for n in range(veces - 1): #Borra tantas veces -1 como aparezca el valor en la lista
                lista.remove(dato)
            if veces >= 2:
                break
            
#--------------------------------------- PROGRAMA PRINCIPAL ------------------------        
def main():
    print("Ejercicio 1.")
    a= [1, 2, 3, 4, 5]
    nueva= recortarLista(a)
    print("La lista:", a, "recortada es:", nueva)
    
    b= [2, 3, 4]
    nueva2= recortarLista(b)
    print("La lista:", b, "recortada es:", nueva2)
    
    c= []
    nueva3= recortarLista(c)
    print("La lista:", c, "recortada es:", nueva3)
    
    print(" ")
    
    #------------------------------------------------------
    print("Ejercicio 2.")
    numeros= [7, 12, 53]
    listaOrdenadaA= estanOrdenados(numeros)
    if listaOrdenadaA == True:
        print("La lista:", numeros, "está ordenada")
    else:
        print("La lista:", numeros, "no está ordenada")
        
    numeros2= [7, 23, 15]
    listaOrdenadaB= estanOrdenados(numeros2)
    if listaOrdenadaB == True:
        print("La lista:", numeros2, "está ordenada")
    else:
        print("La lista:", numeros2, "no está ordenada")
        
    print(" ")
    
    #-----------------------------------------------------
    print("Ejercico 3.")
    cadena1= "Roma"
    cadena2= "Mora"
    
    if sonAnagramas(cadena1, cadena2) == True:
        print("Las palabras", cadena1, "y", cadena2, "son anagramas")
    else:
        print("Las palabras", cadena1, "y", cadena2, "no son anagramas")
        
    cadena3= "Hola"
    cadena4= "Hello"
    
    if sonAnagramas(cadena3, cadena4) == True:
        print("Las palabras", cadena3, "y", cadena4, "son anagramas")
    else:
        print("Las palabras", cadena3, "y", cadena4, "no son anagramas")
        
    cadena3= "Ana"
    cadena4= "Nana"
    
    if sonAnagramas(cadena3, cadena4) == True:
        print("Las palabras", cadena3, "y", cadena4, "son anagramas")
    else:
        print("Las palabras", cadena3, "y", cadena4, "no son anagramas")
    
    print(" ")
    
    #--------------------------------------------------------    
    print("Ejercico 4.")  
    d= [1, 2, 3, 1, 4, 5]
    listaDuplicada= hayDuplicados(d)
    if listaDuplicada == True:
        print("La lista:", d, "tiene números duplicados")
    else:
        print("La lista:", d, "no tiene números duplicados")
        
    e= [5, 7, 4, 6, 10]
    listaDuplicada= hayDuplicados(e)
    if listaDuplicada == True:
        print("La lista:", e, "tiene números duplicados")
    else:
        print("La lista:", e, "no tiene números duplicados")
    
    print(" ")
    
    #-------------------------------------------------------
    print("Ejercico 5.")
    f= [1, 8, 3, 4, 3, 1, 8, 2, 7, 8]
    print("La lista original:", f, "tiene números duplicados")
    borrarDuplicados(f)
    print("La lista cambiada:", f, "ya no tiene números duplicados")
    
    print(" ")
    
main()