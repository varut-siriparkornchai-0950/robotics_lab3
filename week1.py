def alphabet_position(sentence):
    contain = ""
    sentence = sentence.lower()                                   # convert sentence to lowercase
    for a in sentence:
        if a.isalpha() == True:
            contain += (str(ord(a)-96))+(" ")                    
    print(contain)

alphabet_position(input("Fill your sentence : "))