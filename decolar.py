def decolar(n):
    if n == 0:
        print("decoalr!")
    else:
        print(n)
        decolar(n - 1)
def main():
    n =  int(input("digite um valor: "))
    if n < 0:
        while n < 0:
            print("digite um nymero positivo")
    decolar(n)
main()
