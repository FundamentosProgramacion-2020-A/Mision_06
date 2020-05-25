#AUTOR: Alondra Miranda Aguilera A01746742
#Misión 6: Listas

def sonAnagramas(cadena1, cadena2):
    cadena1 = cadena1.upper()
    cadena2 = cadena2.upper()
    
    lista1 = list(cadena1)
    lista2 = list(cadena2)
    
    lista1.sort()
    lista2.sort()
    
    if lista1==lista2:
        return True
    return False


def recortarLista(lista):
    if len(lista)<=2:
        return []
    #copia
    nuevaLista = list(lista) #Duplicado
    ultimo = nuevaLista[len(nuevaLista)-1]
    nuevaLista.remove(ultimo)
    primero = nuevaLista[0]
    nuevaLista.remove(primero)
    return nuevaLista

def estanOrdenados(lista):
    nuevaLista = list(lista)
    nuevaLista.sort()
    if lista == nuevaLista:
        return "Si están ordenados"
    else:
        return "No están ordenados"
    

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
            for n in range(veces-1):
                lista.remove(dato)
            if veces>=2:
                break
        return lista
            
#------------------------------------------------------

def main():
    print("ANAGRAMAS")
    a = input("Dame una palabra: ")
    b = input("Dame otra palabra: ")
    
    print("Las palabras", a, "y", b)
    if sonAnagramas(a,b) == True:
        print("Son anagramas")
    else:
        print("No son anagramas")        
    
#--------------------------------------- PIDE LISTA
    lista = [] #lista vacía
    
    num = int(input("Teclea un número, si ya no quieres teclear presiona -1: "))
    while num != -1:
        #Procesar dato
        lista.append(num)
        
        #Leer Nuevamente
        num = int(input("Teclea un número, si ya no quieres teclear presiona -1: "))
    
    print(lista)
    
#-------------------------------------YA HAY UNA LISTA
    
    print("RECORTAR LISTA")
    n = recortarLista(lista)
    print(n)
    
    print("DUPLICADOS")
    print(hayDuplicados(lista))
    
    print("BORRAR DUPLICADOS")
    print("La lista original es: ", lista)
    x = borrarDuplicados(lista)
    print("Eliminando duplicados queda como: ", x)
    
    print("ORDENADOS")
    print(estanOrdenados(lista))
              
main()