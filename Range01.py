a = int(input("정수 a의 값을 입력하세요 : "))
b = int(input("정수 b의 값을 입력하세요 : "))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b+1):
    if i < b:
        print(f"{i} + ", end = "") #end=""는 줄바꿈 없음
    else:
        print(f"{i} = ", end ="")
    sum += i

print(sum)
