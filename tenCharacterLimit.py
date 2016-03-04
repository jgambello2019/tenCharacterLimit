f = open('input.txt','r')
lines = f.readlines()
f.close()

f = open('output.txt','w')
output = ''

for line in lines:
	length = len(line)
	while length > 10:
		line = line[:-1]
		length = len(line)
	output += line
	if line != lines[-1]:
		output += '\n'



print(output)
output.strip()
f.write(output)
		