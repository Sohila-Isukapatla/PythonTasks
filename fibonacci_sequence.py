n = int(input("Enter the value:"))
a, b = 0, 1

for _ in range(n):
    print(a)
    a, b = b, a + b