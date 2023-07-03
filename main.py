import mysql.connector

mydb = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='Manali123hastam',
    port='3306',
    database='mydb'
)

mycursor = mydb.cursor()


def reserve_food(student_id, food_id, reserve_or_delete):
    if reserve_or_delete == "reserve":
        mycursor.execute(f'insert into reserved_food value ({student_id}, {food_id});')
    else:
        mycursor.execute(f'delete from reserved_food where studentID = {student_id} and foodID = {food_id}')

    mycursor.execute('select * from reserved_food')
    return mycursor.fetchall()


def review_schedule(student_id):
    mycursor.execute(
        f'SELECT CourseName, classDay, classLocation, classTime, professor FROM mydb.course, mydb.presenceabsence as p where CourseNo = p.course_courseNo and p.CourseSchedule_Student_universityID = "{student_id}";')
    return mycursor.fetchall()


def edit_info(student_id, field, edit):
    mycursor.execute(f'update student set {field} = "{edit}" where universityID = {student_id}')
    mycursor.execute('select * from student')
    return mycursor.fetchall()


def observe():
    mycursor.execute('select * from course')
    return mycursor.fetchall()


def karname(student_id):
    mycursor.execute(f'SELECT * FROM mydb.academictranscrips where Student_univercityID = {student_id};')
    return mycursor.fetchall()


def present_absent(student_id):
    mycursor.execute(f'SELECT * FROM mydb.presenceabsence where CourseSchedule_Student_universityID = {student_id};')
    return mycursor.fetchall()


def prof_score(student_id, score, prof_name):
    mycursor.execute(f'update evaluationofprofessors set ProfessorScore = {score} where Student_universityID = "{student_id}" and ProfessorsName = "{prof_name}";')
    mycursor.execute('select * from evaluationofprofessors where Student_universityID = "{student_id}" and ProfessorsName = "{prof_name}";')
    return mycursor.fetchall()


def exam_schedule(student_id):
    mycursor.execute(f'SELECT distinct CourseName, examDay, examTime, examLocation FROM mydb.course, mydb.presenceabsence as p where CourseNo = p.course_courseNo and p.CourseSchedule_Student_universityID = "{student_id}";')
    return mycursor.fetchall()


def pool(student_id):
    mycursor.execute(f'SELECT StartTime, FinishTime, Price FROM mydb.pool where Student_universityID = "{student_id}";')
    return mycursor.fetchall()


def pool_priceSum(student_id):
    mycursor.execute(f'SELECT Student_universityID, sum(price) FROM mydb.pool group by Student_universityID having Student_universityID = "{student_id}";')
    return mycursor.fetchall()


def lab(prof_id):
    mycursor.execute(f'SELECT LabName, LabID, LabLoc FROM mydb.lab, mydb.professor as p where p.idProfessor = Professor_idProfessor and p.idProfessor = "{prof_id}";')
    return mycursor.fetchall()


def money(student_id):
    mycursor.execute(f'SELECT Money FROM mydb.student where universityID = "{student_id}";')
    return mycursor.fetchall()


def count_on_gender_stu():
    mycursor.execute('SELECT gender, count(gender) FROM mydb.student group by gender ;')
    return mycursor.fetchall()


def count_on_gender_prof():
    mycursor.execute('SELECT gender, count(gender) FROM mydb.professor group by gender ;')
    return mycursor.fetchall()


def manager_prof():
    mycursor.execute('SELECT ProfName FROM mydb.professor where MProf = 1;')
    return mycursor.fetchall()


def course_reservation():
    mycursor.execute('SELECT CourseName, reserved FROM mydb.course order by reserved desc;')
    return mycursor.fetchall()


# reserve_food(input(), int(input()), input())
# mycursor.execute('select * from reserved_food')

# print(review_schedule(input()))

# print(edit_info(input(), input(), input()))

# for elem in observe(): print(elem)

# for elem in karname(input()): print(elem)

# for elem in present_absent(input()): print(elem)

# for elem in prof_score(input(), int(input()), input()): print(elem)

# for elem in exam_schedule(input()): print(elem)

# for elem in pool(input()): print(elem)

# print(pool_priceSum(input()))

# for elem in lab(input()): print(elem)

# print(money(input())[0][0])

# for elem in count_on_gender_stu(): print(elem)

# for elem in count_on_gender_prof(): print(elem)

# for elem in manager_prof(): print(elem[0])

for elem in course_reservation(): print(elem)

users = mycursor.fetchall()
for user in users:
    print(user)

mydb.commit()
mydb.close()









# mycursor.execute('''CREATE
#     ALGORITHM = UNDEFINED
#     DEFINER = `root`@`localhost`
#     SQL SECURITY DEFINER
# VIEW `mydb`.`crime` AS
#     SELECT
#         `s`.`name` AS `name`,
#         `s`.`universityID` AS `universityID`,
#         SUM(`c`.`unit`) AS `sum(c.unit)`
#     FROM
#         ((`mydb`.`academictranscrips` `a`
#         JOIN `mydb`.`student` `s`)
#         JOIN `mydb`.`course` `c`)
#     WHERE
#         ((`a`.`Student_univercityID` = `s`.`universityID`)
#             AND (`a`.`Course_courseNo` = `c`.`CourseNo`)
#             AND (`a`.`Professor_idProfessor` = `c`.`Professor_idProfessor`))
#     GROUP BY `s`.`name`
#     HAVING (SUM(`c`.`unit`) < 12)''')