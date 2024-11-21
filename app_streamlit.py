import streamlit as st
import cv2
from PIL import Image, ImageDraw, ImageFont
from yolov11.detect import detect_objects
from io import BytesIO
# Đường dẫn đến phông chữ (lưu ý phải tải và cung cấp đường dẫn đúng)
FONT_PATH = './static/fonts/DejaVuSans.ttf'

# Tạo thanh bên (sidebar)
st.sidebar.title("Menu")
menu_option = st.sidebar.selectbox("Chọn mục", ["Trang chủ", "Thành viên", "Phân loại rác"])

# Hiển thị nội dung tương ứng với lựa chọn trong thanh bên
if menu_option == "Trang chủ":
    st.title("Mô tả dự án")
    st.write("""
    Đây là ứng dụng phân loại rác sử dụng mô hình YOLOv11. Mục tiêu của chúng tôi là giúp người dùng nhận diện các loại rác phổ biến và cung cấp thông tin về cách tái chế mỗi loại.
    1. **Chai nhựa**: Hãy rửa sạch và đem đến điểm tái chế.
    2. **Dép lê**: Thu gom và giao cho cơ sở tái chế cao su.
    3. **Giày**: Tái chế tại các cơ sở chuyên xử lý giày.
    4. **Hộp xốp**: Làm sạch và tái chế tại điểm tiếp nhận xốp.
    ...
    """)

elif menu_option == "Thành viên":
    st.title("Thông tin thành viên")
    
    st.write("""
    Dự án được thực hiện bởi nhóm các thành viên sau:
    """)

    # Chia layout thành 2 cột
    col1, col2 = st.columns([1, 3])

    # Thành viên 1
    with col1:
        # Đọc ảnh từ file hoặc URL và chuyển thành hình tròn
        image_path_1 = "images/member.jpg"  # Đường dẫn ảnh thành viên 1
        image_1 = Image.open(image_path_1)
        
        # Chuyển ảnh thành hình tròn
        image_1 = image_1.resize((150, 150))  # Resize ảnh nếu cần
        image_1_bytes = BytesIO()
        image_1.save(image_1_bytes, format="PNG")
        st.image(image_1_bytes, width=150, use_column_width=False, caption="")

    with col2:
        st.subheader("Nguyễn Văn A")
        st.write("""
        - Vai trò: Lập trình viên, chuyên gia về machine learning.
        - Công việc chính: Xây dựng mô hình YOLO và huấn luyện mô hình nhận diện rác.
        """)

    # Thành viên 2
    with col1:
        # Đọc ảnh từ file hoặc URL và chuyển thành hình tròn
        image_path_2 = "images/member.jpg"  # Đường dẫn ảnh thành viên 2
        image_2 = Image.open(image_path_2)
        
        # Chuyển ảnh thành hình tròn
        image_2 = image_2.resize((150, 150))  # Resize ảnh nếu cần
        image_2_bytes = BytesIO()
        image_2.save(image_2_bytes, format="PNG")
        st.image(image_2_bytes, width=150, use_column_width=False, caption="")

    with col2:
        st.subheader("Trần Thị B")
        st.write("""
        - Vai trò: Quản lý dự án, thiết kế giao diện người dùng.
        - Công việc chính: Thiết kế giao diện ứng dụng và quản lý tiến độ dự án.
        """)

    # Thành viên 3
    with col1:
        # Đọc ảnh từ file hoặc URL và chuyển thành hình tròn
        image_path_3 = "images/member.jpg"  # Đường dẫn ảnh thành viên 3
        image_3 = Image.open(image_path_3)
        
        # Chuyển ảnh thành hình tròn
        image_3 = image_3.resize((150, 150))  # Resize ảnh nếu cần
        image_3_bytes = BytesIO()
        image_3.save(image_3_bytes, format="PNG")
        st.image(image_3_bytes, width=150, use_column_width=False, caption="")

    with col2:
        st.subheader("Lê Thị C")
        st.write("""
        - Vai trò: Nghiên cứu và phát triển, chuyên gia về phân loại rác.
        - Công việc chính: Nghiên cứu các phương pháp phân loại rác hiệu quả và cập nhật cơ sở dữ liệu.
        """)

elif menu_option == "Phân loại rác":
    st.title("Phân Loại Rác với YOLOv11")
    st.write("""
    Đây là ứng dụng phân loại rác sử dụng mô hình YOLOv11. Bạn có thể tải lên một bức ảnh hoặc sử dụng camera để nhận diện rác!
    """)

    # Chọn giữa việc upload ảnh hoặc sử dụng camera
    input_option = st.radio("Chọn cách nhận diện", ("Tải ảnh lên", "Dùng Camera"))

    if input_option == "Tải ảnh lên":
        uploaded_file = st.file_uploader("Chọn một bức ảnh để phân loại", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            # Đọc ảnh từ file tải lên
            image = Image.open(uploaded_file)
            
            # Phân loại rác từ ảnh đã upload
            results = detect_objects(image)
            
            # Tạo đối tượng vẽ và chỉ định phông chữ
            draw = ImageDraw.Draw(image)
            try:
                font = ImageFont.truetype(FONT_PATH, 20)  # Chọn kích thước phông chữ
            except IOError:
                font = ImageFont.load_default()  # Sử dụng phông chữ mặc định nếu không tìm thấy phông chữ

            # Vẽ bounding boxes lên ảnh
            for result in results:
                label = result['label']
                confidence = result['confidence']
                x1, y1, x2, y2 = result['box']
                draw.rectangle([x1, y1, x2, y2], outline="red", width=3)
                draw.text((x1, y1), label, font=font, fill="red")

            # Hiển thị ảnh với bounding box
            st.image(image, caption="Ảnh đã phân loại", use_column_width=True)

            # Hiển thị kết quả phân loại
            st.subheader("Danh sách các đối tượng được nhận diện:")
            for result in results:
                st.write(f"**{result['label']}** - Độ tin cậy: {result['confidence']*100:.2f}%")
                st.write(f"**Lời khuyên tái chế:** {result['recycle_tip']}")

    elif input_option == "Dùng Camera":
        # Khởi động camera
        cap = cv2.VideoCapture(0)

        # Kiểm tra nếu webcam không mở được
        if not cap.isOpened():
            st.error("Không thể truy cập camera.")
            st.stop()

        # Hiển thị video feed trong Streamlit
        stframe = st.empty()

        # Hiển thị và lấy ảnh khi người dùng nhấn nút "Chụp ảnh"
        capture_button = st.button("Chụp ảnh")

        image_taken = False
        processed_image = None

        while True:
            ret, frame = cap.read()
            if not ret:
                st.error("Không thể lấy video từ webcam.")
                break

            # Chuyển đổi từ BGR (OpenCV) sang RGB (Streamlit)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb)

            # Hiển thị video trực tiếp trong Streamlit
            if not image_taken:  # Chỉ hiển thị video feed nếu chưa chụp ảnh
                stframe.image(img, channels="RGB", use_column_width=True)

            if capture_button and not image_taken:
                # Khi nhấn nút, xử lý ảnh đã chụp
                processed_image = img
                results = detect_objects(processed_image)

                # Tạo đối tượng vẽ và chỉ định phông chữ
                draw = ImageDraw.Draw(processed_image)
                try:
                    font = ImageFont.truetype(FONT_PATH, 20)
                except IOError:
                    font = ImageFont.load_default()

                # Vẽ bounding boxes lên ảnh
                for result in results:
                    label = result['label']
                    confidence = result['confidence']
                    x1, y1, x2, y2 = result['box']
                    draw.rectangle([x1, y1, x2, y2], outline="red", width=3)
                    draw.text((x1, y1), label, font=font, fill="red")

                # Đánh dấu là đã có ảnh đã chụp
                image_taken = True

                # Dừng vòng lặp sau khi ảnh đã chụp
                break

        # Hiển thị ảnh đã xử lý sau khi nhấn nút "Chụp ảnh"
        if image_taken:
            st.image(processed_image, caption="Ảnh đã phân loại", use_column_width=True)

            # Hiển thị kết quả phân loại
            st.subheader("Danh sách các đối tượng được nhận diện:")
            for result in results:
                st.write(f"**{result['label']}** - Độ tin cậy: {result['confidence']*100:.2f}%")
                st.write(f"**Lời khuyên tái chế:** {result['recycle_tip']}")

        # Giải phóng tài nguyên webcam sau khi hoàn thành
        cap.release()
