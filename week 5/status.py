def status_count(students):

    list_1 = []
    list_2 = []
    result = { "finalized": list_1,
               "not_finalized": list_2,
             }

    

    for student in students:
        if student["status"] == "finalized":
            list_1 += [student["name"]]
        else:
            list_2 += [student["name"]]
    return result

students = [{
              "name": "RadoRado",
              "status": "not_finalized"
            }, {
              "name": "Ivo",
              "status": "finalized"
            }, {
              "name": "Genadi",
              "status": "finalized"
            }]

print(status_count(students))
