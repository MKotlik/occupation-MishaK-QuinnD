import random, csv
# Main function
#def main():
	


# Reading function
def reader():

	#open the file, and turn it into one big string
	f = open('occupations.csv', 'r')
	rawdata = f.read()

	#split the string by the \n character, remove the heading and footing
	joblist = rawdata.split("\r\n")
	joblist.pop(0)
	joblist.pop(-1)
	joblist.pop(-1)

	#turn each entry into a seperate list, remove " characters, convert the numbers to floats
	jobs = []
	for x in joblist:
		if x[0] == '"':
			x = x[1:len(x)]
			x = x.split('",')
		else:
			x = x.split(',')
		x[1] = float(x[1])
		jobs += [x]

	#return the list of lists
	return jobs 

# Dictionary creater function
def librarian(givenlist):
	occupations = {}
	for x in givenlist:
		occupations[x[0]] = x[1]
	return occupations

# Storage function
def storer(givenlist):

	return

# Choosing function
def chooser(storage):

	return

# Runtime
z = reader()
print librarian(z)
