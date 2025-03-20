from ultralytics import YOLO
import cv2
import multiprocessing
# import smtplib
import cvzone
import urllib.request
import math


def fun1():
    # vid = cv2.VideoCapture("C:\\Users\\sarth\\PycharmProjects\\yolo_project\\chlid.mp4")

    vid = cv2.VideoCapture("car_fire.mp4")
    # vid1 = cv2.VideoCapture("C:\\Users\\sarth\\PycharmProjects\\yolo_project\\car_fire.mp4")
    # vid.set(3, 1280)
    # vid.set(4, 720)

    # model = YOLO("C:\\Users\\sarth\\PycharmProjects\\yolo_project\\yolov8l.pt")
    model = YOLO("best.pt")
    names = ['fire', 'smoke']

    while True:
        success, img = vid.read()
        # succ , im = vid1.read()
        results = model(img, stream=True)
        # results1 = model(im,stream=True)
        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                w, h = x2 - x1, y2 - y1
                cvzone.cornerRect(img, (x1, y1, w, h))

                conf = math.ceil((box.conf[0] * 100)) / 100

                # if conf > 0.7 :
                #     data = urllib.request.urlopen(f"https://api.thingspeak.com/update?api_key=BJZJPZ1BZ3BO44E3&field1={conf}")
                #     client = Client(keys.account_sid, keys.auth_token)
                #     message = client.messages.create(
                #         body="your child is not in his room",
                #         from_=keys.twillio_number,
                #         to=keys.my_num
                #     )
                # s = smtplib.SMTP('smtp.gmail.com', 465)
                # s.starttls()
                # s.login("sarthakmalikmeerut@gmail.com", "doomgqtqjkqoosyc")
                # message = "your location is jalandhar"
                # s.sendmail("sarthakmalikmeerut@gmail.com", "sarthakmalikmeerut@gmail.com", message)
                cls = int(box.cls[0])

                cvzone.putTextRect(img, f'{conf}', (max(0, x1), max(35, y1)))

        cv2.imshow("image", img)

        cv2.waitKey(1)
fun1()

