f = 1
n = 0
for n in range(11):  # Loop from 0 to 10
    if n == 0:
        fact = 1
    else:
        fact *= n
    print(f"{n}! = {fact}")