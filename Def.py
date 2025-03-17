def max3(a,b,c):
    max3 = a 
    if max3 < b : max3 = b
    if max3 < c : max3 = c
    return max3


print(max3(10,20,30))
print(max3(20,30,10))
print(max3(30,20,10))
