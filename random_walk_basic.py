def main():
    # Imports
    import matplotlib.pyplot as plt
    import random
    # Variables called
    x_pos = 0
    y_pos = 0
    x = [0]
    y = [0]
    z = [zip(x, y)]
    a = 101
    # For loop, gets random number and goes in direction based on that 
    for b in range(a):
        plt.plot(x, y, 'o-')
        rand = random.choice(0,1,2,3)
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
    plt.show()
main()