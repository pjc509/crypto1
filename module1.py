#
# Project 1, Applied Cryptography
# NYU Tandon School of Engineeering Spring 2021 
# [names here] 
#
#
import random

#constants
IN_LENGTH = 500
KEY_LENGTH = 5
UPPER = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER = " abcdefghijklmnopqrstuvwxyz"

#This function can be used to encrypt a plain-text with a random repeating key
def encrypt(string):
    key = []
    index_plain = []
    index_cipher = []
    string_ciphered = ""
    i = 0

    # generate a randon key of keylength and save into an array (key)
    while len(key) < KEY_LENGTH:
        key.append(random.randint(0, 26))
    print(key)

    # turn the input string into an array of numerical values. Using all caps ("UPPER") 
    while i < len(string):
        index = UPPER.find(string[i])
        index_cipher.append((index + key[i % KEY_LENGTH]) % len(UPPER))
        i=i+1
    
    for character in index_cipher:
        string_ciphered+=UPPER[character]
   
    return string_ciphered


#Determine frequency of characters given a key length.  Break full cipher text into chunks of key length and looks for frequency in each.
def frequency(susp_length, string):
    frequency_arrays = [None] * susp_length
    start = 0
    freq = [dict() for x in range(susp_length)]

    #each list in frequency_arrays is a substring of every nth letter in the ciphertext. Uses a helper function to generate the list.
    while start < susp_length:
        frequency_arrays[start] = getNthletter(susp_length, string[start:])
        #print("string sent: "+ string[start:])
        #print("nth char arr. " + str(start) + ": " + str(frequency_arrays[start]))
        start+=1
    
        
    #create a dictionary in the freq list based on each substring in frequency_arrays.  That is, count frequency within each substring.
    j = 0
    while j < len(frequency_arrays):
        t_dict = {}
        for char in frequency_arrays[j]:
            if (char in t_dict):
                t_dict[char] += 1
            else:
                t_dict[char] = 1

        freq[j] = t_dict
        j+=1
    
    # test printing a dictionary: print(freq[0])


# helper function. Just returns a substring of every nth char in a string
def getNthletter(n, string):
    builtstring=""
    i = 0
    while i < len(string):
        if i%n==0:
            builtstring=builtstring+string[i]
        i+=1
    return builtstring 





#primary instructions go here

# c_in = input("Please enter your cipher text: ")
# p_in = input("Please enter your plaintext: ")
test = "This is a test the quick brown fox jumped over the lazy dog"
print("The test text is: " + test)
returned = encrypt(test.upper())
print("The encrypted text is: " + returned)
frequency(5, returned)
