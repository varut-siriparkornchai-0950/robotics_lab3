def alphabet_position(sentence):
    contain = ""
    sentence = sentence.lower()                                   # convert sentence to lowercase
    for a in sentence:
        if a.isalpha() == True:                                   # .isalpha means Is that alphabet?
            contain += (str(ord(a)-96))+(" ")                    
    return print(contain.strip())                                  # cut blank first and last letter

senten = input("Fill your sentence : ")
alphabet_position(senten)



