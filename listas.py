#Kathia Alejandra Cervantes López
#Este programa realiza listas de diferentes maneras



#Función para recortar la lista
def recortarLista (lista):
    #condición para dejar en blanco si sólo hay dos o menos números
    if len(lista) <=2:
        return []
    nuevaLista = list(lista)
    #se quita el último número de la lista
    ultimo = nuevaLista[len(nuevaLista)-1]
    nuevaLista.remove(ultimo)
    #se quita el primer número de la lista
    primero = nuevaLista[0]
    nuevaLista.remove(primero)
    return nuevaLista


#Función para ver si estan ordenados los números
def estanOrdenados (lista):
    
    lista1 = list(lista)
    lista1.sort()
    #condición
    if lista1 == lista:
        return True
        
    else:
        return False
    

#Función para convertir las cadenas en listas
def sonAnagramas (cadena1, cadena2):
    #se asegura de que todas las letras son mayúsculas
    cadena1 = cadena1.upper()
    cadena2 = cadena2.upper()
    
    #convierte las cadenas en listas
    lista1 = list(cadena1) 
    lista2 = list(cadena2) 
    
    #ordena las listas
    lista1.sort() 
    lista2.sort()
    
    #condición
    if lista1 == lista2:
        return True
        
    else:
        return False
    
    
def hayDuplicados (lista):
    #Para tomar el valor de cada elemento en la lista
    for dato in lista :
        #condición
        if lista.count(dato)>=2:
            return True 
          
    return False


#Función para saber si hay números duplicados
def borrarDuplicados (lista):
    while hayDuplicados(lista) == True:
        for l in range(len(lista)):
            dato = lista[l]
            veces = lista.count(dato)
            #borra los número duplicados
            for n in range (veces-1): 
                lista.remove(dato)
            if veces >=2:
                break
    

#Función principal
def main ():
    #Ejercicio 1
    print ("Ejercicio 1")
    #opción que recibe muchos números
    a = [1,2,3,4,5,6,7,8,9]
    nuevaListaA = recortarLista(a)
    print ("La lista", a, "al recortarla queda así: ", recortarLista(a))
    
    #opción que recibe tres números
    b = [26,27,28]
    nuevaListaB = recortarLista (b)
    print ("La lista", b, "al recortarla queda así: ", recortarLista(b))
    
    #opción que no recibe números
    c = []
    nuevaListaC = recortarLista (c)
    print ("La lista", c, "al recortarla queda así: ", recortarLista(c))
    
    
    #Ejercicio 2
    print("\n")
    print ("Ejercicio 2")
    #prueba ordenada
    uno = [1,2,3,4,5,6,7,8,9]
    print ("Los numeros", uno)
    orden = estanOrdenados(uno)
    
    #condición
    if orden == True:
        print ("Estan ordenados")
    else:
        print ("No estan ordenados")
    
    #prueba desordenada
    dos = [1,5,2,4,3,8,7,9,6]
    print ("Los números", dos)
    ordenDos = estanOrdenados(dos)
    
    #condición
    if ordenDos == True:
        print ("Están ordenados")
    else:
        print ("No están ordenados")
        
        
    #Ejercicio 3
    print ("\n")
    print ("Ejercicio 3")
    #prueba correcta
    a = "frase"
    b = "fresa"
    print ("Las palabras", a, "y", b,":")
    #condición
    if sonAnagramas(a,b) == True:
        print ("Son anagramas")
    else:
        print ("No son anagramas")
    
    #prueba incorrecta
    a = "amor"
    b = "ramón"
    print ("Las palabras", a, "y", b, ":")
    #condición
    if sonAnagramas(a,b) == True:
        print ("Son anagramas")
    else:
        print ("No son anagramas")
        
        
    #Ejercicio 4
    print ("\n")
    print("Ejercicio 4")
    #números duplicados
    a = [1,3,4,6,8,4,2,6,9,5]
    print ("En la lista", a)
    nueva = hayDuplicados(a)
    if nueva == True:
        print ("Hay números duplicados")
    else:
        print ("No hay números duplicados")
     
    #numeros únicos
    b = [1,3,4,6,8,2,5,7,9,0]
    print ("En la lista", b)
    nueva = hayDuplicados(b)
    if nueva == True:
        print ("Hay números duplicados")
    else:
        print ("No hay números duplicados") 
    
    
    #Ejercicio 5
    print ("\n")
    print ("Ejercicio 5")
    #Números repetidos
    unicos = [1,3,4,6,8,4,2,4,5,4,5,3,4,5,4]
    print ("La lista original es:", unicos)
    borrarDuplicados(unicos)
    print ("Elimanando los números duplicados queda: ", unicos)
    
    #Números únicos
    unicos = [0,9,8,7,6,5,4,3,2,1]
    print ("La lista original es:", unicos)
    borrarDuplicados(unicos)
    print ("Elimanando los números duplicados queda: ", unicos)
    
    #Sin números
    unicos = []
    print ("La lista original es:", unicos)
    borrarDuplicados(unicos)
    print ("Elimanando los números duplicados queda: ", unicos)
    
#Llamar a la función
main ()