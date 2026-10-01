from fastapi import Response
from models.student_model import Student


# List to store students
students = []
student_id = 0


async def create_student_controller(student: Student, response: Response):
    global student_id

    student_id += 1
    student.id = student_id

    students.append(student)

    response.status_code = 201

    return {
        "isSuccess": True,
        "message": "Student created successfully",
        "data": student
    }



async def get_students_controller(response: Response):
    try:
        response.status_code = 200

        return {
            "isSuccess": True,
            "data": students
        }

    except Exception as e:
        print(e)
        response.status_code = 500

        return {
            "isSuccess": False,
            "message": "Error fetching students"
        }



def get_student_by_id_controller(id: int, response: Response):
    for student in students:
        if student.id == id:
            response.status_code = 200

            return {
                "isSuccess": True,
                "data": student
            }

    response.status_code = 404

    return {
        "isSuccess": False,
        "message": "Student not found"
    }




def update_student_controller(
    id: int,
    student: Student,
    response: Response
):
    for i in range(len(students)):
        if students[i].id == id:
            student.id = id
            students[i] = student

            response.status_code = 200

            return {
                "isSuccess": True,
                "message": "Student updated successfully",
                "data": student
            }

    response.status_code = 404

    return {
        "isSuccess": False,
        "message": "Student not found"
    }



def delete_student_controller(id: int, response: Response):
    for i in range(len(students)):
        if students[i].id == id:
            students.pop(i)

            response.status_code = 204
            return

    response.status_code = 404

    return {
        "isSuccess": False,
        "message": "Student not found"
    }