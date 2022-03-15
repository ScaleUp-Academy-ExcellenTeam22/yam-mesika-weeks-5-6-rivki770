import random
from datetime import date, timedelta, datetime
import calendar


def check_monday(date):
    print(f'The random date is : {date.date()}')
    day = calendar.day_name[date.weekday()]
    if day == "Monday":
        print("אין לי ויניגרט!")


def random_date(date1, date2):         #The left date is bigger
    dates_bet = (date2 - date1).days
    date_between = random.randrange(dates_bet)
    random_date = date1 + timedelta(days=date_between)
    check_monday(random_date)


def main():
    user_input = str(input("Enter the first date (format: YYYY-MM-DD):\n"))
    date1 = datetime.strptime(user_input, "%Y-%m-%d")
    user_input = str(input("Enter the second date (format: YYYY-MM-DD):\n"))
    date2 = datetime.strptime(user_input, "%Y-%m-%d")

    if date1 > date2:
        random_date(date2, date1) #The left date is bigger

    else:
        random_date(date1, date2) #The left date is bigger


if __name__ == '__main__' :
    main()