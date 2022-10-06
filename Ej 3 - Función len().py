#Definir una función que calcule la longitud de una lista o una cadena dada. 
#(Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio).

def long(l):
    x = 0
    for i in l:
        x+=1
    print("La longitud de la cadena de carácteres es: ",x)

    exit()

def main():
    l = str(input("Escriba una cadena de carácteres: "))
    long(l)

main()
