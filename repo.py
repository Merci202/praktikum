import os

from flask import Flask, request, jsonify, send_file
from cv2 import VideoCapture, imwrite

app = Flask(__name__)


@app.route('/get_picture', methods=['GET'])
def get_picture():
    filename = request.args.get('name')+".png"
    return send_file(filename, mimetype='image/png')

# 拍照 API
@app.route('/take_picture', methods=['POST'])
def take_picture():
    cam_port = 0
    cam = VideoCapture(cam_port)

    # reading the input using the camera
    result, image = cam.read()

    # If image will detected without any error,
    # show result
    if result:
        # saving image in local storage
        imwrite(request.json["name"]+".png", image)
    # If captured image is corrupted, moving to else part
    else:
        print("No image detected. Please! try again")

    return jsonify({'url': request.json['name']+".png"}), 200


@app.route('/detect_image', methods=['POST'])
def detect_image():
    data = request.json
    image_url = data['url']

    # read image
    image = cv2.imread(image_url)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 检测圆圈
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20,
                               param1=50, param2=30, minRadius=0, maxRadius=0)

    # 如果检测到圆圈,获取圆圈列表
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
    else:
        # 如果未检测到圆圈，返回空列表
        return [([(False, None)] * 3) for _ in range(3)]

    # 创建九宫格结果列表，初始化
    grid_result = [([(False, None)] * 3) for _ in range(3)]

    # 检测每个圆圈
    for (x, y, r) in circles:
        # 确定圆圈所在的九宫格位置，shape 0 是高度 shape 1 是宽度
        grid_x = x // (image.shape[1] // 3)
        grid_y = y // (image.shape[0] // 3)

        # 检测颜色
        # 这里简化处理，只根据颜色的BGR平均值判断是否为红色杯子
        # 实际应用可能需要更复杂的颜色检测逻辑
        circle_color = "transparent"
        (mean_b, mean_g, mean_r) = cv2.mean(image[y - r:y + r, x - r:x + r])[:3]
        if mean_r > mean_g and mean_r > mean_b:
            circle_color = "red"

        # 设置九宫格中的相应位置
        grid_result[grid_y][grid_x] = (True, circle_color)

    result = {'grid': grid_result }
    return jsonify(result), 200


@app.route('/delete_picture', methods=['DELETE'])
def delete_picture():
    filename = request.args.get('name')+".png"
    try:
        os.remove(filename)
        return jsonify({'message': 'yes'})
    except FileNotFoundError:
        return jsonify({'error': 'image not found'}), 404
    except Exception as e:
        return jsonify({'error': 'other error'}), 500

if __name__ == '__main__':
    app.run(debug=True)



