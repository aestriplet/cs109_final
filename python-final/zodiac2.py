##from random import shuffle
##print(" Welcome to the Zodiac/Anime Quiz")
##print(" This quiz has two topic: anime and zodiac signs.")
##start = input(" Choose a topic: Anime or Zodiac signs")
##if start == " Anime":
##    print(" A) Evangelion")
##    print(" B) Devilman")
##    print(" C) Ashita no Joe")
##    question1 = input(" What controversial anime/manga inspiried the dark fanstasy manga and anime Berserk?")
##    if question1 == "B" or question1 == "b":
##        print("Correct!")
##    print(" A) Animation")
##    print(" B) Anima")
##    print(" C) Anime")
##    question2 = input(" What is anime short for?")
##    if question2 == "C" or question2 == "c":
##        print("Correct")
##elif start == " Zodiac signs":
##    question1_1 = input(" ")
##else:
##    print("Goodbye")
##
##

import random
from random import shuffle



def anime_quiz():
    score = 0
    print()
    print(" A) Evangelion")
    print()
    print(" B) Devilman")
    print()
    print(" C) Ashita no Joe")
    print()
    question1 = input(" What controversial anime/manga inspiried the dark fanstasy manga and anime Berserk? ")
    if question1 == "B":
        print()
        print("Correct!")
        score = score + 1
        
    print(" A) Animation")
    print()
    print(" B) Anima")
    print()
    print(" C) Anime")
    print()
    question2 = input(" What is anime short for? ")
    if question2 == "C":
        print()
        print("Correct")
        score = score + 1
    
    print(" A) a Japenese animation")
    print()
    print(" B) a Japanese  comic ")
    print()
    print(" C) a Japanese alcholic drink")
    print()
    question3 = input(" What is manga? ")
    if question3 == "B":
        print()
        print("Correct")
        score = score + 1
        
    print(" A) over 7400")
    print()
    print(" B) 950")
    print()
    print(" C) 1000")
    print()
    question4 = input(" How many episodes does the longest running anime have? ")
    if question4 == "A":
        print()
        print("Correct")
        score = score + 1
        
    print(" A) One Piece, Naruto, Bleach")
    print()
    print(" B) Little Witch Academia, My Hero Academia, Love is like a cocktail ")
    print()
    print(" C) One Piece, Naruto, Dragon Ball Z")
    print()
    question5 = input(" What are the top three mainstream anime almost everyone knows? ")
    if question5 == "C":
        print()
        print("Correct")
        score = score + 1
    else:
        print(score)
       
print(" Welcome to the Anime Quiz ")
print()
print(" This quiz is about popular anime facts")
print()
category = str(input(" Would you like to play?" ))
 
if category == " yes":
    anime_quiz()
else: 
    print("goodbye")

