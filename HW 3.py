def find_cooccurance(d, inp_str): #Finds which lines the user's input appears in the dictionary
    inp_str = inp_str.strip().split(' ') #Splits the user's inputted words into a list
    t1=tuple()
    t2=tuple()
    s1=set()
    s2=set()
    for word in inp_str: #Goes through each word the user inputted
        word = word.strip(',.\n')
        word = word.lower()
        print("\n", "The co-occurance for: ", word) #Displays which lines the given input(s) appear in
        print("Line(s): ", d.get(word, "word doesn't appear in dictionary"))
        t1+=tuple(d.get(word, "word doesn't appear in dictionary")) #Adds each word's line number to a tuple
    s1.update(t1) #Adds the tuple to a set
    for word2 in d: #Goes through each words in the dictionary and adds their values to a tuple
        t2+=tuple(d.get(word2, "Somthing happened"))
    s2.update(t2) #Adds the tuple to a set
    inter=s1.intersection(s2) #Creates a set that contains the elements that are found in both s1 & s2

def read_data(fp): #Goes through each word in the opended file, and adds them all to a dictionary
    mydict=dict() #Creates an empty dictionary
    linum=0
    for line in fp: #Goes through each line in the opened file
        line = line.strip('., ').split(' ')
        linum+=1
        for word in line: #Goes through each word in each line of the opened file
            word = word.strip(',.\n')
            if word.lower() in mydict and linum not in mydict[word.lower()]: #Adds word to the dictionary with it's value being the line number it appears in
                mydict[word.lower()].append(linum)
            else: #Adds word to the dictionary if it isn't there already
                mydict.setdefault(word.lower(), [linum])
    for word in mydict:
        mydict[word]=set(mydict[word])
    return mydict #Gives the function (read_data(fp)) the value of mydict

def open_file(): #Opens the file that's going to be read from
    while True:
        try:
            f=input('Enter file name: ') #Asks the user to input a file name
            fp=open(f, 'r') #Attempts to open the inputted file and assings it to the variable (fp)
            break
        except IOError: #If file doesn't exist, lets the user know the file doesn't exist and restarts the program
            print("Sorry, that file doesn't exist")
    return fp

def main(): #Holds the beginning function and controls wether the program continues or not
    fp = open_file() #Calls the function to open a file and holds the file
    mydict = read_data(fp) #Calls the function to create a dictionary and holds the dictionary
    while True:
        string=input("Enter space-seperated word(s), or enter 'quit'/'Q' to exit: ") #Asks user to input a word(s)
        string=string.strip('.,!?\n ')
        if string == 'quit' or string == 'Q':
            fp.close()
            print("End of program")
            break
        else:
            find_cooccurance(mydict, string) #Calls the function to find the occurance of the word(s) the user inputted
main() #Starts the entire program
