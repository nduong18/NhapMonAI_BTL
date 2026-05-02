# Bài Tập Lớn: Nhập Môn AI - Mô phỏng Thuật toán DFS Sinh Mê Cung

Đây là kho lưu trữ (Repository) chung chứa toàn bộ Source Code và Tài liệu hướng dẫn cho Bài tập lớn môn Nhập Môn AI của nhóm. 
**Yêu cầu tất cả các thành viên đọc kỹ file README này để nắm rõ tiến độ, cách chạy code và phần việc của mình.**

---

## 1. Cấu trúc thư mục hiện tại
- `maze_logic.py`: Chứa mã nguồn cốt lõi của Thuật toán DFS sinh mê cung. (Đã hoàn thiện)
- `main.py`: Chứa mã nguồn giao diện đồ họa (Pygame) hiển thị hoạt ảnh thuật toán. (Đã hoàn thiện)
- `kich_ban_thuyet_trinh_tong_hop.md`: Kịch bản thuyết trình tổng hợp chi tiết cho tất cả các thành viên. (Đã hoàn thiện)

---

## 2. Hướng dẫn cài đặt và chạy thử Code (Dành cho mọi thành viên)
Để các thành viên làm Báo cáo và Slide có thể lấy tư liệu (chụp ảnh màn hình, quay video), hãy làm theo 2 bước sau để tự chạy code trên máy mình:

**Bước 1: Cài đặt thư viện đồ họa (Chỉ cần làm 1 lần)**
Mở Terminal / Command Prompt và gõ lệnh sau:
```bash
pip install pygame
```

**Bước 2: Chạy chương trình**
Tại thư mục chứa dự án, gõ lệnh:
```bash
python main.py
```
*(Chương trình sẽ hiển thị cửa sổ trực quan hóa. Khi mê cung tạo xong, có thể nhấn phím **SPACE** để tạo lại).*

---

## 3. Bảng Phân Công Công Việc & Tiến Độ (Cập nhật liên tục)

| Vai trò | Tên Thành Viên | Mô tả công việc chi tiết | Deadline | Trạng thái |
| :--- | :--- | :--- | :--- | :--- |
| **Thành viên 1**<br>*(Core Algorithm)* | **Nguyễn Ngọc Hoàng Nam** | - Viết code thuật toán DFS để sinh ma trận mê cung (`maze_logic.py`).<br>- Đảm bảo tính logic, tối ưu hóa thuật toán (Dùng Generator/Yield).<br>- Thuyết trình phần thuật toán. | **02/05** | ✅ **Đã Xong** |
| **Thành viên 2**<br>*(UI/UX & Visualization)* | **Dương** | - Nhận ma trận từ Nam để vẽ lên màn hình (`main.py`).<br>- Làm hiệu ứng animation (hoạt ảnh) để thấy rõ DFS đào tường thế nào.<br>- Thuyết trình phần giao diện. | **03/05** | ✅ **Đã Xong** |
| **Thành viên 3**<br>*(Tài liệu & Báo cáo)* | **Hoàng** | - Tổng hợp phần "Nội dung" và "Báo cáo".<br>- Vẽ lưu đồ thuật toán (Flowchart) dựa trên file `maze_logic.py`.<br>- Gom thành file báo cáo hoàn chỉnh (PDF) theo cấu trúc mẫu. | **04/05** | ⏳ **Đang làm** |
| **Thành viên 4**<br>*(Thuyết trình, Slide)* | **[Điền Tên]** | - Làm Slide chắt lọc ý.<br>- Ghép nối các phần lại với nhau, lên kịch bản trình bày.<br>- Trực tiếp thuyết trình phần mở đầu và kết luận. | **05/05** | ⏳ **Đang làm** |

---

## 4. Ghi chú & Lời khuyên quan trọng cho từng cá nhân

### 📌 Gửi Thành viên 1 (Hoàng Nam - Code Logic)
- Code của bạn ở file `maze_logic.py` đã hoạt động xuất sắc. Việc sử dụng hàm `yield` thay vì `return` là một điểm cộng lớn giúp tối ưu bộ nhớ.
- **Nhiệm vụ tiếp theo:** Bạn hãy chuẩn bị lời giải thích về cách bạn dùng danh sách `stack` để theo dõi quá trình duyệt DFS và cách kiểm tra `visited`. Hãy phối hợp với Hoàng (TV3) để vẽ Flowchart cho đúng với logic code của bạn.

### 📌 Gửi Thành viên 2 (Dương - Code UI/UX)
- Code giao diện `main.py` đã kết nối thành công với logic của Nam để tạo ra Hoạt ảnh.
- **Nhiệm vụ tiếp theo:** Đọc kỹ file `kich_ban_thuyet_trinh_tong_hop.md` để tập luyện trước đoạn thuyết trình của mình. Hãy nhắc các bạn khác đọc kịch bản chung này.

### 📌 Gửi Thành viên 3 (Hoàng - Làm Báo Cáo & Flowchart)
- **Tài nguyên cho bạn:** Bạn hãy mở file `maze_logic.py` lên đọc. Thuật toán hoạt động theo các bước: 
  1. Đưa ô bắt đầu vào mảng (Stack). 
  2. Tìm hàng xóm chưa đi qua. 
  3. Nếu có hàng xóm: Phá tường, đánh dấu đã đi qua, đưa vào Stack. 
  4. Nếu KHÔNG có hàng xóm (Ngõ cụt): Lấy ô hiện tại ra khỏi Stack (Backtrack).
- Hãy dựa vào các bước trên để vẽ **Flowchart (Lưu đồ)**.
- Khi viết báo cáo, nhớ nhấn mạnh việc nhóm sử dụng **Generator trong Python** để tối ưu hóa bộ nhớ cho phần Animation.

### 📌 Gửi Thành viên 4 (Làm Slide & Thuyết Trình Chung)
- **Tài nguyên cho bạn:** Hãy chạy thử code bằng lệnh `python main.py` và dùng phần mềm quay màn hình để chèn một đoạn video / ảnh động (GIF) ngắn vào Slide. Giảng viên sẽ rất thích nhìn hình ảnh thực tế.
- Mở file `kich_ban_thuyet_trinh_tong_hop.md` để lấy kịch bản, chắt lọc các gạch đầu dòng quan trọng để dán lên các trang Slide và phân vai cho các bạn luyện tập.
- Lên lịch để 4 thành viên cùng Call/Gặp mặt chạy thử (Rehearsal) toàn bộ bài báo cáo trước ngày nộp.
