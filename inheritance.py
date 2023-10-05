class inheritance:
    def config(self):
        print("i5, 16gb, 1TB")

com1= inheritance()
inheritance.config(com1)

class a:
    def feature1(self):
        print("I am a boy")

    def feature2(self):
        print("I am 19 years old")

class b():
    def feature3(self):
        print("I am child")

    def feature4(self):
        print("I am small")

class c(a,b):
    def feature5(self):
        print("I am multilevel")

# a1=a()
# b1=b()
c1= c()
c1.feature1()

