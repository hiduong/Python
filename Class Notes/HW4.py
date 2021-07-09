# WRITE YOUR NAME and YOUR COLLABORATORS HERE
# Hien Duong

#------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations
opstack = []  #assuming top of the stack is the end of the list

# Now define the HELPER FUNCTIONS to push and pop values on the opstack 
# Remember that there is a Postscript operator called "pop" so we choose 
# different names for these functions.
# Recall that `pass` in python is a no-op: replace it with your code.

def opPop():
    if len(opstack) != 0: #if the opstack is not empty pop the top element
        return opstack.pop()
    else:
        print("Error: The opstack is empty")
    # opPop should return the popped value.
    # The pop() function should call opPop to pop the top value from the opstack, but it will ignore the popped value.

def opPush(value):
    opstack.append(value) #push the value onto the opstack

#-------------------------- 20% -------------------------------------
# The dictionary stack: define the dictionary stack and its operations
dictstack = []  #assuming top of the stack is the end of the list

# now define functions to push and pop dictionaries on the dictstack, to 
# define name, and to lookup a name

def dictPop():
    if len(dictstack) != 0: #if the dictstack is not empty pop the top element
        dictstack.pop()
    else:
        print("Error: The dictstack is empty")
    # dictPop pops the top dictionary from the dictionary stack.

def dictPush(d):
    dictstack.append(d) #push the dictionary onto the dictstack
    #dictPush pushes the dictionary ‘d’ to the dictstack. 
    #Note that, your interpreter will call dictPush only when Postscript 
    #“begin” operator is called. “begin” should pop the empty dictionary from 
    #the opstack and push it onto the dictstack by calling dictPush.

def define(name, value):
    newDict = {}
    if len(dictstack) != 0: #if the dict stack is not empty
        retDict = dictstack.pop() #pop the top dictionary from the dictstack 
        retDict[name] = value #add or replace the item in the dictionary
        dictPush(retDict) #push it back onto the dictstack
    else:
        newDict[name] = value #add value to the new dictionary we want to add
        dictPush(newDict) #add it to the dictstack
    #add name:value pair to the top dictionary in the dictionary stack. 
    #Keep the '/' in the name constant. 
    #Your psDef function should pop the name and value from operand stack and 
    #call the “define” function.

def lookup(name):
    for dictionary in reversed(dictstack): #reversed because we want to return the first dictionary with the name on the stack
        for key,val in dictionary.items(): #go through each item in the dictionary
            if key == "/"+name: #if we find it return the value
                return val 
    print("Error: "+name+" does not exist") # if we reach here it does not exist so print error message
    # return the value associated with name
    # What is your design decision about what to do when there is no definition for “name”? If “name” is not defined, your program should not break, but should give an appropriate error message.


#--------------------------- 10% -------------------------------------
# Arithmetic, comparison, and boolean operators: add, sub, mul, eq, lt, gt, and, or, not 
# Make sure to check the operand stack has the correct number of parameters 
# and types of the parameters are correct.
def add():
    if len(opstack) > 1: #error checking to make sure length is greater than 1 because we need 2 operands
        op2 = opPop() #let op2 be the first pop
        op1 = opPop() #let op2 be the second pop
        if(isinstance(op1,int) and isinstance(op2,int)): #type checking to make sure they are both int
            opPush(op1+op2) #push the result to the opstack
        else:
            print("Error: add - one of the operands is not a numerical value")
            opPush(op1)
            opPush(op2)
    else:
        print("Error: add expects 2 operands")

def sub():
    if len(opstack) > 1: #error checking to make sure length is greater than 1 because we need 2 operands
        op2 = opPop() #let op2 be the first pop
        op1 = opPop() #let op2 be the second pop
        if(isinstance(op1,int) and isinstance(op2,int)): #type checking to make sure they are both int
            opPush(op1-op2) #push the result to the opstack
        else:
            print("Error: sub - one of the operands is not a numerical value")
            opPush(op1)
            opPush(op2)
    else:
        print("Error: sub expects 2 operands")

def mul():
    if len(opstack) > 1: #error checking to make sure length of stack is greater than 1 because we need 2 operands
        op2 = opPop() #let op2 be the first pop
        op1 = opPop() #let op2 be the second pop
        if(isinstance(op1,int) and isinstance(op2,int)): #type checking to make sure they are both int
            opPush(op1*op2) #push the result to the opstack
        else:
            print("Error: mul - one of the operands is not a numerical value")
            opPush(op1)
            opPush(op2)
    else:
        print("Error: mul expects 2 operands")

def eq():
    if len(opstack) > 1: #error checking to make sure length of stack is greater than 1 because we need 2 operands
        op2 = opPop() #let op2 be the first pop
        op1 = opPop() #let op1 be the second pop
        if(op1 == op2): #if op1 is equal to op2 push True to the stack
            opPush(True)
        else:
            opPush(False) #else push false
    else:
        print("Error: eq expects 2 operands")

def lt():
    if len(opstack) > 1: #error checking to make sure length of stack is greater than 1 because we need 2 operands
        op2 = opPop() #let op2 be the first pop
        op1 = opPop() #let op1 be the second pop
        if(op1 < op2): #if op1 is less than op2 push True to the stack
            opPush(True)
        else:
            opPush(False) #else push false
    else:
        print("Error: lt expects 2 operands")

def gt():
    if len(opstack) > 1: #error checking to make sure length of stack is greater than 1 because we need 2 operands
        op2 = opPop() #let op2 be the first pop
        op1 = opPop() #let op1 be the second pop
        if(op1 > op2): #if op1 is greater than op2 push True to the stack
            opPush(True)
        else:
            opPush(False) #else push false
    else:
        print("Error: gt expects 2 operands")

def psAnd():
    if len(opstack) > 1: #make sure that we have 2 operands
        op2 = opPop() #let op2 be the first pop
        op1 = opPop() #let op1 be the second pop
        if(isinstance(op1,bool) and isinstance(op2,bool)): #type checking to make sure they are booleans
            opPush(op1 and op2) #push the value of op1 and op2 to the stack
        else:
            print("Error: and - one of the operands is not a boolean value")
            opPush(op1)
            opPush(op2)
    else:
        print("Error: and expects 2 operands")

def psOr():
    if len(opstack) > 1: #make sure that we have 2 operands
        op2 = opPop() #let op2 be the first pop
        op1 = opPop() #let op1 be the second pop
        if(isinstance(op1,bool) and isinstance(op2,bool)): #type checking to make sure they are booleans
            opPush(op1 or op2) #push the value of op1 and op2 to the stack
        else:
            print("Error: or - one of the operands is not a boolean value")
            opPush(op1)
            opPush(op2)
    else:
        print("Error: or expects 2 operands")

def psNot():
    if len(opstack) != 0: #making sure the stack is not empty
        op1 = opPop() #pop the value we want to negate
        if(isinstance(op1,bool)): #making sure it's a boolean value
            opPush(not op1) #negate it and push it to the stack
        else:
            print("Error: not - operand is not a boolean value")
            opPush(op1)
    else:
        print("Error: opstack is empty")

#--------------------------- 25% -------------------------------------
# Array operators: define the string operators length, get, getinterval, put, putinterval
def length():
    count = 0 #declaring the count 
    if len(opstack) != 0: #making sure the stack is not empty
        op1 = opPop() #pop the array from the stack
        if(isinstance(op1,list)): #checking to make sure it's an array
            for op in op1: #iterating through the array
                if(isinstance(op,bool) or isinstance(op,int)): #for part 1 we only check for boolean and integer constants
                     count += 1 #if one of those, increment count counter
            opPush(count) #at the end push the count to the stack
        else:
            print("Error: length - operand is not an array")
            opPush(op1)
    else:
        print("Error: opstack is empty")

def get():
    if len(opstack) > 1: #check to make sure there is atleast 2 operands on the stack
        op2 = opPop() #let op2 be the first pop
        op1 = opPop() #op1 be the second pop
        if(isinstance(op1,list) and isinstance(op2,int)): #making sure that its an array and int
            if(op2 < len(op1)):
                opPush(op1[op2]) #push the value at the index in the array onto the stack
            else:
                print("Error: index out of range")
                opPush(op1)
                opPush(op2)
        else:
            print("Error: invalid parameters, must be types array followed by int")
            opPush(op1)
            opPush(op2)
    else:
        print("Error: get expects 2 operands")

def getinterval():
    retList = [] #declaring the list we will return 
    if len(opstack) > 2: #making sure there are atleast 3 operands on the stack
        op3 = opPop() #op3 = first pop
        op2 = opPop() #op2 = second pop
        op1 = opPop() #op1 = first pop
        if(isinstance(op1,list) and isinstance(op2,int) and isinstance(op3,int)): #making sure that the type is array, int, int
            boundarycheck = op1[op2:]
            if(op3 <= len(boundarycheck) and op3 >= op2):
                for i in range(op2,op2+op3): #starting from the starting index and going up to the end index
                    retList.append(op1[i]) #append the values into our return list
                opPush(retList) #return the interval
            else:
                print("Error: index out of range")
                opPush(op1)
                opPush(op2)
                opPush(op3)
        else:
            print("Error: invalid parameters, must be types array followed by int followed by int")
            opPush(op1)
            opPush(op2)
            opPush(op3)
    else:
        print("Error: getinterval expects 3 operands")

def put():
    if len(opstack) > 2: #making sure there are atleast 3 operands on the stack
        op3 = opPop() #op3 = first pop
        op2 = opPop() #op2 = second pop
        op1 = opPop() #op1 = first pop
        if(op2 < len(op1)):
            if(isinstance(op1,list) and isinstance(op2,int) and isinstance(op3,int)): #making sure that the type is array, int, int
                op1[op2] = op3 #set the value at the index in the array
            else:
                print("Error: invalid parameters, must be types array followed by int followed by int")
                opPush(op1)
                opPush(op2)
                opPush(op3)
        else:
            print("Error: index out of range")
            opPush(op1)
            opPush(op2)
            opPush(op3)
    else:
        print("Error: put expects 3 operands")

def putinterval():
    if len(opstack) > 2: #making sure there are atleast 3 operands on the stack
        op3 = opPop() #op3 = first pop
        op2 = opPop() #op2 = second pop
        op1 = opPop() #op1 = first pop
        if(isinstance(op1,list) and isinstance(op2,int) and isinstance(op3,list)): #making sure that the type is array, int, array
            op1[op2:(len(op3)+op2)] = op3 #splicing the first array from the starting index to the end of the second array setting that interval to the second array
        else:
            print("Error: invalid parameters, must be types array followed by int followed by array")
            opPush(op1)
            opPush(op2)
            opPush(op3)
    else:
        print("Error: putinterval expects 3 operands")

#--------------------------- 15% -------------------------------------
# Define the stack manipulation and print operators: dup, copy, count, pop, clear, exch, mark, cleartomark, counttotmark
def dup():
    if len(opstack) != 0: #making sure the stack is not empty
        opPush(opstack[-1]) #duplicating the top of the stack and pushing it to the opstack
    else:
        print("Error: opstack is empty")

def copy():
    if len(opstack) != 0: #making sure the stack isn't empty
        op1 = opPop() #popping the top of the stack
        opstackDup = opstack.copy() #creating a copy of the opstack 
        if(isinstance(op1,int)): #making sure the type of op1 is int
            if(op1 <= len(opstackDup)):
                for x in reversed(range(1,op1+1)): #while range of op1 to 1
                    opPush(opstackDup[-x]) #gonna get the last item in the opstack copy and push it to the opstack
            else:
                print("Error copy - operand is greater than size of the opstack")
        else:
            print("Error copy - operand is not a numerical value")
            opPush(op1)
    else:
        print("Error: opstack is empty")

def count():
    opPush(len(opstack)) #return the length of the opstack

def pop(): #removes the top value from the op stack, opPop already does Error checking
    opPop()

def clear(): #clears the opstack
    opstack [:] = []

def exch(): #swaps the top two items in the opstack
    if len(opstack) > 1: #error checking to make sure we have atleast 2 operands
        op2 = opPop() #get the values
        op1 = opPop()
        # swapping the values by pushing them in reverse order
        opPush(op2)
        opPush(op1)
    else:
        print("Error: exch expects 2 operands")

def mark(): #add a mark to the top of the opstack
    opstack.append("-mark-")

def cleartomark():
    markExists = False
    length = len(opstack) #set the length to be the length of the opstack
    for op in reversed(opstack): #starting from the top of the stack
        if(op == "-mark-"): #check to see if the op stack is marked
            markExists = True
            break 
    if markExists == True:
        for x in reversed(range(0,length)): #while going down the stack
            if opstack[x] == "-mark-": #if we hit the mark pop it and break out of loop
                opPop()
                break
            else: 
                opPop() #pop the stack until the mark
    else:
        print("Error: opstack not marked")

def counttomark():
    length = len(opstack) #obtaining the length of the opstack
    count = 0 #declaring the initial count
    for x in reversed(range(0,length)): #go through the opstack
        if opstack[x] == "-mark-": #if we hit the mark push the count to the opstack and break out of loop
            opPush(count)
            break
        else:
            count += 1 #if not mark increment count by 1

def stack(): 
    for op in reversed(opstack): #starting from the top of the stack
        print(op) #print the current value

#--------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in Python. Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your own "define" operator (pass those values as parameters).
# Note that psDef()won't have any parameters.

def psDict(): 
    if len(opstack) != 0: #making sure the opstack is not empty
        op1 = opPop() #poping the initial size 
        if(isinstance(op1,int)): #making sure it's an integer
            opPush({}) #push an empty dictionary onto the opstack
        else:
            print("Error: dict - operand is not a int value")
            opPush(op1)
    else:
        print("Error: opstack is empty")

def begin():
    if len(opstack) != 0: #making sure opstack is not empty
        if(isinstance(opstack[-1],dict)): #making sure it's a dictionary
            op = opPop() #pop the dictionary from the opstack
            dictPush(op) #push the dictionary onto the dictionary stack
        else:
            print("Error: begin - operand is not a dict value")
    else:
        print("Error: opstack is empty")

def end(): #pop the dictionary from the dictstack and trash it
    dictPop()

def psDef():
    if len(opstack) > 1: #making sure we have atleast 2 operands on the stack
        op2 = opPop() #popping the value 
        op1 = opPop() #popping the name
        if(isinstance(op1,str)): #making sure that it's a string
            if(op1[0]=="/"): #making sure that it is a variable
                define(op1,op2) #calling the define function
            else:
                print("Error: def - not a variable")
                opPush(op1)
                opPush(op2)
        else:
            print("Error: def - operand is not a string value")
            opPush(op1)
            opPush(op2)    
    else:
        print("Error: get expects 2 operands")
