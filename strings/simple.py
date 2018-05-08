data = {'school':'DAV', 'class': '7', 'name': 'abc', 'city': 'pune'}


def my_function(**args):
    schoolname  = data['school']
    cityname = data['city']
    standard = data['class']
    studentname = data['name']
    print(schoolname,cityname,standard,studentname)
    print(data)
my_function(**data)