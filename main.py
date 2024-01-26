names = open("./Input/Names/invited_names.txt")
letter = open("./Input/Letters/starting_letter.txt", "r").read()

for name in names:
    new_name = name.strip()
    output_path = "./Output/ReadyToSend/"
    new_letter_name = f"invitation_{name}.txt"

    new_file_path = output_path + new_letter_name
    new_letter = letter.replace("[name]", new_name)

    with open(new_file_path, "x") as modified_letter:
        modified_letter.write(new_letter)