class Student1:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student1(m1, m2)
        return s3

    def __mul__(self, other):
        m1 = self.m1 * other.m1
        m2 = self.m2 * other.m2
        s3_a = Student1(m1, m2)
        return s3_a

    def __gt__(self, other):   # gt is greater than method   ge is greater equal to method
        s1 = self.m1 + self.m2
        s2 = other.m1 + other.m2

        if s1>s2:
            return True
        else:
            return False


s1 = Student1(98, 70)
s2 = Student1(77, 90)

s3= s1+s2
s3_a= s1*s2
print(s3.m1)
print(s3.m2)

print(s3_a.m1)
print(s3_a.m2)

if s1 > s2:
    print("S1 wins")
else:
    print("S2 wins")

