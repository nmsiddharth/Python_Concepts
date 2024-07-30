def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)

person("Siddu",age=23,place="Bengaluru")