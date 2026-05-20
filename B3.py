#Input: Mã nhân viên, Họ và tên, Phòng ban (kiểu chuỗi).
#Output: Phiếu Hồ sơ Điện tử hoặc Dòng cảnh báo lỗi.
#Vòng lặp: Dùng vòng lặp for để chạy đúng 3 lần.
#Xử lý bẫy dữ liệu: Sử dụng hàm .strip() để xóa khoảng trắng thừa. Khi đó, cả việc bỏ trống (nhấn Enter) 
#hay nhập toàn dấu cách đều sẽ biến thành chuỗi rỗng "".
#Điều kiện: Dùng cấu trúc if-else. Nếu Mã hoặc Tên là chuỗi rỗng thì chặn lại và in cảnh báo. Nếu hợp lệ thì cho phép in hồ sơ.
#Bắt đầu vòng lặp 3 lần ➔ Nhập 3 thông tin ➔ Làm sạch dữ liệu bằng .strip() ➔ Kiểm tra rỗng ➔ Rẽ nhánh (Báo lỗi hoặc In phiếu hồ sơ).

print("--- KIOSK NHAP LIEU NHAN SU SO ---")

for i in range(1, 4):
    print(f"\n--- Nhan vien {i} ---")
    
    employee_id = input("Ma nhan vien: ")
    full_name = input("Ho va ten: ")
    department = input("Phong ban: ")
    
    if not employee_id or not full_name:
        print("[CANH BAO] Du lieu ten hoac ma khong hop le! Huy bo tao ho so cho nhan vien nay.")
    else:
        print("---------PHIEU HO SO DIEN TU---------")
        print(f"Ma nhan vien : {employee_id}")
        print(f"Ho va ten    : {full_name}")
        print(f"Phong ban    : {department}")
        print("--------------------------------------")

print("\nQuy trinh nhap lieu da hoan thanh!")