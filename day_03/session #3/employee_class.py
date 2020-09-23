class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)


emp1 = Employee("Kumar", 2000)
emp2 = Employee("Abhinav", 5000)

emp1.displayEmployee()
emp2.displayEmployee()

print ("Total Employee %d" % Employee.empCount)

emp3 = Employee("Ram", 10000)
emp3.displayEmployee()
print ("Total Employee %d" % emp2.empCount)