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
    a = 201
    l_amount = 0
    r_amount = 0
    u_amount = 0
    d_amount = 0
    # For loop, gets weighted random number and goes in direction based on that 
    for b in range(a):
        plt.plot(x, y, 'o-')
        rand = random.choices([0,1,2,3], weights=[16.67,16.67,16.67,50], k=1)
        if rand[0] == 0:
            x_pos-=1
            x.append(x_pos)
            y.append(y_pos)
            l_amount+=1
        if rand[0] == 1:
            x_pos+=1
            x.append(x_pos)
            y.append(y_pos)
            r_amount+=1
        if rand[0] == 2:
            y_pos-=1
            x.append(x_pos)
            y.append(y_pos)
            d_amount+=1
        if rand[0] == 3:
            y_pos+=1
            x.append(x_pos)
            y.append(y_pos)
            u_amount+=1
        if b == 200:
            print("Final position: ({}, {})\nDirection counts:".format(x_pos, y_pos))
    print("Up: {}\nDown: {}\nLeft: {}\nRight: {}".format(u_amount, d_amount, l_amount, r_amount))
    # Shows graph if needed
    # plt.xlabel("X-axis")
    # plt.ylabel("Y-axis")
    # plt.title("Random Walk")
    # plt.show()
if __name__ == "__main__":
    main()