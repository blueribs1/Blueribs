def main():
    """Takes input and ensures that it is valid"""
    try:
        start_num = int(input("Enter starting number: "))
        end_num = int(input("Enter ending number: "))
        step_size = int(input("Enter step size: "))
    except:
        restart = input("Invalid input, try again? (y) or (n)")
        if restart.lower() == "y":
            main()
        else:
            quit
    
    """creates variables needed for for() loop, and goes through the range, adding the numbers to a list"""
    list_array = []
    i = end_num
    start_num+=1
    for i in range(end_num, start_num):
        if(i in range(end_num, start_num, step_size)):
            list_array.append(i)
        i+=1
    list_size=len(list_array)
    
    """Outputs list to a text document"""
    with open("number_series.txt", "w") as output:
        f=0
        for f in range(list_size):
            begin = list_array[f]
            output.write(f"{begin}\n")
            f+=1
    print(f"Saved {list_size} numbers to number_series.txt")
    
    """Extra code to check if text document is correct"""
    # with open("number_series.txt", "r") as in_put:
    #     array = in_put.read()
    #     print(array)
    
if __name__ == "__main__":
    main()
