students= [{
    'id:':101,
    'Name:':'rahul',
    'class:':'cse',
    'marks:':{
        'python:':34,
        'java:':56,
        'html:':78

    }
},

{
 'id:':102,
    'Name:':'ram',
    'class:':'cse',
    'marks:':{
        'python:':54,
        'java:':68,
        'html:':34

    }
}


]

def calculate_total(marks):
    total=0

    for mark in marks:
        total = total+mark
    return total

print(students[0])
print(calculate_total(
    students["marks"[0]]))





