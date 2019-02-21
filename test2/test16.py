filename = input("请输入文件名：")
print(f"We 're going to erase {filename}")
print("If you don't want that ,hit CTRL-C (^c)")
print("If you want that ,hit RETURN")

input("?")

print("Opening the file...")
target = open(filename, 'w')
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I 'm going to ask you for three lines.")
line1 = input("line1 : ")
line2 = input("line2 : ")
line3 = input("line3 : ")

print("I 'm going to write these ao the file.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("Finally we close it.")
target.close()