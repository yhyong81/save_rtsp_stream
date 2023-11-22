# save_rtsp_stream
Save rstp video link or video file (Python).

Python implementation to stream camera feed from OpenCV videoCapture via RTSP or select vidoe file from drive.

# Installation
pip install esaygui

# Requirement
Python 3.x
Opencv 3.x or above ( pip install opencv-python )

# Usage

Run save_rtsp_stream.py with required arguments

Try save_rtsp_stream.py --help to view the arguments

optional arguments:
 
  -h, --help            show this help message and exit
  
  -v VIDEO, --video VIDEO
                        path to the video file
  
  -f FORMAT, --format FORMAT
                        video file format (1=mp4v, 2=MJPG)
  
  -s SIZE, --size SIZE  video resolution (width,height), None=keep the same
                        resolution

The default save video format is mp4v and keep the same resolution with the streaming video

You can can the video resolution eg: --size (800,600)

python save_rtsp_stream.py --video rtsp://admin:sl888888@192.168.2.86

# Run program

python save_rtsp_stream.py to select vidoe file from drive

eg: python save_rtsp_stream.py --video rtsp://admin:sl888888@10.1.1.85:554 to connect with IP camera

eg: python save_rtsp_stream.py --video rtsp://admin:sl888888@10.1.1.85:554 --format 2 -- size (1024,786) to customize the video format and size

# Keyboard function:

ESC to quit the program

"R" or "r" to start the recording

"S" or "s" to stop the recording

The vidoe files are stored at inside the record folder

