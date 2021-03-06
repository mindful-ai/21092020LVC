


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
        


# ---------------------------------------------------------


s1 = student('Ram', 5, '007')
s2 = student('Krish', 5, '008')
print(s1)
s1.printinfo()

print("\n\n")
s1.setschoolname("Kendriya Vidyalaya")
s1.setMaths(100)
s1.setPhysics(90)
s1.setChemistry(92)
s1.setBiology(97)
s1.printinfo()


print("\n\n")
s1.calcAverage()
s1.printinfo()


print(s1 + s2)