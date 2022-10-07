#Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas). 
#Ejemplo: es_palindromo ("radar") tendría que devolver True.

from sqlite3 import enable_shared_cache


def es_palindromo(palindromo):
    if(palindromo == palindromo[::-1]):
        print("True")
    else:
        print("False")

    exit()

def main():
    palindromo = str(input("Escribe una palabra: "))
    es_palindromo(palindromo)

main()