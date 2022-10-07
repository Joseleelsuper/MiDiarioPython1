#Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. 
#Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

def generar_n_caracteres(x, y):
    print(x*y)

    exit()

def main():
    x = int(input("Escribe un número: "))
    y = str(input("Escribe un carácter: "))

    generar_n_caracteres(x,y)

main()
    