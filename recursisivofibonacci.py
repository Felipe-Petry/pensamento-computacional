def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n - 2) 
    
def main():
    n = int(input("digite um numero: "))
    print(fib(n))
main()

#TESTE de MESA
#main n = 5

#fib n = 5

#fib(5) = fib(4) + fib(3) = 3 + 2 = 5

#fib(4) = fib(3) + fib(2) = 2 + 1 = 3

#fib(3) = fib(2) + fib(1) = 1 + 1 = 2

#fib(2) = fib(1) + fib(0) = 1


#1 0
