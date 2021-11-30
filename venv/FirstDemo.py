print("Hello")

# here are the comments i have defined

a = 3
print(a)

Str = "Hello world"
print(str)

b, c, d = 5, 6.4, "Great"

#print("Value is"+b)

print("{} {}".format("value is", b))

print(type(b))

print(type(c))

print(type(d))

# Datatypes list

values = [1, 2, "Sagar", 4, 5]
# list is a data types that allows multiple values and can be differnet  data types
print(values[0])  #1
print(values[3])  #4
print(values[-1]) #5
print(values[1:3]) # 2 sagar

values.insert(3 ,"makwana")  #[1, 2, 'Sagar', 'makwana', 4, 5]
print(values)

values.append("END")  #[1, 2, 'Sagar', 'makwana', 4, 5, 'END']
print(values)

values[2] = "SAGAR"   #updating

del values[0]
print(values)

###############################


#tuple -Same as list data type but immutable
val =[1,2, "sagar" ,4 , 5]

print(val[1])

val[2] = "SAGAR"


# Dictionary

dic ={"a":2 , 4 :"bcd" ,"C":"Hello world"}

print(dic[4])
print(dic["C"])

#
dict = {}

dict["firstname"] = "Sagar"
dict["lastname"] = "Makwana"
dict["gender"] = "male"
print(dict)

print(dict["lastname"])











