def reader():
    with open("data/1000_common_passwords.txt") as new_file:
        word_list = []
        for line in new_file:
            word_list.append(line.strip())

    with open("data/usernames.txt") as new_file:
        username_list = []
        for line in new_file:
            username_list.append(line.strip())

        return word_list, username_list