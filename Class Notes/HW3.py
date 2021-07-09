# CptS 355 - Spring 2020 Assignment 3
# NAME : Hien Duong

debugging = True
def debug(*s):
    if debugging:
        print(*s)

from functools import reduce

# (Dictionaries)
# 1a. sumSales
def sumSales(d): 
    sumSalesDict = {} #defining an empty dictionary for return 
    for days in d.values(): #looping through each store key in the dictionary and obtaining its days dictionary
        for day,sales in days.items(): #going though each day key in the days dictionary and getting the total sales
            sumSalesDict[day] = sumSalesDict.get(day,0)+sales #add the total sales value for the day key in the dictionary
    return sumSalesDict #return dictionary

# 1b. sumSalesN
def sumSalesN(L):
    def sumSalesNHelper(d,sumSalesDict): #defining a inner helper function to combine the result of map
        for day,sales in d.items(): #go through day key in the dictionary
            sumSalesDict[day] = sumSalesDict.get(day,0)+sales #add the total sales value for the day key in the dictionary
        return sumSalesDict #return the dictionary
    return reduce(sumSalesNHelper,list(map(sumSales,L))) 

# (Dictionaries and Lists)
# 2a. searchDicts
def searchDicts(L,k): 
    returnValue = None #declaring the return value as initially None
    for dictionary in L: #go through all the dictionaries in the list
        for key,value in dictionary.items(): #go through all the keys in the dictionary
            if key == k: #if the key matches the key we want
                returnValue = value #set the return value to the value of that key
    return returnValue #return the return value

# 2b. searchDicts2
def searchDicts2(L,k):
    def searchDicts2Helper(d,k,L,index): #defining a recursive inner helper function, parameters are the tuple at an index, k, the original list, and the next index
        for key,value in d[1].items(): #go through all the keys in the dictionary 
            if key == k: #if the key we want exists
                return value #return it's value
        if index == 0: #if the index is 0 and the key we want does not exists 
            return None #return none
        else:
            if d[0] == index: #if the next index is the current index return none
                return None    
        if d[0] >= (len(L) - 1): #if the next index is out of bounds return None
            return None
        return searchDicts2Helper(L[d[0]],k,L,d[0]) #else recursively call with the tuple at the next index, k, the original list, and the index at the next tuple
    return searchDicts2Helper(L[len(L) - 1],k,L,len(L) - 1) 

# (List Comprehension)
# 3. busStops
def busStops (buses,stop):
    return [key for (key,value) in buses.items() if stop in value] #using list comprehension, will return the key if the stop is in the value

# (Lists)
# 4. palindromes
# my algorithm is as follows
# using racecar as an example
# while looping through the string and removing the first character each loop
# I will have another loop that removes the last character and will compare the current string with its reversed form
# loop 1 : while loop 1: racecar == racecar so append it, break out of while loop
# loop 2 : while loop 1: acecar != raceca so the second while loop will remove the last character of the string
# still loop 2: while loop 2: aceca == aceca so append it, break out of while loop, continues until end.
def palindromes(S):
    palindromeList = [] #declaring the return list
    temp = S #reference to the string S
    j = len(S) #the length of the string 
    for i in range(0,len(S)): #go through the whole string, each loop remove first character
        j = len(S) #setting j to the length of string
        while j >= i: 
            if temp == temp[::-1]: #if it equals it's reversed form
                palindromeList.append(temp) #append it to our return list
                break
            temp = temp[:-1] #if not equal will remove the last character of the string
            j = j - 1
        temp = S[i+1:] #removing the first character of the string each loop
    return sorted([x for x in palindromeList if len(x) >= 2])

# (Iterators)
# 5a. interlaceIter
class interlaceIter():
    def __init__(self,list1,list2): #initializing the iterator
        self.current = list1.__next__() #setting the current to be the first element in the first list. exception raised if reached the end
        self.list1 = list1 #storing the list1
        self.list2 = list2 #storing the list2
        self.currentList = 0 #check what list to print 0 for 1 and 1 for 2
    def __next__(self):
        result = self.current #set the result
        if self.currentList == 0: #if the current list is list 1
            self.current = self.list2.__next__() #the next will be from list 2, exception raised if reached the end
            self.currentList = 1 #sets to 1 for list 2
        else: #if current is list 2
            self.current = self.list1.__next__() #next will be from list 1
            self.currentList = 0 #set to 0 for list 1
        return result #return the result
    def __iter__(self):
        return self

# 5b. typeHistogram
def typeHistogram (it,n):
    histogramDict = {} # declaring a dictionary for counting the types key = type, value = count
    i = 0 # iterator
    try: # catching the stop iteration exception being raised from end of list
        while i < n: # iterate up to n
            key = it.__next__() # return value in current list
            histogramDict[type(key).__name__] = histogramDict.get(type(key).__name__,0)+1 # increment count by 1 for every instance of the type key we come across
            i = i + 1 
    except StopIteration: # if stop iteration is raised just go to the return 
        pass
    return [(key,value) for key,value in histogramDict.items()] # list comprehension to get the key and value from the dict to create list of tuples


