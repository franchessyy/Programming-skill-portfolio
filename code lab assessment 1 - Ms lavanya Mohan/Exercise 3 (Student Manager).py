import tkinter as tk
from tkinter import messagebox, simpledialog
import csv

class StudentManagementSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Manager")
        self.master.configure(bg="#f7c3cf")  # this sets the main window background color

        self.filename = 'C:\\Users\\ASUS\\Downloads\\code lab assessment 1 - Ms lavanya Mohan\\resources\\studentMarks.txt'
        self.students = self.load_student_data(self.filename)

      
        self.frame = tk.Frame(master)
        self.frame.pack(pady=20)

       
        self.view_all_button = tk.Button(self.frame, text="View All Students", command=self.view_all_students)
        self.view_all_button.pack(pady=5)

        self.view_individual_button = tk.Button(self.frame, text="View Individual Student", command=self.view_individual_student)
        self.view_individual_button.pack(pady=5)

        self.add_button = tk.Button(self.frame, text="Add Student", command=self.add_student)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(self.frame, text="Delete Student", command=self.delete_student)
        self.delete_button.pack(pady=5)

        self.update_button = tk.Button(self.frame, text="Update Student", command=self.update_student)
        self.update_button.pack(pady=5)

        self.show_highest_button = tk.Button(self.frame, text="Show Highest Scorer", command=self.show_highest_student)
        self.show_highest_button.pack(pady=5)

        self.show_lowest_button = tk.Button(self.frame, text="Show Lowest Scorer", command=self.show_lowest_student)
        self.show_lowest_button.pack(pady=5)

        self.exit_button = tk.Button(self.frame, text="Exit", command=self.exit_program)
        self.exit_button.pack(pady=10)

    def load_student_data(self, filename):
        students = []
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                first_line = next(reader, None)
                if first_line is None:
                    messagebox.showerror("Error", "The file is empty.")
                    return students

                num_students = int(first_line[0])
                for _ in range(num_students):
                    student_data = next(reader)
                    if student_data:
                        code = int(student_data[0])
                        name = student_data[1]
                        course_marks = list(map(int, student_data[2:5]))
                        exam_mark = int(student_data[5])
                        students.append({
                            'code': code,
                            'name': name,
                            'course_marks': course_marks,
                            'exam_mark': exam_mark,
                        })
        except FileNotFoundError:
            messagebox.showerror("Error", f"The file '{filename}' was not found.")
        except ValueError as e:
            messagebox.showerror("Error", f"Incorrect data format in the file: {e}")
        return students

    def calculate_student_details(self, student):
        total_coursework = sum(student['course_marks'])
        total_marks = total_coursework + student['exam_mark']
        percentage = (total_marks / 160) * 100
        grade = self.get_grade(percentage)
        return total_coursework, percentage, grade

    def get_grade(self, percentage):
        if percentage >= 70:
            return 'A'
        elif percentage >= 60:
            return 'B'
        elif percentage >= 50:
            return 'C'
        elif percentage >= 40:
            return 'D'
        else:
            return 'F'

    def view_all_students(self):
        all_students_info = ""
        total_percentage = 0
        for student in self.students:
            total_coursework, percentage, grade = self.calculate_student_details(student)
            total_percentage += percentage
            all_students_info += (f"Name: {student['name']}\n"
                                  f"Student Number: {student['code']}\n"
                                  f"Total Coursework Mark: {total_coursework}\n"
                                  f"Exam Mark: {student['exam_mark']}\n"
                                  f"Overall Percentage: {percentage:.2f}%\n"
                                  f"Grade: {grade}\n\n")
        
        num_students = len(self.students)
        average_percentage = total_percentage / num_students if num_students > 0 else 0
        all_students_info += (f"Number of students: {num_students}\n"
                              f"Average Percentage: {average_percentage:.2f}%\n")
        messagebox.showinfo("All Students", all_students_info)

    def view_individual_student(self):
        student_code = simpledialog.askinteger("Input", "Enter student number (1000-9999):")
        student = next((s for s in self.students if s['code'] == student_code), None)
        if student:
            total_coursework, percentage, grade = self.calculate_student_details(student)
            info = (f"Name: {student['name']}\n"
                    f"Student Number: {student['code']}\n"
                    f"Total Coursework Mark: {total_coursework}\n"
                    f"Exam Mark: {student['exam_mark']}\n"
                    f"Overall Percentage: {percentage:.2f}%\n"
                    f"Grade: {grade}\n")
            messagebox.showinfo("Student Information", info)
        else:
            messagebox.showwarning("Not Found", "Student not found.")

    def add_student(self):
        code = simpledialog.askinteger("Input", "Enter student number (1000-9999):")
        name = simpledialog.askstring("Input", "Enter student name:")
        course_marks = simpledialog.askstring("Input", "Enter three course marks (comma-separated):")
        exam_mark = simpledialog.askinteger("Input", "Enter exam mark:")
        if course_marks:
            course_marks = list(map(int, course_marks.split(',')))
            self.students.append({
                'code': code,
                'name': name,
                'course_marks': course_marks,
                'exam_mark': exam_mark,
            })
            messagebox.showinfo("Success", "Student added successfully.")

    def delete_student(self):
        code = simpledialog.askinteger("Input", "Enter student number to delete:")
        self.students[:] = [s for s in self.students if s['code'] != code]
        messagebox.showinfo("Success", "Student deleted successfully.")

    def update_student(self):
        code = simpledialog.askinteger("Input", "Enter student number to update:")
        student = next((s for s in self.students if s['code'] == code), None)
        if student:
            new_name = simpledialog.askstring("Input", "Enter new name (leave blank to keep current):")
            student['name'] = new_name if new_name else student['name']

            new_course_marks = simpledialog.askstring("Input", "Enter new course marks (comma-separated, leave blank to keep current):")
            if new_course_marks:
                student['course_marks'] = list(map(int, new_course_marks.split(',')))

            new_exam_mark = simpledialog.askinteger("Input", "Enter new exam mark (leave blank to keep current):")
            if new_exam_mark is not None:
                student['exam_mark'] = new_exam_mark
            
            messagebox.showinfo("Success", "Student updated successfully.")
        else:
            messagebox.showwarning("Not Found", "Student not found.")

    def show_highest_student(self):
        highest_student = max(self.students, key=lambda s: sum(s['course_marks']) + s['exam_mark'], default=None)
        if highest_student:
            total_coursework, percentage, grade = self.calculate_student_details(highest_student)
            info = (f"Highest Student:\nName: {highest_student['name']}\n"
                    f"Student Number: {highest_student['code']}\n"
                    f"Total Coursework Mark: {total_coursework}\n"
                    f"Exam Mark: {highest_student['exam_mark']}\n"
                    f"Overall Percentage: {percentage:.2f}%\n"
                    f"Grade: {grade}\n")
            messagebox.showinfo("Highest Scorer", info)
        else:
            messagebox.showwarning("No Students", "No students found.")

    def show_lowest_student(self):
        lowest_student = min(self.students, key=lambda s: sum(s['course_marks']) + s['exam_mark'], default=None)
        if lowest_student:
            total_coursework, percentage, grade = self.calculate_student_details(lowest_student)
            info = (f"Lowest Student:\nName: {lowest_student['name']}\n"
                    f"Student Number: {lowest_student['code']}\n"
                    f"Total Coursework Mark: {total_coursework}\n"
                    f"Exam Mark: {lowest_student['exam_mark']}\n"
                    f"Overall Percentage: {percentage:.2f}%\n"
                    f"Grade: {grade}\n")
            messagebox.showinfo("Lowest Scorer", info)
        else:
            messagebox.showwarning("No Students", "No students found.")

    def exit_program(self):
        self.save_students_to_file(self.filename, self.students)
        messagebox.showinfo("Exit", "Exiting program.")
        self.master.quit()

    def save_students_to_file(self, filename, students):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([len(students)])
            for student in students:
                row = [student['code'], student['name']] + student['course_marks'] + [student['exam_mark']]
                writer.writerow(row)
#run the main loop
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()
