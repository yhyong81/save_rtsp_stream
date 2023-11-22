# python save_rtsp_stream.py
# or
# python save_rtsp_stream.py --video rtsp://admin:sl888888@10.1.1.85:554
# or
# python save_rtsp_stream.py --video video_path --format 1 -- size (WIDTH,HEIGHT)

# import the necessary packages
import cv2
import datetime
import argparse
import os
import easygui

Display_Resolution = (800, 600)
if not os.path.exists("./record"): os.makedirs("./record")
Video_Name = "./record/blank.mp4"
out = cv2.VideoWriter(Video_Name, cv2.VideoWriter_fourcc('m','p','4','v'), 10, Display_Resolution)
out.release()
Video_Path = None
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
FPS = 10
Record = True
Label = "Record"
Count = 10

ap = argparse.ArgumentParser(description="save_rstp_stream")
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-f", "--format", type=int, default=1, help="video file format (1=mp4v, 2=MJPG)")
ap.add_argument("-s", "--size", help="video resolution (width,height), None=keep the same resolution")
args = vars(ap.parse_args())

# if the video argument is None, then we are reading from video file from easygui
if args.get("video", None) is None:
    Video_Path = easygui.fileopenbox()
    if Video_Path is None: Video_Path = 0
# otherwise, we are reading from a video file
else:
    Video_Path = args["video"]
vs = cv2.VideoCapture(Video_Path)
WIDTH = int(vs.get(cv2.CAP_PROP_FRAME_WIDTH))
HEIGHT = int(vs.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(Video_Path)

if args.get("format", None) is not None:
    if format == 1:
        fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
        print("FourCC code MJPG")
    elif format == 2:
        fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
        print("FourCC code MP4V")
    else: print("FourCC code MJPG")
else: print("FourCC code MJPG")

if args.get("size", None) is not None:
    value = args["size"].replace("(", "").replace(")", "").split(",")
    if len(value) > 1:
        WIDTH = int(value[0])
        HEIGHT = int(value[1])
print(WIDTH, HEIGHT, FPS)

ret, frame = vs.read()
while (ret):
    # grab the frame
    ret, frame = vs.read()
    frame_save = frame.copy()
    frame_display = frame.copy()
    if ret is True:
        if Record is True:
            # save image
            if out.isOpened() is False:
                Video_Name = "./record/" + datetime.datetime.now().strftime("%Y-%m-%d_%H;%M;%S") + ".mp4"
                print(Video_Name)
                out = cv2.VideoWriter(Video_Name, fourcc, FPS, (WIDTH, HEIGHT))
            if out.isOpened() is True:
                frame_save = cv2.resize(frame_save, (WIDTH, HEIGHT), interpolation=cv2.INTER_AREA)
                out.write(frame_save)
            Count += 1
            if Count > 10:
                Count = 0
                if len(Label) >= 9: Label = "Record"
                else: Label = Label + "."
            cv2.putText(frame_display, Label, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 3.0, (0, 0, 255), 3)
        else:
            if out.isOpened() is True: out.release()
        frame_display = cv2.resize(frame_display, Display_Resolution, interpolation=cv2.INTER_AREA)
        cv2.imshow("video streaming", frame_display)
    key = cv2.waitKey(10) & 0xFF
    if key == 27: #esc key to exit
         break
    elif key == ord("R") or key == ord("r"): # r key to start record video
        Record = True
        Count = 0
        Label = "Record"
    elif key == ord("S") or key == ord("s"): # s key to stop record video
        Record = False
if out.isOpened() is True: out.release()
vs.release()
cv2.destroyAllWindows()
print("Exit")