def average(*args):
    avg = 0
    for arg in args:
        avg += int(arg)
    avg /= len(args)
    avg /= 10
    return round(avg)
    
def situation(grade, absences):
    if is_failed_for_absence(absences):
        result = "Reprovado por Falta"
    elif grade < 5:
        result = "Reprovado por Nota"
    elif grade >= 5 and grade < 7:
        result = "Exame Final"
    else:
        result = "Aprovado"
    return result
        
def is_failed_for_absence(absences):
    total_of_classes = 60
    max_allowed_absence = 25
    frequency = (absences * 100) / total_of_classes
    return frequency > max_allowed_absence

def approval_grade(grade):
    ag = 10 - grade
    if ((grade + ag) / 2) >= 5:
        return ag