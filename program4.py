numbers = list(map(int, input("Enter the numbers:").split()))
divisor=[1,2,3,4,5,6,7,8,9]

result={}

for d in divisor:
    count=0
    for num in numbers:
        if num%d==0:
            count+=1
    result[d]=count

print(result)