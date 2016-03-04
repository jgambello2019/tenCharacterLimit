f = open('input.txt','r')
lines = f.readlines()
f.close()

f = open('output.txt','w')
output = ''
x = 0

for line in lines:
	#while x == 0:
	length = len(line)
	while length > 10:
		line = line[:-1]
		length = len(line)
		#if line == lines[-1]:
			#x = 1
	output += line
	output +='\n'
print(output)

f.write(output)
		