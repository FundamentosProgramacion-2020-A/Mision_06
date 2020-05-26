# Autor: Miguel Castillo Ordaz
# Programa que detecta anagramas.

def sonAnagramas(cadena1,cadena2):
    cadena1 = cadena1.upper()
    cadena2 = cadena2.upper()
    
    lista1 = list(cadena1) # Convierte las cadenas en la lista 
    lista2 = list(cadena2) # "R","O","M","A"
    
    lista1.sort()
    lista2.sort()
    
    if lista1 == lista2:
        return True
    return False

def main(): # Pruebas de funcionamiento.

    a = "oMaR"
    b = "Mora"
    print("Las palabras", a, "y",b)
    if sonAnagramas(a,b)==True:
        print("Son  anagramas")
    else:
        print("No son anagramas")
        
    print("")

    a = "Roma"
    b = "Mora"
    print("Las palabras", a, "y",b)
    if sonAnagramas(a,b)==True:
        print("Son  anagramas")
    else:
        print("No son anagramas")
    
    print("")
    
    a = "Hello"
    b = "Hola"
    print("Las palabras", a, "y",b)
    if sonAnagramas(a,b)==True:
        print("Son  anagramas")
    else:
        print("No son anagramas")
    
    print("")
    
    a = "ana"
    b = "nana"
    print("Las palabras", a, "y",b)
    if sonAnagramas(a,b)==True:
        print("Son  anagramas")
    else:
        print("No son anagramas")
        
    
main()