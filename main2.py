#Take input
n = int(input("Enter the number of rows for the half pyramid: "))
print("Half Pyramid Pattern of Stars (*):")
#outer loopto handle number of rows
for i in range(n):
    #inner loop to handle number of columns
    for j in range(i + 1):
        #display result
        print("*", end="")
    print()