import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from yolov11.detect import detect_objects
from io import BytesIO
from streamlit_option_menu import option_menu
# Đường dẫn đến phông chữ (lưu ý phải tải và cung cấp đường dẫn đúng)
FONT_PATH = './static/fonts/DejaVuSans.ttf'

with st.sidebar:
    st.image("images/Logo.png", width=300)  # Đặt đường dẫn đến hình ảnh của bạn tại đây

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
    st.markdown('<div class="header">Giới thiệu dự án</div>', unsafe_allow_html=True)
    st.write("""
    **Tên dự án:** EnRonC  

              
    **Mục đích:** Phân loại rác và giáo dục, cung cấp thông tin về rác thải nhằm nâng cao nhận thức về môi trường.  

             
    **Đối tượng sử dụng:**  
    - Tất cả những người quan tâm tới môi trường.  
             
    - Những người muốn tìm hiểu thêm kiến thức hoặc cải thiện lối sống xanh.  

             
    **Tính năng chính:**  
    - Cung cấp thông tin về các loại rác và tính chất của chúng (được chia thành rác tái chế được và không tái chế được).  
             
    - Gợi ý ý tưởng tái chế để đưa rác vào sử dụng lại trong đời sống.  
             
    - Nhận diện và phân biệt loại rác qua hình ảnh hoặc camera, giúp người dùng xử lý đúng cách.  

             
    **Ứng dụng thực tế:**  
    - Hỗ trợ trong đời sống hàng ngày, đặc biệt đối với rác thải sinh hoạt.  
             
    - Góp phần nâng cao ý thức về môi trường, hướng tới lối sống xanh và tiến đến môi trường bền vững.  
    """)

elif menu_option == "Thành viên":
    # Tiêu đề cho phần thành viên
    st.markdown('<div class="subheader">Thông tin thành viên</div>', unsafe_allow_html=True)

    # Layout cho các thành viên
    col1, col2 = st.columns([1, 3])

    # Thành viên 1
    with col1:
        image_path = "images/leader_resized.jpg"  # Đường dẫn ảnh thành viên
        image = Image.open(image_path)
        image = image.resize((150, 150))  # Resize ảnh nếu cần
        st.image(image,width=150, caption="", use_container_width =False)

    with col2:
        st.subheader("Nguyễn Lê Trung Nghĩa - 10A1")
        st.write("""
        - Vai trò: Nhóm trưởng, Lập trình viên chính
        - Công việc chính: Quản lý dự án, thiết kế và triển khai mô hình để phân loại rác.
        """)

    # Thành viên 2
    with col1:
        image_path = "images/member1_resized.jpg"  # Đường dẫn ảnh thành viên
        image = Image.open(image_path)
        image = image.resize((150, 150))  # Resize ảnh nếu cần
        st.image(image, width=150, caption="", use_container_width =False)

    with col2:
        st.subheader("Lê Mai Khánh Chi - 11A4")
        st.write("""
        - Vai trò: Thành viên
        - Công việc chính: Nghiên cứu thị trường, thu thập dữ liệu để đảm bảo mô hình phân loại rác có tính ứng dụng cao.
        """)

    # Thành viên 3
    with col1:
        image_path = "images/member2_resized.jpg"  # Đường dẫn ảnh thành viên
        image = Image.open(image_path)
        image = image.resize((150, 150))  # Resize ảnh nếu cần
        st.image(image, width=150, caption="", use_container_width =False)

    with col2:
        st.subheader("Châu Bảo Quyên - 12A7")
        st.write("""
        - Vai trò: Thành viên
        - Công việc chính: Hỗ trợ thu thập dữ liệu và đóng góp vào việc phát triển hệ thống.
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
    
    st.markdown('<div class="subheader">Phân loại rác với EnRonC</div>', unsafe_allow_html=True)
    st.write("""
    **Chào mừng bạn đến với tính năng Phân loại rác của EnRonC!**  
    - **Nhận diện rác qua ảnh**: Tải lên hình ảnh để phân loại các loại rác thải.  
    - **Sử dụng camera**: Chụp ảnh trực tiếp từ thiết bị của bạn để phân biệt loại rác.  
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
                confidence = round(result['confidence'],3)
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
                confidence = round(result['confidence'],3)
                recycle_info = result['recycle_info']

                # Định dạng hiển thị thông tin
                st.write(f"""
                **{label}** (**{recycle_info['type']}**): {', '.join(recycle_info['materials'])}.
                
                **Cách tái chế tại nhà**: {recycle_info['tips']}
                """)