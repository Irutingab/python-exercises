import mysql.connector
import matplotlib.pyplot as plt

def generate_performance_graph():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="irutingaboRai1@",
        database="students"
    )
    cursor = conn.cursor()

    # Retrieve student IDs and performance data from the report table
    cursor.execute("SELECT id, percentage FROM report ORDER BY percentage DESC")
    students = cursor.fetchall()

    if not students:
        print("No data found in the report table!")
        return

    ids = [student[0] for student in students]  # Student IDs
    percentages = [student[1] for student in students]  # Percentages

    # Plotting the data
    plt.figure(figsize=(10, 6))
    plt.bar(ids, percentages, color='skyblue')
    plt.title("Student Performance", fontsize=16)
    plt.xlabel("Student ID", fontsize=12)
    plt.ylabel("Percentage (%)", fontsize=12)
    plt.xticks(rotation=0, fontsize=10)  # Use student IDs as x-axis labels
    plt.tight_layout()

    # Save the graph as an image and show it
    plt.savefig("student_performance.png")
    plt.show()

    cursor.close()
    conn.close()

# Call the function to generate the graph
generate_performance_graph()
