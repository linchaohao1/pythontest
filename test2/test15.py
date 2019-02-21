from sys import argv

script,filename = argv   #执行脚本时输入参数

txt = open(filename)     #打开文件1

print(f"Here is your file {filename}")
print(txt.read())        #将文件1的内容打印出来
txt.close()
print("Type the filename again:")
file_again = input(">")  #输入第二个文件名

txt_again = open(file_again)    #打开第二个文件

print(txt_again.read())  #打印文件2的内容
txt_again.close()