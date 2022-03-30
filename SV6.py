import math
ban = input("반지름을 입력하시오: ")
b=float(ban)
S=4*math.pi*(b**2)
V=4/3*math.pi*(b**3)
print("겉면적은",S, ",부피는",V)