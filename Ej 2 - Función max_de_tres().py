#Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

def max_de_tres(a,b,c):
    if (a > b > c or a > c > b):
        print("El número mayor es: ",a)
    elif (b > a > c or b > c > a):
        print("El número mayor es: ",b)
    else:
        print("El número mayor es: ",c)

    exit()
    
def main():
    a = int(input("Escribe un número: "))
    b = int(input("Escribe otro número: "))
    c = int(input("Escribe un último número: "))
    max_de_tres(a,b,c)

main()