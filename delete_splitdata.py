import os
import shutil
import random

# Đường dẫn đến thư mục chứa train, valid, test
base_dir = 'datasets'
output_dir = 'Output'

# Tạo thư mục tạm để gom dữ liệu
all_images_dir = os.path.join(base_dir, 'all_images')
all_labels_dir = os.path.join(base_dir, 'all_labels')
os.makedirs(all_images_dir, exist_ok=True)
os.makedirs(all_labels_dir, exist_ok=True)

# Gom tất cả ảnh và nhãn
for subfolder in ['train', 'valid', 'test']:
    img_dir = os.path.join(base_dir, subfolder, 'images')
    label_dir = os.path.join(base_dir, subfolder, 'labels')
    
    for file in os.listdir(img_dir):
        shutil.copy(os.path.join(img_dir, file), all_images_dir)
    for file in os.listdir(label_dir):
        shutil.copy(os.path.join(label_dir, file), all_labels_dir)

# Lấy danh sách file ảnh và nhãn
all_images = sorted([f for f in os.listdir(all_images_dir) if f.endswith(('.jpg', '.png'))])
all_labels = sorted([f for f in os.listdir(all_labels_dir) if f.endswith('.txt')])

# Chỉ giữ lại 600 cặp dữ liệu
paired_data = [(img, img.replace('.jpg', '.txt').replace('.png', '.txt')) for img in all_images if img.replace('.jpg', '.txt').replace('.png', '.txt') in all_labels]
selected_data = random.sample(paired_data, 600)

# Chia dữ liệu theo tỷ lệ 8:2
train_data = selected_data[:480]
valid_data = selected_data[480:]

# Tạo thư mục kết quả
for subset in ['train', 'valid']:
    os.makedirs(os.path.join(output_dir, subset, 'images'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, subset, 'labels'), exist_ok=True)

# Copy dữ liệu vào thư mục mới
for subset, data in zip(['train', 'valid'], [train_data, valid_data]):
    for img, lbl in data:
        shutil.copy(os.path.join(all_images_dir, img), os.path.join(output_dir, subset, 'images', img))
        shutil.copy(os.path.join(all_labels_dir, lbl), os.path.join(output_dir, subset, 'labels', lbl))

# Dọn dẹp thư mục tạm nếu cần
shutil.rmtree(all_images_dir)
shutil.rmtree(all_labels_dir)

print("Hoàn thành!")
