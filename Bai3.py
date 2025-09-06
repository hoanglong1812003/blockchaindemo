from datetime import datetime, timedelta    # Thư viện dùng để lấy thời gian hiện tại
import hashlib  # Thư viện dùng để băm dữ liệu

# Định nghĩa class Block
class Block:
    def __init__(self, data):
        self.data = data  # Dữ liệu trong block
        self.prev_hash = "" # Mã băm của block trước (ban đầu rỗng)
        self.nonce  = 0  # Giá trị nonce để điều chỉnh độ khó
        self.hash = ""    # Mã băm của block (ban đầu rỗng)
        self.total_time = "" # Thời gian tạo block

# Hàm tính hash của block
def hash(block):
    data = block.data + block.prev_hash + str(block.nonce) # Lấy dữ liệu từ block
    data = data.encode('utf-8')      # Chuyển dữ liệu sang dạng bytes
    return hashlib.sha256(data).hexdigest()  # Băm dữ liệu bằng SHA-256


# Lớp Blockchain (chuỗi các block)
class Blockchain:
    def __init__(self):
        self.chain = []  # Danh sách các block trong blockchain

        # Tạo block đầu tiên (Genesis Block)
        block = Block("Genesis Block")
        block.hash = hash(block)
        self.chain.append(block)

    # Hàm thêm block mới
    def add_block(self, data):
        block = Block(data)      # Tạo block mới
        block.prev_hash = self.chain[-1].hash # Lấy mã băm của block trước
        block.hash = hash(block) # Gán giá trị hash
        start = datetime.now()
        while hash(block).startswith('000') == False: # Yêu cầu hash phải bắt đầu bằng 2 số 0
            block.nonce = block.nonce + 1
        block.hash = hash(block) # Gán giá trị hash
        end = datetime.now()
        block.total_time = str(end - start)

        self.chain.append(block) # Thêm block vào chuỗi

    # Hàm in toàn bộ blockchain
    def print(self):
        for block in self.chain:
            print("----------------")
            print("Data:", block.data)
            print("Previous Hash:", block.prev_hash)
            print("Hash:", block.hash)
            print("Nonce:", block.nonce)
            print("Total time:", block.total_time)
            print("----------------")

    # Kiểm tra tính hợp lệ của toàn bộ blockchain 
    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i] # Block hiện tại
            prev_block = self.chain[i-1] # Block trước đó

            # Nếu dữ liệu block đã bị thay đổi thì hash sẽ không khớp
            if hash(current_block) != current_block.hash:
                return False
            if prev_block.hash != current_block.prev_hash:
                return False
        return True

# Khởi tạo blockchain
blockchain = Blockchain()
blockchain.add_block("Huỳnh Hoàng Long")
blockchain.add_block("Bùi Hoàng Việt")
blockchain.add_block("Bùi Chí Bảo")
blockchain.add_block("Phạm Trần Nhật Minh")
blockchain.add_block("Ferb")


# Kiểm tra lại toàn bộ blockchain
print("Is valid?:", blockchain.is_valid())
blockchain.print()