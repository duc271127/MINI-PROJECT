def checklist(l1st,id_student):
    for x in l1st:
        if x["id"]==id_student:
            return True
        return False

def add_student(students):
    try:
        id=int(input("Nhập mã số sinh viên "))
    except ValueError:
        print("Vui lòng nhập mã số sinh viên hợp lệ ")

    
    if checklist(students,id):
        print("ID đã tồn tại trên hệ thống ")
        return

    try:
        name=input("Nhập họ tên sinh viên ")
    except ValueError:
        print("Vui lòng nhập họ tên sinh viên hợp lệ ")
    
    try:
        scores={}
        scores["Đại số tuyến tính"]=float(input("Nhập điểm số môn Đại số tuyến tính "))
        scores["Tư duy tính toán"]=float(input("Nhập điểm số môn Tư duy tính toán "))
        scores["Tư tưởng Hồ Chí Minh"]=float(input("Nhập điểm số môn Tư tưởng Hồ Chí Minh "))
        scores["Giải tích 1"]=float(input("Nhập điểm số môn Giải tích 1 "))
    except ValueError:
        print("Vui lòng nhập điểm số hợp lệ")

    student={
        "id":id,
        "name":name,
        "scores":scores
    }
    students.append(student)
    print("Đã thêm sinh viên thành công")

students = []

add_student(students)
add_student(students)

print(students)
