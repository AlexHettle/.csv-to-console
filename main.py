import csv
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
def try_opening(filename):
    try:
        file=open(filename,"r")
        file.seek(0)
        read_and_display(file)
    except:
        print("Invalid filename. Please try again.")
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
