# Part 2
#opens a file through the provided command line and sums up the floats on every line
def open_file(): # takes no arguments
    try:
        file = input("Enter a file you wish to open: ") # command line argument
        file_contents = open(file, "r") # opens the wanted file
        for line in file_contents: # splits the text, converts the numbers into floats, and adds them
            try:
                line = line.rstrip("\n")
                line_list =  line.split(" ")
                sum = round(float(line_list[0]) + float(line_list[1]), 2)
                print(sum)
            except: # fails if the text are not numbers
                print("Failed to add this line")

    except IOError as e: # fails if the file doesn't exist
        print("Error: ", e)

open_file()