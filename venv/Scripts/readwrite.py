file = open('test.txt')

#read all the contents of file
#read n number of character by passing parameter
# read one sigle line at a time readline()
#print(file.read(5))
print(file.readline())


#file.close() #alwys close the text file.


#print line by line using readline method
#line = file.readline()
#while line!="":
#   print(line)
#    line= file.readline()

#values =[abc , bvdsf , "cat" , dog , elephant]
for line in file.readline():
    print(line)



