n = int(input("몇 개를 출력할까요? : "))

for i in range(n):
    if i % 2:    #True임
        print('-', end='')
    else:        # 0 출력됨, False임
        print('+', end='')

print()
