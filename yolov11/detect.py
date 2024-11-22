from ultralytics import YOLO

MODEL_PATH = './yolov11/yolo11n.pt'

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
            'box': (x1, y1, x2, y2),  # Tọa độ bounding box
            'recycle_tip': get_recycle_tip(label)  # Gợi ý tái chế
        })

    return output

def get_recycle_tip(label):
    recycle_tips = {
        'Chai nhựa': 'Hãy rửa sạch và đem đến điểm tái chế.',
        'Dép lê': 'Thu gom và giao cho cơ sở tái chế cao su.',
        'Giày': 'Tái chế tại các cơ sở chuyên xử lý giày.',
        'Hộp xốp': 'Làm sạch và tái chế tại điểm tiếp nhận xốp.',
        'Ly Nhựa': 'Rửa sạch và tái chế.',
        'Nắp nhựa': 'Gỡ ra và thu gom tại điểm tái chế nhựa.',
        'Ống hút nhựa': 'Thu gom vào túi nhựa tái chế.',
        'Khăn giấy': 'Sử dụng làm phân xanh hoặc đốt cháy.',
        'Nắp chai': 'Thu gom và đưa đến nơi tái chế kim loại.',
        'Nhãn chai nước': 'Bóc ra và phân loại theo nhựa.',
        'Que kem': 'Có thể tái sử dụng hoặc làm đồ trang trí.',
        'Vỏ kẹo': 'Phân loại vào túi tái chế tổng hợp.',
        'Bao kem': 'Đưa đến điểm tái chế túi nylon.',
        'Tái chế': 'AAA',
        'person': 'Con nguoi'
    }
    return recycle_tips.get(label, 'Không có thông tin tái chế.')
