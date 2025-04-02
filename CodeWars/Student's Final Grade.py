# Gracida Tapia Bryan.
# 1 de Abril del 2025.
"""
Create a function finalGrade, which calculates the final grade of a student depending on two parameters: a grade for the exam and a number of completed projects.

This function should take two arguments: exam - grade for exam (from 0 to 100); projects - number of completed projects (from 0 and above);

This function should return a number (final grade). There are four types of final grades:

100, if a grade for the exam is more than 90 or if a number of completed projects more than 10.
90, if a grade for the exam is more than 75 and if a number of completed projects is minimum 5.
75, if a grade for the exam is more than 50 and if a number of completed projects is minimum 2.
0, in other cases
"""
def final_grade(exam, projects):
    """
    Función que devuelve la calificación de un alumno según la calificación de examen y de su proyecto.
    :param exam: Calificación del examen.
    :param projects: Calificación del proyecto
    """
    if exam>90 or projects >10: return 100
    if exam>75 and projects >= 5: return 90
    if exam>50 and projects >= 2: return 75
    else: return 0

if __name__ == '__main__':
    resultado = final_grade(100, 12)
    print(resultado)