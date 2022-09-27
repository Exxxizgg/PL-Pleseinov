n = int(input())
sum = 0
pr = 1   
for i in range(1, n + 1):
    k = pr * i    
    sum += k
    pr = k
print(sum)