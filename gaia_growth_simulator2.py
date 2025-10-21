import sys
sys.argv
# python gaia_growth_simulator.py 0.1 2.5 20
def main():
    try:
        init_pop = float(sys.argv[1])
        grow_rate = float(sys.argv[2])
        iterations = int(sys.argv[3])+1
    except:
        restart = input("Invalid input (make sure to use floats for population and growth rate, and integer for iterations)\n would you like to try again? (y) or (n) ")
        if restart.lower == 'y':
            main()
        else:
            quit
    population = logistic_equation(init_pop, grow_rate, iterations)
    b=0
    while b < iterations:
        pop3 = round(float(population[b]), 3)
        
        print("{}   {:.3f}".format(b, pop3))
        b+=1
    
    # """Outputs list to a text document"""
    # with open("number_series.txt", "w") as output:
    #     f=0
    #     for f in range(list_size):
    #         begin = list_array[f]
    #         output.write(f"{begin}\n")
    #         f+=1
    # print(f"Saved {list_size} numbers to number_series.txt")
    
    # """Extra code to check if text document is correct"""
    # # with open("number_series.txt", "r") as in_put:
    # #     array = in_put.read()
    # #     print(array)

def logistic_equation(init_pop, grow_rate, iterations):
    population = []
    population.append(init_pop)
    a = 1
    while a < iterations:
        pop2 = grow_rate*population[a-1]*(1-population[a-1])
        
        population.append(pop2)
        a+=1
    return population

main()