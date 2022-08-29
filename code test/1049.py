N, M = map(int, input().split())
six = []
one = []
for i in range(M):
    package, single = map(int, input().split())
    six.append(package)    ## 묶음과 낱개를 각각 append
    one.append(single)
if min(six) <= (min(one) * 6):
    answer = min(six) * (N//6) + min(one) * (N % 6)
    if min(six) < (min(one) * (N % 6)):
        answer = min(six) * (N//6 + 1)
else:
    answer = min(one) * N
print(answer)