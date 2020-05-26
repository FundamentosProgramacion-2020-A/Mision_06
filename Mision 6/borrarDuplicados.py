# Autor: Miguel Castillo Ordaz
# Programa que borra los duplicados en la lista.

def hayDuplicados(lista): # Función que detecta duplicados en la lista.
    
    for dato in lista:
        if lista.count(dato)>=2:
            return True
        else:
            return False
    
def borrarDuplicados(lista):
    
    while hayDuplicados(lista) == True: # Si existen duplicados en la lista, los analiza esta parte de la función.
        
        for k in range(len(lista)):
            dato = lista[k]
            veces = lista.count(dato)
            for n in range(veces-1):
                lista.remove(dato) # Remueve el dato repetido.
            if veces>=2: 
                break # No remueve el dato original.
            
def main(): # Pruebas de funcionamiento.
    
    a = [1,2,3,4,5,4,1,2,3,1]
    print("La lista original es", a)
    borrarDuplicados(a)
    print("Al eliminar los duplicados queda:", a)
    
    print("")
    
    a = [1,8,3,4,3,1,8,2,7,8]
    print("La lista original es", a)
    borrarDuplicados(a)
    print("Al eliminar los duplicados queda:", a)
    
    print("")
    
    a = [1,2,3,4,5]
    print("La lista original es", a)
    borrarDuplicados(a)
    print("Al eliminar los duplicados queda:", a)
    
    print("")
    
    a = [1,1,1,1,2,3,4,5]
    print("La lista original es", a)
    borrarDuplicados(a)
    print("Al eliminar los duplicados queda:", a)
    
    print("")
    
    a = [1,1,1,1]
    print("La lista original es", a)
    borrarDuplicados(a)
    print("Al eliminar los duplicados queda:", a)
    
    print("")
    
    a = []
    print("La lista original es", a)
    borrarDuplicados(a)
    print("Al eliminar los duplicados queda:", a)
    
    
    
    
main()
