import sys
myF = open("file.txt", "w")
myF.write("Opens a file for reading only in binary.\n")
myF.write("The file pointer is placed.\n")
myF.write("This is the default mode.")
myF.close()

try:
    user = input("요청 할 파일이름을 적으시오: ")
    fileName = user
    accessMode = "r"
    myFile = open(fileName, accessMode)
    num = 0
    line = myFile.readline()
    while line != "":
        num += 1
        print(num,":",line)
        line = myFile.readline()


except:
    error = sys.exc_info()
    print("요청하시는 파일이 없습니다.")
    print("어떤 오류인지 확인:",error)
