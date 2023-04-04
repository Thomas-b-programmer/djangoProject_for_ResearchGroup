def judge(n):
    if (n % 4 == 0 and n % 100 != 0):
        return True
    elif n % 400 == 0:
        return True
    else:
        return False
n,m = map(int,input().split())
listd = [1,3,5,7,8,10,12]
listx = [4,6,9,11]
if m != 2:
    if m in listd:
        print(31)
    if m in listx:
        print(30)
else:
    if judge(n):
        print(29)
    else:
        print(28)