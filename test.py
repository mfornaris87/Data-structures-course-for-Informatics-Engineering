def ruse(a, b):
    c = 0
    while a != 0:
        if a % 2 != 0:
            c += b
        a = a // 2
        b = b * 2
    return c

print(ruse(37, 12))

def fibonacci(n):
    a, b = 0, 1
    while(b < n):
        print(b, end=' ')
        a, b = b, a+b
    print()

fibonacci(5)
