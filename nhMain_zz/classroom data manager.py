import tkinter as tk
from tkinter import messagebox

students = []

def checklist(lst, id_student):
    for x in lst:
        if x["id"] == id_student:
            return True
    return False

def add_student_gui():
    try:
        id = int(entry_id.get())
    except ValueError:
        messagebox.showerror("Lỗi", "Mã sinh viên không hợp lệ")
        return

    if checklist(students, id):
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
    listbox.insert(tk.END, f"{id} - {name}")
    clear_entries()
    messagebox.showinfo("Thành công", "Đã thêm sinh viên")


def clear_entries():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_dai_so.delete(0, tk.END)
    entry_tu_duy.delete(0, tk.END)
    entry_tu_tuong.delete(0, tk.END)
    entry_giai_tich.delete(0, tk.END)


def show_scores(event):
    score_text.delete("1.0", tk.END)

    selection = listbox.curselection()
    if not selection:
        return

    index = selection[0]
    student = students[index]

    score_text.insert(tk.END, f"MSSV: {student['id']}\n")
    score_text.insert(tk.END, f"Họ tên: {student['name']}\n\n")

    for mon, diem in student["scores"].items():
        score_text.insert(tk.END, f"{mon}: {diem}\n")

root = tk.Tk()
root.title("Classroom data manager")
root.geometry("750x450")
root.configure(bg="#E8F0FE")

tk.Label(
    root,
    text="CLASSROOM DATA MANAGER",
    font=("Arial", 16, "bold"),
    fg="#1A237E",
    bg="#E8F0FE"
).pack(pady=10)

main_frame = tk.Frame(root, bg="#E8F0FE")
main_frame.pack(fill="both", expand=True, padx=10)

left = tk.Frame(main_frame, bg="white", padx=15, pady=15)
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

tk.Button(
    left,
    text="➕ Thêm sinh viên",
    command=add_student_gui,
    bg="#1A73E8",
    fg="white",
    bd=0,
    pady=5
).pack(fill="x", pady=10)

center = tk.Frame(main_frame, bg="white", padx=10, pady=10)
center.pack(side="left", fill="y")

tk.Label(center, text="Danh sách sinh viên", bg="white").pack()

listbox = tk.Listbox(center, width=30)
listbox.pack(fill="y")
listbox.bind("<<ListboxSelect>>", show_scores)

right = tk.Frame(main_frame, bg="white", padx=15, pady=15)
right.pack(side="right", fill="both", expand=True)

tk.Label(right, text="Bảng điểm", bg="white").pack()

score_text = tk.Text(right)
score_text.pack(fill="both", expand=True)

root.mainloop()