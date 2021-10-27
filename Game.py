
user_input = input("What do you want to do? ") 

def menu():
  user_choice_in_menu = input("What do you want to do? Rock Paper Scissors (rps) ")
  
  
  while user_choice_in_menu.lower is ("rock paper scissors" or "rps"):
    print ("okay")

    if not user_choice_in_menu.lower is ("rock paper scissors" or "rps"):
      user_choice_in_menu = input("Please choose one, Rock Paper Scissors (rps) ")


  

if user_input.lower == ("menu"):
  menu()

menu()
