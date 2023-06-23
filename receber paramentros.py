def x(a, b, limite):
    if (a + b) > limite:
        return True
    else:
        return False

def main():
    a = int(input("digite um numero: "))
    b = int(input("digite um numero: "))
    limite = int(input("digite um numero: "))
    c = x(a, b, limite)
    print(c)
main()
