#Autor: Andy Dino Martínez Hernández, A01376720
#Ejercicio. Misión 6 de listas


#Función 1. Para eliminar el primer y último elemento de la lista
def recortarLista(lista):
    if len (lista)==0:
        return []
    elif len (lista)==1:
        return []
    #copiar lista y remover numeros
    copiaLista= list (lista) #Para duplicarla y que no sobreescribas la original
    
    ultimo= copiaLista [len(copiaLista)-1]
    copiaLista.remove(ultimo)  #Así se elimina el último dato
    
    primero= copiaLista [0]
    copiaLista.remove(primero)
    
    return copiaLista


#Función 2. Para acomodar la lista
def estaOrdenada(lista):
    lista1= list(lista)
    lista2= lista.sort()
    
    if lista1==lista2:
        return True
    else:
        return False
    
#Función 3. Comparación de anagramas y letras de las cadenas
def sonAnagramas (str1,str2):
    str1= str1.upper()
    str2= str2.upper()
    
    lista1= list(str1)  #Hace la cadena en lista
    lista2= list (str2)
    
    lista1.sort() #Siempre ordena de menor a mayor 
    lista2.sort() #O alfabéticamente
    
    if lista1==lista2:
        return True
    return False

#Función 4, para identificar si hay duplicados
def hayDuplicados (lista):
    for dato in lista:
        if lista.count(dato)>=2:
            return True #Termina y me da un resultado
    return False

#Función 5, para borrar los duplicados
def borrarDuplicados(lista):
    while hayDuplicados(lista)==True: #U R THE PROBLEM BISH
        for x in range (len(lista)):
            dato=lista[x]
            veces=lista.count(dato)
            if veces >=2:
                for n in range (veces-1):
                    lista.remove(dato)  #para borrar todo, excepto una cantidad
                if veces >=2:
                    break #Para que regrese al ciclo while y vuelva a preguntar si aún hay duplicados
        


#Función Main
def main():
        
    lista= [1,2,3,7,7,1,3,5,3,4]
    b= str (input("Ingresa la palabra que quieras: "))
    c= str(input("Ingresa otra palabra similar: "))
    
    
    #Función 1, recorte
    nuevaLista= recortarLista (lista)
    print ("La lista", lista, "recortada es:", nuevaLista)
    
    #Función 2, Sort
    orden= estaOrdenada(lista)
    print("la Lista está Ordenada?")
    if orden==True:
        print ("Si, la lista está ordenada")
    elif orden==False:
        print("No. Ordenando la lista se ve así: ", lista)
    
    #Función 3, anagramas
    print("¿Las palabras", b, "y", c, "son Anagramas? ", sonAnagramas(b,c))
    
    #Función 4. Duplicados.
    print ("¿Hay duplicados en la lista?", hayDuplicados(lista))
    
    #Función 5. borrar Duplicados
    print ("La lista original es: ", lista)
    borrarDuplicados(lista)
    print ("Eliminando los duplicados la lista es: ", lista)
   

main()
    