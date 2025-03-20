var = int(input("직사각형의 넓이를 입력하세요 : "))

for i in range(1, var + 1):
    if i * i > var: break
    if var % i: continue
    print(f"{i} x {var // i}")

    
