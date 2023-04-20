list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]

# considering all the student have unique ids assigned to them
def merge_lists(list_1, list_2) -> list:
    list_3 = []
    student_ids=[]  

    for student in list_1 + list_2:
        id=student.get("id")
        student_ids.append(id)   

    # student_ids has all the duplicate values to get the unique values we use set method
    unique_student_ids=set(student_ids)

    for student_id in unique_student_ids:
        updated_student={}
        for student in list_1 + list_2:
            if(student.get("id")==student_id):
                updated_student.update(student)
        list_3.append(updated_student)

    return list_3

    
    
list_3 = merge_lists(list_1, list_2)
print(list_3)