def function(n):
    s = 0
    while n > 0:
        s += n
        n -= 1
    return s
    
n = int(input("값을 입력하세요 : "))
print(f"1부터 {n}까지의 합은 {function(n)}입니다.")
