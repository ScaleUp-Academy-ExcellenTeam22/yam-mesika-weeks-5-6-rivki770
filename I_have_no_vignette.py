import random
from datetime import date, timedelta, datetime
import calendar


def check_date_if_its_monday(date_to_check: date) -> bool:
    """
    The function check if date is monday.
    :param date_to_check: The date we need check if its monday.
    :return: True if is monday. False if isn't.
    """
    day_in_week = calendar.day_name[date_to_check.weekday()]
    return True if day_in_week == "Monday" else False


def random_date_between_two_dates(date_low: date, date_high: date):
    """
    Function that selects a random date between 2 dates.
    :param date_low: the older date.
    :param date_high: the bigger date.
    """
    number_days_between_two_dates = (date_high - date_low).days
    random_number = random.randrange(number_days_between_two_dates)
    new_date_between_two_dates = date_low + timedelta(days=random_number)
    print(f'The random date is : {new_date_between_two_dates.date()}')
    if check_date_if_its_monday(new_date_between_two_dates):
        print("אין לי ויניגרט!")


def main():
    user_input = str(input("Enter the first date (format: YYYY-MM-DD):\n"))
    date1 = datetime.strptime(user_input, "%Y-%m-%d")
    user_input = str(input("Enter the second date (format: YYYY-MM-DD):\n"))
    date2 = datetime.strptime(user_input, "%Y-%m-%d")

    if date1 > date2:
        random_date_between_two_dates(date2, date1)

    else:
        random_date_between_two_dates(date1, date2)


if __name__ == '__main__':
    main()