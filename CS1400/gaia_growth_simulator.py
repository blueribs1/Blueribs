import sys
sys.argv
# python gaia_growth_simulator.py 0.1 2.5 20
def main():
    try:
        init_pop = float(sys.argv[1])
        grow_rate = float(sys.argv[2])
        iterations = int(sys.argv[3])+1
    except:
        1==1
        
    population = []
    population.append(init_pop)
    a = 1
    while a < iterations:
        pop2 = grow_rate*population[a-1]*(1-population[a-1])
        
        population.append(pop2)
        a+=1
    print(population)
    b=0
    c=0
    while b < iterations:
        pop3 = round(float(population[b]), 3)
        
        print("{}, {:.3f}".format(b, pop3))
        b+=1
        c+=1
        


main()