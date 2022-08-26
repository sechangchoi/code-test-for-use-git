N, M = map(int, input().split())
six = []
one = []
for i in range(M):
    package, single = map(int, input().split())
    if package < single * 6:
        six.append(package)
    else:
        six.append(single * 6)
    if single * (N % 6) < package:
        one.append(single * (N % 6))
    else:
        one.append(package)
if N <= 6:
    total = six + one
    print(min(total))
else:
    print(min(one) + (min(six) * (N // 6)))
