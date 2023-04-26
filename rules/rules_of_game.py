import random
from utils.messages import messege_winner, show_selected_options, message_select_a_option, show_message, invalid_option_message, tie_message, defeat_message, victory_menssage

options = ('piedra', 'papel', 'tijera')

def select_option():
    user_option = input(f"{message_select_a_option(options)}").lower()
    computer_option = random.choice(options)

    return user_option, computer_option

def rules_of_game(user_option, computer_option, user_win, computer_win):
  
  if user_option in options:
      show_selected_options(user_option, computer_option)
  
      if user_option == computer_option:
        show_message(tie_message)
      elif user_option == 'piedra' and computer_option == 'tijera':
        show_message(victory_menssage)
        user_win += 1
      elif user_option == 'tijera' and computer_option == 'papel':
        show_message(victory_menssage)
        user_win += 1
      elif user_option == 'papel' and computer_option == 'piedra':
        show_message(victory_menssage)
        user_win += 1
      else:
        show_message(defeat_message)
        computer_win += 1
        
  elif not user_option in options:
    show_message(invalid_option_message)
      
  return user_win, computer_win



