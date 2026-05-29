def reader():
    with open("1000_common_passwords.txt") as new_file:
        word_list = []
        for line in new_file:
            word_list.append(line.strip())

        return word_list