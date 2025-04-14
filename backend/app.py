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
            (x,y,w,h)=cv2.boundingRect(c);
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


@app.route('/deleteItem', methods=['POST'])
def deleteFromJson():
    reqjson = request.get_json()
    vehicleNo = reqjson['vehicleNo']
    deleteItem(vehicleNo)
    return jsonify({'msg': 'ok'})


@app.route('/pay-challan', methods=['POST'])
def payChallan():
    reqjson = request.get_json()
    vehicleNo = reqjson['vehicleNo']
    payTheChallan(vehicleNo)
    return jsonify({'msg': 'ok'})


@app.route('/video', methods=['POST'])
def predictVideo():
    print("got here something")
    myfile = request.files['file']
    filename = myfile.filename
    filepath = f"upload/{filename}"
    myfile.save(filepath)
    readVideo(filepath)
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
    # return jsonify({'msg': 'ok'})


@app.route('/output')
def serve_video():
    return send_from_directory(".","output_video.mp4")



if __name__ == '__main__':
    app.run(debug=True)
