import hashlib  # Thư viện dùng để băm dữ liệu

# Định nghĩa class Block
class Block:
    def __init__(self, data):
        self.data = data  # Dữ liệu trong block
        self.prev_hash = "" # Mã băm của block trước (ban đầu rỗng)
        self.hash = ""    # Mã băm của block (ban đầu rỗng)

# Hàm tính hash của block
def hash(block):
    data = block.data + block.prev_hash                # Lấy dữ liệu từ block
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

        self.chain.append(block) # Thêm block vào chuỗi

    # Hàm in toàn bộ blockchain
    def print(self):
        for block in self.chain:
            print("Data:", block.data)
            print("Previous Hash:", block.prev_hash)
            print("Hash:", block.hash)
            print("----------------")

# Chạy thử
blockchain = Blockchain()
blockchain.add_block("Huynh Hoang Long")
blockchain.add_block("Bui Hoang Viet")
blockchain.add_block("Bui Chi Bao")
blockchain.add_block("Pham Tran Nhat Minh")
blockchain.add_block("Ferb")

blockchain.print()