
# 挂载 Google Drive
from google.colab import drive
drive.mount('/content/drive')

# 导入库
import os
import pandas as pd

# 设置路径
project_folder = '/content/drive/MyDrive/33/'
data_folder = os.path.join(project_folder, 'Images/QaTa-dataset/')
cov19_folder = os.path.join(data_folder, 'QaTa-COV19/')
control_folder = os.path.join(data_folder, 'control_images/')

# 初始化列表
image_ids = []
image_paths = []
labels = []

# 遍历 control_images 文件夹（正常图像）
for img_name in os.listdir(control_folder):
    if img_name.endswith(('.png', '.jpg', '.jpeg')):  # 确保是图像文件
        image_ids.append(img_name)  # 文件名作为 image_id
        image_paths.append(os.path.join(control_folder, img_name))  # 使用绝对路径
        labels.append(0)  # 0 表示无肺炎

# 遍历 QaTa-COV19 文件夹（肺炎图像）
for img_name in os.listdir(cov19_folder):
    if img_name.endswith(('.png', '.jpg', '.jpeg')):
        image_ids.append(img_name)
        image_paths.append(os.path.join(cov19_folder, img_name))  # 使用绝对路径
        labels.append(1)  # 1 表示有肺炎

# 创建 DataFrame
pair_df = pd.DataFrame({
    'image_id': image_ids,
    'image_path': image_paths,
    'label': labels
})

# 打印数据集总数
print(f"数据集总数为 {len(pair_df)} 张，将使用全部数据")

# 保存配对表
output_path = os.path.join(data_folder, 'pair_table.csv')  # 使用 data_folder 确保路径正确
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # 确保目录存在
pair_df.to_csv(output_path, index=False)
print("配对表已保存到:", output_path)
