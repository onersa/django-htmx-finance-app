import random
from datetime import date, timedelta

def generate_random_date(start_date, end_date):
    """
    Generates a random date between start_date and end_date (inclusive).
    """
    if start_date > end_date:
        raise ValueError("Start date cannot be after end date.")

    time_between_dates = end_date - start_date
    print(f"time_between_dates: {time_between_dates}")
    days_between_dates = time_between_dates.days
    print(f"days_between_dates: {days_between_dates}")
    random_number_of_days = random.randrange(days_between_dates + 1) # +1 to include end_date
    print(f"random_number_of_days: {random_number_of_days}" )
    random_date = start_date + timedelta(days=random_number_of_days)
    print(f"random_date: {random_date}")
    return random_date

# Example usage:
start_dt = date(2024, 12, 1)
end_dt = date(2025, 12, 10)

random_generated_date = generate_random_date(start_dt, end_dt)
print(f"Random date between {start_dt} and {end_dt}: {random_generated_date}")