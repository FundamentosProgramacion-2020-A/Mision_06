# Autor: Miguel Castillo Ordaz
# Programa que detecta si hay duplicados en la lista.

def hayDuplicados(lista):
    for dato in lista:
        if lista.count(dato)>=2: # Detecta el duplicado.
            return True
        else:
            return False 
    
def main(): # Pruebas de funcionamiento.
    
    a = [1,2,3,4,5,6,1,2,3,1]
    print("En la lista",a)
    if hayDuplicados(a)==True:
        print("Hay duplicados")
    else:
        print("No hay duplicados")
    
    
    print("")
    
    a= [5,7,4,6,10]
    print("En la lista ",a)
    if hayDuplicados(a)==True:
        print("Hay duplicados")
    else:
        print("No hay duplicados")
        
    print("")
    
    a= [5,5,5,5]
    print("En la lista ",a)
    if hayDuplicados(a)==True:
        print("Hay duplicados")
    else:
        print("No hay duplicados")
        
    print("")
    
    a= [4,4]
    print("En la lista ",a)
    if hayDuplicados(a)==True:
        print("Hay duplicados")
    else:
        print("No hay duplicados")
    
    print("")
    
    a= [5,4]
    print("En la lista ",a)
    if hayDuplicados(a)==True:
        print("Hay duplicados")
    else:
        print("No hay duplicados")
        
    print("")
    
    a= [5]
    print("En la lista ",a)
    if hayDuplicados(a)==True:
        print("Hay duplicados")
    else:
        print("No hay duplicados")
        
        

main()