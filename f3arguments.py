#positional argument
# keyword argument
# default argument
# variable length  argument/ variable no of argument
# # unknown argu (extra mainly 4 type ke he hote h)

#positional arugument

def personalInfo(fname, lname):
    print("First name =", fname)
    print('Last namae =',lname)
personalInfo("Nshika", "Deotale")

# keyword argument
fname ="Nishika"
lname="Deotale"
personalInfo(fname,lname) #variable name same hone chahiye example fname, lname


#default argument
def cityName(city = "delhi"):
    print(city)
cityName("mumbai")
cityName("nagpur")
cityName(" ")
#cityName() #error aayega
# value koi  argument pass ni krre toh default value print hoga
cityName()

#variable length argument

def studentName(*name):
    print(name)
studentName("nishika","bhavika","arpita","namrata","shreya") 
#output me tupple aayga twisted way me puch sakte

