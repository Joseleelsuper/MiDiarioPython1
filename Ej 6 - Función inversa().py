#Definir una función inversa() que calcule la inversión de una cadena. 
#Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

def inversa(cadena):
    cadena = cadena[::-1]
    print(cadena)

    exit()

def main():
    cadena = str(input("Escriba una palabra o frase y se le dará la vuelta: "))
    inversa(cadena)

main()