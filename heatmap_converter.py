import cv2
import numpy as np
import pandas as pd

def resize_image(image, max_width=800, max_height=600):
    """缩放图片，使其适应屏幕大小"""
    h, w = image.shape[:2]
    scale = min(max_width / w, max_height / h)
    return cv2.resize(image, (int(w*scale), int(h*scale))), scale

# 读取图片
img = cv2.imread('/Users/davidfeng/Downloads/WechatIMG1554.jpg')
img_resized, scale_factor = resize_image(img)

# 手动框选 colorbar 区域
roi_colorbar = cv2.selectROI("Select Colorbar", img_resized, False, False)
colorbar_img = img[int(roi_colorbar[1]/scale_factor):int((roi_colorbar[1]+roi_colorbar[3])/scale_factor), 
                  int(roi_colorbar[0]/scale_factor):int((roi_colorbar[0]+roi_colorbar[2])/scale_factor)]

# 手动框选热图区域
roi_heatmap = cv2.selectROI("Select Heatmap", img_resized, False, False)
heatmap_img = img[int(roi_heatmap[1]/scale_factor):int((roi_heatmap[1]+roi_heatmap[3])/scale_factor), 
                  int(roi_heatmap[0]/scale_factor):int((roi_heatmap[0]+roi_heatmap[2])/scale_factor)]

# 假设 colorbar 是线性的，计算颜色到数值的映射
color_values = np.linspace(0, 1, colorbar_img.shape[0])
avg_colorbar_colors = np.mean(colorbar_img, axis=1)  # 取 colorbar 的平均颜色值

# 将热图的颜色转换为数值
heatmap_values = np.zeros((heatmap_img.shape[0], heatmap_img.shape[1]), dtype=float)
for i in range(heatmap_img.shape[0]):
    for j in range(heatmap_img.shape[1]):
        color = heatmap_img[i, j]
        # 找到与当前颜色最接近的 colorbar 颜色
        idx = np.argmin(np.linalg.norm(avg_colorbar_colors - color, axis=1))
        heatmap_values[i, j] = color_values[idx]

# 使用 pandas 导出为 CSV
df = pd.DataFrame(heatmap_values)
df.to_csv('heatmap_values.csv', index=False)

cv2.destroyAllWindows()
