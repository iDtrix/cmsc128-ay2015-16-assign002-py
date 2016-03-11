# CMSC 128
# Assignment 002: Programming a Simple Bioinformatics Library
# Coded by: Daryl Patrick M. Roco
# AB - 4L

# for regex
import re 
# Function for getting Hamming Distance of 2 strings 
def getHammingDistance(str1, str2):
	# If condition for checking if str1 and str2 are both strings
	if((type(str1) is str) & (type(str2) is str)):
		checker = 0;
		str1len = len(str1)
		str2len = len(str2)

		# If condition for checking of str1 and str2 are equal in string length
		if((str1len != str2len)):
			print ("Argument length not equal")
		else:
			i = 0
			# While loop for checking every different element of the both strings
			while i < str1len:
				if(str1[i] != str2[i]):
					checker = checker + 1
					i = i + 1
				return checker
	else:
		print("Argument type invalid")

# Function for counting occurence of a pattern from the original string
def countSubstrPattern(original, pattern):
	# For checking type mismatch
	if((type(original) is str) & (type(pattern) is str)):
		# re.finditer is used to find string patterns in the original string
		print (len([a for a in re.finditer('(?=' + pattern + ')', original)]))
	else:
		print("Argument type invalid")

# Function for checking if a string is valid to a given set of characters
def isValidString(string, alphabet):
	# Type mismatch checker
	if((type(string) is str) & (type(original) is str)):
		strlen = len(string)
		alphalen = len(alphabet)
		i = 0
		while i < strlen:
			j = 0
			counter = 0
			while j < alphalen:
				if(string[i] == alphabet[j]):	# Checks every element of both strings
					counter = counter + 1
				j = j + 1
			if(counter == 0):
				return False
			else:
				return True		
		i = i + 1
	else:
		print("Argument type invalid")

# Function for getting skew of G and C
def getSkew(string, n):
	# Type mismatch cheker
	if((type(string) is str)):
		strlen = len(string)
		if(n > 0 and n < strlen+1):
			countG = 0
			countC = 0
			for index in range(n):
				if(string[index] == 'G'): countG+=1 # Counts occurances of G
				if(string[index] == 'C'): countC+=1	# Counts occurances of C
			return print(countG - countC) #returns skew
		else:
			print("Argument 2 is invalid")
	else:
		print("Argument type invalid")

# Function for getting the maximum skew of a given string
def getMaxSkew(string, n):
	# Type mismatch checker
	if((type(string) is str)):
		strlen = len(string)
		if(n > 0 and n < strlen+1):
			countG = 0
			for index in range(n):
				if(string[index] == 'G'): countG+=1 # Gets the count of Gs in the string
			return print(g)
		else:
			print("Argument 2 is invalid")
	else:
		print("Argument type invalid")

# Function for getting the minumum skew of a given string
def getMinSkew(string, n):	
	# Type mismatch checker
	if((type(string) is str)):
		strlen = len(string)
		if(n > 0 and n < strlen+1):
			countG = 0
			countC = 0
			for index in range(n):
				if(string[index] == 'G'): countG+=1 # Gets the count of Gs in the string
				if(string[index] == 'C'): countC+=1 # Gets the count of Cs in the string
			if(countG-countC > 1): return print(1)	# Returns the value of 1 if its greater than 1
			else: return print(countG-countC)	
		else:
			print("Argument 2 is invalid")
	else:
		print("Argument type invalid")