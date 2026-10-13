def quarter_of_the_year(month):
    if month < 1 or month > 12:
        return "invalid month"
    if month <= 3:
        return 1
    elif month <= 6:
        return 2
    elif month <= 9: 
        return 3
    elif month <= 12:
        return 4


print(quarter_of_the_year(-1))