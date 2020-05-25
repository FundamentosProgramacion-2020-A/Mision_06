# Autor: Daniel Rojas, A01376572
# Misión 6. Listas en Python

def recortarLista(enteros):   #Elimina el primer y último valor de una lista
    enteros2 = []
    for indice in range(len(enteros)):
        n = enteros[indice]
        if indice != 0 and indice != len(enteros)-1:
            enteros2.append(n)
    return enteros2


def estanOrdenados(lista):
    orden = sorted(lista)
    if orden == lista:
        return True
    else:
        return False
    
    
def sonAnagramas(a,b):
    orden1 = sorted(a.lower())
    orden2 = sorted(b.lower())
    print(orden1)
    print(orden2)
    if orden1 == orden2:
        return True
    else:
        return False
    

def hayDuplicados(enteros):
    for x in enteros:
        veces = enteros.count(x)
        if veces > 1:
            return True
            break
        else:
            continue
    return False
    
    
def borrarDuplicados(enteros):
    while hayDuplicados(enteros)==True:
        for indice in range(len(enteros)):
            dato = enteros[indice]
            veces = enteros.count(dato)
            for n in range(veces-1):
                enteros.remove(dato)
            if veces>=2:
                break
        

def main():
    print("Ejercicio 1:")   #Ejercicio 1
    enteros = [1,2,3,4,5]
    enterosRecortada = recortarLista(enteros)
    print("Lista original", enteros, ", recortada es", enterosRecortada)
    
    print("""
Ejercicio 2:""")             #Ejercicio 2
    lista = [7,12,53]
    ordenada = estanOrdenados(lista)
    if ordenada == True:
        print("La lista",lista,"SÍ está ordenada")
    else:
        print("La lista",lista,"NO está ordenada")
    
    print("""
Ejercicio 3:""")             #Ejercicio 3
    cadena1 = "Roma"
    cadena2 = "Mora"
    anagrama = sonAnagramas(cadena1,cadena2)
    if anagrama == True:
        print(cadena1, "y", cadena2, "SÍ son anagramas")
    else:
        print(cadena1, "y", cadena2, "NO son anagramas")

    print("""
Ejercicio 4:""")             #Ejercicio 4
    lista = [2,8,5,3,4]
    duplicados = hayDuplicados(lista)
    if duplicados == True:
        print("En la lista",lista,"SÍ hay números duplicados")
    else:
        print("En la lista",lista,"NO hay duplicados")
    
    print("""
Ejercicio 5:""")             #Ejercicio 5
    lista = [1,2,2,2,3,3,3,4,5]
    print("La lista original es",lista)
    borrarDuplicados(lista)
    print("Y sin números duplicados queda así:",lista)
    
    
main()