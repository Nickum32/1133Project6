# CSci 1133 HW 6
# Nicholas Mayer
# Problem B
#
# Applies a Caesar cypher to a text file

def main():
    Done = False
    while not Done: # main program loop
        fname = input('Enter file name of text file to encrypt: ')
        try: # try except block to test for valid file name
            fObj = open(fname, 'r')
        except FileNotFoundError:
            print('Input Error: No such file or directory:', fname)
            continue
        keepGoing = True
        while keepGoing: # while loop to ensure valid encryption shift value
            shift = input('Enter a shift number from 1 to 13: ')
            if shift.isdigit():
                shift = int(shift)
                if shift >= 1 and shift <= 13:
                    keepGoing = False # exits the while loop once shift value has been evaluated to meet criteria
        fRead = fObj.read()
        newStr = encrypt(fRead, shift)
        fObj.close()
        print('Result of encryption:\n', newStr)
        keepGoing = input('Continue? (Enter "Y" or "y"): ')
        if keepGoing not in ('Y', 'y'):
            Done = True
        

def encrypt(astr, shiftNum): # encryption function
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    astr = astr.lower() # convert all alphabetical characters to lwercase
    encrypted = '' # create empty string on which to concatenate
    for char in astr: # iterate over each character in the string
        if char in alphabet: # check if the character is a letter
            index = alphabet.index(char) # get the letter's 'number'
            index += shiftNum # applies encryption shift
            if index > 25: # checks if new index is greater than the alphabet
                index -= 26 # starts index values back at 0
            encrypted += alphabet[index] # adds the shifted letter to encrypted string
        else:
            encrypted += char
    return encrypted

def decrypt(astr, shiftNum):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    astr = astr.lower()
    decrypted = ''
    for char in astr:
        if char in alphabet:
            index = alphabet.index(char)
            index -= shiftNum
            if index < 0:
                index +=26
            decrypted += alphabet[index]
        else:
            decrypted += char
    return decrypted

if __name__ == '__main__':
    main()
