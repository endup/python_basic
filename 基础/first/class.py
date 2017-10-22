class Employee:
   '所有员工的基类'
   empCount = 0
 
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)
 
   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)
 
"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp1.displayCount()
emp2.displayEmployee()
print ("Total Employee",Employee.empCount)
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b
 #当输出类的实例的时候调用
   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   #类的实例相加的时候调用
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)
 
v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)
print(v1)



class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量

    def __init__(self, a, b):
       self.__a = a
       self.b = b
    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print (self.__secretCount)
 
counter = JustCounter(25,52)
counter.count()
counter.count()
print (counter.publicCount)
#print (counter.__secretCount)  # 报错，实例不能访问私有变量\
#Python不允许实例化的类访问私有数据，但你可以使用 object._className__attrName 访问属性
print (counter._JustCounter__secretCount)
print(counter.b)
