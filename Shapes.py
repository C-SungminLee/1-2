import turtle as trtl

painter = trtl.Turtle()


def shape(user_choice_radius, user_choice_angles, user_choice_sides, user_choice_color):

  painter.color(user_choice_color)
  painter.begin_fill()
  painter.circle(user_choice_radius, user_choice_angles, user_choice_sides)
  painter.end_fill()

user_choice_amount = int(input("How many times do you want to make a shape?"))

for i in range(user_choice_amount):
  user_choice_radius = int(input("What is the Radius of this shape? "))
  user_choice_angles = int(input("What are the Angles of this shape? "))
  user_choice_sides = int(input("What is the amount of Sides of this shape? "))
  user_choice_color = input("What is the color of this shape? ")
  shape(user_choice_radius, user_choice_angles, user_choice_sides, user_choice_color)

wn = trtl.Screen()
wn.mainloop()