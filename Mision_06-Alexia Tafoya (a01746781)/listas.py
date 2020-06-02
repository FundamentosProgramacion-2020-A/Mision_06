#Autor: Anayansi Alexia Tafoya Soto
# Misión 06. Listas

def recortarLista(lista):
    if len(lista) <= 2:
        return []
    # COPIA
    nuevaLista = list (lista)   #DUPLICADO
    ultimo = nuevaLista [len(nuevaLista)-1]
    nuevaLista.remove (ultimo)   #Elimina el ultimo dato
    primero = nuevaLista [0]
    nuevaLista.remove (primero)
    return nuevaLista

   
def estanOrdenados(valores):
    lista = list(valores)
    lista.sort()
    if valores == lista:
        return True
    else:
        return False
    
    
def sonAnagramas(cadena1, cadena2):
    cadena1 = cadena1.upper()
    cadena2 = cadena2.upper()
    
    lista1 = list(cadena1)  #convierte la cadena en lista ["r", "o", "m", "a"]
    lista2 = list(cadena2) 
    
    lista1.sort()      #Ordena de menor a mayor o alfabeticamente
    lista2.sort()        # ["a", "m", "o", "r"]
    
    if lista1 == lista2:
        return True
    else:
        return False
    
    
def hayDuplicados(enteros):
    for dato in enteros:
        if enteros.count (dato) >= 2:
            return True
    return False
     
  
def borrarDuplicados(lista):
    while hayDuplicados (lista)==True:   #Elimina duplicados
        for k in range (len(lista)):
            dato = lista[k]
            veces = lista.count(dato)
            for n in range (veces-1):  #Borra tantas veces -1, como aparezca el valor en la lista
                lista.remove(dato)
            if veces>=2:
                break
  
  
def main():
    lista = [1,2,3,4,5]
    a = recortarLista(lista)
    print ("Ejercicio 1: ")
    print ("La lista original", lista, ", regresa", a)
    lista = []
    b = recortarLista(lista)
    print ("La lista original", lista, ", regresa", b)
    lista = [7,8]
    c = recortarLista(lista)
    print ("La lista original", lista, ", regresa", c)
    
    
    print ("\n ") 
    
    
    print ("Ejercicio 2: ")
    valores = [1,2,3,4,5]
    print ("Los elementos de la lista: ", valores) 
    if estanOrdenados (valores) == True:
        print ("Están ordenados")
    else:
        print ("No están ordenados")
    
    valores = [36,4,9,24]
    print ("Los elementos de la lista: ", valores) 
    if estanOrdenados (valores) == True:
        print ("Están ordenados")
    else:
        print ("No están ordenados")
    
    
    print ("\n ") 
    
    
    print ("Ejercicio 3:")
    cadena1 = "Roman"
    cadena2 = "Amor"
    print ("Las palabras", cadena1, "y", cadena2)
    if sonAnagramas (cadena1,cadena2) == True:
        print ("Son anagramas")
    else:
        print ("No son anagramas")
        
    cadena1 = "Jabon"
    cadena2 = "Banjo"
    print ("Las palabras", cadena1, "y", cadena2)
    if sonAnagramas (cadena1,cadena2) == True:
        print ("Son anagramas")
    else:
        print ("No son anagramas")
        
        
    print ("\n ") 
     
     
    print ("Ejercicio 4: ")
    enteros = [1,2,3,4,5,3]
    print ("En la lista", enteros)
    if hayDuplicados (enteros) == True:
        print ("Hay duplicados")
    else:
        print ("No hay duplicados")
        
    enteros = [2,4,6,8,10]
    print ("En la lista", enteros)
    if hayDuplicados (enteros) == True:
        print ("Hay duplicados")
    else:
        print ("No hay duplicados")

    
    print ("\n ")
    
    
    print ("Ejercico 5:")
    x = [1,8,3,4,3,1,8,2,7,8]
    print ("La lista original es", x)
    borrarDuplicados(x)
    print ("Eliminando duplicados es ", x)
    
    x = [5,2,7,9,3,2,4,5,7]
    print ("La lista original es", x)
    borrarDuplicados(x)
    print ("Eliminando duplicados es ", x)
    
main()
