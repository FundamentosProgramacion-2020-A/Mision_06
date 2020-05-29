#Autor: Ana Fernanda Martínez
#Ejercicio con listas

#Ejercicio 1
def recortarLista(lista):                
    if len(lista)<=2:                    
        return []

    nuevaLista= list(lista)
    último = nuevaLista [len(nuevaLista)-1]
    nuevaLista.remove(último) #Elimina el último dato
    primero = nuevaLista [0]
    nuevaLista.remove (primero)
    return nuevaLista

#Ejercicio 2
def estanOrdenados (lista):
    #Copia
    nuevaLista = list(lista)
    nuevaLista.sort()              #Ordenas la lista
    
    if nuevaLista == lista:
        return True
    return False
    
#Ejercicio 3 

def sonAnagramas(cadena1, cadena2):        
    cadena1 = cadena1.upper()             
    cadena2 = cadena2.upper()
    lista1 = list(cadena1)                 
    lista2 = list(cadena2)
    lista1.sort()                         
    if lista1==lista2:                     
        return True                        
    else: 
        return False                       

#Ejercicio 4
def hayDuplicados(lista):
    for dato in lista:
        if lista.count(dato)>=2:
            return True #termina y me da un resultado
        
    return False


#Ejercicio 5
def borrarDuplicados(lista):
   while hayDuplicados(lista) == True:
       #Eliminar duplicados
       for k in range(len(lista)):
           dato =lista[k]
           veces = lista.count(dato)
           for n in range (veces-1): #Borra tantas veces menos 1 , como aparesca el valor en la lista owo
               lista.remove(dato)
           if veces>=2:
               break
        

#Función principal
def main ():

    #Ejercicio 1
    print("Ejercicio 1: ")                
    
    lista = [1,2,3,4,5]
    nuevaLista = recortarLista(lista)
    print("La lista", lista, "recortada es: ", nuevaLista)
    
    lista1_2 = [1,2]
    nuevaLista = recortarLista(lista1_2)
    print("La lista", lista1_2, "recortada queda así: ", nuevaLista)
    
      
    print("_____________________________")
 
    
    #Ejercicio 2
    
    print("Ejercicio 2: ")                  
    
    lista2_1 = [1,2,3,4,5,6,7]
    print ("La secuencia", lista2_1)
    orden = estanOrdenados(lista2_1)

    if orden == True:
        print ("está ordenada")
    else:
        print ("no está ordenada")
    
    lista2_2 = [7,5,4,2]
    print ("La secuencia", lista2_2)
    orden = estanOrdenados(lista2_2)

    if orden == True:
        print ("está ordenada")
    else:
        print ("no está ordenada")

        
    print("_____________________________")
    
    
    #Ejercicio 3
    
    print("Ejercicio 3: ")
    
    a = "roma"
    b = "amor"
    
    print(a, "y", b)         
    if sonAnagramas (a, b) == True:
        print ("sí son anagramas")
    else:
        print ("no son anagramas")

    b = "anime"
    c= "calaca"
    
    print(b, "y", c) 
    if sonAnagramas (b, c) == True:
        print ("sí son anagramas")
    else:
        print ("no son anagramas")
         
    print("_____________________________")
 
    
    #Ejercicio 4
    
    print("Ejercicio 4: ")                   
    
    lista4_1 = [3,2,5,67,8,9,40]
    if hayDuplicados(lista4_1) == False:
        print("En la lista:",lista4_1 , "no tiene duplicados")
    else:
        print("En la lista",lista4_1 , "hay duplicados")
        
    lista4_2 = [2,4,55,60,55,1]
    if hayDuplicados(lista4_2) == False:
        print("En la lista", lista4_2, "no tiene duplicados")
    else:
        print("En la lista", lista4_2, "tiene duplicados")
          
    print("_____________________________")
    
    #Ejercicio 5
    
    lista5 = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,]
    print("La lista original es: ", lista5)
    borrarDuplicados(lista5)
    print("Si los duplicados son eliminados es: ", lista5)

    
    lista5_2= [2,4,5,7,9,2]
    print("La lista original es: ", lista5_2)
    borrarDuplicados(lista5_2)
    print("Si los duplicados son eliminados es: ", lista5_2)
    
    print("_____________________________")
    

main()