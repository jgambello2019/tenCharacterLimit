f = open('input.txt','r') #opens file
lines = f.read().splitlines() #reads file and splits up file by line
f.close()

f = open('output.txt','w') #Opens file to write cut down characters to
output = ''

for line in lines: #goes through each line
	length = len(line) #checks if line is longer then 10 to start
	while length > 10: #10,11 cut down string by the last character
		line = line[:-1]
		length = len(line) #checks the length of the line to see if it is less than 10
	output += line #adds the cut down string to output
	output +='\n'
output = output[0 :-1] #gets rid of final space at the end of output that was appearing
print(output) #shows the user their cutdown file

f.write(output) #writes the output to the file
f.close()
		