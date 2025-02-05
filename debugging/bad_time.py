'''
Given the current time (integer hour, integer min) and 
    the wait time (integer hour, integer min)
    compute the the final time after the wait.
'''

current_hour, current_min = input("Current time? ").split()
wait_hour, wait_min = input("Wait time? ").split()

min = int(current_min) + int(wait_min)  
final_time_hour = int(current_hour) + int(wait_hour) 
if min % 60 != min:
    final_time_hour += 1
    min = min % 60
final_time_hour = final_time_hour % 24

print(f'The time after waiting is: {final_time_hour}h{min}')