import sys


def double123():
    for i in [1, 2, 3]:
        print((lambda x: x * i)(2))
    print("end")


count = 0
for line in sys.stdin:
    count += 1

print(count)
