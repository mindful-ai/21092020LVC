# -------------------------------------------------
# LAB 4 - Create a fibonacci module and test it
# -------------------------------------------------


# Fibonacci -> 0 1 1 2 3 5 8 ...
# fibo.py

def fibonacci(i):
    return fibo

def genfibo(n):
    fibolist = []
    x = 0
    fibolist.append(x)
    y = 1
    fibolist.append(y)
    for i in range(n-2):
        z = x + y
        fibolist.append(z)
        x = y
        y = z
    return fibolist

def checkfibo(n): 
    x = 0
    y = 1
    
    for i in range(n-2):
        z = x + y
        if(z > n):
            left = abs(n - y)
            right = abs(n - z)
            return(left, right)
        elif(z == n):
            return(0, 0)
        x = y
        y = z
   


# ------------------------------------------

if __name__ == "__main__":

    print(genfibo(10))
    print(checkfibo(8))
    print(checkfibo(7))
