# Autor: Paloma Cueto
# LISTAS

def recortarLista(lista):
    if len(lista)<=2:
        return []
    #COPIA
    nuevaLista = list(lista) #Se crea una nueva con la función
    ultimo = nuevaLista[len(nuevaLista)-1]
    nuevaLista.remove(ultimo) #elimina el ultimo dato
    primero = nuevaLista [0]
    nuevaLista.remove(primero)
    return nuevaLista

def estanOrdenados(lista):
    #Hacer una copia para comparar
    nuevaLista = list(lista)
    nuevaLista.sort()  #ordenar
    
    if nuevaLista == lista:
        return True
    return False

def sonAnagramas(cadena1, cadena2):
    cadena1 = cadena1.upper()
    cadena2 = cadena2.upper()
    
    lista1 = list(cadena1) #convierte la cadena en lista
    lista2 = list(cadena2) #["R", "O", "M", "A"]
    
    lista1.sort() #sort ordena
    lista2.sort()
    
    if lista1==lista2:
        return True
    
    return False

def hayDuplicados(lista):
    for dato in lista:
        if lista.count(dato)>=2:
            return True #Ya no sigue buscando y regresa un resultado
    
    return False

def borrarDuplicados(lista):
    while hayDuplicados(lista) == True:
        #Elimina duplicados
        for k in range(len(lista)):
            dato = lista[k]
            veces = lista.count(dato)
            for n in range(veces-1):  #Borra tantas veces menos uno como aparezca el valor en la lista
                lista.remove(dato)
            if veces>=2:
                break
            
    
def main():
    print ("Ejercicio 1: ")
    print (" ")
    a = [1,2,3,4,5]
    nuevaA = recortarLista(a)
    print("La lista original", a, "regresa la lista recortada:", nuevaA)
    b = [1,2]
    nuevaB = recortarLista(b)
    print("La lista original", b, "regresa la lista recortada:", nuevaB)
    c = []
    nuevaC = recortarLista(c)
    print("La lista original", c, "regresa la lista recortada:", nuevaC)
    print (" ")
    
    print ("Ejercicio 2: ")
    print (" ")
    a = [7,12,53]
    orden = estanOrdenados(a)
    if orden == True:
        print ("La Lista", a, "está ordenada")
    else:
        print ("La lista", a, "no está ordenada")
    b = [7,23,15]
    orden2 = estanOrdenados(b)
    if orden2 == True:
        print ("La Lista", b, "está ordenada")
    else:
        print ("La Lista", b, "no está ordenada")
        
    print (" ")
        
    
    print ("Ejercicio 3:")
    print (" ")
    a = "Roma"
    b = "Mora"
    print ("Las palabras", a, "y", b)
    if sonAnagramas(a,b) == True:
        print ("Son anagramas")
    else:
        print ("No son anagramas")
    a = "Hola"
    b = "Hello"
    print ("Las palabras", a, "y", b)
    if sonAnagramas(a,b) == True:
        print ("Son anagramas")
    else:
        print ("No son anagramas")
    a = "ana"
    b = "nana"
    print ("Las palabras", a, "y", b)
    if sonAnagramas(a,b) == True:
        print ("Son anagramas")
    else:
        print ("No son anagramas")
    print (" ")
        
    print ("Ejercicio 4: ")
    print (" ")
    a = [1,2,3,1,1,4,5]
    duplicados = hayDuplicados(a)
    if hayDuplicados(a) == True:
        print ("La lista", a, "si tiene duplicados")
    else:
        print ("La lista", a, "no tiene duplicados")
    a = [5,7,4,6,10]
    duplicados = hayDuplicados(a)
    if hayDuplicados(a) == True:
        print ("La lista", a, "si tiene duplicados")
    else:
        print ("La lista", a, "no tiene duplicados")
    print (" ")
    
    print ("Ejercicio 5: ")
    a = [1,8,3,4,3,1,8,2,7,8]
    print ("La lista original es", a)
    borrarDuplicados(a)
    print("Eliminando duplicados queda como: ",a)
    print (" ")
    
main()