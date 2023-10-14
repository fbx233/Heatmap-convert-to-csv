# Heatmap-convert-to-csv
This tool allows users to extract numerical values ​​from heatmap images with colorbars. Users can manually select the colorbar and heat map area, and then the tool will convert the color of the heat map to a value between 0 and 1 based on the color range of the colorbar. Finally, the values ​​are exported to a csv file.

## Main function
* **Manual frame**: selection Using the gui function of open cv, users can manually frame the colorbar and heat map areas.
* **Color to Value Mapping**: tool will calculate the color to value mapping based on the user selected colorbar area and the known 0 1 range.
* **Heat map value extraction**: tool will traverse each pixel of the heat map, find the corresponding value based on its color value, and store these values.
* **Export to csv**: The extracted values ​​will be saved as csv files for subsequent analysis and use.
## Usage scenarios
Applicable to users who want to extract numerical data from heat map pictures, but do not have original data or only pictures. For example, extract heatmap data from scientific articles, reports, or other documents.
## Precautions
* For best results, it is recommended to use high-resolution heatmap images. 
* The tool assumes that colorbar is linear and its value range is 0 to 1 (Pearson correlation). 
* After completing the box selection, press the enter key or the space key to confirm the selection, and press the esc key to cancel the box selection.

# Python 热图数值提取工具
这个工具允许用户从带有 colorbar 的热图图片中提取数值。用户可以手动框选 colorbar 和热图区域，然后工具会根据 colorbar 的颜色范围将热图的颜色转换为 [0, 1] 之间的数值。最后，这些数值会被导出为 CSV 文件。

## 主要功能
* 手动框选: 使用 OpenCV 的 GUI 功能，用户可以手动框选 colorbar 和热图区域。
* 颜色到数值的映射: 工具会根据用户框选的 colorbar 区域和已知的 [0, 1] 范围计算颜色到数值的映射。
* 热图数值提取: 工具会遍历热图的每个像素，根据其颜色值找到对应的数值，并存储这些数值。
* 导出为 CSV: 提取的数值会被保存为 CSV 文件，方便后续分析和使用。

## 使用场景
适用于那些希望从热图图片中提取数值数据，但没有原始数据或只有图片的用户。例如，从科学文章、报告或其他文档中提取热图数据。

## 注意事项
* 为了获得最佳效果，建议使用高分辨率的热图图片。
* 工具假设 colorbar 是线性的，并且其数值范围是 [0, 1]。
* 在框选完毕后，按下 "Enter" 键或 "Space" 键确认选择，按 "Esc" 键取消框选。
* **ps：目前工具正处于开发中，可能会产生多种不稳定的结果**
