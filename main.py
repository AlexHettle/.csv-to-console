import csv
#This function runs through the csv file twice, the first time to find the
#largest amount of characters in each column. These numbers are used in order
#to format when printing. The second run through prints out the lines in a 
#properly formatted fashion using the max characters numbers found previously.
def read_and_display(file):
    reader=csv.reader(file)
    first_row=next(reader)
    length_of_column_list=len(first_row)*[0]
    file.seek(0)
    for line in reader:
        if line!=first_row:
            for i in range(len(length_of_column_list)):
                if len(line[i])>length_of_column_list[i]:
                    length_of_column_list[i]=len(line[i])+2
    file.seek(0)
    for line in reader:
        final_line=""
        newline=200
        print("-"*200)
        for i in range(len(length_of_column_list)):
            if line[i]:
                final_line+=line[i]+((length_of_column_list[i]-len(line[i]))*" ")+" "
            if len(final_line)>=newline-50:
                final_line+="\n"
                newline+=200
        print(final_line)
    print("-"*200)
#This function tries to open the file and run it through the read_and_display
#function. If the path does not work, the function print out an error.
def try_opening(filename):
    try:
        file=open(filename,"r")
        file.seek(0)
        read_and_display(file)
    except:
        print("Invalid filename. Please try again.")
#This function takes in the path from the user and decides how to handle it.
#If the user enters EXIT, the program ends, if the user enters a path to a 
#csv file, it passes that path through the functions try_opening.
def main():
    print("Welcome!")
    descision=0
    while descision==0:
        filename=input("Please enter the path of a .csv file you want "+
                       "printed into the console, or enter EXIT to quit "+
                       "the program:\n")
        if(filename.upper()=="EXIT"): descision=1
        else: try_opening(filename)
    print("Goodbye!")
main()
