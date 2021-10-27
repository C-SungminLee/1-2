# Allen, Sungmin, Yejun, Taiga
import turtle as trtl

t = trtl.Turtle()

t.speed(0)


# The Slope and Y-intecept
equation = input("Please enter your eqaution as Y = m x + b: ")
equation_list = equation.split()
m = int(equation_list[2])
b = int(equation_list[5])

if m == abs(m):
  m_value = True
else:
  m_value = False


# coordanite plane


  # y hashmark
t.pencolor("grey")
x = 0
y_pos = -400
while x < 85:
    t.penup()
    t.goto(-400,y_pos)
    t.pendown()
    t.forward(800)
    t.backward(800)
    y_pos += 10
    x += 1 

  # y hashmark
t.setheading(0)
t.left(90)
y = 0
x_pos = -400
while y < 81:
    t.penup()
    t.goto(x_pos,-400 )
    t.pendown()
    t.forward(800)
    t.backward(800)
    x_pos += 10
    y += 1
       
  # Y & X axis
t.color("black")
t.pensize(3)
t.penup() 
t.goto(0,0) 
t.setheading(0) 
t.pendown() 
t.forward(400)
t.backward(800) 
t.goto(0,0) 
t.setheading(90) 
t.pendown 
t.forward(400) 
t.backward(800)
t.penup()

# The line

x_cor = 0
y_cor = 10*b
t.penup()
t.goto(x_cor,y_cor)


# b
t.color("red")
t.setheading(0)

# m

if m_value == True:

    #Line going up'
  for i in range(40):
    t.pendown()
    x_cor = m*i
    y_cor = x_cor + b
    t.goto(10*x_cor, 10*y_cor)
    t.penup()
  t.pendown()
  t.left(45)
  t.shape("arrow")
  t.stamp()
  t.penup()
  t.goto(0, 10*b)

  x_cor = 0
  y_cor = 10*b



    #Line going down
  for i in range(40):
    t.pendown()
    x_cor = m*i
    y_cor = x_cor-b
    t.goto(10*-(x_cor), 10*-(y_cor))
    t.penup()

  t.pendown()
  t.setheading(270)
  t.right(45)
  t.stamp()

else:
      #Line going up
  for i in range(40):
    t.pendown()
    x_cor = m*i
    y_cor = x_cor + b
    t.goto(10*-(x_cor), 10*y_cor)
    t.penup()
  t.pendown()
  t.right(45)
  t.shape("arrow")
  t.stamp()
  t.penup()
  t.goto(0, 10*b)


    #Line going down
  for i in range(40):
    t.pendown()
    x_cor = m*i
    y_cor = x_cor - b
    t.goto(10*(x_cor), 10*-(y_cor))
    t.penup()

  t.pendown()
  t.setheading(270)
  t.left(225)
  t.stamp()



wn = trtl.Screen()
wn.mainloop()