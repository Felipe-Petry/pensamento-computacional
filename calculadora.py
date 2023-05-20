
def soma(x, y):
    soma = x + y 
    return soma

def sub (x, y):
    sub = x - y 
    return sub

def mult(x, y):
    multi = x * y   
    return multi

def div(x, y):
    div = x / y 
    return div    

def main():
    n1 = int(input("digite um numero: "))
    n2 = int(input("digite um numero: "))
    print("1- vc deseja somar")
    print("2- vc deseja subtrair")
    print("3- vc deseja multiplicar")
    print("4- vc deseja dividir")
    opc = int(input("escolha uma opcao: "))

    s = soma(n1, n2)
    su = sub(n1, n2)
    m = mult(n1,n2)  
    d = div(n1,n2)

    if opc == 1:
        resultado = soma(n1 ,n2)
        print(resultado)
    elif opc == 2:
        reltado = sub(n1 ,n2)
        print(resultado)
    elif opc == 3:
        resultado = mult(n1 ,n2)
        print(resultado)
    elif opc == 4:
        resultado = div(n1 ,n2)

main()
