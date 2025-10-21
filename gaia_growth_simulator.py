import sys
sys.argv
# (the input) python gaia_growth_simulator.py 0.1 2.5 20 output.txt
def main():
    """Takes input and verifies it is valid"""
    try:
        init_pop = float(sys.argv[1])
        grow_rate = float(sys.argv[2])
        iterations = int(sys.argv[3])+1
        if 0<init_pop<1:
            1==1
        else:
            restart = input("Invalid input (Ensure that initiial population is an percentage (between 0 and 1.0))\n Enter any input to exit: ")
            quit
    except:
        restart = input("Invalid input (make sure to use floats for population and growth rate, and integer for iterations)\n Enter any input to exit: ")
        quit
    
    """Calls logistic equation in order to calculate population"""
    population = logistic_equation(init_pop, grow_rate, iterations)

    """Opens and writes output to text file"""
    with open("output.txt", "w") as output:
        i=0
        for i in range(iterations):
            temp = population[i]
            output.write("{}  {:.3f}\n".format(i, temp))
            i+=1
    
    """Extra code to check if text document is correct"""
    # with open("output.txt", "r") as in_put:
    #     array = in_put.read()
    #     print(array)

def logistic_equation(init_pop, grow_rate, iterations):
    """Equation, first creates array to ouput to, adds the first variable and then runs a loop that runs the equation for each variable"""
    population = []
    population.append(init_pop)
    a = 1
    while a < iterations:
        pop2 = grow_rate*population[a-1]*(1-population[a-1])
        
        population.append(pop2)
        a+=1
    return population

if __name__ == "__main__":
    main()