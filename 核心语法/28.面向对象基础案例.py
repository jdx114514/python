
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
        if all (0 <= score <=100 for score in (chinese, match, english)):
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
      if all(0 <= score <= 100 for score in (chinese, match, english)):
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
          if len(self.student_list) == 0:
            print("没找到")

          for s in self.student_list:
             print(s)

     #运行系统
    def run(self):
         print(f"欢迎使用系统 V{EduManagement.system_version}") #system_version 系统版本号

         while True:
             print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
             print("# 1.添加学生  2.修改学生 3.删除学生 4.查询指定学生 5.查询全部学生 6.退出系统")
             print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")


             choice=input("\n请选择要执行的操作，输入1-6:")

             try:
                 match choice:
                     case "1":  # 添加学生
                         self.add_student()
                     case "2":  # 修改学生
                         self.update_student()
                     case "3":  # 删除学生
                         self.delete_student()
                     case "4":  # 查询指定学生
                         self.query_student()
                     case "5":  # 查询全部学生
                         self.list_student()
                     case "6":  # 退出系统
                         break
                     case _:  # 其他情况
                         print("输入错误，请输入“1—6”")
             except ValueError as e:
                 print("输入的数据有问题，请检查，重新输入")
             except Exception as e:
                 print("程序运行出错了，请重新选择",e)

#测试
if __name__ == "__main__":
    edm_management = EduManagement()
    edm_management.run()
