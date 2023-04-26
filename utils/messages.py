# Messages
victory_menssage = 'Has ganado'
defeat_message = 'Has perdido'
tie_message = 'Empate'
invalid_option_message = 'Opción no valida :('


# Select a option
def message_select_a_option(options):
  list_of_options = ', '.join(options)
  messege = f"{list_of_options}: ¿Qué elijes? => "
  return messege

# show selected options
def show_selected_options(user_option, computer_option):
  print("Usuario = ", user_option)
  print("Computadora = ", computer_option)
      
# What's the round?
def message_start_round(rounds):
  print('*' * 10)
  print('ROUND', rounds)
  print('*' * 10)

# Show a messages
def show_message(message):
  return print(message)

# Show results of each round
def mesagge_result_of_each_round(user_win, computer_win):
  print('Resultados:')
  print(f"Usuario => {user_win}")
  print(f"Computadora => {computer_win}")
  print("-" * 50)
  
# Messega to winner
def messege_winner(winner: str):
  return print(f"El ganador es el {winner}")

# Duration of the game
def timer_duration(duration):
  return print(f"Este juego ha durado {duration} segundos")