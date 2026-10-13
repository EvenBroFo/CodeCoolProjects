def year_to_century(year):
    if year % 100 == 0:
        return year // 100
    else:
        return (year // 100) + 1


print(year_to_century(1999))
print(year_to_century(2000))
print(year_to_century(2001))