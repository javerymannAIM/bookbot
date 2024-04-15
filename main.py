import os

def main():
    path_to_file = r"./books/frankenstein.txt"
    book = getBook(path_to_file) # Get book text as string
    word_count = countWords(book)

    print(f"---------- Begin report of {os.path.basename(path_to_file)} ----------")
    print(f"{len(word_count)} words in document.\n")
    letter_count = createReport(countLetters(book))



    return

def countWords(body):
    word_list = body.split()
    print("There are ", len(word_list), " words.")

    return word_list

def getBook(path):
    with open(path) as f:
        text = f.read()
    print(text)

    return text

def countLetters(text):
    text = text.replace(" ", "").lower()
    # print(new_str)
    
    count = {}
    
    for i in text:
        if i.isalpha():
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
    # createReport(count)
    return count

def createReport(count):
    log = ""
    for key in count:
        log += f"The {key} character appears {count[key]} times.\n"
    return print(log)
    
    # take text, remove all spaces
    # convert string to lowercase
    # iterate through new string and if in list, add to count, otherwise add entry and initialize with count = 1

main()