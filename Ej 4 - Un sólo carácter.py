#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def vocal(v):
    if (v == 'a' or v == 'e' or v == 'i' or v == 'o' or v == 'u' or
       v == 'A' or v == 'E' or v == 'I' or v == 'O' or v == 'U'):
        print("True")
    else:
        print("False")
    
    exit()

def main():
    v = str(input("Escribe un  sólo carácter: "))
    if (len(v) > 1):
        print("Por favor, escribe un sólo carácter.")
        main()
    vocal(v)

main()
    
