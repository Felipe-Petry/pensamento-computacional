def calcula(n):
    if n % 4 == 0:
        return True
    else:
        return False

def main():
    numero = int(input("Digite um ano: "))
    c = calcula(numero)
    print(c)
main()
