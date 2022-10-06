#Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
#(Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

def max(a,b):
    if (a > b):
        print("El número mayor es: ",a)
    else:
        print("El número mayor es: ",b)
    
    exit()

def main():
    a = int(input("Escribe un número: "))
    b = int(input("Escribe otro número: "))
    max(a,b)

main()
