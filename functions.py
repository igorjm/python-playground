# Author: @igorjm
#
# Functions

def minutes_to_hours(minutes):
    hours = minutes / 60
    return hours

def seconds_to_hours(seconds):
    hours = seconds / 3600
    return hours

def minutes_and_seconds_to_hours(minutes, seconds):
    hours = minutes / 60 + seconds / 3600
    print(hours)

print(minutes_to_hours(60))
print(seconds_to_hours(7200))

minutes_and_seconds_to_hours(70, 300)