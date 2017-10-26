import base64     
#貌似只是对二进制数据进行另一种方式的编码以及解码
b =base64.b64encode(b'binary\x00string') # 对字符串编码    
print(b)    
print(base64.b64decode(b)) # 对字符串解码    


c = base64.urlsafe_b64encode(b'binary\x00string') # 进行url的字符串编码    
print(c)   
print(base64.urlsafe_b64decode(c))