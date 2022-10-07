#Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. 
#Escribir la función usando el bucle for anidado.

def superposicion(lista1, lista2):
    for i in lista1:
        for j in lista2:
            if (i == j):
                print("True")
                exit()
    
    if(j != i ):
        print("False")

    exit()

def main():
    x = int(input("Escribe el número de elementos en la lista 1: "))
    lista1 = [0]*x
    y = int(input("Escribe el número de elementos en la lista 2: "))
    lista2 = [0]*y

    for i in range(x):
        lista1[i] = input(f"Escribe el elemento {i+1} de la lista 1: ")
    
    print("\n")

    for i in range(y):
        lista2[i] = input(f"Escribe el elemento {i+1} de la lista 2: ")

    superposicion(lista1, lista2)

main()

