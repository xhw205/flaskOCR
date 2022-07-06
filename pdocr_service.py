# -*- coding: utf-8 -*-
from paddleocr import PaddleOCR
from flask import request
from flask_cors import CORS
from flask import  Flask
import json
import base64
import cv2
import numpy as np
paddle_ocr = PaddleOCR(det_db_box_thresh=0.3)

app = Flask(__name__)
CORS(app)
@app.route('/ocr/', methods=['GET', 'POST'])
def ocr_main():
    in_data = json.loads(request.get_data())
    img = in_data["image"]

    img = base64.b64decode(img)
    img = np.fromstring(img, np.uint8)
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)

    _, res = paddle_ocr(img)
    print(res)
    text = ""
    for i in res:
        text = text + i[0] + "\n"
    ocr_res = {}
    ocr_res["res"] = text
    ocr_res = json.dumps(ocr_res, ensure_ascii=False)
    return ocr_res

if __name__ == '__main__':
    app.run(host="192.168.8.60", port=9999)

