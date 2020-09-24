class Matrix:
    def __init__(self, arr):
        self.mat = arr

    def show(self):
        print(self.mat)
        
    def __add__(self, other):
        pass

m1 = Matrix([[1,2],[3,4]])
m2 = Matrix([[4,5],[6,7]])
m3 = m1 + m2
print("The addition of Matrix: ")
m3.show()

