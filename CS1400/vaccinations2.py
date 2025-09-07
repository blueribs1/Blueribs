mathh = 0
percent = 0
rate_needed = 0
days = 0
new_vaccinated = 32000000
population = 330000000
vaccinated = 32000000
vacc_rate = 1200000
weeks = input("Target time periods (in weeks):")
weeks = int(weeks)
days = weeks*7
vacc_rate_increase = input("Daily vaccination increase rate (in %):")
vacc_rate_increase = int(vacc_rate_increase)
mathh = vacc_rate*(vacc_rate_increase/100)
vacc_rate_increase = 1+vacc_rate_increase/100
while (days > 0):
    vaccinated = vaccinated + vacc_rate
    vacc_rate = vacc_rate+mathh
    days = days-1
percent = vaccinated/population*100
print(f"Percentage of population vaccinated by the end of the target period ({weeks} week(s)) is {percent:.2f}%")
print(f"Vaccination rate needed to reach herd immunity (80% of population) is {rate_needed:.2f} million per day. (couldn't figure this part out)")
