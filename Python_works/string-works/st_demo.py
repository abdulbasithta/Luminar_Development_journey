"""
string

    > sequence of character

OOP is a programming paradiagram (style of coding) that allows us to bring real-world entities in to programming by using classes and objects.

class: plan, blueprint, design, pattern, template
object: (realword entity) 

"""
# These method only works in string object

#class str:
    #def capitalize()    
    #def casefold()
    #def upper()
    #def lower()
    #def isalpha() => return True if string object is alphabet return False otherwise
    #def isdigit() => return True if string object is digit return False otherwise
    #def isalnum() => return True if string object is alphabet or digit return False otherwise
    #def index(str) => return index of first occurance of substr else return valuerror
    #def count(str) => return number of times sub string occurs in the string object
    #def startswith(prefix) => return True if string object start with given prefix else return False
    #def endswith(suffix) => return True if string object end with given suffix else return False
    #def strip(char) => return copy of string in which char removed from both end
    #def lstrip(char) => return copy of string in which char removed for begining
    #def rstrip(char) => return copy of string in which char removed for end


name = "luminartechnolab"
#       0123456789012345  (indexing)

id = "200292"

name_cap = name.capitalize() 

# print(name_cap) #Luminartechnolab

name_casefold = name.casefold()

# print(name_casefold) #Luminartechnolab

name_upp = name.upper()

# print(name_upp) #LUMINARTECHNOLAB

name_low = name.lower()

# print(name_low) #luminartechnolab

# print(name.isalpha()) #True

# print(id.isdigit()) #True

# print(name.isalnum()) #True

# index_pos = name.index("nar")

index_pos = name.index("l")

# print(index_pos) #0

occ_cout = name.count("l")

# print(occ_cout) #2

# print(name.startswith("lum")) #True

# print(name.endswith("lab")) #True

name_strip = name.strip(">,!") #>Luminartechnolab!

# print(name_strip)

# print(name.lstrip(">"))

# print(name.rstrip(">"))

