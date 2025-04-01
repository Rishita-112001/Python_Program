days = int(input("Enter the number of days in the month: "))
start_day = int(input("Enter the start day of the week (0 for Monday, 1 for Tuesday, etc.): "))

# Print the days of the week
print("\nMon Tue Wed Thu Fri Sat Sun")

# Print leading spaces for the first week
print("    " * start_day, end="")

for day in range(1, days + 1):
    print(f"{day:3}", end=" ")

    if (start_day + day) % 7 == 0:  # Move to the next line after Sunday
        print()