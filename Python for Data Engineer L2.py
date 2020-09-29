#!/usr/bin/env python
# coding: utf-8

# Program 1: Write a python program using regex or by any other method to check. if the credit card number given is valid or invalid. your python program should read the credit card number from input
# 

# In[12]:


import re

PATTERN='^([456][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$'

def is_valid_card_number(sequence):
    """Returns `True' if the sequence is a valid credit card number.

    A valid credit card number
    - must contain exactly 16 digits,
    - must start with a 4, 5 or 6 
    - must only consist of digits (0-9) or hyphens '-',
    - may have digits in groups of 4, separated by one hyphen "-". 
    - must NOT use any other separator like ' ' , '_',
    - must NOT have 4 or more consecutive repeated digits.
    """

    match = re.match(PATTERN,sequence)

    if match == None:
        return False

    for group in match.groups():
        if group[0] * 4 == group:
            return False
    return True

def main():
  cc_num = str(input('Enter at 16-digit credit card number: '))
    
  if not is_valid_card_number(cc_num):
      print('Invalid credit card number')
  else:
      print('valid card number')



main()


# Program 2: Write a python program to output the following look and say sequence of numbers. It should print
# up to 10 numbers
# 

# In[14]:


from itertools import groupby
def lookandsay(number):
    return ''.join( str(len(list(g))) + k
       for k,g in groupby(number) )
 
numberstring='1'
for i in range(10):
 print(numberstring)
 numberstring = lookandsay(numberstring)


# Program 3 : Convert the given roman number in to decimal number. The syntax of roman number is given below . Write the python program using functools

# In[4]:


class Solution(object):
   def romanToInt(self, s):
      """
      :type s: str
      :rtype: int
      """
      roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
      i = 0
      num = 0
      while i < len(s):
         if i+1<len(s) and s[i:i+2] in roman:
            num+=roman[s[i:i+2]]
            i+=2
         else:
            num+=roman[s[i]]
            i+=1
      return num
ob1 = Solution()
print(ob1.romanToInt("XL"))
print(ob1.romanToInt("CDXLIII"))


# Program 4 :Write a python proram to count the occurences of string two in string one. Your python program should read the strings from input
# 

# In[1]:


# define string
string =  str(input('Enter First String: '))
substring = str(input('Enter Second String: '))


def occurrences(string, substring):
    count = 0
    start = 0
    while True:
        start = string.find(substring , start) + 1
        if start > 0:
            count+=1
            
        else:
            return print("The count is:", count)

# print count
occurrences(string, substring)


# Program 5 :write a python program to reverse the words in a given sentence as given below. your python program should read the sentence from input

# In[3]:


def rev_sentence(sentence): 
  
    # first split the string into words 
    words = sentence.split(' ')  
  
    # then reverse the split string list and join using space 
    reverse_sentence = ' '.join(reversed(words))  
  
    # finally return the joined string 
    return reverse_sentence   
  
if __name__ == "__main__": 
    input = str(input('Enter Sentance: '))
    print(rev_sentence(input))

