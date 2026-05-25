def nhap_thong_tin_benh_nhan():
    print("--- HỆ THỐNG TIẾP NHẬN BỆNH NHÂN ---")
    
    # Thu thập dữ liệu
    ho_ten = input("Nhập họ và tên bệnh nhân: ").strip()
    ma_ba = input("Nhập mã bệnh án (ví dụ BN1024): ").strip()
    khoa_kham = input("Nhập khoa/phòng khám chỉ định: ").strip()
    
    # Hiển thị Phiếu khám bệnh điện tử
    print("\n" + "="*30)
    print("PHIẾU KHÁM BỆNH ĐIỆN TỬ")
    print(f"Bệnh nhân: {ho_ten} - Mã BA: {ma_ba} - Chuyển tới: {khoa_kham}")
    print("="*30)

# Chạy chương trình
if __name__ == "__main__":
    nhap_thong_tin_benh_nhan()
    

#     Input (Đầu vào): 3 trường dữ liệu dạng chuỗi (str):

# name: Tên bệnh nhân.

# id: Mã bệnh án.

# department: Khoa/Phòng khám.

# Output (Đầu ra): Một chuỗi được định dạng theo mẫu: Bệnh nhân: [Họ tên] - Mã BA: [Mã bệnh án] - Chuyển tới: [Khoa/Phòng khám]

# Giải pháp: Sử dụng hàm input() để thu thập dữ liệu và f-string (trong Python) để định dạng chuỗi xuất ra một cách sạch sẽ và hiệu quả.

# Thuật toán (Mã giả):

# Khởi tạo các biến để lưu thông tin từ người dùng (nhân viên lễ tân).

# Sử dụng câu lệnh input() kèm hướng dẫn rõ ràng.

# Lấy dữ liệu nhập vào và lưu trữ vào các biến tương ứng.

# Sử dụng template để in thông báo xác nhận theo đúng chuẩn phòng khám.