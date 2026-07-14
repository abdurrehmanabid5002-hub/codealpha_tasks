print("Hello, World!")
a=2 
b=3
c=a+b
print("The sum of a and b is:", c)
a= [1, 2, 3, 4, 5]
print("The list a is:", a)
def hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]
    result = [f"{rods[0]} {rods[1]} {rods[2]}"]
    
    def move(k, source, target, auxiliary):
        if k > 0:
            move(k - 1, source, auxiliary, target)
            rods[target].append(rods[source].pop())
            result.append(f"{rods[0]} {rods[1]} {rods[2]}")
            move(k - 1, auxiliary, target, source)
            
    move(n, 0, 2, 1)
    return "\n".join(result)

# for loop
for i in range(1, 6):
    print("*" * i)

# pattren of A
rows = 7

for i in range(rows):
    for j in range(rows):
        if (j == 0 or j == rows - 1) and i != 0:
            print("*", end="")
        elif i == 0 and j != 0 and j != rows - 1:
            print("*", end="")
        elif i == rows // 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()