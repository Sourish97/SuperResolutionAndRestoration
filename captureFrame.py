import cv2
vidcap = cv2.VideoCapture('new1.avi')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("test_%d.png" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
