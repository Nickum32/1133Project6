# CSci 1133 HW 6
# Nicholas Mayer
# Problem C
#
# This program creates an inverted file
#
def main():
    space = ' ' 
    word_delimiters = (space, ',', ';', ':', '.', '"',"'", '(',
    ')','?','!','','\n')
# list of word delimiters for document manipulation
    doc1 = open('doc1.txt', 'r', encoding = 'UTF-8') # open all docs
    doc2 = open('doc2.txt', 'r', encoding = 'UTF-8')
    doc3 = open('doc3.txt', 'r', encoding = 'UTF-8')
    doc4 = open('doc4.txt', 'r', encoding = 'UTF-8')
    invertedDoc = open('mayer379', 'w', encoding = 'UTF-8')
    docList = [doc1, doc2, doc3, doc4] # create a list of docs for iteration
    wordDict = {}
    for item in docList: # main for loop to parse through each file
        docString = item.read() # create a string version of the file's text
        docString = docString.lower() 
        docNum = docList.index(item) + 1 # creates an integer variable for each document (e.g. 1 for doc1)
        for char in docString:
            if char in word_delimiters:
                docString = docString.replace(char, ' ')
        docString = docString.split(' ')
        for word in docString:
            if word == '':
                continue
            if word.isnumeric():
                continue
            if word in wordDict:
                if docNum not in wordDict[word]:
                    wordDict[word].append(docNum)
            else:
                wordDict[word] = []
                wordDict[word].append(docNum)
        item.close()
    for entry in sorted(wordDict):
        for item in wordDict[entry]:
            invertedDoc.write(entry + ' ' + str(item) + '\n')
    invertedDoc.close()

if __name__ == '__main__':
    main()
