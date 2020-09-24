# Starter code

class Matrix:
    def __init__(self, arr):
        self.mat = arr

    def show(self):
        print(self.mat)
        
    def __add__(self, other):
        a = self.mat[0][0] + other.mat[0][0]
        b = self.mat[0][1] + other.mat[0][1]
        c = self.mat[1][0] + other.mat[1][0]
        d = self.mat[1][1] + other.mat[1][1]
        return Matrix([[a,b], [c,d]])

m1 = Matrix([[1,2],[3,4]])
m2 = Matrix([[4,5],[6,7]])
m1.show()
m2.show()
m3 = m1 + m2
print("The addition of Matrix: ")
m3.show()


# ---------------------- Additional Exercise: Matrix Multiplications
m4 = m1 * m2
print("The multiplication of Matrix: ")
m4.show()