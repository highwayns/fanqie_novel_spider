# import os
# from PIL import Image
# import pytesseract
# import cv2
#
# def ocr_images_to_dict(folder_path):
#     # 初始化结果字典
#     results = {}
#
#     # 遍历文件夹中的所有文件
#     for file_name in os.listdir(folder_path):
#         file_path = os.path.join(folder_path, file_name)
#         try:
#             # 打开图片
#             image = Image.open(file_path)
#             # 单字符识别模式
#             custom_config = "--psm 10"
#             # OCR 识别
#             ocr_result = pytesseract.image_to_string(image, lang="chi_sim", config=custom_config).strip()
#             print(f"{file_name}:{ocr_result}")
#             # 将结果存入字典
#             results[file_name] = ocr_result.strip()
#         except Exception as e:
#             print(f"Error processing {file_name}: {e}")
#
#     return results
#
# if __name__ == '__main__':
#     # 指定文件夹路径
#     _folder_path = './wait_for_identify_images'
#     ocr_results = ocr_images_to_dict(_folder_path)
#
#     # 打印结果
#     for img_name, ocr_text in ocr_results.items():
#         print(f"{img_name}: {ocr_text}")

import os
from PIL import Image, ImageTk
import pytesseract
from UI import UI


def ocr_images_to_dict(folder_path):
    # 初始化结果字典
    results = {}
    stop_loop = False    # 如果变为True则跳出循环
    # 遍历文件夹中的所有文件
    for file_name in os.listdir(folder_path):
        if stop_loop:
            break
        file_path = os.path.join(folder_path, file_name)
        # 打开图片
        image = Image.open(file_path)
        # 单字符识别模式
        custom_config = "--psm 10"
        # OCR 识别
        ocr_result = pytesseract.image_to_string(image, lang="chi_sim", config=custom_config).strip()
        ui = UI(image, file_name, ocr_result, stop_loop)
        right_result = ui.final_result
        results[file_name] = right_result
        print(f"{file_name}:{right_result}")
        stop_loop = ui.stop_loop
    return results

if __name__ == '__main__':
    # 指定文件夹路径
    _folder_path = '../output/wait_for_identify_images'

    # 执行 OCR 识别并交互确认
    results = ocr_images_to_dict(_folder_path)

    # 打印最终结果
    print("\n最终确认的结果:")
    with open("../output/charmap_dic.txt", "w", encoding="utf-8") as f:
        _str = str(results)
        print(_str)
        f.write(_str)



