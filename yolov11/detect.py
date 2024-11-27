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
            'materials': ['Thường được làm từ các loại nhựa phổ biến như PET, HDPE, PP, …'],
            'tips': 'Dùng chai nhựa làm chậu cây hoặc hệ thống tưới tự động, tạo các món đồ thủ công cho trẻ em như heo đất, hộp bút, cắt chai nhựa để làm đèn lồng, giỏ đựng đồ.'
        },
        'Dép': {
            'type': 'Rác tái chế',
            'materials': ['Thường làm bằng nhựa EVA hoặc cao su.'],
            'tips': 'Có thể tái sử dụng làm vật dụng trong nhà (tấm lót nồi, lót chân ghế), làm đồ chơi hoặc đồ trang trí (đồ chơi trẻ em, đồ trang trí),...'
        },
        'Giày': {
            'type': 'Rác tái chế',
            'materials': ['Được làm từ nhiều loại vật liệu như vải, da, nhựa, …'],
            'tips': 'Sửa chữa để tái sử dụng, tái chế thành đồ dùng như chậu cây mini, túi đựng dụng cụ hoặc bán lại, từ thiện nếu còn tốt.'
        },
        'Hộp xốp': {
            'type': 'Rác tái chế',
            'materials': ['Được làm chủ yếu từ nhựa PS'],
            'tips': 'Làm vật liệu cách nhiệt hoặc sáng tạo đồ dùng như chậu trồng cây nhẹ, làm mô hình, đồ chơi,...'
        },
        'Ly nhựa': {
            'type': 'Rác tái chế',
            'materials': ['Được làm từ các loại nhựa như PP, PS, PET, …'],
            'tips': 'Dùng làm chậu cây nhỏ, làm vật đựng, đồ trang trí.'
        },
        'Khăn giấy': {
            'type': 'Rác không tái chế',
            'materials': ['Thành phần chủ yếu là bột gỗ tự nhiên'],
            'tips': 'Làm phân bón hữu cơ, làm chất độn cho cây, chất nhóm lửa.'
        },
        'Nắp chai': {
            'type': 'Rác tái chế',
            'materials': ['Thường được làm từ nhựa PP hoặc HDPE.'],
            'tips': 'Làm đồ trang trí (làm trang ghép hoặc sơn, vẽ nắp chai để trang trí tường, cửa), chế tạo đồ chơi, dùng làm đồ gia dụng.'
        },
        'Bao tay': {
            'type': 'Rác không tái chế',
            'materials': ['Làm từ cao su (bao tay cao su), nhựa PVC (bao tay nhựa), nylon (bao tay nylon), cotton (bao tay vải)'],
            'tips': 'Hầu như không có cách tái chế tại nhà, cần mang đến nơi xử lý.'
        },
        'Cốc giấy': {
            'type': 'Rác không tái chế',
            'materials': ['Chủ yếu làm từ giấy'],
            'tips': 'Dùng làm chậu cây, hộp đựng nhỏ, đồ thủ công.'
        },
        'Pin': {
            'type': 'Rác tái chế',
            'materials': ['Gồm các kim loại nặng, thép không gỉ.'],
            'tips': 'Không có cách tái chế tại nhà, phải mang đến nơi tái chế pin.'
        },
        'Lon nước': {
            'type': 'Rác tái chế',
            'materials': ['Hầu hết được làm bằng nhôm'],
            'tips': 'Rửa sạch, sau đó có thể dùng làm khuôn làm bánh, vòng tay, móc khóa, đồ thủ công mỹ nghệ, đồ trang trí,..'
        },
        'Hộp cát-tông': {
            'type': 'Rác tái chế',
            'materials': ['Chủ yếu là giấy bột'],
            'tips': 'Dùng để lưu trữ đồ đạc, làm đồ thủ công hoặc trồng cây.'
        },
        'Hộp sữa': {
            'type': 'Rác tái chế',
            'materials': ['Thường được làm từ vật liệu Tetrapak (gồm lớp giấy, lớp nhựa PE, lớp nhôm)'],
            'tips': 'Làm chậu cây mini, vật để cất đồ hoặc làm đồ chơi.'
        }
    }
    return recycle_tips.get(label, {
        'type': 'Không xác định',
        'materials': ['Không xác định'],
        'tips': 'Không có thông tin tái chế.'
    })

