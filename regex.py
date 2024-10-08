import re

text = "The agent's phone number is 9611849570,Call to phone soon!"

pattern = 'phone'

print(re.search(pattern,text))
match = re.findall(pattern,text)
print(match)
print(len(match))

print(re.findall(r'^\d','1 number is 1'))
print(re.findall(r'\d$','number is 1'))
