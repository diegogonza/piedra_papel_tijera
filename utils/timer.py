from utils.messages import timer_duration

def calc_timer(final_time, initial_time):
  timer = round(final_time - initial_time, 1)
  timer_duration(timer)