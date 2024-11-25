from ultralytics import YOLO

MODEL_PATH = './yolov11/best.pt'

def detect_objects(image):
    # Load model từ file best.pt
    model = YOLO(MODEL_PATH)

    # Chạy dự đoán trên ảnh
    results = model(image,conf=0.4)

    # Lấy kết quả từ đối tượng đầu tiên (vì YOLO trả về danh sách)
    boxes = results[0].boxes  # Kết quả hộp dự đoán

    output = []
    for box in boxes:
        x1, y1, x2, y2 = box.xyxy[0]  # Tọa độ hộp
        confidence = box.conf[0].item()  # Độ tin cậy
        class_id = int(box.cls[0].item())  # ID của lớp dự đoán
        label = results[0].names[class_id]  # Tên lớp từ ID

        # Thêm thông tin vào danh sách kết quả
        output.append({
            'label': label,
            'confidence': confidence,
            'box': (x1, y1, x2, y2),
            'recycle_info': get_recycle_tip(label)  # Thông tin chi tiết
        })

    return output

def get_recycle_tip(label):
    recycle_tips = {
        'Chai nhựa': {
            'type': 'Rác tái chế',
            'materials': ['Nhựa PET'],
            'tips': 'Dùng chai nhựa làm chậu cây hoặc hệ thống tưới tự động, tạo các món đồ thủ công cho trẻ em như heo đất, hộp bút, đèn lồng, giỏ đựng đồ.'
        },
        'Dép lê': {
            'type': 'Rác khó tái chế',
            'materials': ['Cao su', 'Nhựa tổng hợp'],
            'tips': 'Có thể tái sử dụng làm vật dụng trong nhà (tấm lót nồi, lót chân ghế), làm đồ chơi hoặc đồ trang trí.'
        },
        'Giày': {
            'type': 'Rác tái chế',
            'materials': ['Da', 'Cao su'],
            'tips': 'Sửa chữa để tái sử dụng, tái chế thành đồ dùng như chậu cây mini, túi đựng dụng cụ hoặc bán lại, từ thiện nếu còn tốt.'
        },
        # Thêm các loại rác khác
    }
    return recycle_tips.get(label, {
        'type': 'Không xác định',
        'materials': ['Không xác định'],
        'tips': 'Không có thông tin tái chế.'
    })

