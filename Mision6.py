# Patricio León
# Misión 6


def recortarLista(lista):
    if len(lista)<=2:
        return []
    #COPIA
    nuevaLista = list(lista)    #Duplicado
    ultimo = nuevaLista[len(nuevaLista)-1]
    nuevaLista.remove(ultimo)   #Elimina el último dato
    primero = nuevaLista[0]
    nuevaLista.remove(primero)
    return nuevaLista


def estanOrdenados(lista):
    for dato in lista:
        if lista.sort(dato)>=2:
            return True      # TERMINA y me da un resultado
    return False


def sonAnagramas(cadena1, cadena2):
    cadena1 = cadena1.upper()
    cadena2 = cadena2.upper()
    
    lista1 = list(cadena1)   # convierte la cadena en lista
    lista2 = list(cadena2)   # ["R", "O", "M", "A"]
    
    lista1.sort()
    lista2.sort()            # ["A", "M", "O", "R"]
    
    if lista1==lista2:
        return True
    
    return False


def hayDuplicados(lista):
    for dato in lista:
        if lista.count(dato)>=2:
            return True      # TERMINA y me da un resultado
    return False


def borrarDuplicados(lista):
    while hayDuplicados(lista)== True:
        # Elimina duplicados
        for k in range(len(lista)):   #[1,2,3,2,7,6,2,2,9]
            dato = lista[k]
            veces = lista.count(dato)
            for n in range(veces-1):    # Borra tantas veces menos 1 como aparezca el valor en la lista
                lista.remove(dato)
            if veces>=2:
                break
            

    
def main():
    a = [4,7,1,3,4,2]
    nuevaA = recortarLista(a)
    print("La lista", a, "recortada es", nuevaA)
    
    
    a = "Roma"
    b = "Mora"
    print("Las palabras", a, "y", b)
    if sonAnagramas(a,b)==True:
        print("Son anagramas")
    else:
        print("No son anagramas")
        
        
    a= [1,2,3,4,1,5]
    print(hayDuplicados(a))
    
    
    a = [1,2,3,2,7,6,2,2,9]
    print("La lista original es", a)
    borrarDuplicados(a)
    print("Eliminando duplicados queda como: ", a)
    
    
main()