# Autor: Miguel Castillo Ordaz
# Programa que recorta el primer y el último valor de una lista.

def recortarLista(lista):
    
    if len(lista)<=2: # Conversión de la lista para creación de nueva lista.
        return[]
    else:
        nuevaLista = list(lista) # Se crea una nueva lista con los valores de la misma lista.
        ultimo = nuevaLista[len(nuevaLista)-1] # Se remueve el último valor de la nueva lista.
        nuevaLista.remove(ultimo)
        primero = nuevaLista[0] # Se remueve el primer valor de la nueva lista.
        nuevaLista.remove(primero)
        return nuevaLista

def main(): # Pruebas de funcionamiento.
    
    
    a = [1,1,1,1,1]
    nuevaA = recortarLista(a)
    print("La lista", a,"recortada es", nuevaA)
    
    print("")
    
    a = [1,2,3,4,5]
    nuevaA = recortarLista(a)
    print("La lista", a,"recortada es", nuevaA)
    
    print("")
    
    a = [4]
    nuevaA = recortarLista(a)
    print("La lista", a,"recortada es", nuevaA)
    
    print("")
    
    a = []
    nuevaA = recortarLista(a)
    print("La lista", a,"recortada es", nuevaA)
    
    print("")
    
    nuevaA = recortarLista(a)
    print("La lista", a,"recortada es", nuevaA)
    
    

main()  