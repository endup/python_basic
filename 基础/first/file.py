import os

# 打开一个文件
fo = open("foo.txt", "a")
fo.write( "www.runoob.com!\nVery good site!\n");
 
# 关闭打开的文件
fo.close()
# 打开一个文件
fo = open("foo.txt", "r+")
str = fo.read();
print ("读取的字符串是 : ", str)
# 关闭打开的文件
fo.close()

# 在 write 内容后，直接 read 文件输出会为空，是因为指针已经在内容末尾


# 打开一个文件
fo = open("foo.txt", "r+")
str = fo.read(10);
print ("读取的字符串是 : ", str)
 
# 查找当前位置
position = fo.tell();
print ("当前文件位置 : ", position)
 
# 把指针再次重新定位到文件开头
position = fo.seek(10, 0);
str = fo.read();
print ("重新读取字符串 : ", str)
# 关闭打开的文件
fo.close()

 
# 给出当前的目录
print (os.getcwd())
# 新建文件目录
os.mkdir("newdir")
# 更换目录
os.chdir("newdir")

fo = open("foo.txt", "w+")
fo.close()

print (os.getcwd())
os.chdir("../")
print (os.getcwd())
# 删除目录，只能删除空目录
os.rmdir('newdir')
