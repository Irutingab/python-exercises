import csvintosql
import mysql.connector

def generate_report():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="irutingaboRai1@",
        database="students"
    )
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name, email, mathematics, science, history, english, art, computer_science 
        FROM students_records
    """)
    students = cursor.fetchall()

    report_data = []
    total_percentages = 0
    for student in students:
        name, email, math, sci, hist, eng, art, cs = student
        grades = [math, sci, hist, eng, art, cs]
        total = sum(map(float, grades))
        percentage = total / 6
        total_percentages += percentage
        report_data.append((name, email, percentage))

    class_average = total_percentages / len(students) if students else 0

    report_data.sort(key=lambda x: x[2], reverse=True)

    cursor.execute("DELETE FROM report")
    conn.commit()

    for data in report_data:
        cursor.execute("""
            INSERT INTO report (name, email, percentage, class_average)
            VALUES (%s, %s, %s, %s)
        """, (*data, class_average))
    conn.commit()

    if report_data:
        top_student = report_data[0]
        print(f"Top Student: {top_student[0]} with {top_student[2]:.2f}%")
    print(f"Class Average: {class_average:.2f}%")

    cursor.close()
    conn.close()

generate_report()
