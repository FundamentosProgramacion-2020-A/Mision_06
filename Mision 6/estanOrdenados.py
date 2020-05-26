# Autor: Miguel Castillo Ordaz
# Programa que detecta si están o no ordenados los valores de la lista.

def estanOrdenados(lista):
    
    nuevaLista = list(lista) # Crea nueva lista basada en los valores de la lista.
    nuevaLista.sort()
    
    if lista == nuevaLista: # Detecta valores ordenados en nueva lista.
        
        return "Si están ordenados"
    else:
        return "No están ordenados"
    
def main (): # Pruebas de funcionamiento.
    
    lista = [7, 12, 53]
    print("Los valores en la lista", lista, estanOrdenados(lista))
    
    print("")
    
    lista = [7, 23, 15]
    print("Los valores en la lista", lista, estanOrdenados(lista))
    
    print("")
    
    lista = [1,2,3,4,5]
    print("Los valores en la lista", lista, estanOrdenados(lista))
    
    print("")
    
    lista = [1,1,1,1]
    print("Los valores en la lista", lista, estanOrdenados(lista))
    
    print("")
    
    lista = [1,7,1,8]
    print("Los valores en la lista", lista, estanOrdenados(lista))
    print("")
    
    
    lista = [4]
    print("Los valores en la lista", lista, estanOrdenados(lista))
    
    print("")
    
    lista = []
    print("Los valores en la lista", lista, estanOrdenados(lista))
    
    
main()