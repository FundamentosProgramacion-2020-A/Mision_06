# Autor: Fernando Pérez González, A01376508
# realizar ejercicios con listas

#primer ejercicio 
def recortarLista(lista):
    if len(lista) <= 2: #si tiene dos o menos valores la lista está vacía
        return []
    #copia de la lista anterior 
    nuevaLista = list(lista) #duplicado
    ultimo = nuevaLista[len(nuevaLista)-1]
    nuevaLista.remove(ultimo) #elimina el ultimo numero
    primero = nuevaLista [0]
    nuevaLista.remove(primero)
    return nuevaLista


#segundo ejercicio
def estanOrdenados(lista):
    nuevaLista = list(lista) #copia de la lista
    nuevaLista.sort() #ordena
    if lista == nuevaLista: 
        return True
    
    return False


#tercer ejercicio
def sonAnagramas(cadena1, cadena2):
    cadena1 = cadena1.upper() #hace que todas las letras sean mayúsculas
    cadena2 = cadena2.upper()
    
    lista1 = list(cadena1) #convierte cadena en lista
    lista2 = list(cadena2)
    
    lista1.sort() #sort las ordena 
    lista2.sort()
    
    if lista1 == lista2:
        return True
    
    return False


#cuarto ejercicio
def hayDuplicados(lista):
    for dato in lista:
        if lista.count(dato)>=2: #al primero que se repite ya hay duplicados
            return True 
    
    return False


#quinto ejercicio
def borrarDuplicados(lista):
    while hayDuplicados(lista) == True: #significa que mientras al menos un dato está repetido, sigue corriendo
        #elimina duplicados
        for k in range (len(lista)):
            dato = lista[k]
            veces = lista.count(dato) #contar cuantas veces aparece el dato
            for n in range(veces-1): #borra tantas veces menos 1, si aparece 5 veces lo borra 4 veces
                lista.remove(dato)
            if veces >= 2:
                break
                
            
    
def main():
    #ejercicio1
    listaA = [13,24]
    nuevaA = recortarLista(listaA)
    listaAB = [55,39,62,94,44]
    nuevaAB = recortarLista(listaAB)
    listaAC = []
    nuevaAC = recortarLista(listaAC)
    print("Ejercicio 1:\n" "La lista", listaA, "cuando es recortado el primer y último número es", nuevaA)
    print("La lista", listaAB, "cuando es recortado el primer y último número es", nuevaAB)
    print("La lista", listaAC, "cuando es recortado el primer y último número es", nuevaAC, "\n")

    
    #ejercicio2
    listaB = [13,9,21,24]
    print("Ejercicio 2: \n" "La lista ", listaB)
    if estanOrdenados(listaB) ==True:
        print("Está en orden")
    else:
        print("No está en orden")
    listaBA = [9,13,21,24]
    print("La lista ", listaBA)
    if estanOrdenados(listaBA) ==True:
        print("Está en orden")
    else:
        print("No está en orden")
    listaBB = [10,9,8,7,6,5]
    print("La lista ", listaBB)
    if estanOrdenados(listaBB) ==True:
        print("Está en orden\n")
    else:
        print("No está en orden\n")
        
    #ejercicio3
    palabra1 = "Ironicamente"
    palabra2 = "RenaciMienTo"
    print("Ejercicio 3: \n" "Las palabras", palabra1, "y", palabra2)
    if sonAnagramas(palabra1,palabra2) ==True: #convertir True y False a palabras
        print("Son anagramas")
    else:
        print("No son anagramas")
    palabra3 = "cOLinAS"
    palabra4 = "Nicolas"
    print("Las palabras", palabra3, "y", palabra4)
    if sonAnagramas(palabra3,palabra4) ==True: #convertir True y False a palabras
        print("Son anagramas")
    else:
        print("No son anagramas")
    palabra5 = "calor"
    palabra6 = "Carlos"
    print("Las palabras", palabra5, "y", palabra6)
    if sonAnagramas(palabra5,palabra6) ==True: #convertir True y False a palabras
        print("Son anagramas\n")
    else:
        print("No son anagramas\n")

    #ejercicio4
    listaD = [14,19,22,14,23]
    print("Ejercicio 4: \n" "En la lista: ", listaD)
    if hayDuplicados(listaD) ==True:
        print("Hay duplicados")
    else:
        print("No hay duplicados")
    listaDA = [1,3,3,5,5,8,7,9,9,9,9]
    print("En la lista: ", listaDA)
    if hayDuplicados(listaDA) ==True:
        print("Hay duplicados")
    else:
        print("No hay duplicados")
    listaDB = [1,2,3,13,16,21]
    print("En la lista: ", listaDB)
    if hayDuplicados(listaDB) ==True:
        print("Hay duplicados\n")
    else:
        print("No hay duplicados\n")
    
    #ejercicio5
    
    listaE = [1,2,2,2,2,2,3,3,4,5,6,7,8,9,9,10]
    print("Ejercicio 5: \n" "La lista original es", listaE)
    borrarDuplicados(listaE)
    print("Eliminando los datos duplicados queda como", listaE)
    listaEA = [13,13,13,13,13,13,13]
    print("Ejercicio 5: \n" "La lista original es", listaEA)
    borrarDuplicados(listaEA)
    print("Eliminando los datos duplicados queda como", listaEA)
    listaEB = [1,4,3,5,10,13,17]
    print("Ejercicio 5: \n" "La lista original es", listaEB)
    borrarDuplicados(listaEB)
    print("Eliminando los datos duplicados queda como", listaEB)
    print("\nTermina el programa")
    
main()
