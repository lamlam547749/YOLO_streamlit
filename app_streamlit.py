import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from yolov11.detect import detect_objects
from io import BytesIO
from streamlit_option_menu import option_menu
# Đường dẫn đến phông chữ (lưu ý phải tải và cung cấp đường dẫn đúng)
FONT_PATH = './static/fonts/DejaVuSans.ttf'

with st.sidebar:
    st.image("images/member.jpg", width=300)  # Đặt đường dẫn đến hình ảnh của bạn tại đây

    # Tạo menu chọn mục
    menu_option = option_menu(
        menu_title=None,  # Không dùng tiêu đề mặc định
        options=['Trang chủ', 'Thành viên', 'Phân loại rác'],
        icons=['house', 'people', 'camera'],
        menu_icon="cast",
    )
# menu_option = st.sidebar.selectbox("Chọn mục", ["Trang chủ", "Thành viên", "Phân loại rác"])
st.markdown("""
<style>
    .header {
        color: #ff6347;
        font-size: 36px;
        text-align: center;
        font-weight: bold;
    }
    .subheader {
        color: #4682b4;
        font-size: 28px;
        font-weight: 600;
    }
    .container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px;
    }
    .container img {
        border-radius: 50%;
        border: 5px solid #ff6347;
    }
    .content {
        padding: 10px;
        font-size: 16px;
        color: #333;
        background-color: #f9f9f9;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)
# Hiển thị nội dung tương ứng với lựa chọn trong thanh bên
if menu_option == "Trang chủ":
    # Title for "Trang chủ"
    st.markdown('<div class="header">Mô tả Dự Án</div>', unsafe_allow_html=True)
    st.write("""
    Đây là ứng dụng phân loại rác sử dụng mô hình YOLOv11. Mục tiêu của chúng tôi là giúp người dùng nhận diện các loại rác phổ biến và cung cấp thông tin về cách tái chế mỗi loại.
    """)

elif menu_option == "Thành viên":
    # Tiêu đề cho phần thành viên
    st.markdown('<div class="subheader">Thông tin thành viên</div>', unsafe_allow_html=True)

    # Layout cho các thành viên
    col1, col2 = st.columns([1, 3])

    # Thành viên 1
    with col1:
        image_path = "images/member.jpg"  # Đường dẫn ảnh thành viên
        image = Image.open(image_path)
        image = image.resize((150, 150))  # Resize ảnh nếu cần
        st.image(image, width=150, caption="", use_container_width =False)

    with col2:
        st.subheader("Nguyễn Văn A")
        st.write("""
        - Vai trò: Lập trình viên, chuyên gia về machine learning.
        - Công việc chính: Xây dựng mô hình YOLO và huấn luyện mô hình nhận diện rác.
        """)

    # Thành viên 2
    with col1:
        image_path = "images/member.jpg"  # Đường dẫn ảnh thành viên
        image = Image.open(image_path)
        image = image.resize((150, 150))  # Resize ảnh nếu cần
        st.image(image, width=150, caption="", use_container_width =False)

    with col2:
        st.subheader("Nguyễn Văn B")
        st.write("""
        - Vai trò: Lập trình viên, chuyên gia về machine learning.
        - Công việc chính: Xây dựng mô hình YOLO và huấn luyện mô hình nhận diện rác.
        """)

    # Thành viên 3
    with col1:
        image_path = "images/member.jpg"  # Đường dẫn ảnh thành viên
        image = Image.open(image_path)
        image = image.resize((150, 150))  # Resize ảnh nếu cần
        st.image(image, width=150, caption="", use_container_width =False)

    with col2:
        st.subheader("Nguyễn Văn C")
        st.write("""
        - Vai trò: Lập trình viên, chuyên gia về machine learning.
        - Công việc chính: Xây dựng mô hình YOLO và huấn luyện mô hình nhận diện rác.
        """)

elif menu_option == "Phân loại rác":
    # Thêm CSS để tạo hiệu ứng hover cho nút
    st.markdown("""
    <style>
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="subheader">Phân loại rác với YOLOv11</div>', unsafe_allow_html=True)
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
                draw.text((x1, y1), label, font=font, fill="blue")

            # Hiển thị ảnh với bounding box
            st.image(image, caption="", use_container_width =True)

            # Hiển thị kết quả phân loại
            st.markdown('<div class="content">Danh sách các đối tượng được nhận diện:</div>', unsafe_allow_html=True)
            for result in results:
                label = result['label']
                confidence = result['confidence']
                recycle_info = result['recycle_info']

                # Định dạng hiển thị thông tin
                st.write(f"""
                **{label}** (**{recycle_info['type']}**): {', '.join(recycle_info['materials'])}.
                
                **Cách tái chế tại nhà**: {recycle_info['tips']}
                """)

    elif input_option == "Dùng Camera":
        # Sử dụng st.camera_input để lấy hình ảnh từ camera
        image = st.camera_input("Chụp ảnh từ camera")

        if image is not None:
            # Khi có hình ảnh từ camera, xử lý ảnh đã chụp
            processed_image = Image.open(image)
            results = detect_objects(processed_image)

            # Tạo đối tượng vẽ và chỉ định phông chữ
            draw = ImageDraw.Draw(processed_image)
            try:
                font = ImageFont.truetype(FONT_PATH, 20)  # Tăng kích thước phông chữ lên 40
            except IOError:
                font = ImageFont.load_default()

            # Vẽ bounding boxes lên ảnh
            for result in results:
                label = result['label']
                confidence = result['confidence']
                x1, y1, x2, y2 = result['box']
                draw.rectangle([x1, y1, x2, y2], outline="red", width=3)
                draw.text((x1, y1), label, font=font, fill="blue")

            # Hiển thị ảnh đã xử lý
            st.image(processed_image, caption="", use_container_width =True)

            # Hiển thị kết quả phân loại
            st.markdown('<div class="content">Danh sách các đối tượng được nhận diện:</div>', unsafe_allow_html=True)
            for result in results:
                label = result['label']
                confidence = result['confidence']
                recycle_info = result['recycle_info']

                # Định dạng hiển thị thông tin
                st.write(f"""
                **{label}** (**{recycle_info['type']}**): {', '.join(recycle_info['materials'])}.
                
                **Cách tái chế tại nhà**: {recycle_info['tips']}
                """)