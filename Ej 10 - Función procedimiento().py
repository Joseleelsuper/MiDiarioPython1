#Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. 
#Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
#****
#*********
#*******

def procedimeinto(lista):
    for i in lista:
        print("*"*i)

    exit()

def main():
    x = int(input("Escribe el número de espacios de la lista: "))
    lista = [0]*x
    for i in range(x):
        lista[i] = int(input(f"Escribe el número {i+1}: "))

    procedimeinto(lista)

main()