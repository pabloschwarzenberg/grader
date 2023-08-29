#nota final
homework_grade = float(input('Ingrese nota de tareas: '))
interrogation_grade = float(input('Ingrese nota de interrogación: '))
exam_grade = float(input('Ingrese nota de examen: '))
presentation_grade = float(input('Ingrese nota de presentación: '))

final_grade = (
    homework_grade * 0.3 +
    interrogation_grade * 0.3 +
    exam_grade * 0.3 +
    presentation_grade * 0.1)

print(round(final_grade, 1))