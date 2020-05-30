#Autor: Samara Andrea Vega
#Programa que recorta, ordena, y elimina duplicados en listas; además identifica anagramas.

#Problema 1
def recortarLista(lista):
    if len(lista)<=2:
        return[]
    #COPIA
    nuevaLista= list(lista)   #Este es el duplicado
    ultimo= nuevaLista[len(nuevaLista)-1]
    nuevaLista.remove(ultimo)   #Se elimina último dato
    primero= nuevaLista[0]
    nuevaLista.remove(primero)
    return nuevaLista
 
#Problema 2
def estanOrdenados(lista):
    valorA = list(lista)
    valorB = list(lista)
    valorB.sort()
    for lista in valorA:
        if valorA == valorB:
            return True
        return False
    
    
#Problema 3
def sonAnagramas(cadenaA, cadenaB):
    cadenaA = cadenaA.upper()
    cadenaB = cadenaB.upper()
    
    lista1 = list(cadenaA)   #Convierte la cadena en lista para ordenar facilmente
    lista2 = list(cadenaB)   # ["R", "O", "M", "A" ]
    
    lista1.sort()
    lista2.sort()            # [ "A", "M", "O", "R" ]
    
    if lista1 == lista2:
        return True
    
    return False

#Problema 4
def hayDuplicados(lista):
    for dato in lista:
        if lista.count(dato)>=2:
            return True   #Si se cumple, termina y da un resultado
        
    return False

#Problema 5
def borrarDuplicados(lista):
    while hayDuplicados(lista) ==True:
        # Elimina duplicados
        for k in range(len(lista)):     #[1,2,3,2]
            dato = lista[k]
            veces = lista.count(dato)
            for n in range(veces-1): #Borra tantas veces menos 1, como aparezca el valor en la lista
                lista.remove(dato)
            if veces>=2:
                break
            



def main():
    a= [1,2,3]
    nueva1= recortarLista(a)
    print("La lista", a, "ya recortada es", nueva1)
    
    b= [1,2,4,7,9]
    nueva2= recortarLista(b)
    print("La lista", b, "ya recortada es", nueva2)
    
    c= []
    nueva3= recortarLista(c)
    print("La lista", c, "ya recortada es", nueva3)
    
    
    valores1=[8,16,24]
    valoresOrdenados = estanOrdenados(valores1)
    valores2= [8,24,16]
    valoresOrdenados1 = estanOrdenados(valores2)
    valores3=[]
    valoresOdenados2 = estanOrdenados(valores3)
    print("Los valores", valores1, "están ordenados", valoresOrdenados)
    print("Los valores", valores2, "no están ordenados", valoresOrdenados1)
    print("No existen valores para ordenar")
    
    
    a = "Roma"
    b = "Mora"
    print("Las palabras", a, "y", b, ":")
    
    if sonAnagramas(a,b) == True:
        print("Son anagramas")
    else:
        print("No son anagramas")
        
    a = "Mortal"
    b = "Talón"
    print("Las palabras", a, "y", b, ":")
    
    if sonAnagramas(a,b) == True:
        print("Son anagramas")
    else:
        print("No son anagramas")
        
    
    a= [3,4,5,6,7]
    print(hayDuplicados(a))
    
    b= [3,4,3,1,5,6,7,7]
    print(hayDuplicados(b))
    
    c= []
    print("No hay valores, por lo tanto no existen duplicados")
    
    
    a=[1,2,3,4,5,4,1,2,3,1]
    print("La lista original es", a)
    borrarDuplicados(a)
    print("Eliminando los duplicados existentes, queda así: ", a)
    
    b= []
    print("La lista original es", b)
    borrarDuplicados(b)
    print("Como la lista está vacía, no hay duplicados para borrar")
    
    c= [1,2,3]
    print("La lista original es", c)
    borrarDuplicados(c)
    print("No hay duplicados, la lista queda igual: ", c)
    


    
main()