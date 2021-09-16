# Find the sum of all multiples of 3, 5
# added challenge, remove the multiples of the same number twice from repeating

total = 0
total2 = 0
total3 = 0
for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        total += i
        continue
    if i % 3 == 0:
        total += i
    if i % 5 == 0:  # if you add an elif statement here you don't need 7 to 9 lines
        total += i


print(total)


# the total with duplicates is 950 + 1683 = 2633
# 2318 without duplicates
