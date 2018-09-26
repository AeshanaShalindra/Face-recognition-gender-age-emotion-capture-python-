# -*- coding: utf-8 -*-
import json
import StringIO
import cv2
import numpy as np
import StringIO
import angus.client
import datetime
import pytz
import  time
import math
import itertools
import operator

class Video(object):
    def __init__(self,path):
        self.path = path

    def play(self):
        from os import startfile
        startfile(self.path)

class Ad_MP4(Video):
    type = "MP4"

timeout = time.time() + 15

def most_common(lst):
     # get an iterable of (item, iterable) pairs
  SL = sorted((x, i) for i, x in enumerate(lst))
  # print 'SL:', SL
  groups = itertools.groupby(SL, key=operator.itemgetter(0))
  # auxiliary function to get "quality" for an item
  def _auxfun(g):
    item, iterable = g
    count = 0
    min_index = len(lst)
    for _, where in iterable:
      count += 1
      min_index = min(min_index, where)
    # print 'item %r, count %r, minind %r' % (item, count, min_index)
    return count, -min_index
  # pick the highest-count/earliest item
  return max(groups, key=_auxfun)[0]

def main(stream_index):
    camera = cv2.VideoCapture(stream_index)
    camera.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640)
    camera.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)
    camera.set(cv2.cv.CV_CAP_PROP_FPS, 10)
    a=[]
    g=[]
    if not camera.isOpened():
        print("Cannot open stream of index {}".format(stream_index))
        exit(1)

    print("Video stream is of resolution {} x {}".format(camera.get(3), camera.get(4)))

    conn = angus.client.connect()
    service = conn.services.get_service("age_and_gender_estimation", version=1)
    service.enable_session()

    while camera.isOpened():
        ret, frame = camera.read()

        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, buff = cv2.imencode(".jpg", gray,  [cv2.IMWRITE_JPEG_QUALITY, 80])
        buff = StringIO.StringIO(np.array(buff).tostring())

        job = service.process({"image": buff})
        res = job.result

        for face in res['faces']:
            x, y, dx, dy = face['roi']
            age = face['age']
            a.append(math.ceil(age))
            gender = face['gender']
            g.append(gender)

            cv2.rectangle(frame, (x, y), (x+dx, y+dy), (0,255,0))
            cv2.putText(frame, "(age, gender) = ({:.2f}, {})".format(age, gender),
                        (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                        0.8, (255, 255, 255))
            print("{:.2f} | {}".format(math.ceil(age) , gender))

       # cv2.imshow('Smart Billboard', frame)

	if time.time() > timeout:
            break
    if most_common(g) == 'male':
        if most_common(a) < 30 :
            movie = Ad_MP4(r"vid\Cadbury Dairy Milk.mp4")
        else :
            movie = Ad_MP4(r"vid\coca-cola.mp4")
    else :
        if most_common(a) < 30 :
            movie = Ad_MP4(r"vid\M&S Women's Fashion.mp4")
        else :
            movie = Ad_MP4(r"vid\coca-cola.mp4")

    print("{}".format(most_common(g)))
    print("{}".format(len(g)))
    print("{}".format(most_common(a)))
    print("WAITING............COMMERCIAL BREAK!!!!")
			#if age < 30 :
			#	movie = Ad_MP4(r"vid\Cadbury Dairy Milk.mp4")



    # if raw_input("Press enter to play, anything else to exit") == '':
    movie.play()

    service.disable_session()

    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    ### Web cam index might be different from 0 on your setup.
    ### To grab a given video file instead of the host computer cam, try:
    ### main("/path/to/myvideo.avi")
    main(0)