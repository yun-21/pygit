import random
answer="Y"
count = 0
begood = 0
while answer=="Y":

    n1 = random.randint(1, 9)
    n2 = random.randint(1, 9)
    print(n1, "*", n2)
    result = n1 * n2
    res = int(input("답: "))
    if (result==res) :
        print("정답입니다.")
        count += 1
        begood += 1
    else:
        print("틀렸습니다.")
        count += 1
    answer=input("계속 할까요?(Y/N):")
    if answer == "N":
        good = (begood/count)*100
        print("정답률",good,"%")