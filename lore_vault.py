def main():
    """Takes arguments in to get the sourcefile"""
    import sys
    sys.argv
    text_old = sys.argv[1]
    text = sys.argv[1] + ".txt"
    text_out = text_old + "_book.txt"
    """Opens file"""
    with open("TTL.txt", "r", encoding="utf-8") as in_put:
        """Creates variables needed for for() loop"""
        output = []
        output_2 = dict()
        largest_line = " "
        average = 0
        line_number = 0
        sorting = []
        """Splits text up, adds the text size to average, keeps track of # of lines"""
        for line in in_put:
            if "|" in line:
                output = line.split('|')
                average += len(output[0])
                line_number += 1
                """Checks to see if each line is the new largest"""
                if len(output[0]) > len(largest_line): 
                    largest_line = output[0]
                    largest_line_2 =  output[1]
                """Adds line to list"""
                sorting.append({"line_text":output[0],"number":int(output[1])})
        """Finds average, sorts the list by numbers"""
        average/=line_number
        average=round(average)
        sorting.sort(key=sortation)
        """Opens output, outputs everything needed to file"""
        with open(text_out, "w") as output:
            output.write("{}\nLongest ({}): {}".format(text_old, largest_line_2, largest_line))
            output.write(f"\nAverage length: {average}\n")
            outputer = []
            for i in sorting:
                outputer.append(i["line_text"])
            for f in outputer:
                output.write(f + "\n")
def sortation(e):
    return e["number"]
if __name__ == '__main__':
    main()