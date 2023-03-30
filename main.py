#Generating a encoded messages which follows the following rules
#If the words has atleast 3 letters :The first letter of the word is placed at the end and 3 random letters are placed before the word
#and three random letters are placed at the end
#If the word has equal to or less than 2 letters it is reversed

import string
import random

#generating random letters
n=3
r1=''.join(random.choices(string.ascii_lowercase +string.digits,k=n))
r2=''.join(random.choices(string.ascii_lowercase+string.digits,k=n))

mode=int(input("Select 1 for encoding and 2 for decoding \n"))
print("key generated are ",r1,r2)
a=input("Enter your message")
a.lower()

#sepearting the words

words=list(a.split(" "))



print("the keys generated are",r1,r2)

enlist = []
declist=[]


if mode==1:
    print("Encoding Mode Selected \n")

    for word in words:

        if (len(word)>=3):
            newword= r1 + word[1:]+ word[0] + r2

            enlist.append(newword) #making a list of the encoded words

        else:
            enlist.append(word[::-1])

print("The Encoded message is \n\n")
print(enlist)

if mode==2:


    for word in words:
        if len(word)<=2:
            declist.append(word[::-1])

        if len(word)>=3:
            decword= word[-4]+word[3:-4]
            declist.append(decword)

    print(declist)














