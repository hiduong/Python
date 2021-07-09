# WRITE YOUR NAME and YOUR COLLABORATORS HERE
# Hien Duong

import re

def tokenize(s):
    return re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[\[][a-zA-Z-?0-9_\s!][a-zA-Z-?0-9_\s!]*[\]]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)

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
            for i in range(op2,op2+op3): #starting from the starting index and going up to the end index
                retList.append(op1[i]) #append the values into our return list
            opPush(retList) #return the interval
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


#---------------------------------- PART 2 --------------------------

#------------------ PART 2 OPERATORS -------------------
def psIf():
    if len(opstack) > 1: #making sure the op stack contains at least 2 arguments on the op stack
        codearray = opPop() #get the code array
        condition = opPop() #get the condition
        if isinstance(codearray, dict) and isinstance(condition, bool): #making sure we are pulling a dictionary and boolean
            if condition == True: #if the condition is true
                interpretSPS(codearray) #interpret the code array
        else:
            print("Error: if expects a boolean and code array")
            opPush(condition)
            opPush(codearray)
    else:
        print("Error: if expects 2 operands")

def psIfElse():
    if len(opstack) > 2: #making sure there are atleast 3 arguments on the op stack
        codearray2 = opPop() #get the first code array
        codearray1 = opPop() #get the second code array
        condition = opPop() #get the condition
        if isinstance(codearray2, dict) and isinstance(codearray1, dict) and isinstance(condition, bool): #making sure you are popping a dict, dict and boolean
            if condition == True: #if the condition is true interpret the first code array
                interpretSPS(codearray1)
            else: #else interpret the second array
                interpretSPS(codearray2)
        else:
            print("Error: ifelse expects a boolean and code array and code array")
            opPush(condition)
            opPush(codearray1)
            opPush(codearray2)
    else:
        print("Error: ifelse expects 3 operands")

def repeat():
    if len(opstack) > 1: #making sure there are atleast 2 arguments on the op stack
        codearray = opPop() #pop the code arrray
        n = opPop() #pop the number of times we want to repeat, n
        if isinstance(codearray, dict) and isinstance(n, int): #making sure we pop a dict and integer
            i = 0 
            while(i < n): #while looping to n interpret the code array
                interpretSPS(codearray)
                i = i + 1
        else:
            print("Error: repeat expects a integer and code array")
            opPush(n)
            opPush(codearray)
    else:
        print("Error: repeat expects 2 operands")

def forall():
    if len(opstack) > 1: #making sure there are atleast 2 arguments on the op stack
        codearray = opPop() #pop the code array
        op2 = opPop() #pop the constant array
        if isinstance(codearray, dict) and isinstance(op2, list): #making sure it's a list and dict
            for x in op2: #for each element in the constant array
                opPush(x) #push that element
                interpretSPS(codearray) #and preform the code array
        else:
            print("Error: repeat expects a list and code array")
            opPush(op2)
            opPush(codearray)
    else:
        print("Error: forall expects 2 operands")

#------------------- PARSER AND INTERPRETER -----------------

# built in operators dictionary
builtinoperators = {'if':psIf, 'ifelse':psIfElse, 'repeat':repeat, 'forall':forall, 'add':add, 'sub':sub, 'mul':mul, 'eq': eq, 'lt':lt, 'gt':gt, 'and':psAnd, 'or':psOr, 'not':psNot, 'length':length, 'get':get, 'getinterval':getinterval, 'put':put, 'putinterval':putinterval, 'dup':dup, 'copy':copy, 'count':count, 'pop':opPop, 'clear':clear, 'exch':exch, 'mark':mark, 'cleartomark':cleartomark, 'counttomark':counttomark, 'stack':stack, 'dict':psDict, 'begin':begin, 'end':end, 'def':psDef}

# handler that will take a constant array as input
# if it is a number or boolean convert it
# if it is an operator or name we will ignore it for now and evaluate it when we interpret.
def constantArrayHandler(L):
    res = [] #return list
    splitList = L[1:-1].split() #split it by white space
    for c in splitList: # through each element in the split list
        if c == 'true' or c == 'True': #if true append python true
            res.append(True)
        elif c == 'false' or c == 'False': #if false append python false
            res.append(False)
        else:
            try:
                res.append(int(c)) #if it's a integer convert it and append it
            except:
                res.append(c) #if not append the string
    return res

def evaluateArray(token):
    returnList = [] #the return list
    mark() #mark the list so we know when the list started
    for values in token: #go thorugh each element in the list
        if isinstance(values, int) or isinstance(values, bool): #if it is a integer or boolean, push it onto the op stack
            opPush(values)
        elif values in builtinoperators: #if it is a built in operator call the function
            builtinoperators[values]()
        elif isinstance(values, str): #if it is a string
            val = lookup(values) #look it up in the dictionary
            opPush(val) #push the value into the stack
    length = len(opstack) #get the length of the op stack
    for x in reversed(range(0,length)): #while going down the stack
            if opstack[x] == "-mark-": #if we hit the mark pop it and break out of loop
                opPop()
                break
            else: 
                returnList.append(opPop()) #pop the stack until the mark
    return returnList[::-1] #return the list reversed

# COMPLETE THIS FUNCTION
# The it argument is an iterator.
# The tokens between '{' and '}' is included as a sub code-array (dictionary). If the
# parenteses in the input iterator is not properly nested, returns False.
def groupMatch(it):
    res = [] #return list
    for c in it: #iterate thorugh
        if c == '}':
            return {'codearray':res}
        elif c=='{':
            # Note how we use a recursive call to group the tokens inside the
            # inner matching parenthesis.
            # Once the recursive call returns the code-array for the inner 
            # parenthesis, it will be appended to the list we are constructing 
            # as a whole.
            res.append(groupMatch(it))
        else:
            if c == 'false' or c == 'False': #if false change it to python False
                res.append(False)
            elif c == 'true' or c == 'True': #if true change it to python True
                res.append(True)
            elif c[0] == '[' and c[-1] == ']': #if constant array call the handler
                res.append(constantArrayHandler(c))
            else:
                try:
                    res.append(int(c)) #see it it's an int, if it is append it
                except: #int() raises an error if c is not an integer
                    res.append(c) #if not append the string
    return False



# COMPLETE THIS FUNCTION
# Function to parse a list of tokens and arrange the tokens between { and } braces 
# as code-arrays.
# Properly nested parentheses are arranged into a list of properly nested dictionaries.
def parse(L):
    res = []
    it = iter(L)
    for c in it:
        if c=='}':  #non matching closing parenthesis; return false since there is 
                    # a syntax error in the Postscript code.
            return False
        elif c=='{':
            res.append(groupMatch(it))
        else:
            if c == 'false' or c == 'False': #if false change it to python False
                res.append(False)
            elif c == 'true' or c == 'True': #if true change it to python True
                res.append(True)
            elif c[0] == '[' and c[-1] == ']': #if constant array call the handler
                res.append(constantArrayHandler(c))
            else:
                try:
                    res.append(int(c)) #see it it's an int, if it is append it
                except: #int() raises an error if c is not an integer
                    res.append(c) #if not append the string
    return {'codearray':res}

# COMPLETE THIS FUNCTION 
# This will probably be the largest function of the whole project, 
# but it will have a very regular and obvious structure if you've followed the plan of the assignment.
# Write additional auxiliary functions if you need them. 
def interpretSPS(code): # code is a code array
    for token in code["codearray"]: #go through the elements of the code array
        if isinstance(token, int) or isinstance(token, bool): #if the token is an integer of boolean push it to op stack
            opPush(token)
        elif isinstance(token, dict): #if the token is a dict push it on the op stack
            opPush(token)
        elif isinstance(token, list): #if the token is a list, evaluate the list and push the evaluated list onto the op stack
            opPush(evaluateArray(token))
        elif isinstance(token, str): #if the token is a string
            if token in builtinoperators: #if it is a built in operator, call that operator
                builtinoperators[token]()
            elif token[0] == "/": #if it starts with /, it is a name so push it onto the op stack
                opPush(token)
            else:
                val = lookup(token) #look up the value in the dictionary
                if isinstance(val, dict): #if the value is a dictionary, interpret it
                    interpretSPS(val)
                else:
                    opPush(val)  #push the value on the stack
        else:
            print("Error: Undefined Token")

            
def interpreter(s): # s is a string
    interpretSPS(parse(tokenize(s)))


#clear opstack and dictstack
def clearStacks():
    opstack[:] = []
    dictstack[:] = []


input1 = """
            /square {dup mul} def
            0 [-5 -4 3 -2 1]
            {square add} forall
            55 eq false and
        """

# print(tokenize(input1))
# print(parse(tokenize(input1)))
print(parse(['b', 'c', '{', 'a', '{', 'a', 'b', '}', '{', '{', 'e', '}', 'a', '}', '}']))
