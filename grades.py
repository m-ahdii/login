labs = []
for i in range(1, 9):
    score = float(input(f"Enter score for labs {i} (out of 100): "))
    labs.append(score)
    
aver_lab = sum(labs) / len(labs)
cover_lab = aver_lab * 0.5 

mid_sem = float(input("Enter mid sem score (out of 100): "))
end_sem = float(input("Enter end sem score (out of 100): "))

aver_exam = (mid_sem + end_sem) / 2
cover_exam = aver_exam * 0.5

final_grade = cover_lab + cover_exam

def get_letter_grade(final_grade):
    if final_grade >= 90:
        return 'A'
    elif final_grade >= 80:
        return 'B'
    elif final_grade >= 70:
        return 'C'
    elif final_grade >= 60:
        return 'D'
    else:
        return 'F'

grade = get_letter_grade(final_grade)

print("You got an: ", grade)