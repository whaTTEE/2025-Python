def change(lst,idx, val):
    lst[idx] = val

list = [11,22,33,44,55]
print(f"list = {list}")

index = int(input("바꿀 인덱스 값을 입력하세요 : "))
value = int(input("바꿀 값을 입력하세요 : "))

change(list,index,value)
print(f"list = {list}")
