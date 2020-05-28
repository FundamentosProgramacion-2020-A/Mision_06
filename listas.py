#Paulina Mendoza Iglesias
#Programa que corre diferentes funciones relacionadas a listas

def recortarLista(lista):
    if len(lista)<=2:
        return[]
    #COPIA
    nuevaLista = list(lista) #Duplicado
    ultimo = nuevaLista[len(nuevaLista)-1]
    nuevaLista.remove(ultimo) #Elimina el último valor
    primero = nuevaLista[0]
    nuevaLista.remove(primero)
    return nuevaLista


def estanOrdenados(lista):
    listaUno= list(lista)
    listaUno.sort()
    if lista == listaUno:
        return True, listaUno
    else:
        return False, listaUno
    


def sonAnagramas(cadena1, cadena2):
    cadena1 = cadena1.upper()
    cadena2 = cadena2.upper()
    
    lista1 = list(cadena1) #convierte la cadena en lista
    lista2 = list(cadena2) #["R", "O", "M", "A"]
    
    lista1.sort()
    lista2.sort()          #["A", "M", "O", "R"]
    
    if lista1 ==lista2:
        return True
    
    return False



def hayDuplicados(lista):
    for dato in lista:
        if lista.count(dato)>=2:
            return True  # Termina y da un resultado
    
    return False


    
    
def borrarDuplicados(lista):
    while hayDuplicados(lista) == True:
        #Elimina duplicados
        for k in range(len(lista)):
            dato = lista[k]
            veces = lista.count(dato)
            for n in range(veces-1):
                lista.remove(dato)
            
            if veces>=2:
                break
            

def main():
    
    
    print ("Ejercicio 1: ") #Primera función
    a = [1,2,3,4,5]
    nuevaA = recortarLista(a)
    print("La lista", a, "recortada es", nuevaA)
    
    a = [1,2]
    nuevaA = recortarLista(a)
    print ("La lista", a, "recortada es", nuevaA)
    
    a = []
    nuevaA = recortarLista (a)
    print ("La lista", a, "recortada es", nuevaA)
    
    
    
    print (" ")
    
    
    print ("Ejercicio 2: ") #Segunda función
    b = [9, 23, 50]
    orden = estanOrdenados(b)
    if orden == True:
        print ("La lista", b, "está ordenada")
    else:
        print ("La lista", b, "no está ordenada")
        
    
    b = [9, 50, 23]
    orden = estanOrdenados(b)
    if orden == True:
        print ("La lista", b, "está ordenada")
    else:
        print ("La lista", b, "no está ordenada")
        
        
        
    print (" ")
    
    
    
    print ("Ejercicio 3: ") #Tercera función
    cadenaUno = "Roma"
    cadenaDos = "Mora"
    anagrama = sonAnagramas (cadenaUno, cadenaDos)
    print("Las palabras", cadenaUno, "y", cadenaDos)
    if sonAnagramas (cadenaUno,cadenaDos)==True:
        print("Son anagramas")
    else:
        print("No son anagramas")
        
        
    cadenaUno = "Árbol"
    cadenaDos = "Lago"
    anagrama = sonAnagramas (cadenaUno, cadenaDos)
    print("Las palabras", cadenaUno, "y", cadenaDos)
    if sonAnagramas (cadenaUno, cadenaDos)==True:
        print("Son anagramas")
    else:
        print("No son anagramas")
        
    
    cadenaUno = "Cocoa"
    cadenaDos = "Coco"
    anagrama = sonAnagramas (cadenaUno, cadenaDos)
    print("Las palabras", cadenaUno, "y", cadenaDos)
    if sonAnagramas (cadenaUno, cadenaDos)==True:
        print("Son anagramas")
    else:
        print("No son anagramas")
        
        
    
    print (" ")
    
    
        
    print ("Ejercicio 4: ") #Cuarta función     
    c = [1,2,3,4,5,1]
    duplicar = hayDuplicados (c)
    if duplicar == True:
        print ("La lista", c, "tiene números duplicados")
        
    else:
        print ("La lista", c, "no tiene números duplicados")
        
        
    c = [1,2,3,4,5,6]
    duplicar = hayDuplicados (c)
    if duplicar == True:
        print ("La lista", c, "tiene números duplicados")
        
    else:
        print ("La lista", c, "no tiene números duplicados")
        
        
    
    print (" ")
    
    
    print ("Ejercicio 5: ")
    d = [1,2,3,6,7,8,8,9]
    print ("La lista original es", d)
    borrarDuplicados(d)
    print("eliminando duplicados queda como: ", d)
    
    d = [1,2,3,4]
    print ("La lista original es", d)
    borrarDuplicados(d)
    print("eliminando duplicados queda como: ", d)
    
    d = []
    print ("La lista original es", d)
    borrarDuplicados(d)
    print("eliminando duplicados queda como: ", d)
    


    
    
main()
