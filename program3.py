a = int(input("Enter a number: "))
n = a if a % 2 == 1 else a - 1
odds = [str(2*i + 1) for i in range(n)]
print(", ".join(odds))


