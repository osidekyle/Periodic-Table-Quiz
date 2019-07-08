


entered = []




def answer_getter():
    while len(entered) < 5:
        enter = input("Enter an element:")
        if enter in entered:
            print("No duplicates allowed\n")
        else:
            entered.append(enter.lower())




print("Enter the name of 5 of the first 20 elements on the periodic table of elements\n")
answer_getter()




get_ipython().system('curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements1_20.txt')




twenty_elements = open("elements1_20.txt","r")




true_elems=[]
one_elem = ''


for item in range(20):
    one_elem = twenty_elements.readline().lower()
    true_elems.append(one_elem.strip().lower())




print(true_elems)




correcto = []
incorrecto = []




for words in entered:
    if words.lower() in true_elems:
        correcto.append(words)
    else:
        incorrecto.append(words)





percen = len(correcto)*20




print("Quiz score:",percen,"% correct\n")
print("Correct answers:",correcto)
print("Incorrect answers:",incorrecto)

