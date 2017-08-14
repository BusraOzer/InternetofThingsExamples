import re

contactInfo = 'name: tolga, surname: buyuktanir, phone: 555-1212'
m = re.search(r'(\w+): (\w+), (\w+): (\w+), (\w+): (\S)', contactInfo)
print(m.groups())
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.group(4))

