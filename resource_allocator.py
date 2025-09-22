# variables
citizens = 0
units = 0
crew_share = 0
mira_share = 0
tov_share = 0
math = 0

# citizens
print("How many citizens:")
citizens = input()
citizens = float(citizens)

# units
print("How many total units:")
units = input()
units = float(units)

# math
units -= (citizens-2)*3
mira_share = units*0.13
units -= mira_share
tov_share = units*0.11
units-=tov_share
math = units/20
mira_share+=math
tov_share+=math
crew_share+=math+3

# output and rounding (works by having beginning f, then " and curly brackets around variables
# that can be rounded with :.2f)
print(f"Mira's share: {mira_share:.2f}")
print(f"Tov's share: {tov_share:.2f}")
print(f"Crew's share: {crew_share:.2f}")