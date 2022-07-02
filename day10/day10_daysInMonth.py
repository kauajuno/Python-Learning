def leap_check(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(month, year):
    """
    checks how many days a month has.
    :param month:
    :param year:
    :return:
    """
    if month < 1 or month > 12:
        return 'MONTH_ERROR'
    if leap_check(year) is True and month == 2:
        return month_days[month - 1] + 1
    else:
        return month_days[month - 1]


month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

result = days_in_month(int(input('Month\n')), int(input('Year\n')))
if result == 'MONTH_ERROR':
    print('Invalid month')
else:
    print(f"It has {result} days!")
