# Welcome to Blockchain Demo
Đây là các bài demo về blockchain
## Bài 1
Đây là bài cơ bản để hiểu blockchain được hình thành như thế nào.
Đầu tiên là khởi tạo một block và in ra giá trị hash của block đó

Sau đó chúng ta sẽ tiến hành tạo chuỗi các block kèm với mã hash của mỗi block, với Genesis Block là block đầu tiên. Còn Genesis Block là gì tự search Google.

Ok vậy là bạn đã hoàn thành bài 1.

## Bài 2
Đến với bài 2 chúng ta sẽ tìm hiểu về cách bảo mật trong blockchain, giả sử ai đó thay đổi mã hash của 1 block nào đó để đánh cắp dữ liệu.
Is valid sẽ tiến hành duyệt và băm lại từng block, nếu block nào thay đổi mã hash thì các block còn lại sẽ thay đổi theo, hệ thống sẽ trả về Is valid: false.
Bây giờ hacker nó khôn hơn, nó vừa thay đổi dữ liệu và nó vừa cập nhật mã hash của dữ liệu bị thay đổi luôn.
Thêm dòng này vào bên dưới dòng **blockchain.chain[1].data = "Anime Girl"** . Sau đó Crtl S và chạy lại

        blockchain.chain[1].hash = hash(blockchain.chain[1]) # Cập nhật lại hash của block bị thay đổi

Và hệ thống nó tự nhận là True luôn?
Vậy bây giờ chúng ta sẽ thêm một điều kiện bên dưới dòng 52.

       if prev_block.hash != current_block.prev_hash:
                return False

Dòng này sẽ tiến hành duyệt lại luôn block trước đó. Cuối cùng hệ thống trả về False.
Đến đây các bạn nghĩ hệ thống chúng ta đã an toàn.
# Đéo nhé

## Bài 3
Bây giờ chúng ta sẽ thêm cơ chế Proof of Work vào. Cơ chế PoW sẽ thêm số nonce vào. Số nonce có thể hiểu đơn giản là **số lần thử** để thỏa mãn điều kiện mã hash.
Ví dụ ở đây chúng ta có vòng lặp while, lặp lại khi nào mã hash có 2 chữ số 0 đầu tiên thì mới đáp ứng được yêu cầu.

Quy luật Hash (data + nonce) = 00

=> hash (data + số 0) = a0x9...(hỏng)

=> hash (data + số 1) = b1x5...(hỏng)

=> hash (data + số 2) = 00x8 (thỏa mãn)

Như vậy số nonce = 3

OK bây giờ bạn thử thay đổi điều kiện **while hash(block).startswith('00')** thành 3 hoặc 4 hoặc 5 số 0 xem số nonce và thời gian có tăng lên không nhé? (Lưu ý càng nhiều số 0 chạy càng lâu, có thể gây nổ máy).

