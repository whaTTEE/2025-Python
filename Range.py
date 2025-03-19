a = int(input("a의 값을 입력하세요 : "))
b = int(input("b의 값을 입력하세요 : "))



if a > b:
    a, b = b, a    # a와 b를 오름차순으로 정렬

sum = 0
for i in range(a, b + 1):
    sum += i

print(f"{a}부터 {b}까지의 합은 {sum}입니다.")
