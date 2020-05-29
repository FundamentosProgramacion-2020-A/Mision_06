def recortarLista(lista):
    if len(lista)<=1:
        return []
    #Copia
    nuevaLista = list(lista)  #Duplicado
    ultimo = nuevaLista[len(nuevaLista)-1]
    nuevaLista.remove(ultimo)
    primero = nuevaLista[0]
    nuevaLista.remove(primero)
    return nuevaLista

def estanOrdenados(lista):
    nuevalista = list(lista) #Copia de la lista
    nuevalista.sort() #Lista ordenada
    if nuevalista == lista: #Comparación
        return True
    return False

def sonAnagramas(cadena1, cadena2):
    cadena1 = cadena1.upper()
    cadena2 = cadena2.upper()
    
    lista1 = list(cadena1) #convierte la cadena en lista
    lista2 = list(cadena2) # [R,O,M,A]
    
    lista1.sort()
    lista2.sort()  # [A,M,O,R]
    
    if lista1==lista2:
        return True
    return False

def hayDuplicados(lista):
    for dato in lista:
        if lista.count(dato)>=2:
            return True   #Termina y me da un resultado
    
    return False 

def borrarDuplicados(lista):
    while hayDuplicados(lista) == True:
        # Elimina duplicados
        for k in range (len(lista)):
            dato = lista[k]
            veces = lista.count(dato)
            for n in range(veces-1):  #Borra tantas veces como esta repetida
                lista.remove(dato)
            if veces>2:
                break

def main():
    print("Ejercicio 1:")
    a = [1,2,3,4,5,6,7]
    nuevaA = recortarLista(a)
    print("La lista",a, "recortada es", nuevaA)
    
    aa = [1,2,3]
    paroim = estanOrdenados(aa)
    print("La lista", aa, "¿Estan ordenados?",paroim)
    
    c = "Omar"
    d = "Mora"
    print("¿Son anagramas?", c, "y", d)
    if sonAnagramas(c,d)==True:
        print("Son anagramas")
    else:
        print("No son anagramas")
        
    cc = [1,2,3,4,5]
    print("¿Hay duplicados en la lista?",cc, hayDuplicados(cc))
    
    dd = [1,2,5,5,3,4,5,6,7,7,7,8,8,8]
    print("La lista original es", dd)
    borrarDuplicados(dd)
    print("Eliminando duplicados queda como:",dd)
    
    print("_____________\n")
    print("Ejercicio 2:")
    a = [2,4,5,7,8,9]
    nuevaA = recortarLista(a)
    print("La lista",a, "recortada es", nuevaA)
    
    aa = [1,5,3,7,8,10]
    paroim = estanOrdenados(aa)
    print("La lista", aa, "¿Estan ordenados?",paroim)
    
    c = "Luz"
    d = "Rojo"
    print("¿Son anagramas?", c, "y", d)
    if sonAnagramas(c,d)==True:
        print("Son anagramas")
    else:
        print("No son anagramas")
        
    cc = [3,4,4,5,6,7,7]
    print("¿Hay duplicados en la lista?",cc, hayDuplicados(cc))
    
    dd = [1,2,5,5,3,4,5,6,7,7,7,8,8,8]
    print("La lista original es", dd)
    borrarDuplicados(dd)
    print("Eliminando duplicados queda como:",dd)
   
    print("_____________\n")
    print("Ejercicio 3:")
    a = [3,4,6,7,8,9]
    nuevaA = recortarLista(a)
    print("La lista",a, "recortada es", nuevaA)
    
    aa = [1,4,6,7,9,3]
    paroim = estanOrdenados(aa)
    print("La lista", aa, "¿Estan ordenados?",paroim)
    
    c = "Amor"
    d = "Roma"
    print("¿Son anagramas?", c, "y", d)
    if sonAnagramas(c,d)==True:
        print("Son anagramas")
    else:
        print("No son anagramas")
        
    cc = [3,4,5,6,7]
    print("¿Hay duplicados en la lista?",cc, hayDuplicados(cc))
    
    dd = [1,2,5,5,3,4,5,6,7,7,7,8,8,8]
    print("La lista original es", dd)
    borrarDuplicados(dd)
    print("Eliminando duplicados queda como:",dd)
    
    print("_____________\n")
    print("Ejercicio 4:")
    a = [2,4,5,7,8,9,10,13,16]
    nuevaA = recortarLista(a)
    print("La lista",a, "recortada es", nuevaA)
    
    aa = [1,2,3,4,5,6,7]
    paroim = estanOrdenados(aa)
    print("La lista", aa, "¿Estan ordenados?",paroim)
    
    c = "Carro"
    d = "Amarillo"
    print("¿Son anagramas?", c, "y", d)
    if sonAnagramas(c,d)==True:
        print("Son anagramas")
    else:
        print("No son anagramas")
        
    cc = [2,4,5,7,7,8,9,12,12,15,17]
    print("¿Hay duplicados en la lista?",cc, hayDuplicados(cc))
    
    dd = [1,2,5,5,3,4,5,6,7,7,7,8,8,8]
    print("La lista original es", dd)
    borrarDuplicados(dd)
    print("Eliminando duplicados queda como:",dd)
    
    print("_____________\n")
    print("Ejercicio 5:")
    a = [12,14,15,17,18,19]
    nuevaA = recortarLista(a)
    print("La lista",a, "recortada es", nuevaA)
    
    aa = [5,6,8,9,10]
    paroim = estanOrdenados(aa)
    print("La lista", aa, "¿Estan ordenados?",paroim)
    
    c = "Frase"
    d = "Fresa"
    print("¿Son anagramas?", c, "y", d)
    if sonAnagramas(c,d)==True:
        print("Son anagramas")
    else:
        print("No son anagramas")
        
    cc = [2,4,5,7,8,9,14,16,17]
    print("¿Hay duplicados en la lista?",cc, hayDuplicados(cc))
    
    dd = [1,2,5,5,3,4,5,6,7,7,7,8,8,8]
    print("La lista original es", dd)
    borrarDuplicados(dd)
    print("Eliminando duplicados queda como:",dd)
   
main()