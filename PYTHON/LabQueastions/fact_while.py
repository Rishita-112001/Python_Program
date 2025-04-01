n = 0
fact = 1

while fact < 2_000_000_000:  # Keep computing while factorial is below 2 billion
    print(f"{n}! = {fact}")
    n += 1
    fact *= n