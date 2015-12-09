# Comment

# type int
print(type(20))
print(20)

# type string
print(type("string"))
print("string")

# type complax string
print(type("""'complax' string"""))
print("""'complax' string""")

# type tuple : 튜플은 추가하거나 삭제할 수 없다.
simpleTuple = (1, 2)

# type List
simpleList = [1, 2, 3, 4]
complexList = [1, "two", 3, 4.0, ["a", "b"], (5, 6)] 

print("tuple")
print(simpleTuple)
print("tuple First")
print(simpleTuple[0])
print("simpleList")
print(simpleList)
print("simpleList First")
print(simpleList[0])
print("complexList")
print(complexList)
print("simpleList First")
print(simpleList[0])
print("simpleList 2~3")
print(simpleList[1:3])
print("simpleList First From Back")
print(simpleList[-1])
print("simpleList 2 From First 2 From Back")
print(simpleList[1:-1])
print("simpleList 2~")
print(simpleList[1:])
print("simpleList ~3")
print(simpleList[:3])

# string
print('Let"s go')
print("Let's go")
print('''Let's go''')
print("""Let"s go""")
x = "Hello, "
y = "workld!"
print(x + y)

# dictionary {key:value}
x = {}
print(x)
x = {1:"one", 2:"two"}
print(x)
print(x[1])
print(x.get(2))
print(x.get(4, "not available"))

# set
x = set([1, 2, 2, 3, 3, 3, 4, 5])
print(x)
print("2 in x")
print(2 in x)
print("6 in x")
print(6 in x)

# variable
x = 3
print(x * 5)
x = input("How old are you?")
print(x)
print("type is")
print(type(x))
print("convert number")
print(type(int(x)))
