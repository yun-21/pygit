import sys
user = input("요청 할 파일이름을 적으시오: ")
fileName = user
accessMode = "r"
try:
    myFile = open(fileName, accessMode)
    for i in range(1,4):
        line = myFile.readline()
        num=0
        num += i
        print(num,":",line)

    myFile.close()
except:
    error = sys.exc_info()
    print("요청하시는 파일이 없습니다.")
    print(error)