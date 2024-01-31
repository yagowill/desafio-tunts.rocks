from logic import average, is_failed_for_absence, situation, approval_grade

def test_average():
    assert average(42,93,57) == 6
    
def test_situation_disapproved():
    assert situation(4, 15) == "Reprovado por Nota"
    
def test_situation_final_exam():   
    assert situation(6, 14) == "Exame Final"
    
def test_situatioin_approved():
    assert situation(8, 8) == "Aprovado"
    
def test_situatioin_failed_for_absence():
    assert situation(7,17)
    
def test_is_failed_for_absence_true():
    assert is_failed_for_absence(16)

def test_is_failed_for_absence_false():
    assert is_failed_for_absence(15) == False
    
def test_approval_grade_five():
    assert approval_grade(5) == 5
    
def test_approval_grade_six():
    assert approval_grade(6) == 4