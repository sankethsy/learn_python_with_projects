class Shape:
      def __init__(self,color,is_filled):
            self.color=color
            self.is_filled=is_filled

      def describe(self):
            print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius=radius

    def describe(self):
          print(f"It is a circle with an Area of {3.14*self.radius*self.radius}cm^2")
          super().describe()

class square(Shape):
      def __init__(self,color,is_filled,width):
            super().__init__(color,is_filled)
            self.width=width

      def describe(self):
                print(f"It is a square with an Area of {self.width*self.width}cm^2")
                super().describe()

      
class triangle(Shape):
        def __init__(self,color,is_filled,width,length):
                 super().__init__(color,is_filled)
                 self.width=width
                 self.length=length

        def describe(self):
                print(f"It is a Triangle with an Area of {self.width*self.length/2}cm^2")
                super().describe()
      
Circle=circle("red",False,5)
print(f"{Circle.color},{Circle.is_filled},{Circle.radius}")

Square=square("blue",False,6)
print(f"{Square.color},{Square.is_filled},{Square.width},")

Triangle=triangle("yelllow",True, 7,2)
print(f"{Triangle.color},{Triangle.is_filled},{Triangle.width},{Triangle.length}")

Circle.describe()

Square.describe()

Triangle.describe()



# shape1=circle("red","False","2")

# shape2= square("red","False","5")

# shape2=triangle("red","False","2","5")



    
