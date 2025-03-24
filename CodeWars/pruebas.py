def people_with_age_drink(age):
    if type(age) == int:
        if (age <= 14): return "Kids drink toddy."
        elif (age <= 18): return "Teens drink coke."
        elif (age <= 21): return "Young adults drink beer."
        elif (age >= 21): return "Adults drink whisky."
    else:
        return 'unknown value'


if __name__ == '__main__':
    people_with_age_drink(13)
    people_with_age_drink(0)
    people_with_age_drink("s")
    people_with_age_drink(17)
    people_with_age_drink(22)
    people_with_age_drink(20)