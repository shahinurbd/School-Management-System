from school import School
from classroom import Classroom
from person import Student,Teacher
from subject import Subject

school = School('ABC','Dhaka')
#adding classroom
eight = Classroom('Eight')
nine = Classroom('Nine')
ten = Classroom('Ten')

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

#adding students
rahim = Student('Rahim',eight)
karim = Student('Karim',nine)
shahin = Student('Shahin',ten)
sajjad = Student('Sajjad',ten)

school.student_addmission(rahim)
school.student_addmission(karim)
school.student_addmission(shahin)
school.student_addmission(sajjad)

#adding techars
abul = Teacher('Abul Khan')
babul = Teacher('Babul Khan')
kabul = Teacher('Kabul Khan')
sabul = Teacher('Sabul Khan')

school.add_teacher('Bangla','Abul Khan')
school.add_teacher('English','Babul Khan')
school.add_teacher('ICT','Kabul Khan')
school.add_teacher('Math','Sabul Khan')

#adding subjects
bangla = Subject('Bangla', abul)
english = Subject('English', babul)
ict = Subject('ICT', kabul)
math = Subject('Math', sabul)

eight.add_subject(bangla)
eight.add_subject(math)
eight.add_subject(english)
nine.add_subject(english)
nine.add_subject(ict)
nine.add_subject(bangla)
ten.add_subject(ict)
ten.add_subject(bangla)
ten.add_subject(english)
ten.add_subject(math)

eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()

print(school)