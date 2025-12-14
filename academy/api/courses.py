from fastapi import APIRouter ,HTTPException ,status
from academy.models.course import Course
from academy.schemas.course import CourseCreate, CourseResponse , CourseUpdate,CourseView,CourseJoinView
from typing import List

router = APIRouter(prefix="/courses", tags=["Courses"])

@router.post("/create_course", response_model=CourseResponse)
async def create_course(course: CourseCreate):
    course_obj = Course(**course.model_dump())
    await course_obj.save()
    return course_obj.to_dict()

@router.get("/get-all-courses",response_model=list[CourseResponse])
async def get_all_courses():
    return await Course.select().run()

@router.put("/course/{id}",response_model=CourseUpdate)
async def update_course(id:int,course:CourseUpdate):
    data = course.model_dump(exclude_unset=True)
    if not data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid id"
        )

    rows_updated = await Course.update(data).where(Course.id == id).run()
    if rows_updated == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )
    updated_course = await Course.select().where(Course.id == id).first().run()
    return updated_course

# @router.delete("/delete_course/{id}")
# async def delete_course(id:int):
#     dlt_course = await Course.delete().where(Course.id == id)
#     return dlt_course

@router.delete("/delete_course/{id}")
async def delete_course(id: int):
    course = await Course.select().where(Course.id == id).first().run()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    await Course.delete().where(Course.id == id).run()
    return {"deleted_course": course}

# @router.get("/get-single-names",response_model=CourseView)
# async def get_single_courses():
#     return await Course.raw('SELECT name FROM COURSE')

# @router.get("/get-single-names",response_model=CourseView)

@router.get("/get-single-names", response_model=List[CourseView])
async def get_single_courses():
    results = await Course.raw("SELECT name FROM COURSE")
    return results

@router.get("/get-all-names", response_model=List[CourseView])
async def get_single_courses():
    results = await Course.raw("SELECT *  FROM COURSE")
    return results


@router.get("joins_operation",response_model=List[CourseJoinView])
async def joins_operation():
    join_query = await Course.select(Course.name, Course.instructor).run()
    return join_query


#task 1

@router.get("/singlecourse/{id}",response_model=CourseResponse)
async def singleCourse(id:int):
    singleCourseQuery = await Course.select().where(Course.id == id).first().run()
    if not singleCourseQuery:
        raise HTTPException (
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Given id = {id} is not correct"

        )
    return singleCourseQuery
