#---------------------------------------------------IMPORTING LIBRARIES-------------------------------------------------------------------------------
import subprocess
import cv2
import numpy as np
import os
from flask import Flask, jsonify, request, render_template, send_from_directory
import json
import cv2
import easyocr
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import cv2
import numpy as np
import time
import vehicle
from threading import Thread

os.environ["KMP_DUPLICATE_LIB_OK"]= 'TRUE'

def readVideo(filepath):  
    #---------------------------------------------------------------------------------------------------------------------------------
    cap=cv2.VideoCapture(filepath)

    # Get the width, height, and FPS from the original video
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps    = cap.get(cv2.CAP_PROP_FPS)
    # Define the codec and output file
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 'XVID' for .avi
    out = cv2.VideoWriter("output_video1.mp4", fourcc, fps, (width, height))
    socketio.emit('totalFrames', int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
    count_line_position=550
    min_width_Rect=80
    min_height_Rect=80
    detect=[]
    offset=6 # ALLowable Error between pixel
    counter=0

    #------------------------------------------------------------------------------------------------------------------------------------
    def center_handle(x,y,w,h):
        x1=int(w/2)
        y1=int(h/2)
        cx=x+x1
        cy=y+y1
        return cx,cy

    #Intialize Subtractor
    algo=cv2.bgsegm.createBackgroundSubtractorMOG()
    frameCount = 0
    while(True):
        ret,frame1=cap.read()
        if not ret or frame1 is None:
            print("file ended")
            break
        grey=cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        blur=cv2.GaussianBlur(grey,(3,3),5)
        #applying on each frame
        img_sub=algo.apply(blur)
        dilat=cv2.dilate(img_sub,np.ones((5,5)))
        kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
        dilatada=cv2.morphologyEx(dilat,cv2.MORPH_CLOSE,kernel)
        dilatada=cv2.morphologyEx(dilatada,cv2.MORPH_CLOSE,kernel)
        counterShape,h=cv2.findContours(dilatada,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        cv2.line(frame1,(25,count_line_position),(1200,count_line_position),(255,127,0),3)




        for (i,c) in enumerate(counterShape):
            (x,y,w,h)=cv2.boundingRect(c)
            validate_counter=(w>=min_width_Rect) and (h>=min_height_Rect)
            if not validate_counter:
                continue

            cv2.rectangle(frame1, (x,y), (x+w,y+h), (255, 0, 0), 3)
            cv2.putText(frame1,"Vehicle NO : "+str(counter),(x,y-20),cv2.FONT_HERSHEY_TRIPLEX,1,(255,244,0),2)

            center=center_handle(x,y,w,h)
            detect.append(center)
            cv2.circle(frame1,center,4,(0,0,255),-1)

            for (x,y) in detect:
                if y<(count_line_position+offset) and y>(count_line_position-offset):
                    counter+=1

                cv2.line(frame1,(25,count_line_position),(1200,count_line_position),(0,127,255),3)
                detect.remove((x,y))


        cv2.putText(frame1,"VEHICLE COUNTER : "+str(counter),(450,70),cv2.FONT_ITALIC,2,(0,0,255),5)

        # cv2.imshow("OUTPUT VIDEO",frame1)
        out.write(frame1) 
        frameCount+=1
        socketio.emit('frameCount', frameCount)

        if cv2.waitKey(1)==13:
            break
    cv2.destroyAllWindows()
    cap.release()
    out.release()

def classify(filepath):

    #---------------------------------------------------VARIABLE DECLARATIONS-------------------------------------------------------------------------------
    cap=cv2.VideoCapture(filepath) 
    fgbg=cv2.createBackgroundSubtractorMOG2(detectShadows=False,history=200,varThreshold = 90)
    kernalOp = np.ones((3,3),np.uint8)
    kernalOp2 = np.ones((5,5),np.uint8)
    kernalCl = np.ones((11,11),np.uint8)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cars = []
    max_p_age = 5
    pid = 1
    cnt_up=0
    cnt_down=0
    line_up=400
    line_down=250
    up_limit=230
    down_limit=int(4.5*(500/5))


    carCount = 0
    truckCount = 0



    # Get the width, height, and FPS from the original video
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps    = cap.get(cv2.CAP_PROP_FPS)
    # Define the codec and output file
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 'XVID' for .avi
    out = cv2.VideoWriter("video_classification1.mp4", fourcc, fps, (width, height))

    print("VEHICLE DETECTION,CLASSIFICATION AND COUNTING")

    #---------------------------------------------------RETRIEVING VEHICLES-------------------------------------------------------------------------------
    if (cap.isOpened()== False):
      print("Error opening video stream or file")

    while(cap.isOpened()):
        ret,frame=cap.read() 
        if not ret or frame is None:
            break
        frame=cv2.resize(frame,(900,500))
        for i in cars:
            i.age_one()
        fgmask=fgbg.apply(frame)

    #------------------------------------------------------BINARIZATION----------------------------------------------------------------------------
        if ret==True:
            ret,imBin=cv2.threshold(fgmask,200,255,cv2.THRESH_BINARY)
            mask = cv2.morphologyEx(imBin, cv2.MORPH_OPEN, kernalOp) #Opening :E->D
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernalCl) #Closing :D->E

            (contours0,hierarchy)=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #Contour Extraction
            for cnt in contours0:
                area=cv2.contourArea(cnt)
                #print(area) #Printing the Area of each Object 

                if area>300:
                    m=cv2.moments(cnt)
                    #Extracting Centroid Values
                    cx=int(m['m10']/m['m00'])
                    cy=int(m['m01']/m['m00'])
                    x,y,w,h=cv2.boundingRect(cnt) #x,y coordinates,width,height


                    new=True
                    if cy in range(up_limit,down_limit):
                        for i in cars:
                            if abs(x - i.getX()) <= w and abs(y - i.getY()) <= h:
                                new = False
                                i.updateCoords(cx, cy)

                                if i.going_UP(line_down,line_up)==True:
                                    cnt_up+=1
                                    # img=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                                    # cv2.imwrite("./detected_vehicles/vehicleUP" + str(cnt_up) + ".png", img[y:y + h - 1, x:x+w])



                                elif i.going_DOWN(line_down,line_up)==True:
                                    cnt_down+=1
                                    # img=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                                    # cv2.imwrite("./detected_vehicles/vehicleDOWN" + str(cnt_down) + ".png", img[y:y + h - 1, x:x+w])


                            #     break
                            if i.getState()=='1':
                                if i.getDir()=='down'and i.getY()>down_limit:
                                    i.setDone()
                                elif i.getDir()=='up'and i.getY()<up_limit:
                                    i.setDone()
                            if i.timedOut():
                                index=cars.index(i)
                                cars.pop(index)
                                del i

                        if new==True:
                            p=vehicle.Car(pid,cx,cy,max_p_age)
                            carCount+=1
                            cars.append(p)
                            pid+1
                    #cv2.circle(frame, (cx, cy), 20, (0, 0, 255), 2)
                    # img=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)





            for i in cars:
                cv2.putText(frame, str(i.getId()), (i.getX(), i.getY()), font, 0.3, (255,255,0), 1, cv2.LINE_AA)
                if line_down+20<= i.getY() <= line_up-20:
                   a = (h + (.74*w)- 100)

                   if a >= 0:
                         cv2.putText(frame, "Truck", (i.getX(), i.getY()), font, 1, (0,255,255), 2, cv2.LINE_AA)
                         truckCount+=1
                   else:
                         cv2.putText(frame, "car", (i.getX(), i.getY()), font, 1, (0,0,255), 2, cv2.LINE_AA)
                         carCount+=1


            # str_up='UP: '+str(cnt_up)
            # str_down='DOWN: '+str(cnt_down)

            #To display the Lines
            # frame=cv2.line(frame,(0,line_up),(900,line_up),(255,0,255),3,8) #Magenta
            # frame=cv2.line(frame,(0,up_limit),(900,up_limit),(0,255,255),3,8) #Cyan
            # frame=cv2.line(frame,(0,down_limit),(900,down_limit),(255,0,0),3,8) #Yellow
            # frame = cv2.line(frame, (0, line_down), (900, line_down), (255, 0,0), 3, 8) #Blue

            # #To display the Texts
            # cv2.putText(frame, str_up, (10, 40), font, 0.5, (0, 0, 255), 2, cv2.LINE_AA)
            # cv2.putText(frame, str_down, (10, 90), font, 0.5, (255, 0, 0), 2, cv2.LINE_AA)

            cv2.imshow('Frame',frame)
            # out.write(frame)

            if cv2.waitKey(1)&0xff==ord('q'):
                break

        else:
            break


    print(carCount)
    # print(truckCount)
    cap.release()
    # out.release()

    # subprocess.run([
    #     r"C:\ffmpeg\bin\ffmpeg.exe",
    #     "-i", "output_video1.mp4",
    #     "-vcodec", "libx264",
    #     "-acodec", "aac",
    #     "-strict", "-2",
    #     "output_video.mp4"
    # ])
    subprocess.run([
        r"C:\ffmpeg\bin\ffmpeg.exe",
        "-i", "video_classification1.mp4",
        "-vcodec", "libx264",
        "-acodec", "aac",
        "-strict", "-2",
        "video_classification.mp4"
    ])


    socketio.emit("classify","http://127.0.0.1:5000/classify")
    # cv2.destroyAllWindows()



def deleteItem(vehicleNo):
    items = []

    with open('data.json', 'r') as f:
        items = json.load(f)

    for i in range(len(items)):
        if items[i]['vehicleNo'] == vehicleNo:
            print('deleting', items[i])
            del items[i]
            break

    with open('data.json', 'w') as f:
        json.dump(items, f)


def payTheChallan(vehicleNo):
    items = []

    with open('data.json', 'r') as f:
        items = json.load(f)

    for i in range(len(items)):
        if items[i]['vehicleNo'] == vehicleNo:
            items[i]['paid'] = True
            break

    with open('data.json', 'w') as f:
        json.dump(items, f)



static_path = os.path.join(os.path.dirname(__file__), 'static')
app = Flask(__name__)
CORS(app) 

threshold = 0.25
reader = easyocr.Reader(['en'], gpu=False)



socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('connect')
def on_connect():
    print("Client connected")
    emit('server_message', {'msg': 'Hello from Flask server!'})

@socketio.on('client_message')
def handle_client_message(data):
    print("Client sent:", data)


@app.route('/')
def index():
    return jsonify({"status":"Server is running successfully"})


# @app.route('/deleteItem', methods=['POST'])
# def deleteFromJson():
#     reqjson = request.get_json()
#     vehicleNo = reqjson['vehicleNo']
#     deleteItem(vehicleNo)
#     return jsonify({'msg': 'ok'})


# @app.route('/pay-challan', methods=['POST'])
# def payChallan():
#     reqjson = request.get_json()
#     vehicleNo = reqjson['vehicleNo']
#     payTheChallan(vehicleNo)
#     return jsonify({'msg': 'ok'})


@app.route('/video', methods=['POST'])
def predictVideo():
    print("got here something")
    try:
        os.remove("output_video1.mp4")
    except:
        print("File doesnt existed then how delete")
    try:
        os.remove("output_video.mp4")
    except:
        print("File doesnt existed then how delete")
    try:
        os.remove("video_classification.mp4")
    except:
        print("File doesnt existed then how delete")
    try:
        os.remove("video_classification1.mp4")
    except:
        print("File doesnt existed then how delete")
    myfile = request.files['file']
    filename = myfile.filename
    filepath = f"upload/{filename}"
    myfile.save(filepath)
    videoThread = Thread(target=readVideo,args=(filepath,))
    videoThread.start()
    Thread(target=classify,args=(filepath,)).start()
    # readVideo(filepath)
    # classify(filepath)
    videoThread.join()
    os.remove(filepath)
    subprocess.run([
        r"C:\ffmpeg\bin\ffmpeg.exe",
        "-i", "output_video1.mp4",
        "-vcodec", "libx264",
        "-acodec", "aac",
        "-strict", "-2",
        "output_video.mp4"
    ])
    return jsonify({"Status":"http://127.0.0.1:5000/output"})


@app.route('/output')
def serve_video():
    return send_from_directory(".","output_video.mp4")


@app.route('/classify')
def serve_classify():
    return send_from_directory(".","video_classification.mp4")


if __name__ == '__main__':
    app.run(debug=True)
