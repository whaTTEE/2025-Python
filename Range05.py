while True:
    n = int(input("n값을 입력하세요 : "))
    if n > 0:
        break    #n이 0보다 커질 때까지 반복
    else:
        print("양의 정수값만 입력가능합니다.")

sum = 0
i = 1

for i in range(1, n + 1):
    sum += i
    i += 1

print(f"1부터 {n}까지 정수의 합은 {sum}입니다.")
