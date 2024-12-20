#1
# -- SELECT exam_year, AVG(grade) AS avg_grade
# -- FROM grades
# -- GROUP BY exam_year;

# 2
# -- SELECT student_name, AVG(grade) AS avg_grade_2024
# -- FROM grades
# -- WHERE exam_year == 2024
# -- GROUP BY student_name

# 3
# -- SELECT subject_name,exam_year, MAX(grade) AS max_grade_per_year, MIN(grade) AS min_grade_per_year
# -- FROM grades
# -- GROUP BY subject_name,exam_year

# 4
# -- SELECT subject_name,exam_year, COUNT(subject_name) AS test_count
# -- FROM grades
# -- GROUP BY subject_name,exam_year

# 5
# -- SELECT subject_name, AVG(grade) AS avg_bigger_than_85
# -- FROM grades
# -- GROUP BY subject_name
# -- HAVING AVG(grade) > 85

# 6
# -- SELECT grade, count(*) AS bigger_than_90
# -- FROM grades
# -- WHERE grade>90
# -- GROUP BY grade