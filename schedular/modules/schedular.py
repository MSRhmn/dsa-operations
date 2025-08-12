from .time_utils import parse_time, add_minutes, overlaps


def get_free_slots(bookings, working_hours, service_duration, buffer_minute, step=5):
    """Return list of available start times for a given working day, avoiding overlapping with existing bookings."""
    free_slots = []

    work_start = parse_time(working_hours[0])
    work_end = parse_time(working_hours[1])

    total_required = service_duration + buffer_minute

    booking_intervals = [
        (parse_time(start), parse_time(end)) for start, end in bookings
    ]

    current_start = work_start

    while add_minutes(current_start, total_required) <= work_end:
        current_end = add_minutes(current_start, total_required)
        has_conflict = False

        for b_start, b_end in booking_intervals:
            if overlaps(current_start, current_end, b_start, b_end):
                has_conflict = True
                break

        if not has_conflict:
            free_slots.append(current_start.strftime("%H:%M"))

        current_start = add_minutes(current_start, step)

    return free_slots
