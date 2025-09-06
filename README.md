# Welcome to Blockchain Demo
Đây là các bài demo về blockchain
### Bài 1
Đây là bài cơ bản để hiểu blockchain được hình thành như thế nào.
Đầu tiên là khởi tạo một block và in ra giá trị hash của block đó

    # Khởi tạo một block mới với dữ liệu
    block = Block("Huynh Hoang Long")
    # In ra giá trị hash của block
    print(hash(block))
