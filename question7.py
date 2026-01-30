# Question 7: Time Conversion Function

def convert_time(seconds):
    if seconds < 0 or seconds >= 86400:
        return "Invalid input"

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    if hours >= 12:
        period = "PM"
    else:
        period = "AM"

    hours = hours % 12
    if hours == 0:
        hours = 12

    return f"{hours} {minutes} {secs} {period}"


print(convert_time(19067))
