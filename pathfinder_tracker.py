# Imports
import matplotlib.pyplot as plt
import random
def main():
    lance()
    sophie()
    finn()

def lance():
    # Variables called
    x_pos = 0
    y_pos = 0
    x = [0]
    y = [0]
    z = [zip(x, y)]
    a = 501
    # For loop, gets random number and goes in direction based on that 
    for b in range(a):
        plt.plot(x, y, 'o-')
        rand = random.choice([0,1,2,3])
        if rand == 0:
            x_pos-=1
            x.append(x_pos)
            y.append(y_pos)
        if rand == 1:
            x_pos+=1
            x.append(x_pos)
            y.append(y_pos)
        if rand == 2:
            y_pos-=1
            x.append(x_pos)
            y.append(y_pos)
        if rand == 3:
            y_pos+=1
            x.append(x_pos)
            y.append(y_pos)
    # Exports graph
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Random Walk")
    plt.savefig("Lance_spacewalk.png", format="png")
    # plt.show()
def sophie():
    # Variables called
    x_pos = 0
    y_pos = 0
    x = [0]
    y = [0]
    z = [zip(x, y)]
    a = 501
    l_amount = 0
    r_amount = 0
    u_amount = 0
    d_amount = 0
    # For loop, gets weighted random number and goes in direction based on that 
    for b in range(a):
        plt.plot(x, y, 's-')
        rand = random.choices([0,1,2,3], weights=[16.67,16.67,16.67,50], k=1)
        if rand[0] == 0:
            x_pos-=1
            x.append(x_pos)
            y.append(y_pos)
        if rand[0] == 1:
            x_pos+=1
            x.append(x_pos)
            y.append(y_pos)
        if rand[0] == 2:
            y_pos-=1
            x.append(x_pos)
            y.append(y_pos)
        if rand[0] == 3:
            y_pos+=1
            x.append(x_pos)
            y.append(y_pos)
    # Plots graph
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Random Walk")
    plt.savefig("Sophie_spacewalk.png", format="png")
def finn():
    # Variables called
    x_pos = 0
    y_pos = 0
    x = [0]
    y = [0]
    z = [zip(x, y)]
    a = 501
    l_amount = 0
    r_amount = 0
    u_amount = 0
    d_amount = 0
    # For loop, gets weighted random number and goes in direction based on that 
    for b in range(a):
        plt.plot(x, y, '^-')
        rand = random.choice([0,1])
        if rand == 0:
            x_pos-=1
            x.append(x_pos)
            y.append(y_pos)
        if rand == 1:
            x_pos+=1
            x.append(x_pos)
            y.append(y_pos)
    # Plots graph
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Random Walk")
    plt.savefig("Finn_spacewalk.png", format="png")
if __name__ == "__main__":
    main()