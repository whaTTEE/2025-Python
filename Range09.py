var = int(input("짧은 변의 길이를 입력하세요 : "))

for i in range(var):
    for k in range(var - (i+1)):
        print(' ', end='')
    for j in range(i + 1):
        print('*', end='')

    print() #행 변경
