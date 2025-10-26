def main():
    """Variables created that are needed for the function"""
    info = 0
    warning = 0
    error = 0
    i = 0
    longest = ""
    """Reads server logs and splits them up"""
    with open("server_logs.txt", "r") as in_put:
        test = in_put.read()
        test = test.split("|")
        """Loop that first checks if each message is the new longest, and then counts the severities"""
        for a in test:
            if len(a) > len(longest):
                longest = a
            if "INFO" in a:
                info+=1
            if "WARNING" in a:
                warning+=1
            if "ERROR" in a:
                error+=1
        """Outputs to the summary log"""
        with open("log_summary.txt", "w") as output:
            output.write("Log Summary\nINFO: {}\nWARNING: {}\nERROR: {}\nLongest message: {}".format(info, warning, error, longest))
            
if __name__ == '__main__':
    main()