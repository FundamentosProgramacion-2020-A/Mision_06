#Autor José Manuel Rivera Sosapavón
#Misión 06

def recortarLista (lista): #Ejercicio 1
    if len(lista) <=2:
        return []
    nuevaLista=list(lista)
    ultimo = nuevaLista[len(nuevaLista)-1]
    nuevaLista.remove(ultimo)
    primero = nuevaLista[0]
    nuevaLista.remove(primero)
    return nuevaLista

def estanOrdenados (lista1,lista2): #Ejercicio 2
    lista2.sort()
    
    if lista1 == lista2:
        return True
    return False
    
    

def sonAnagramas (cadena1, cadena2): #Ejercicio 3
    cadena1 = cadena1.upper()
    cadena2 = cadena2.upper()
    
    lista1 = list(cadena1)
    lista2 = list(cadena2)
    
    lista1.sort()
    lista2.sort()
    
    if lista1 == lista2:
        return True
    
    return False

def hayDuplicados(lista): #Ejercicio 4
    for dato in lista:
        if lista.count(dato) >=2:
            return True
    return False

def borrarDuplicados (lista): #Ejercicio 5
    while hayDuplicados(lista) ==True:
        for k in range(len(lista)):
            dato = lista[k]
            veces = lista.count (dato)
            for n in range(veces -1):
                lista.remove(dato)
            if veces>=2:
                break
    

def main():
    #1
    a = [4,3,2,1]
    nuevaA = recortarLista(a)
    print(" Ejercicio 1:")
    print ("La lista",a,"recortada es", nuevaA)
    b = [9,8,7,6,5]
    nuevaB = recortarLista(b)
    print ("La lista",b,"recortada es", nuevaB)
    c = []
    nuevaC = recortarLista(c)
    print ("La lista",c,"recortada es", nuevaC)
    print ("--------------")
    
    #2
    print("Ejercicio 2:")
    a = [1,2,3,5,4]
    b = [2,5,4,3,1]
    print (estanOrdenados(a,b))
    c = [6,7,8,9]
    d = [6,7,8,9]
    print (estanOrdenados(c,d))
    e = [5,7,9,3,5]
    f = [3,5,5,7,9]
    print (estanOrdenados(e,f))
    print("---------------")
    
    #3
    print("Ejercico 3:")
    a = "OmAr"
    b = "Mora"
    print ("Las palabras",a,"y",b)
    if sonAnagramas(a,b) ==True:
        print ("son anagramas.")
    else:
        print ("No son anagramas.")
    c = "Roma"
    d = "moro"
    print ("Las palabras",c,"y",d)
    if sonAnagramas(c,d) ==True:
        print ("son anagramas.")
    else:
        print ("No son anagramas.")
    e = "Maro"
    f = "AMOR"
    print ("Las palabras",e,"y",f)
    if sonAnagramas(e,f) ==True:
        print ("son anagramas.")
    else:
        print ("No son anagramas")
    print ("--------------")
    
    #4
    print("Ejercicio 4:")   
    a = [1,2,1,3,5,4]
    print(hayDuplicados(a))
    b = [5,6,3,4,7,1]
    print(hayDuplicados(b))
    c = [2,4,6,2,4,7,8]
    print(hayDuplicados(c))
    print ("--------------")
    
    #5
    print("Ejercicio 5:")
    a = [3,5,7,6,4,3,1,9,8,3,3]
    print ("La lista original es",a)
    borrarDuplicados (a)
    print ("eliminando duplicados queda como: ",a)
    b = [7,8,9,5,6,4,3,2,1]
    print ("La lista original es",b)
    borrarDuplicados (b)
    print ("eliminando duplicados queda como: ",b)
    c = [5,7,6,5,7,8,9,1,2,3]
    print ("La lista original es",c)
    borrarDuplicados (c)
    print ("eliminando duplicados queda como: ",c)
    print ("--------------")
    
    
    
    
main()