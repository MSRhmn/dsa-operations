from datetime import datetime, timedelta


def parse_time(t_str):
    """Parse a time string in "HH:MM" format into a time object."""
    return datetime.strptime(t_str, "%H:%M").time()


def add_minutes(t, minutes):
    """Adds specified number of minutes to a time object."""
    full_date = datetime.combine(datetime.today(), t)
    return (full_date + timedelta(minutes=minutes)).time()


def overlaps(start1, end1, start2, end2):
    """Checks if two intervals overlap."""
    return start1 < end2 and end1 > start2
