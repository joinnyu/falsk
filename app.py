from flask import Flask,Blueprint, request, Response, make_response,jsonify
import json
import pyautogui
import logging
from enums import ResponseCode
pyautogui.PAUSE = 1.5  # 调用在执行动作后暂停的秒数，只能在执行一些pyautogui动作后才能使用，建议用time.sleep
pyautogui.FAILSAFE = True  # 启用自动防故障功能，左上角的坐标为（0，0），将鼠标移到屏幕的左上角，来抛出failSafeException异常

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to My Watchlist!'




@app.route('/send', methods=['post'])
def send_msgs():
    print("2222")
    req_parms = request.get_json()
    data = req_parms.get('data')
    if not data or not str(data).strip():
        return response(ResponseCode.PARAMS_ERROR)
    print(data)
    currentMouseX, currentMouseY = pyautogui.position()  # 鼠标当前位置
    print(currentMouseX, currentMouseY)
    # pyautogui.moveRel(200, 200, duration=2)
    # 获取当前鼠桥位置

    # 获取当前鼠标位置
    current_position = pyautogui.position()

    # 拖动鼠标到指定位置
    pyautogui.dragTo(100, 100, duration=1.5)
    # try:
    #     print("2222")
    #     req_parms = request.get_json()
    #     data = req_parms.get('data')
    #     if not data or not str(data).strip():
    #         return response(ResponseCode.PARAMS_ERROR)
    #     print(data)
    #     currentMouseX, currentMouseY = pyautogui.position()  # 鼠标当前位置
    #     print(currentMouseX, currentMouseY)
    #     # pyautogui.moveRel(200, 200, duration=2)
    #     # 获取当前鼠桥位置
    #
    #     # 获取当前鼠标位置
    #     current_position = pyautogui.position()
    #
    #     # 拖动鼠标到指定位置
    #     pyautogui.dragTo(100, 100, duration=1.5)
    #
    #     # # 控制鼠标移动,duration为持续时间
    #     # for i in range(2):
    #     #     pyautogui.moveTo(100, 100, duration=0.25)  # 移动到 (100,100)
    #     #     pyautogui.moveTo(200, 100, duration=0.25)
    #     #     pyautogui.moveTo(200, 200, duration=0.25)
    #     #     pyautogui.moveTo(100, 200, duration=0.25)
    #     #
    #     # for i in range(2):
    #     #     pyautogui.moveRel(50, 0, duration=0.25)  # 从当前位置右移100像素
    #     #     pyautogui.moveRel(0, 50, duration=0.25)  # 向下
    #     #     pyautogui.moveRel(-50, 0, duration=0.25)  # 向左
    #     #     pyautogui.moveRel(0, -50, duration=0.25)  # 向上
    # except:
    #     print("error")
    # return response(ResponseCode.OPERATION_FAIL)



@app.route('/send1')
def send_msgs1():
    try:
        screenshot = pyautogui.screenshot()
        screenshot.save(r'/Users/guoqiang/Downloads/my_screenshot11.png')
        print("Screenshot saved successfully.")
        pyautogui.moveTo(1050, 700, duration=2)
        return response(ResponseCode.SUCCESS)
    except Exception as e:
        print("Error occurred:", e)
    return response(ResponseCode.OPERATION_FAIL)





def response(code_msg, data=[]):
    code, msg = code_msg.value
    return jsonify({'errcode': code, 'errmsg': msg, 'data': data})
