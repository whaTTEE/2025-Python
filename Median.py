def med3(a, b, c):
    if a >= b:
        if b >= c:
            return b    # a b c
        elif a <= c:
            return a    # c a b
        else:
            return c    # a c b
    elif a > c:
        return a        # b a c
    elif b > c: 
        return c        # b c a
    else:
        return b        # a b c 

# 사용자 입력 받기
a = int(input("a의 값을 적으세요: "))
b = int(input("b의 값을 적으세요: "))
c = int(input("c의 값을 적으세요: "))

# 중앙값 출력
print("중앙값은:", med3(a, b, c))
