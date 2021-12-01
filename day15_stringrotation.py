"""
O(n^2) approach : 

loop through the parent string and keep shifiting by right once and comapre 
it to the goal string. if matches then done else keep shifitng

O(n) approach:

concat the parent string ex :  helloworld + helloworld = hellowordlhelloword
now if shifted string is rotation it will be substring, ex :  lloworldhe 


"""


from Day15_substring import issub
from Day15_substring import issub

def isRotation(str1, str2):
    #concat str1 with str1 
    newstr = str1+str1
    #print("newstring = ", newstr)
    #print("substring - ",str2)
    #see if the str2 is substring ofnew str
    if issub(str2,newstr):
        return True

    return False

if __name__ == "__main__":
    str1 = "Helloworld"
    str2 = "lloworldHe"
    print(isRotation(str1, str2))