# KỊCH BẢN THUYẾT TRÌNH TỔNG HỢP (TOÀN NHÓM)
**Đề tài:** Mô phỏng thuật toán sinh mê cung bằng thuật toán tìm kiếm DFS (Depth-First Search)

*Tài liệu này là kịch bản chi tiết cho buổi báo cáo. Các thành viên bám sát trình tự dưới đây để đảm bảo bài thuyết trình trôi chảy, không bị vấp hoặc giẫm chân lên nhau.*

---

## PHẦN 1: MỞ ĐẦU (Người nói: Thành viên 4)
*📌 Nhiệm vụ: Thu hút sự chú ý, giới thiệu đề tài và định hướng buổi thuyết trình.*

**Thành viên 4:** 
"Dạ em chào Thầy/Cô và các bạn. Hôm nay, nhóm chúng em xin phép trình bày Bài tập lớn môn Nhập Môn AI với đề tài: **'Mô phỏng thuật toán sinh mê cung bằng phương pháp Depth-First Search (DFS) kết hợp Backtracking'**.

Về lý do chọn đề tài: Các thuật toán tìm kiếm thường khá trừu tượng và khô khan nếu chỉ nhìn vào code. Vì vậy, nhóm em không chỉ viết thuật toán trên Console, mà còn tập trung xây dựng một hệ thống Giao diện (UI) để **trực quan hóa từng bước đi (Animation)**, giúp người xem thấy được cách AI tư duy, đào tường và quay lui như thế nào.

Để đạt được mục tiêu này, nhóm chúng em chia làm 2 mảng chính:
1. Mảng Logic & Thuật toán cốt lõi.
2. Mảng Giao diện đồ họa (UI/UX).

Sau đây, em xin nhường lời cho bạn **Nguyễn Ngọc Hoàng Nam** trình bày về phần cốt lõi của bài toán là thuật toán DFS."

---

## PHẦN 2: THUẬT TOÁN CỐT LÕI DFS (Người nói: Thành viên 1 - Nam)
*📌 Nhiệm vụ: Trình bày logic thuật toán, cơ chế Stack và lý do dùng `yield`.*

**Nam:**
"Cảm ơn [Tên TV4]. Em là Nam, phụ trách phần thuật toán sinh mê cung. 
Ý tưởng cốt lõi của việc tạo mê cung thực chất là đi phá các bức tường. Em thiết kế mỗi ô (Cell) sẽ có 4 bức tường (Trên, Phải, Dưới, Trái). 

Thuật toán DFS hoạt động theo 3 bước chính:
- **Tiến lên (Khám phá):** Đầu dò đứng ở ô hiện tại, tìm các ô hàng xóm chưa từng đi qua. Nếu có, nó chọn ngẫu nhiên 1 ô, **phá bức tường** giữa 2 ô, và tiến sang đó.
- **Lưu vết (Stack):** Mỗi lần tiến lên, em lưu vị trí đó vào một danh sách tên là `stack`. Việc này nhằm mục đích để nhớ đường về.
- **Quay lui (Backtracking):** Khi đầu dò đi vào ngõ cụt (xung quanh đều là ô đã đi qua), nó sẽ lấy phần tử cuối cùng trong `stack` ra để lùi lại (Pop), cho đến khi tìm thấy ngã rẽ mới.

*(Nhấn mạnh ý này để lấy điểm cao)*
Đặc biệt, để kết hợp với phần giao diện của bạn Dương, em KHÔNG dùng vòng lặp chạy một mạch đến cuối rồi `return` kết quả. Thay vào đó, em dùng kỹ thuật **Generator (từ khóa `yield` trong Python)**. Cứ mỗi lần tiến lên hoặc lùi lại, thuật toán sẽ 'nhả' tọa độ đó ra ngoài rồi tạm dừng, chờ giao diện gọi mới chạy tiếp. Điều này giúp tối ưu 100% dung lượng RAM vì hệ thống không cần tạo mảng để lưu lại toàn bộ lịch sử di chuyển.

Tiếp theo, bạn **Dương** sẽ trình bày về cách Giao diện tiếp nhận dữ liệu này để tạo ra Animation."

---

## PHẦN 3: GIAO DIỆN VÀ TRỰC QUAN HÓA (Người nói: Thành viên 2 - Dương)
*📌 Nhiệm vụ: Báo cáo cách Pygame hoạt động, phối hợp Generator và hiển thị trạng thái.*

**Dương:**
"Chào Thầy/Cô, em là Dương. Để hứng toàn bộ logic từ thuật toán của bạn Nam, em sử dụng thư viện đồ họa **Pygame**. 

Điểm sáng nhất của phần giao diện nằm ở sự đồng bộ hóa. Do thuật toán của bạn Nam viết dưới dạng Generator (`yield`), em đặt nó vào vòng lặp vô tận của game (Game Loop - chạy 30 FPS). Mỗi khung hình, giao diện sẽ dùng hàm `next()` để xin đúng **1 tọa độ**, sau đó ngay lập tức cập nhật lên màn hình. Nhờ vậy chúng ta mới thấy được chuyển động mượt mà như xem video.

Để mô phỏng rõ cách tư duy của DFS, em đã thiết kế một hệ thống **Bảng màu (Color Palette)** riêng:
- **Màu Đỏ:** Là vị trí đầu dò (Head) đang đứng hiện tại, báo hiệu đang đào tường.
- **Màu Xanh nhạt:** Là các ô đã được đi qua.
- **Màu Xanh đậm:** Đây là màu quan trọng nhất! Khi hàm DFS báo hiệu hết đường (`next_cell = None`), giao diện hiểu là thuật toán đang **Quay lui**. Lập tức hệ thống đổi màu nhánh đó sang xanh đậm để đánh dấu ngõ cụt. Việc này giúp Thầy/Cô quan sát thấy cực kỳ rõ quá trình Backtracking.

Sau khi sinh xong mê cung 100%, người dùng có thể nhấn phím **SPACE** để tạo lại một mô hình mới.
Sau đây em xin nhường lời lại cho bạn [Tên TV4] tổng kết lại bài báo cáo."

---

## PHẦN 4: KẾT LUẬN & ĐỊNH HƯỚNG TƯƠNG LAI (Người nói: Thành viên 4)
*📌 Nhiệm vụ: Chốt lại kết quả đạt được, thiếu sót (nếu có) và lời cảm ơn.*

**Thành viên 4:**
"Cảm ơn Dương. Như Thầy/Cô đã thấy qua bản Demo và bài thuyết trình, nhóm chúng em đã hoàn thành được mục tiêu đề ra là: Vận dụng trơn tru thuật toán DFS và tạo ra một giao diện trực quan, tối ưu hóa rất tốt về mặt tài nguyên hệ thống (RAM). (Cảm ơn bạn **Hoàng** đã hỗ trợ đắc lực trong việc làm Slide và xuất bản bộ Báo cáo/Flowchart hoàn chỉnh gửi Thầy/Cô).

Tất nhiên, sản phẩm vẫn có thể phát triển thêm, ví dụ như:
- Tích hợp thêm thuật toán tìm đường (như A* hoặc BFS) để tự động giải quyết cái mê cung vừa tạo ra.
- Cho phép người dùng tùy chỉnh kích thước lưới ngay trên giao diện.

Bài thuyết trình của nhóm đến đây là kết thúc. Chúng em rất mong nhận được những góp ý, chỉ bảo của Thầy/Cô để nhóm tiếp tục hoàn thiện ạ. Em xin cảm ơn!" 
*(Cả nhóm cúi chào)*

---
> **Lời khuyên chung cho lúc báo cáo:**
> 1. Khi một bạn đang nói, bạn bấm Slide hãy chú ý nhấn chuyển trang cho khớp nhịp.
> 2. Lúc Dương và Nam nói về `yield` và Animation, nên có một cái Video/Ảnh GIF chạy trực tiếp trên Slide để minh họa ngay cạnh. Mắt thấy tai nghe sẽ thuyết phục tuyệt đối.
