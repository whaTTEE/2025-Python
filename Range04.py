print('*을 출력한다.')
Q = int(input("몇 개를 출력할까요 ? : "))
Q2 = int(input("몇 개를 줄바꿈할까요 ? : "))

for i in range(Q):
    print('*', end='')
    if i % Q2 == Q2 - 1:   
        print()                #줄바꿈

