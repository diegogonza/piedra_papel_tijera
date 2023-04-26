from utils.messages import mesagge_result_of_each_round, message_start_round, messege_winner
from rules.rules_of_game import rules_of_game, select_option
from utils.timer import calc_timer
import time

def run_game():
  timer_start = time.time()
  rounds = 1
  user_win = 0
  computer_win = 0
  user_option = ''
  computer_option = ''
  
  while True:
    message_start_round(rounds)
    rounds += 1
    
    user_option, computer_option = select_option() # Select a optino
    user_win, computer_win = rules_of_game(user_option, computer_option, user_win, computer_win) # Rules

    mesagge_result_of_each_round(user_win, computer_win) # Show a message about the results of each round

    if user_win == 3:
      messege_winner('usuario')
      timer_end = time.time()
      calc_timer(timer_end, timer_start)
      break

    elif computer_win == 3:
      messege_winner('computador')
      timer_end = time.time()
      calc_timer(timer_end, timer_start)
      break
      
run_game()