
def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count,f):
    print(line_count,f.readline())

input_file = input("请输入打开的文件：")

current_file = open(input_file)

print("First let's print the whole file:\n")
print_all(current_file)

print("Now let's rewind ,kind of like a tape.")
rewind(current_file)

print("Let's print three lines:")
h = len(current_file.readlines())
t = range(h+1)
rewind(current_file)
for current_line in t[1:h+1]:
    print_a_line(current_line, current_file)
rewind(current_file)
print(current_file.readlines())
current_file.close()