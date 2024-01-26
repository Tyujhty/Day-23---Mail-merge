#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
names = open("./Input/Names/invited_names.txt")
letter = open("./Input/Letters/starting_letter.txt", "r").read()

for name in names:
    new_name = name
    output_path = "./Output/ReadyToSend/"
    new_letter_name = f"invitation_{name}.txt"

    new_file_path = output_path + new_letter_name
    new_letter = letter.replace("[name]", new_name)

    with open(new_file_path, "x") as modified_letter:
        modified_letter.write(new_letter)