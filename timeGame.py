def time_interval(start_hour, start_minute, start_second, end_hour, end_minute, end_second):
    hour_interval = end_hour - start_hour
    minute_interval = end_minute - start_minute
    second_interval = end_second - start_second
    hour_interval *= 3600
    minute_interval *= 60
    second_interval = second_interval
    return "Total time interval is " + str(sum([second_interval, minute_interval, second_interval]))


startHour, startMinute, startSecond = input("Enter start time: ").split(":")

startHour = int(startHour)
startMinute = int(startMinute)
startSecond = int(startSecond)

endHour, endMinute, endSecond = input("Enter end time: ").split(":")

endHour = int(endHour)
endMinute = int(endMinute)
endSecond = int(endSecond)

if startHour > 24 or endHour > 24:
    raise Exception("Wrong input, hour cannot be greater than 24")

if startMinute > 60 or endMinute > 60:
    raise Exception("Wrong input, minute cannot be greater than 60")

if startSecond > 60 or endSecond > 60:
    raise Exception("Wrong input, second cannot be greater than 60")

print(time_interval(startHour, startMinute, startSecond, endHour, endMinute, endSecond))
