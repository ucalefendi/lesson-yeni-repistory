import json


# opening the dictionary.json file in read mode
fin = open("dictionary.json","r")
#reading the contents for json file to cont object
cont = json.load(fin)
print(type(cont))


#1.Display the words that begin with a spesific letter.
def dispwords():
    letter = input("Enter the letters to display that words which it begins with:  ")
    for i in cont:
        if i.startswith(letter):
            print(i)

# 2.Find a spesific word.
def  findword():
    word = input("Enter the word to check in the dictionary:  ").lower()
    found = False
    for i in cont:
        if i == word:
            found = True
    if found == False:
        print("No such word exists in the dictionary")
    else:
        print("it is there in the dictionary")  

#3.Display the meaning of the spesific word. 
def  displaym():
    word = input("Enter the word to check the word meaning of:  ").lower()
    found = False
    for key,value in cont.items():
        if key == word:
            found = True
            print("{} word has meaning {}".format(key,value)) 
    if found == False:
        print("No such word exists")  


#4.Display the words-meanings for the spesific word that is there are in the meaning.
def dispsm():
    word = input("Enter the word to be searched in the dictionary and to display meaning of:   ")
    found = False
    for key,value in cont.items():
        if key == word or word in value:
            found = True
            print("Word {} - Meaning {}".format(key,value))
    if found == False:
        print("No such word in dictionary")      

#5.Search and display words by number of letters.
def searchno():
    num = int(input("Enter number of letter of the word:  "))
    found = False
    for key in cont:
        if len(key) == num:
            print(key) 
            found = True
    if found == False:
        print("No words with spesific length")        


# menu for interactive dictionary
while True:
    try:
        print("""
            I N T E R A C T I V E    D I C T I O N A R Y  
            ============================================  
            1.Display the words that begin with a spesific letter.
            2.Find a spesific word.
            3.Display the meaning of the spesific word. 
            4.Display the words-meanings for the spesific word that is there are in the meaning.
            5.Search and display words by number of letters.
            6.Exit.      

        """)
        
        choice = int(input("Enter your choice of operation (1-6):   "))
        if choice == 1:
            dispwords()
        elif choice == 2:
            findword()
        elif choice == 3:
            displaym()
        elif choice == 4:
            dispsm()
        elif choice == 5:
            searchno()
        elif choice == 6:
            break
        else:
            print("invalid number!.Enter any number between: (1-6):")

    except:
        print("invalid input")        

        



