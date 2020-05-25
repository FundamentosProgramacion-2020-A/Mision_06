#Autor: Brandon Julien Celaya Torres
#Descripción: Misión 6, diversos ejercicios con listas



def recortarLista (lista):
    
    if len (lista) <= 2: 
        
        return []
    
    nuevaLista = list(lista)
    ultimo = nuevaLista[len(nuevaLista)-1]
    nuevaLista.remove(ultimo)
    primero = nuevaLista[0]
    nuevaLista.remove(primero)
    
    return nuevaLista


def estanOrdenados(lista):
    
    if len (lista) >= 1 :
    
        nuevaLista = list(lista)
        nuevaLista.sort()
    
        if lista == nuevaLista:
            return True
    
        else:
        
            return False
    else:
        
        return []
    


def sonAnagramas (cadena1, cadena2):
    
    cadena1 = cadena1.upper ()
    cadena2 = cadena2.upper ()
    
    lista1 = list(cadena1)
    lista2 = list(cadena2)
    
    lista1.sort()
    lista2.sort()
    
    if lista1 == lista2:
        return True
    
    return False
    
    
    
def hayDuplicados (lista):
    
    for dato in lista:
        
        if lista.count (dato) >= 2:
            return True
    
    return False
        
        
        
def borrarDuplicados (lista):
    
    while hayDuplicados(lista) == True:
        
        for k in range(len(lista)):
            dato = lista[k]    #valor en la posición k de la lista
            veces = lista.count(dato)
            for n in range (veces-1):
                lista.remove(dato)
            if veces >=2:
                 break
             
             



def main ():
    
    a = [1,2]
    nuevaA = recortarLista(a)
    print ("La lista", a, "recortada es", nuevaA)
    
    
    
    
    b = [1,3,4,5,6,8,74,43]
    orden = estanOrdenados(b)
    
    if orden == True:
        
        print ("La lista", b, "está ordenada")
        
    else:
        
        print ("La lista", b, "no está ordenada")
        
    
    b = [10,100,1000,10000,100000,1000000,10000000,100000000]
    orden = estanOrdenados(b)
    
    if orden == True:
        
        print ("La lista", b, "está ordenada")
        
    else:
        
        print ("La lista", b, "no está ordenada")
    
    
    b = []
    orden = estanOrdenados(b)
    
    if orden == True:
        
        print ("La lista", b, "está ordenada")
        
    else:
        
        print ("La lista", b, "no está ordenada")
    
    
    
    
    
    cadenaA = "Amor"
    cadenaB = "Mora"
    anagrama = sonAnagramas(cadenaA, cadenaB)
    
    if anagrama == True:
        
        print("Las palabras", cadenaA, "y", cadenaB, "son anagramas")
        
        
    else:
        
        print("Las palabras", cadenaA, "y", cadenaB, "no son anagramas")
        
        
    cadenaA = "Rico"
    cadenaB = "Ruco"
    anagrama = sonAnagramas(cadenaA, cadenaB)
    
    if anagrama == True:
        
        print("Las palabras", cadenaA, "y", cadenaB, "son anagramas")
        
        
    else:
        
        print("Las palabras", cadenaA, "y", cadenaB, "no son anagramas")
    

    
        
        
    
        
        c = [1,2,3,4,5,6,7,8,9,9]
        
        repetido = hayDuplicados(c)
        
        if repetido == True:
            
            print ("La lista", c, "sí tiene números repetidos")
        else:
            
            print ("La lista", c, "no tiene números repetidos")
            
        c = []
        
        repetido = hayDuplicados(c)
        
        if repetido == True:
            
            print ("La lista", c, "sí tiene números repetidos")
        else:
            
            print ("La lista", c, "no tiene números repetidos")
        
        
        
        
            
        d = [1,2,3,4,5,4,4,4,4,5,6,7,6,5,5,4,2,1,9,10]
        print ("La lista original es:", d)
        borrarDuplicados(d)
        print ("La lista sin números repetidos es:", d)
        
        e = []
        print ("La lista original es:", e)
        borrarDuplicados(e)
        print ("La lista sin números repetidos es:", e)
            
            
         
    
main ()