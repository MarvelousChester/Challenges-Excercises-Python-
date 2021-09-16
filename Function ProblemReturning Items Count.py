#Write a function that takes a list as a parameter and returns the number of items in the list.
#Make it user input
def items(user_list):
    counter = 0
    for i in user_list:
        counter += 1

    print("The total number of elements:" + str(counter))


print("Type Done when complete")
item_lists2 = []
while True:
    userInput = input("Enter an input ")

    if userInput == "done" or userInput == "Done":
        break
    elif userInput:
        item_lists2.append(userInput)
    else:
        print("Invalid input, try again")
        continue

print(item_lists2)
print(items(item_lists2))
