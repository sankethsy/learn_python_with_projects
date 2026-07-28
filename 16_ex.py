class Shape:
      def __init__(self,color,is_filled):
            self.color=color
            self.is_filled=is_filled
class circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius=radius

class square(Shape):
      def __init__(self,color,is_filled,width):
            super().__init__(color,is_filled)
            self.width=width
    
class triangle(Shape):
        def __init__(self,color,is_filled,width,length):
                 super().__init__(color,is_filled)
                 self.width=width
                 self.length=length

Circle=circle("red","False","5")
print(f"{Circle.color},{Circle.is_filled},{Circle.radius}")
Square=square("blue","False","6")
print(f"{Square.color},{Square.is_filled},{Square.width},")
Triangle=triangle("yelllow","True","7","2")
print(f"{Triangle.color},{Triangle.is_filled},{Triangle.width},{Triangle.length}")



# shape1=circle("red","False","2")

# shape2= square("red","False","5")

# shape2=triangle("red","False","2","5")



    
