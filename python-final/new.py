# objected needed: sign/date
# attributes?
#import pendulum
from datetime import date

class Me:
    """This introduces the topic of the programme """
    Welcome = str(input("Welcome to the Zodiac sign guess questionaire"))
    
    #def __init__(self, sign):
    """In this section I am defining the [constructors] that I want to
use in the progam. Such as, name, sign and numbers. The name is for printing the
users name, the sign is for figuring out their zodiac sign, and the number is for
finding out their lucky numbers"""
        #self.sign = sign
        

    def Zodiac(self):
        """ In this section I ame defining self or attribute of the class "Me". Using uer input, lists, and if, elif, else
statments to describe the... """
        self.sign = sign
        #Zodiac = ["Scopio", "Virgo", "Gemini", "Pisces", "Libra", "Cancer", "Taurus", "Capricorn", "Aires", "Sagittarius", "Leo", "Aquarius"]
        name = input("name")
        print(name)
        input( " Birthday(M/D")
        Birthday = [month/day]
        month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"] 
        day = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

        if month == "Decemeber":
            sign = "Sagittarius"
            if day < 22:
                print(sign)
            else:
                print("Capricorn")
        elif month == "January":
            sign = "Aquarius"
            if day > 20:
                print(sign)
            else:
                print("Pisces")
        elif month == "March":
            sign = "Aires"
            if day > 21:
                print(sign)
            else:
                print("Taurus")
        elif month == "May":
            sign == "Gemini"
            if day > 21:
                print(sign)
            else:
                print("Cancer")
        elif month == "June":
            sign = "Leo"
            if day > 23:
                print(sign)
            else:
                print( "Virgo")
        elif month  == "July":
            sign = "Libra"
            if day > 23:
                print(sign)
            else:
                print("Scorpio")
        else:
            print("Invalid Input")   
               
Zodiac()
print(Zodiac)

##myobject = Me()
##print(myobject.variable)
##
##    
##                   
    #def description:
                      

##
##    def dice(self):
##        number = input(float(" What is your favorite numbers between 1 and 10 (choose 3#'s)")
##                       if number == 2
##            
##            
     
