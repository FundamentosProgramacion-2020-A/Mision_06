#Autor: Guadalupe Iveth Serrano Hernández
#Listas misión 6

def recortarLista(lista):
    if len(lista) <= 2:
        return []
    nuevaLista = list(lista)
    ultimo = nuevaLista[len(nuevaLista)-1]
    nuevaLista.remove(ultimo)
    primero = nuevaLista[0]
    nuevaLista.remove(primero)
    return nuevaLista
    

def estanOrdenados(lista):
    valor1 = list(lista)
    valor2 = list(lista)
    valor2.sort()
    for lista in valor1:
        if valor1 == valor2:
            return True
    return False

def sonAnagramas(cadena1, cadena2):
    cadena1 = cadena1.upper()
    cadena2 = cadena2.upper()
    
    lista1 = list(cadena1) 
    lista2 = list(cadena2)  
    
    lista1.sort()             
    lista2.sort()    
    
    if lista1 == lista2:
        return True
    return False
    
def hayDuplicados(lista):
    for dato in lista:
        if lista.count(dato)>=2:
            return True
    
    return False
    
def borrarDuplicados(lista):
    while hayDuplicados(lista) == True:
        for k in range (len(lista)):
            dato = lista[k]
            veces = lista.count(dato)
            for n in range (veces-1):    
                lista.remove(dato)
            if veces >= 2:
                break           
             
    
def main():
    a = [1,2,4,5,45,2,4,8,7,6,5,3]
    b = recortarLista(a)
    a2 = [1, 2]
    b2 = recortarLista(a2)
    print("Al quitarle el primer y último elemento a la lista", a, "queda así: ", b)
    print("Al quitarle el primer y último elemento a la lista", a2, "queda así: ", b2)
    
    valor = [4, 1, 6]
    valoresOrdenados = estanOrdenados(valor)
    valores = [8, 32, 50]
    valoresOrdenados2 = estanOrdenados(valores)
    print("¿Los valores", valor, "están ordenados? ", valoresOrdenados)
    print("¿Los valores", valores, "están ordenados?", valoresOrdenados2)
    
    cadenaA = "licua"
    cadenaB = "Lucia"
    cadenaC = "frase"
    cadenaD = "FreSa"
    print (cadenaA, "y", cadenaB, "¿son anagramas?", sonAnagramas(cadenaA, cadenaB))
    print (cadenaC, "y", cadenaD,"¿son anagramas?", sonAnagramas(cadenaC, cadenaD))
    print (cadenaA, "y", cadenaC,"¿son anagramas?", sonAnagramas(cadenaA, cadenaC))
    print (cadenaB, "y", cadenaD,"¿son anagramas?", sonAnagramas(cadenaB, cadenaD))
    
    lista = [1, 2, 3, 4, 5]
    lista2 = [2, 4, 8, 20, 8, 8, 4, 3, 2, 1]
    print ("¿La lista", lista, "tiene duplicados?", hayDuplicados (lista))
    print ("¿La lista", lista2, "tiene duplicados?", hayDuplicados (lista2))

    listaDup = [1, 2, 3, 4, 5, 4, 1, 2, 3]
    print ("La lista original es:", listaDup)
    borrarDuplicados(listaDup)
    print("eliminando duplicados queda como", listaDup)
    
main()