# Write a program to print the even numbers from a given list

def even(num):
    even_list = []
    for i in num: # loops through whatever is inside the num checking each value
        if i % 2 == 0: # Checks if the int is even and if so appends into a even list
            even_list.append(i) 
        else: 
            continue
    return even_list  # Once loop done returns even_list as num


a = []
print("Type Stop when done")

while True: # Loop for user input for how many digits they want to check through to see if even or not
    user_input = (input("Enter a digit: "))
    if user_input == "Stop":
        break
    else:
        user_input = int(user_input)
        a.append(user_input)

print(even(a))
