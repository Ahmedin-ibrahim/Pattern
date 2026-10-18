# a pattern needs two things:
# 1) how many rows 
# 2) how many characters per row
for i in range(10):
    for j in range(i + 1):
        print("*", end="")
    print()