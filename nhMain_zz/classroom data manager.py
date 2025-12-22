import tkinter as tk
from tkinter import messagebox

students = []

def checklist(id_student):
    for s in students:
        if s["id"] == id_student:
            return True
    return False


def find_student_by_id(id_student):
    for s in students:
        if s["id"] == id_student:
            return s
    return None

def add_student():
    try:
        id = int(entry_id.get())
    except ValueError:
        messagebox.showerror("Lỗi", "Mã sinh viên không hợp lệ")
        return

    if checklist(id):
        messagebox.showerror("Lỗi", "ID đã tồn tại")
        return

    name = entry_name.get()
    if name == "":
        messagebox.showerror("Lỗi", "Vui lòng nhập họ tên")
        return

    try:
        scores = {
            "Đại số tuyến tính": float(entry_dai_so.get()),
            "Tư duy tính toán": float(entry_tu_duy.get()),
            "Tư tưởng Hồ Chí Minh": float(entry_tu_tuong.get()),
            "Giải tích 1": float(entry_giai_tich.get())
        }
    except ValueError:
        messagebox.showerror("Lỗi", "Điểm không hợp lệ")
        return

    student = {
        "id": id,
        "name": name,
        "scores": scores
    }

    students.append(student)
    messagebox.showinfo("Thành công", "Đã thêm sinh viên")
    clear_output()
    clear_entries()

def search_by_id():
    clear_output()
    try:
        search_id = int(entry_search.get())
    except ValueError:
        messagebox.showerror("Lỗi", "ID tìm kiếm không hợp lệ")
        return

    student = find_student_by_id(search_id)
    if not student:
        output_text.insert(tk.END, "Không tìm thấy sinh viên\n")
        return

    show_student(student)

def display_all_scores():
    clear_output()
    if not students:
        output_text.insert(tk.END, "Chưa có sinh viên nào\n")
        return

    for s in students:
        show_student(s)
        output_text.insert(tk.END, "-" * 30 + "\n")

def delete_by_id():
    try:
        delete_id = int(entry_search.get())
    except ValueError:
        messagebox.showerror("Lỗi", "ID không hợp lệ")
        return

    student = find_student_by_id(delete_id)
    if not student:
        messagebox.showerror("Lỗi", "Không tìm thấy sinh viên")
        return

    students.remove(student)
    clear_output()
    messagebox.showinfo("Thành công", "Đã xóa sinh viên")

def show_student(student):
    output_text.insert(tk.END, f"MSSV: {student['id']}\n")
    output_text.insert(tk.END, f"Họ tên: {student['name']}\n")
    for mon, diem in student["scores"].items():
        output_text.insert(tk.END, f"{mon}: {diem}\n")

def clear_entries():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_dai_so.delete(0, tk.END)
    entry_tu_duy.delete(0, tk.END)
    entry_tu_tuong.delete(0, tk.END)
    entry_giai_tich.delete(0, tk.END)


def clear_output():
    output_text.delete("1.0", tk.END)

root = tk.Tk()
root.title("Classroom Data Manager")
root.geometry("800x480")
root.configure(bg="#E8F0FE")

tk.Label(
    root,
    text="CLASSROOM DATA MANAGER",
    font=("Arial", 16, "bold"),
    fg="#1A237E",
    bg="#E8F0FE"
).pack(pady=10)

main = tk.Frame(root, bg="#E8F0FE")
main.pack(fill="both", expand=True, padx=10)

left = tk.Frame(main, bg="white", padx=15, pady=15)
left.pack(side="left", fill="y", padx=10)

def create_input(label):
    tk.Label(left, text=label, bg="white").pack(anchor="w")
    e = tk.Entry(left)
    e.pack(fill="x", pady=3)
    return e

entry_id = create_input("Mã sinh viên")
entry_name = create_input("Họ tên")
entry_dai_so = create_input("Đại số tuyến tính")
entry_tu_duy = create_input("Tư duy tính toán")
entry_tu_tuong = create_input("Tư tưởng Hồ Chí Minh")
entry_giai_tich = create_input("Giải tích 1")

tk.Button(left, text=" Thêm sinh viên", command=add_student,
          bg="#1A73E8", fg="white", bd=0).pack(fill="x", pady=10)

center = tk.Frame(main, bg="white", padx=15, pady=15)
center.pack(side="left", fill="y")

tk.Label(center, text="Tìm / Xóa theo MSSV", bg="white").pack()

entry_search = tk.Entry(center)
entry_search.pack(fill="x", pady=5)

tk.Button(center, text=" Tìm theo ID", command=search_by_id).pack(fill="x", pady=3)
tk.Button(center, text=" Xóa theo ID", command=delete_by_id).pack(fill="x", pady=3)
tk.Button(center, text=" Hiển thị tất cả điểm", command=display_all_scores).pack(fill="x", pady=3)

right = tk.Frame(main, bg="white", padx=15, pady=15)
right.pack(side="right", fill="both", expand=True)

tk.Label(right, text="Kết quả", bg="white").pack()

output_text = tk.Text(right)
output_text.pack(fill="both", expand=True)

root.mainloop()