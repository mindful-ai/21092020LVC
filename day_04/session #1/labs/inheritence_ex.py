from student_class import student

'''
class student(object):

    nstudents = 0
    schoolname = ''

    # Data/attributes
    def __init__(self, name, cls, rid):
        print('Initializing values.....')
        self.state = ''
        self.name = name
        self.cls = cls
        self.regid = rid
        self.maths = 0
        self.physics = 0
        self.chemistry = 0
        self.biology = 0
        self.average = 0
        student.nstudents += 1
        

    # Functions/methods

    def setschoolname(self, schoolname):
        student.schoolname = schoolname

    def printinfo(self):
        self.state = 'Karnataka'
        print('SELF:   ', self)
        print('STATE : ', self.state)
        print('SCHOOL: ', student.schoolname)
        print('-----------------------------------')
        print('NAME: ', self.name)
        print('CLASS: ', self.cls)
        print('REG ID:', self.regid)
        print('-----------------------------------')
        print('MATHS    : ', self.maths)
        print('PHYSICS  : ', self.physics)
        print('CHEMISTRY: ', self.chemistry)
        print('BIOLOGY  : ', self.biology)
        print('-----------------------------------')
        print('AVERAGE  : ', self.average)
        print('NSTUDENTS  ------> ', student.nstudents)
        print('\n')

    def setMaths(self, marks):
        self.maths = marks

    def setPhysics(self, marks):
        self.physics = marks

    def setChemistry(self, marks):
        self.chemistry = marks

    def setBiology(self, marks):
        self.biology = marks

    def calcAverage(self):
        self.average = (self.maths + self.physics + self.chemistry + self.biology)/4

'''   
# ---------------------------------------------------------

class ext_student(student):

    # Attributes
    def __init__(self, name, cls, rid, native, extra=['music']):
        super().__init__(name, cls, rid)
        self.native = native
        self.extra = extra

    # Functions
    def getGrade(self): # New function in the extended class
        if(self.average > 90):
            return 'A+'
        elif(70 < self.average <= 90):
            return 'A'
        elif(50 < self.average <= 70):
            return 'B'
        else:
            return 'C'

    def printinfo(self):  # Overriding the function
        super().printinfo()
        print('-----------------------------------')
        print('NATIVE  : ', self.native)
        print('EXTRAS  : ', self.extra)
        print('\n')

# ----------------------------------------------- Test for backward compatibiliy

s1 = ext_student('Ram', 5, '007', 'Bangalore')



print(s1)
s1.printinfo()

print("\n\n")
s1.setschoolname("Kendriya Vidyalaya")
s1.setMaths(100)
s1.setPhysics(90)
s1.setChemistry(92)
s1.setBiology(97)
s1.printinfo()


# ----------------------------------------------- New code

s2 = ext_student('Anil', 5, '008', 'Bangalore', ['cricket', 'painting'])
s2.setschoolname("St. Joseph's")
s2.setMaths(98)
s2.setPhysics(90)
s2.setChemistry(92)
s2.setBiology(92)
s2.calcAverage()
s2.printinfo()

# ----------------------------------------------- polymorphism

s3 = student('Sunil', 5, '007')

obj = s3
obj.printinfo()