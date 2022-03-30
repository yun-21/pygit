tem = input("Enter a temperature: ")
convert = input("Convert to (F)ahrenheit or (C)elsius? ")
temp=float(tem)

if(convert =='C'):
    c=(5/9)*(temp-32)
    print(tem,"F =",c,"C")

elif(convert =='F'):
    f=(9/5)*temp+32
    print(tem,"C =",f,"F")

else:
    print("C와 F중에서만 적어주세요")