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


def review_schedule(student_id):
    mycursor.execute(
        f'SELECT CourseName, classDay, classLocation, classTime, professor FROM mydb.course, mydb.presenceabsence as p where CourseNo = p.course_courseNo and p.CourseSchedule_Student_universityID = "{student_id}";')
    return mycursor.fetchall()


# reserve_food(input(), int(input()), input())
# mycursor.execute('select * from reserved_food')

# print(review_schedule(input()))

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

users = mycursor.fetchall()
for user in users:
    print(user)

mydb.commit()
mydb.close()
