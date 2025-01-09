## 番茄小说爬虫
### 1. 简介
番茄小说页面含有大量小说资源，本项目是一个爬虫，用于爬取番茄小说网站上的小说资源。
### 2. 项目结构
```plaintext
fanqie_novel_spider/
├─data
│      dc027189e0ba4cd-500.woff2
│      dc027189e0ba4cd-700.woff2
│      dc027189e0ba4cd.woff2
│
├─output
│  │  charmap_dic.txt
│  │
│  └─wait_for_identify_images
│          58344.jpg
│          58345.jpg
│          ...
│          58715.jpg
│
├─src
│      jpg_to_dic.py
│      UI.py
│      woff_to_jpg.py
├─ fontcreator15alpha1汉化版x64.exe
├─ main.py
└─ README.md
```
### 3. 使用方法
1. 运行`main.py`，输入小说的URL，程序会自动爬取小说资源。
2. 爬取的小说资源会保存在`output`文件夹下。

### 4. 依赖安装
安装`tesseract`并加入环境变量：https://github.com/tesseract-ocr/tesseract
```shell
conda create -n spider python=3.8
conda activate spider
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```
### 5. 注意事项
1. 本项目仅用于学习交流，禁止用于商业用途。
2. 请遵守法律法规，不要爬取违法资源。
3. 请勿频繁爬取，以免对服务器造成压力。
