# Print employee with maximum working hours along with hours

work_hours = [("Sid",3000),("Varun",400),("Ujwal",230)]

def check(work_hours):
    max = 0
    employee = ""

    for emp,hour in work_hours:
        if hour > max :
            max = hour
            employee = emp

    return (employee,max)

print(check(work_hours))


