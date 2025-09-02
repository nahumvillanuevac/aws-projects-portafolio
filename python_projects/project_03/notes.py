def evaluate_students():
    students=[
    {"name": "Alejandro", "notes":[12,14,17,13]},
    {"name": "Nicolas", "notes":[17,12,20]},
    {"name": "Leo", "notes":[16,14,17,13]},
    {"name": "Monica", "notes":[16,7,6,5]}
    ]
    print("Total notes")
    for student in students:
        average = sum (student["notes"])/len(student["notes"])
        if average >= 11:
            print("enough")
            if average>=16:
                print("excelent")
            elif average>=14:
                message="Ok"
            print(f"{student["name"]} PASS: Average: {average}")

evaluate_students()
