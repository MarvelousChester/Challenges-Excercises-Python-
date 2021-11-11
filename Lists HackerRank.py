
# find all the possible permutations of a cuboid on a 3d grid
x = int(input())
# asks for input
y = int(input())
z = int(input())
n = int(input())

a = []
# [i,j,k] are the i you use in loops and in then end of the loop it creates a list for cordinates
print( [[i,j,k] for i in range( x + 1) for j in range( y + 1) for k in range(z+1) if ( ( i + j + k ) != n )  ])


#
# Find the second loest score in Nested Lists
#
track = [] # list for nested lists
new_score = []  # tracking score list
second = [] # list for people second last
for _ in range(int(input())): # loop for input and adding to list
    name = input()
    score = float(input())
    
    track.append([name,score]) # adds a nested list into lists
    new_score.append(score)
    

sorted(set(new_score))  # sorts score

a = new_score[1] # finds the second lowest score

for i in track: # loop to detect the names with the second lowest score
    if a == i[1]: # checks the first index of the nested list to check score if match
        second.append(i[0]) # adds the the names of who match the second lowest score to list

second = sorted(second) # Adds 
for i in second:
    print(i)    
#
# Find Runner up Score
#
#   
n = int(input())
arr = map(int, input().split())

a = sorted(set(arr)) # sorts the list and remove duplicates

count = 0
for i in (a):
    count = count + 1 # Counts how many numbers are in the array


print(a[count-2]) # Finds the second num in the array subtracted by total nums
    
   
# Find the second Lowest Grade in a Class
#
if __name__ == '__main__':
    track = []
    lowest = 0
    low_score = []
    low_name = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        low_score.append(score) 
        track.append([name,score])
        
    low_score = sorted(set(low_score))
        
    a = low_score[1]
        
    for i in track:
        if a == i[1]:
            low_name.append(i[0])
                
    low_name = sorted(low_name)
    for i in (low_name):
        print(i)
