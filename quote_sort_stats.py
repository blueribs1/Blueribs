def main():
    """Opens file"""
    with open("quotes_data.txt", "r") as in_put:
        """Creates variables needed for for() loop"""
        output = {}
        largest_line = " "
        average = 0
        line_number = 0
        sorting = []
        """Splits text up, adds the text size to average, keeps track of # of lines"""
        for line in in_put:
            output = line.split('|')
            average += len(output[0])
            line_number += 1
            """Checks to see if each line is the new largest"""
            if len(output[0]) > len(largest_line): 
                largest_line = output[0]
                largest_line_2 =  output[1]
            """Adds line to list"""
            sorting.append(output[0])
        """finds average, sorts the list from largest to smallest"""
        average/=line_number
        average=round(average)
        sorting.sort(key=len, reverse=True)
        """opens output, outputs everything needed to file"""
        with open("sorted_quotes.txt", "w") as output:
            output.write("Sorted Quote Report\nLongest quote (line {}): {}".format(largest_line_2[0], largest_line))
            output.write(f"Average quote length: {average}")
            for i in sorting:
                output.write(i)

if __name__ == '__main__':
    main()