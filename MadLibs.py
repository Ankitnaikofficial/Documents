#Making a MadLibs Generator
#Asking user to input values
adjective1=input("Enter an adjective: ")
adjective2=input("Enter another adjective: ")
food=input("Enter the name of food: ")
room=input("Enter the room name: ")
verb1=input("Enter a verb (past tense): ")
verb2=input("Enter another verb: ")
relative=input("Enter any relative's name: ")
noun1=input("Enter a noun: ")
liquid=input("Enter name of a liquid: ")
verb3=input("Enter a verb ending with ing: ")
body_part=input("Enter part of body (plural): ")
noun2=input("Enter a plural noun: ")
verb4=input("Enter a verb ending with ing: ")
noun3=input("Enter a noun: ")

#Printing the story
print("It was a "+adjective1+" , cold November day.I woke up to the "+adjective2+" smell of "+food+" roasting in the "+room+" downstairs. I "+verb1+" down the stairs to see if I could help "+verb2+" the dinner. My Mom said, 'see if "+relative+" needs a fresh "+noun1+" .'So I carried a tray of glasses full of "+liquid+" into the "+verb3+" room.When I got there, I couldn't believe my "+body_part+" ! There were "+noun2+" , "+verb4+" on the "+noun3+" !")

next=input("Do you want another madlib/story ? (yes/no)")
if next==("yes"):
    adjective3=input("Enter an adjective: ")
    noun4=input("Enter a noun: ")
    noun5=input("Enter a plural noun: ")
    person=input("Enter a name of a female person: ")
    adjective4=input("Enter another adjective: ")
    article=input("Enter an article of clothing: ")
    noun6=input("Enter a noun: ")
    city=input("Enter a name of a city: ")
    noun7=input("Enter a plural noun: ")
    adjective5=input("Enter an adjective: ")
    body_part2=input("Enter a body part: ")
    letter=input("Enter a letter of the alphabet: ")
    celebrity=input("Enter name of a celebrity: ")
    noun8=input("Enter a plural noun: ")
    adjective6=input("Enter an adjective: ")
    place=input("Enter a place: ")
    body_part3=input("Enter another body part: ")
    adjective7=input("Enter an adjective: ")
    adjective8=input("Enter another adjective: ")
    verb5=input("Enter a verb: ")
    noun9=input("Enter a plural noun: ")
    number=input("Enter a number: ")

    print("There are many "+adjective3+" ways to choose a/an "+noun4+" to read. First, you could ask for recommendations from your friends and "+noun5+". Just don't ask Aunt "+person+" she only reads "+adjective4+" books with "+article+" ripping goddesses on the cover. If your friends and family are no help, try checking out the "+noun6+" review in The "+city+" Times. If the "+noun7+" featured there are too "+adjective5+" for your taste, try something a little more low- "+body_part2+" , like "+letter+" : The "+celebrity+" Magazine, or "+noun8+" Magazine. You could also choose a book the "+adjective6+" - fashioned wsay. Head to your local library or "+place+" and browse the shelves until something catches your "+body_part3+" . or, you could save yourself a whole lot of "+adjective7+" trouble and log on to www.bookish.com, the "+adjective8+" new website to "+verb5+" for books! With all the time you'll save not having to search for "+noun9+" you can read "+number+" more books!")
    
elif next==("no"):
    print("Thank You")
