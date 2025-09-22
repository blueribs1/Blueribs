#variables
colonists = 0
food = 0
original_food = 0
ration_colonist = 0

#colonists
print("Enter the number of colonists:")
colonists = input()
colonists = float(colonists)

#food
print("Enter the total food units available:")
food = input()
food = float(food)
original_food = food

#math
ration_colonist = colonists*4
food-=ration_colonist

#output
print(f"Original supply: {original_food:.2f}") 
print(f"Ration allocation (4 units per colonist): {ration_colonist:.2f}")  
print(f"Festival stockpile remaining: {food:.2f}")