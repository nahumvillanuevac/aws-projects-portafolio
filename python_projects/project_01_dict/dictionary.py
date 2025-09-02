#Objetive of the program: read archives .txt, count lines and words, print a list with top 10 words.
import string
count = 0
dictionary = dict()
while True:
    try:
        filetxt = input("Enter the name of the .txt file: ")
        opentxt = open(filetxt)
        break
    except FileNotFoundError:
        print("Error: File not found. Please try again")
        #
for lines in opentxt:
    count += 1
    lines = lines.rstrip().split()
    #tuples(collections use for count), punctuation used to ignore signs
    for line in lines:
        line = line.strip(string.punctuation).lower()
        dictionary[line] = dictionary.get(line, 0) + 1

print("*******************************************************************************\nThis program is a txt File Analyzer \ncounts lines and words, and displays a top 10 most used words")

totalk = 0
bigword = None
largest = None

#add vk in newlist will help to make a for loop and sort value/key. If it's for most used word.
newlist = list()
for k,v in dictionary.items():
    if largest == None or v > largest:
        largest = v
        bigword = k
        most_used_word = largest, bigword
    kv = (k,v)
    newlist.append(kv)

#lambda, x: x[1] to order based in value
sort = sorted(newlist, key=lambda x: x[1], reverse=True)

print("*******************************************************************************")
print("      Top 10 most used words:")
#use "for" to add spaces in lines
for k,v in sort[:10]:
        print("     ",k,v)
        totalk = totalk + v

print("\n", "\n Most used word in the file is:", bigword,", with a total of",largest,"times." ,"\n Total lines:", count,"\n Total words:",totalk)
