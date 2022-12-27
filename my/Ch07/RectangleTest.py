import Rectangle

# Create a rectangle of width 4 and height 5
r = Rectangle.Rectangle(4, 5)
print(r) # Uses the __str__ method to report the state
# Create a rentangle with the default values for width and height
r = Rectangle.Rectangle()
print(r)
# Create a rectangle of width 4 and default height 1
r = Rectangle.Rectangle(4)
print(r)

r = Rectangle.Rectangle()
# Use the mutator methods
r.setWidth(4)
r.setHeight(5)
print("The rectangle has the following measurements:")
# Use the accessor mothods
print("Width is", r.getWidth())
print("Height is", r.getHeight())
# Use other methods
print("Area is", r.area())
print("Perimeter is", r.perimeter())