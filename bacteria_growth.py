def main():
    """This function begins with taking inputs and automatically changing 
    them to ints or floats depending, taking into account invalid inputs"""
    try:
        start_pop = int(input("Enter starting population: "))
        hourly_growth = float(input("Enter hourly growth rate: "))
        hours = int(input("Enter number of hours (Integers only): "))
    except:
        restart = input("Invalid input, try again? (y) or (n): ")
        if restart.lower == "y":
            main()
        else:
            quit
    """Here, the function creates variables needed for the loop, and then runs a
    loop that calculates the population and puts the population onto a list"""
    hours+=1
    population_history = []
    population = start_pop
    for hour in range(hours):
        population_history.append(f"Hour {hour}: {population:.2f}")
        population*=hourly_growth
    """Then the function prints the list off"""
    for hour in range(hours):
        print(population_history[hour])
main()
