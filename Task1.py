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