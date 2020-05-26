#Autor: Elena R.Tovar
#Misión 6: Listas en Python


def recortarLista(lista):
    if len(lista)<=2:         #Verifica que la lista pueda ser cortada
        return[]
    list2=list(lista)         #crea una copia de la lista para editar
    ultimo=list2[len(list2)-1]
    list2.remove(ultimo)      #elimina el último elemento
    primero=list2[0]
    list2.remove(primero)     #elimina el primer elemento
    return list2              #regresa la lista editada

def estanOrdenados(lista):
    lista1=list(lista)        #crea una copia para edición
    lista1.sort()             #Ordena la lista en orden numérico
    if lista==lista1:         #Compara la lista original con la ordenada
        return True, lista1
    return False, lista1

def sonAnagramas(a,b):
    a=a.upper()               #pasa la cadena a mayúsculas
    b=b.upper()
    
    lista1=list(a)            #Convierte la cadena en lista
    lista2=list(b)
    
    lista1.sort()             #ordena la lista en orden alfabético
    lista2.sort()
    
    if lista1==lista2:        #compara las listas ordenadas
        return True
    return False

def hayDuplicados(lista):
    for dato in lista:        
        if lista.count(dato)>=2:   #revisa si un mismo dato existe más de una vez
            return True
    return False

def borrarDuplicados(lista):
    while hayDuplicados(lista)==True:  #verifica que haya repetición en la lista
        for k in range(len(lista)):
            dato=lista[k]              
            veces=lista.count(dato)    #cuenta el número de repeticiones del dato
            if veces>1:
                for n in range(veces-1): #descuenta el dato original
                    lista.remove(dato)   #elimina los datos repetidos
                break

def main():
    
    lista= [2,2,3,5]
    a=(input("Ingrese una palabra: "))
    b=(input("Ingrese una palabra para comparar: "))
    
    print("""Ejercicio 1:
""")
    print("La lista",lista,"al recortarse regresa",recortarLista(lista))
    print("La lista",lista,"está en orden? ",estanOrdenados(lista))
    print("¿Existen duplicados en la lista",lista,"?",hayDuplicados(lista))
    borrarDuplicados(lista)
    print("La lista sin duplicados es: ",lista)
    print("Las palabras",a,"y",b,"son anagramas? ", sonAnagramas(a,b))
   
   
main()

