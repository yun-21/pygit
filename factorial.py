def factorial(n):
    result = 1
    N = int(n)
    for i in range(1,N+1):
        result *= i
    print("n!의 값은:",result)

n= input("n!를 하기위해 n값을 적으시오: ")
factorial(n)