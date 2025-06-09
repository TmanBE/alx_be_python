from datetime import datetime, date, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return formatted_date

#Calculate future date
def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = date.today() + timedelta(days= number_of_days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")
    return formatted_future_date

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
