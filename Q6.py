def fib (n) :
    if  n == 0 :
        return 0
    if  n == 1 or n == 2  :
        return 1
    return fib(n-1) + fib(n-2)

def printFib(n):
    for i in range(0 ,n) :
        print(fib(i))

x = int(input("Enter a number : "))
print("The fibbonacci terms are as follow : ")
printFib(x)
