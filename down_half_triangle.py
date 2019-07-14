num = int(input("Enter The Number of Pattern = "))
for i in range(num):
    for j in range(num-i):
        print("*",end="")
    print()