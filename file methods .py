#read mode
f = open('file.txt', 'r')
print(f)
text = f.read()
print(text)
f.close()

#write mode
f = open('myfile1.txt', 'w')
f.write('Hello, world!')
f.close()

#append mode
f = open('myfile1.txt', 'a')
f.write('Hello, world!')
f.close()

#writeline method
f = open('myfile2.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()