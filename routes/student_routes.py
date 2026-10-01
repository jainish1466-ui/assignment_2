from fastapi import APIRouter, Response
from models.student_model import Student
from controllers.student_controller import (
    create_student_controller,
    get_students_controller,
    get_student_by_id_controller,
    update_student_controller,
    delete_student_controller
)

studentRouter = APIRouter()


@studentRouter.post("/students")
async def create_student(student: Student, response: Response):
    return await create_student_controller(student, response)


@studentRouter.get("/students")
async def get_students(response: Response):
    return await get_students_controller(response)


@studentRouter.get("/students/{id}")
async def get_student_by_id(id: int, response: Response):
    return get_student_by_id_controller(id, response)



@studentRouter.put("/students/{id}")
async def update_student(
    id: int,
    student: Student,
    response: Response
):
    return update_student_controller(id, student, response)


@studentRouter.delete("/students/{id}")
async def delete_student(id: int, response: Response):
    return delete_student_controller(id, response)