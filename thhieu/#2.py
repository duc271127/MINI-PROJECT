def search_by_id(students):
    search_id=int(input("Nhập mã sinh viên cần tìm: "))
    found = False
    for student in students:
        if student["id"]==search_id:
            print("=== Thông tin sinh viên ===")
            print("ID:",student["id"])
            print("Họ và tên:",student["name"])
            print("Điểm: ")
            for môn,điểm in student["scores"].items():
                print(f"{môn}: {điểm}")
            found=True
            break
    if not found:
        print(f"Không tìm thấy sinh viên có mã sinh viên: {search_id}")
def display_all_students(students):
    for student in students:
        print("=======================")
        print("ID:", student["id"])
        print("Họ và tên:", student["name"])
        print("Điểm:")
        for môn,điểm in student["scores"].items():
            print(f"{môn}: {điểm}")
students = [
    {
        'id': 25021735,
        'name': 'Nguyễn Trọng Đức',
        'scores': {
            'Đại số tuyến tính': 10.0,
            'Tư duy tính toán': 10.0,
            'Tư tưởng Hồ Chí Minh': 10.0
        }
    },
    {
        'id': 90,
        'name': 'duck',
        'scores': {
            'Đại số tuyến tính': 9.0,
            'Tư duy tính toán': 9.0,
            'Tư tưởng Hồ Chí Minh': 9.0,
            'Giải tích 1': 9.0
        }
    }
]
display_all_students(students)



    

        
