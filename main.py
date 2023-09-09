#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

TEXT_TO_REPLACE = "[name]"
invited_people = []

with open('./Input/Letters/starting_letter.txt', 'r') as starting_letter:
    text = starting_letter.read()

with open('./Input/Names/invited_names.txt', 'r') as list_of_names:
    for name in list_of_names:
        name = name.strip()
        invited_people.append(name)

for person in invited_people:
    with open (f'./Output/ReadyToSend/letter_for_{person}.txt', 'w') as final_letter:
        new_text = text.replace(TEXT_TO_REPLACE, person)
        final_letter.write(new_text)
