def listProd(a,b):
    result = 0
    for i in range(0,3):
        result += a[i]*b[i]
    print(result)

a = [int(input("a배열에 들어갈 숫자를 적으시오: ")) for i in range(0, 3)]
b = [int(input("b배열에 들어갈 숫자를 적으시오: ")) for i in range(0, 3)]

listProd(a,b)


