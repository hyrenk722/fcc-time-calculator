def add_time(start, duration, day=None):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Parse the start time into minutes since midnight.
    time_part, period = start.split()
    start_hour, start_minute = (int(x) for x in time_part.split(":"))
    if period == "PM" and start_hour != 12:
        start_hour += 12
    elif period == "AM" and start_hour == 12:
        start_hour = 0
    start_total = start_hour * 60 + start_minute

    # Parse the duration and add it.
    dur_hour, dur_minute = (int(x) for x in duration.split(":"))
    end_total = start_total + dur_hour * 60 + dur_minute

    days_later = end_total // (24 * 60)
    end_minutes = end_total % (24 * 60)
    end_hour24 = end_minutes // 60
    end_minute = end_minutes % 60

    if end_hour24 >= 12:
        end_period = "PM"
    else:
        end_period = "AM"
    end_hour = end_hour24 % 12
    if end_hour == 0:
        end_hour = 12

    new_time = f"{end_hour}:{end_minute:02d} {end_period}"

    if day is not None:
        day_index = days_of_week.index(day.capitalize())
        new_day = days_of_week[(day_index + days_later) % 7]
        new_time += f", {new_day}"

    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time
