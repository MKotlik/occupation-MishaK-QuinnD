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
	for x in joblist:
		if x[0] == '"':
			x = x[1:len(x)]
			x = x.split('",')
		else:
			x = x.split(',')
		x[1] = float(x[1])

	return joblist #returns the list of lists

# Storage function
#def storer(list):


#	return
# Choosing function
#def chooser(storage):



#	return
# Runtime
print reader()
