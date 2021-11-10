sum, hap =0, 0

for i in range(501, 1001, 2):
    hap =hap +i
print("500과 1000사이에 있는 홀수의 합계 : %d" %hap)

for k in range(500, 1001):
    if k % 2 ==1:
        sum += k
print("500과 1000사이에 있는 홀수의 합계 : %d" %sum)