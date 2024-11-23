import os
import shutil
import yaml

# Bước 1: Đọc file goc.yaml để lấy nhãn chuẩn
def load_goc_labels(goc_path):
    with open(goc_path, 'r', encoding='utf-8') as f:
        goc_data = yaml.safe_load(f)
    return {name: idx for idx, name in enumerate(goc_data['names'])}

# Bước 2: Đọc file data.yaml của dataset thu thập
def load_dataset_labels(data_yaml_path):
    with open(data_yaml_path, 'r', encoding='utf-8') as f:
        data_yaml = yaml.safe_load(f)
    return {name: idx for idx, name in enumerate(data_yaml['names'])}

# Bước 3: Xử lý chuyển đổi và sao chép file
def process_and_copy_files(dataset_path, output_path, dataset_label_map, target_label, target_label_id):
    for split in ['train', 'val', 'test']:
        labels_dir = os.path.join(dataset_path, split, 'labels')
        images_dir = os.path.join(dataset_path, split, 'images')

        output_labels_dir = os.path.join(output_path, split, 'labels')
        output_images_dir = os.path.join(output_path, split, 'images')

        # Tạo thư mục đầu ra nếu chưa tồn tại
        os.makedirs(output_labels_dir, exist_ok=True)
        os.makedirs(output_images_dir, exist_ok=True)

        if not os.path.exists(labels_dir) or not os.path.exists(images_dir):
            continue

        # Duyệt qua tất cả các file nhãn
        for label_file in os.listdir(labels_dir):
            if label_file.endswith('.txt'):
                label_path = os.path.join(labels_dir, label_file)
                image_path = os.path.join(images_dir, label_file.replace('.txt', '.jpg'))  # Giả sử ảnh có định dạng .jpg
                
                # Đọc nội dung file nhãn
                with open(label_path, 'r') as f:
                    lines = f.readlines()

                # Kiểm tra xem file nhãn có chứa target_label không
                converted_lines = []
                contains_target_label = False
                for line in lines:
                    parts = line.strip().split()
                    if len(parts) < 5:
                        continue
                    class_id = int(parts[0])
                    if class_id == dataset_label_map.get(target_label, -1):
                        contains_target_label = True
                        # Thay thế nhãn
                        converted_lines.append(f"{target_label_id} " + " ".join(parts[1:]))
                    else:
                        # Bỏ qua các nhãn khác
                        converted_lines.append(line.strip())

                # Nếu file chứa nhãn cần xử lý, copy ảnh và ghi file nhãn mới
                if contains_target_label:
                    # Copy ảnh
                    if os.path.exists(image_path):
                        shutil.copy(image_path, os.path.join(output_images_dir, os.path.basename(image_path)))
                    
                    # Ghi file nhãn mới
                    with open(os.path.join(output_labels_dir, label_file), 'w') as f:
                        f.write("\n".join(converted_lines))
                        
# Bước 4: Cấu hình và chạy script
goc_path = 'HTL/goc.yaml'  # Đường dẫn tới file goc.yaml                            #################### goc.yaml
data_yaml_path = 'HTL/data.yaml'  # Đường dẫn tới file data.yaml                    #################### data.yaml datasets
dataset_path = 'HTL'  # Đường dẫn tới bộ dataset                                    ####################
output_path = 'HTL_processed'  # Đường dẫn tới thư mục lưu kết quả                  #################### Tùy ý

# Tạo ánh xạ nhãn chuẩn từ goc.yaml
goc_labels = load_goc_labels(goc_path)

# Tạo ánh xạ nhãn từ data.yaml
dataset_labels = load_dataset_labels(data_yaml_path)

# Cấu hình nhãn cần lấy
target_label = 'plastic bottle'  # Nhãn cần lấy từ dataset                          #################### datasets download
if target_label in dataset_labels:
    target_label_id = goc_labels.get('Chai nhựa', -1)  # Ánh xạ về nhãn 0 trong goc.yaml    #################### gốc
    if target_label_id != -1:
        # Chuyển đổi nhãn và sao chép file
        process_and_copy_files(dataset_path, output_path, dataset_labels, target_label, target_label_id)
        print(f"Xử lý hoàn tất. Kết quả được lưu tại: {output_path}")
    else:
        print(f"Lỗi: 'Chai nhựa' không có trong goc.yaml.")
else:
    print(f"Lỗi: '{target_label}' không có trong data.yaml.")
