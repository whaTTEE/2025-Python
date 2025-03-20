import random 

n = int(input("난수의 개수를 입력하세요. : "))

for i in range(n):
    r = random.randint(10,99)    #10과 99사이의 임이의 정수를 생성하는 코드
    print(f"{r} ", end=' ')
    if r == 13:                  #13이 나오면 프로그램을 중단
        print("\n프로그램을 중단합니다.")
        break
else:
    print("\n난수 생성을 종료합니다.")
