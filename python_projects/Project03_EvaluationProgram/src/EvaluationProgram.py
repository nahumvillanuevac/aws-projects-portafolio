print("Student Evaluation program:")
def evaluate_students():
	students=[
	{"name": "Alejandro", "notes":[20,15,17,14]},
	{"name": "Nicolas", "notes":[17,12,20, 13]},
    {"name": "Leo", "notes":[12,12,12,13]},
    {"name": "Monica", "notes":[16,7,6,5]}
    ]
	print("\nTotal notes: ")
	for student in students:
		average = sum (student["notes"])/len(student["notes"])
		if average >= 16:
			message = "Excelent"
		elif average >= 14:
			message = "Ok"
		elif average >= 11:
			message = "Enough"
		else:
			message = "Fail"

		print(f"\n|\|{student['name']}: Average -> {average}, {message}")

evaluate_students()
