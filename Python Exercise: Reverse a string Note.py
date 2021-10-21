# Found These solutions Online while trying to do it on my own
# Notes of understanding what these codes to 
# Python Exercise: Reverse a string

def reverse(str1):
    atr1 = ""
    val = len(str1)  # Finds length of index
    while val > 0:
        atr1 += str1[val - 1]  # reduces val to make next index change to next number
        val = val - 1  # reduces val to make next index change to next number

    return atr1


user_input = input("Enter anything you would like to reverse: ")
print(reverse(user_input))


def reversea(itr):
    return itr[::-1]  # Double colon


user_input = input("Enter anything you would like to reverse: ")
print(reversea(user_input))
