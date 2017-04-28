# Classes - Practice & Testscripts


class Person(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    size = "Enter size in meters: e.g. 1.80"

class SchoolGirl(Person):
    def __init__(self, academic_year, body, style):
        self.academic_year = academic_year
        self.body = body
        self.style = style

amy = SchoolGirl("freshman", "busty", "gothic")


print(amy.body)
print(amy.style)

amy.size = 1.80

print(amy.size)


