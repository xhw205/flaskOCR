### 一个丑陋的paddleOCR页面
-----
#### 前言
工作时候，总会遇到图片转文字的需求，这时候会用手机OCR识别后，再复制发给“微信电脑端”

不如借助 flask 和 paddleOCR 搭建一个“**ugly but useful**”的网页吧

paddleOCR 量级也可以达到十分优秀的效果
![ocr](https://s2.loli.net/2022/07/06/I8QvNDizAV6HtFW.png)

#### 依赖

+ pip install paddleocr
+ pip install flask
+ pip install werkzeug
+ pip install base64

#### 运行

+ 先运行 ocr 服务端接口
  `python pdocr_service.py`

+ 再运行主页面（前后端图片采用 base64 流传输）

  `python main.py`

+ 浏览器打开：http://0.0.0.0:8080/  ， 0.0.0.0 改为你本机 IP

