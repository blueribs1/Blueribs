percent = 0
rate_needed = 0
new_vaccinated = 32000000
population = 330000000
vaccinated = 32000000
vaccrate = 8400000
weeks = input("Target time periods (in weeks):")
weeks = int(weeks)
new_vaccinated = vaccrate*weeks + vaccinated
percent = new_vaccinated/population*100
rate_needed = (.8*population-vaccinated)/weeks/7000000
print(f"Percentage of population vaccinated by the end of the target period ({weeks} week(s)) is {percent:.2f}%")
print(f"Vaccination rate needed to reach herd immunity (80% of population) is {rate_needed:.2f} million per day.")