# Input
colonists = int(input("Enter the number of colonists: "))
food = int(input("Enter the total food units available: "))
food2 = food

# Math
festival_allocation = colonists*4
food-=festival_allocation
food3=food
zerin_share = food*0.15
food-=zerin_share
lyria_share=food*0.1
food-=lyria_share
ration_share=food/colonists
lyria_share+=ration_share
zerin_share+=ration_share

# It looks like the sample did not do the after ration share since lyria is getting 165 in the example
# Output
print(f"Original supply: {food2:.2f}")
print(f"Ration allocation (4 units per colonist): {festival_allocation:.2f}")
print(f"Festival stockpile remaining: {food3:.2f}")
print(f"Zerin's share: {zerin_share:.2f}")
print(f"Lyra's share: {lyria_share:.2f}")
print(f"Share per colonist: {ration_share:.2f}")