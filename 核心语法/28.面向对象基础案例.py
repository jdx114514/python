"""
教务管理系统开发需求

1.       添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
2.       修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
3.       删除学生成绩：根据输入的学生姓名，删除对应的学生成绩
4.       查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
5.       展示全部学生成绩：展示出系统中所有学生的成绩
"""



#学生类
class Student:
    def __init__(self,name,chinese,math,english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return f"姓名：{self.name} | 语文:{self.chinese} | 数学:{self.math} | 英语:{self.english}"


    #修改学生成绩
    def update_score(self,chinese =None,math=None,english=None): #诺不填写函数的参数，则默认为空值，将不会执行修改初始数据
        if chinese is not None :
            self.chinese = chinese
        if math is not None :
            self.math = math
        if english is not None :
            self.english = english

#教务管理系统
class EduManagement:
    system_version = "1.0"
    system_name = "教务管理系统"

    def __init__(self):
        self.student_list = [] #列表，记录的是在校学生的成绩

    #添加学生名单
    def add_student(self):

        name = input("请输入学生姓名:")
        # 判断是否学生重复
        for s in self.student_list:
            if s.name == name:
                print("学生重复")
                return

        #判断成绩在 0-100之间
        chinese = int(input("请输入学生语文成绩"))
        match = int(input("请输入学生成绩数学成绩"))
        english = int(input("请输入学生英语成绩"))
        if 0 <= chinese <=100 and 0 <= english >=100 and 0<= match <= 100:
            stu = Student(name,chinese,match,english)
            self.student_list.append(stu)
            print("添加成功")
        else:
              print("错误了")

    #修改学生成绩
    def update_student(self):
     name = input("请输入学生姓名:")

     for s in self.student_list:
      if s.name == name:
          print(f"当前成绩{s}")


      chinese = int(input("请输入学生语文成绩"))
      match = int(input("请输入学生成绩数学成绩"))
      english = int(input("请输入学生英语成绩"))
      if 0 <= chinese <= 100 and 0 <= english >= 100 and 0 <= match <= 100:
          s.update_score(chinese,match,english)
          print("修改成功")
          print(f"修改后成绩：{s}")
          return
      else:
          print("错误了,请输入正确成绩")
          return
     print("没找到该学生")

     #删除学生成绩
     def delete_student(self):
         name = input("请输入删除的学生姓名：")
         for s in self.student_list:
             if s.name == name:
                 self.student_list.remove(s)  #remove():移除列表中第一个匹配的元素
                 print("删除成功")
                 return
             print("没找到")

     #查询学生成绩
     def query_student(self):
         name = input("请输入查询的学生姓名：")
         for s in self.student_list:
             if s.name == name:
                 print(f"学生信息: {s}")
                 return
             print("没找到")
     #查询学生全部成绩
     def list_student(self):
         for s in self.student_list:
             print(s)
             return
         print("没找到")