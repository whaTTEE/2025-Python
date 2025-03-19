a = int(input("a의 정수값을 입력하세요 : "))
b = int(input("b의 정수값을 입력하세요 : "))

if a > b:
    a,b = b,a

sum = 0

for i in range(a,b):
    print(f"{i} + ", end = "")
    sum += i

sum += b
print(f"{b} = {sum}")

