from modules.schedular import get_free_slots

if __name__ == "__main__":
    bookings = [("09:30", "10:10"), ("11:00", "11:40")]
    working_hours = ("09:00", "12:00")
    slots = get_free_slots(
        bookings, working_hours, service_duration=30, buffer_minute=10
    )
    print("Available slots:", slots)
