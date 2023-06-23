
def s(n1,n2):
    produto = 1
    if n2 < 0:
        print("Digite um numero maior que 0" )
    
    else:
        for x in range(0,n2):
            produto = produto * n1
    print(produto)


n1 = int(input("numero:"))
n2 = int(input("numero potencia:"))
 
s(n1,n2)   


