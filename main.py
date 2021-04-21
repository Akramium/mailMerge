with open("./Input/Names/invited_names.txt") as names:
    names_list = names.readlines()
    with open("./Input/Letters/starting_letter.txt") as letter:
        start_letter = letter.read()
        for name in names_list:
            with open(f"./Output/ReadyToSend/letter_for_{name}".strip("\n") + ".txt", mode="w") as letter_to_send:
                relace_name = start_letter.replace("[name]", name.strip("\n"))
                letter_to_send.write(relace_name)
