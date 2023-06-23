def calcular_fatorial(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, n + 1):
            fatorial *= i
        return fatorial

def main():
    numero = int(input("Digite um número inteiro: "))
    fatorial = calcular_fatorial(numero)
    
    print("O fatorial de", numero, "é:", fatorial)

main()
