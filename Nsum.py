n = input("자연수를 입력하시오: ")
N = int(n)
sum=0

for i in range(1, N+1):
    sum += i

print("1~N 사이의 수의 합은:",sum)