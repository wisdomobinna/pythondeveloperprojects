''''
TIMECALC
simple code to evaluate the end time of a meeting/ class/ period of time
taking inputs of start time and total mins spent in the meeting.
'''

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
#calculation of time spent in hours and mins bal: 1hour is 60 mins
hour_duration = int(dura / 60)
mins_bal = dura % 60


new_hours = hour + hour_duration
if new_hours > 23:
    new_hours = new_hours - 24
    
new_mins = mins + mins_bal

end_hour = new_hours + (int(new_mins/60)) 
end_mins = new_mins % 60

print(f'Endtime is: {end_hour}:{end_mins}')


