# 会
STUDENT_NUMBER = 30000# 定义学生人数为3000
SCHOOL_NAME = 'HeBei University Of Economic & Bussiness'# 学校名称

def getStudentNumber():
    return STUDENT_NUMBER

def setStudentNumber(num):
    global STUDENT_NUMBER
    STUDENT_NUMBER = num

def getSchoolName():
    return SCHOOL_NAME

def setSchoolName(name):
    global SCHOOL_NAME
    SCHOOL_NAME = name


def changeValue():
    name = '山东理工大学'
    number = 10000
    print('全局变量STUDENT_NUMBER = ', getStudentNumber())
    print('全局变量SCHOOL_NAME = ', getSchoolName())
    print('=================================')
    print('局部变量namber = ', number)
    print('局部变量name = ', name)
    print('=================================')
    print('改变全局变量值...')
    print('=================================')
    setStudentNumber(number)
    setSchoolName(name)
    print('全局变量STUDENT_NUMBER = ', getStudentNumber())
    print('全局变量SCHOOL_NAME = ', getSchoolName())

if __name__ == '__main__':
    changeValue()
