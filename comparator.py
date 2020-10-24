#GITHUB -> yararbasK

def set_comparable():
    try:
        while True:
            print("Enter the buildpath for comparable txt file (full path)")
            comparable_txt = input()

            #Removing the python's left-to-right embedding marking (\u202a)

            comparable_txt = comparable_txt.strip("\u202a")
            print("Path for selected object is {} if it is true press 1 else press 2 ".format(comparable_txt))
            verification = int(input("Please Only Use 1 or 2"))
            if verification == 1:
                comparable_txt_first = open(file=comparable_txt , mode='r+')
                print("Comparable txt file is successfully added")
                return comparable_txt_first
            elif verification == 2:
                continue
            elif verification == 0:
                print("Exiting from comparable selection")
                break

    except EnvironmentError as E:
        print(str(E))

def set_comparator():
    try:
        while True:
            print("Please Specify the comparator's path")
            comparator_txt = input()
            print("Path for the comparator file is {} If it is correct press 1 else press 2 for re-entering the path ('0' for exit)".format(comparator_txt))
            validator = int(input())
            if validator == 1:
                comparator_txt = comparator_txt.strip("\u202a")
                comparator_txt_first = open(file=comparator_txt, mode="r+")
                print("Comparator txt file is successfully added")

                return comparator_txt_first
            elif validator == 2:
                continue
            elif validator == 0:
                print("Exiting from comparator selection")
                break
    except EnvironmentError as E:
        print(str(E))

def compare(comparator_file , comparable_file):
    result_file = open("matched_strings.txt", "w+")
    comparable_list = []
    comparator_list = []
    for line in comparable_file:
        for word in line.split():
            comparable_list.append(word)
    for comparator_line in comparator_file:
        for comparator_word in comparator_line.split():
            comparator_list.append(comparator_word)

    for word_in_list in comparable_list:
        for comparator_word_in_list in comparator_list:
            if word_in_list == comparator_word_in_list:
                result_file.write(word_in_list+"\n")


if __name__ == '__main__':
    comparable_file = set_comparable()
    comparator_file = set_comparator()
    compare(comparator_file , comparable_file)
