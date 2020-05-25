#Autor: Michelle Ojeda Manjarrez
# Ejercicios con listas

#Defines la función recortar lista
def recortarLista (lista):
    if len (lista) <= 2:
        return []
    
    #COPIA
    nuevaLista = list(lista)      #Duplicado
    ultimo = nuevaLista[len(nuevaLista)-1]
    nuevaLista.remove(ultimo)     #Elimina el ultimo dato
    
    primero = nuevaLista[0]
    nuevaLista.remove(primero)
    return nuevaLista


#Defines la función recortar lista
def estanOrdenados (lista):
    #Copia
    nuevaLista = list(lista)
    nuevaLista.sort()              #Ordenas la lista
    
    if nuevaLista == lista:
        return True
    return False
    
#Defines la función son anagramas
def sonAnagramas (cadena1, cadena2):
    cadena1 = cadena1.upper()
    cadena2 = cadena2.upper()
    
    lista1 = list(cadena1)  #Convertir cadena a lista
    lista2 = list(cadena2)
    
    lista1.sort()           #Se ordena la lista
    lista2.sort()
    
    if lista1 == lista2:
        return True
    else:
        return False
    
    
#Defines la función hay duplicados   
def hayDuplicados (lista):
    
    #Checamos si hay un dato que se repita
    for dato in lista:
        if lista.count(dato) >=2:
            return True 
    return False


#Llamámos a la función borrar duplicados
def borrarDuplicados (lista):
    while hayDuplicados(lista) == True:
        #Elimina duplicados
        for k in range(len(lista)):
            dato = lista[k]
            veces = lista.count(dato)
            for n in range(veces-1): #Veces -1 por que el dato se tiene que quedar al menos una vez en la lista
                lista.remove(dato)
            if veces >=2:
                break
            
            
#Llamámos a la función principal
def main ():
    
    #Ejercicio uno
    print ("Ejercicio 1: ")
    uno = [1,2,3,4,5]
    listaUno = recortarLista(uno)
    print ("La lista", uno, "regresa la lista recortada", listaUno)
    
    uno = [1,2]
    listaUno = recortarLista(uno)
    print ("La lista", uno, "regresa la lista recortada", listaUno)
    
    uno = []
    listaUno = recortarLista(uno)
    print ("La lista", uno, "regresa la lista recortada", listaUno)
    
    print("---------------------------")
    
    
    #Ejercicio dos
    print ("Ejercicio 2: ")
    
    dos= [7, 12, 53]
    listaDos = estanOrdenados (dos)
    if listaDos == True:
        print ("La lista", dos, "está ordenada")
    else:
        print ("La lista", dos, "no está ordenada")
        
    dos= [7, 23, 15]
    listaDos = estanOrdenados (dos)
    if listaDos == True:
        print ("La lista", dos, "está ordenada")
    else:
        print ("La lista", dos, "no está ordenada")
        
    print("---------------------------")
        
    #Ejercicio 3
    print ("Ejercicio 3: ")
    
    cadena1 = "Roma"
    cadena2 = "Mora"
    listaTres = sonAnagramas (cadena1, cadena2)
    if sonAnagramas (cadena1, cadena2) == True:
        print ("La palabra", cadena1, "y", cadena2, "sí son anagramas")
    else:
        print ("La palabra", cadena1, "y", cadena2, "no son anagramas")


    cadena1 = "Hola"
    cadena2 = "Hello"
    listaTres = sonAnagramas (cadena1, cadena2)
    if sonAnagramas (cadena1, cadena2) == True:
        print ("La palabra", cadena1, "y", cadena2, "sí son anagramas")
    else:
        print ("La palabra", cadena1, "y", cadena2, "no son anagramas")


    cadena1 = "Ana"
    cadena2 = "Nana"
    listaTres = sonAnagramas (cadena1, cadena2)
    if sonAnagramas (cadena1, cadena2) == True:
        print ("La palabra", cadena1, "y", cadena2, "sí son anagramas")
    else:
        print ("La palabra", cadena1, "y", cadena2, "no son anagramas")

    print("---------------------------")
    
    #Ejercicio 4
    print ("Ejercicio 4: ")
    
    cuatro = [1,2,3,1,4,5]
    listaCuatro = hayDuplicados (cuatro)
    if listaCuatro == True:
        print ("En la lista", cuatro, "sí existen duplicados")
    else:
        print ("En la lista", cuatro, "no existen duplicados")
        
    cuatro = [5,7,4,6,10]
    listaCuatro = hayDuplicados (cuatro)
    if listaCuatro == True:
        print ("En la lista", cuatro, "sí existen duplicados")
    else:
        print ("En la lista", cuatro, "no existen duplicados")
      
    print("---------------------------")
    
    #Ejercicio 5
    print ("Ejercicio 5: ")
        
    cinco = [1,8,3,4,3,1,8,2,7,8]
    print ("La lista original es: ", cinco)
    borrarDuplicados (cinco)
    print ("Eliminando duplicados queda como: ", cinco)
    
    cinco = [1,2]
    print ("La lista original es: ", cinco)
    borrarDuplicados (cinco)
    print ("Eliminando duplicados queda como: ", cinco)
    
    cinco = []
    print ("La lista original es: ", cinco)
    borrarDuplicados (cinco)
    print ("Eliminando duplicados queda como: ", cinco)
      
main()