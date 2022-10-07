#Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. 
#Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

def sum(lista):
    x = 0
    for i in lista:
        x+=i
    
    print("La suma de los números de la lista es: ",x)

def multip(lista):
    x = 1
    for i in lista:
        x*=i

    print("La multiplicación de los números de la lista es: ",x)

def main():
    x = int(input("Cuantos números quieres en la lista: "))
    lista = [0]*x
    for i in range(x):
        lista[i] = int(input(f"Escribe el número {i+1}: "))
    lista = lista[:x]
    sum(lista)
    multip(lista)

    exit()

main()
