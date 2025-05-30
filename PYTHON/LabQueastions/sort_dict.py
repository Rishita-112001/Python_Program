# Given dictionary
people = {'Arham': 'Blue', 'Lisa': 'Yellow', 'Vinod': 'Purple', 'Jenny': 'Pink'}

# 1. Find out how many students are in the list
print("Total students:", len(people))

# 2. Change Lisa’s favourite colour
people['Lisa'] = 'Red'

# 3. Remove 'Jenny' and her favourite colour
people.pop('Jenny')

# 4. Sort and print students and their favourite colours alphabetically by name
sorted_people = dict(sorted(people.items()))

# Output
print("Sorted students and their favourite colours:", sorted_people)