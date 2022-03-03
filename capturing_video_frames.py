import cv2
import os


def get_frames(vdo_file_path, frame_count=0):
    vdo = cv2.VideoCapture(vdo_file_path)
    i = 0
    frame_skip = 30
    frame_count = frame_count
    while vdo.isOpened():
        ret, frame = vdo.read()
        if not ret:
            break
        if i > (frame_skip-1):
            frame_count += 1
            cv2.imwrite('./frames/' + 'frame_'+str(frame_count)+'.jpg', frame)
            i = 0
            continue
        i += 1
    vdo.release()
    cv2.destroyAllWindows()
    return frame_count

if __name__=='__main__':
    vdos_path = './vdos'
    file_names = os.listdir(vdos_path)
    frame_count = 0
    #total_frames = 0
    #print(len(file_names), file_names)
    for file_name in file_names:
        vdo_file_path = os.path.join(vdos_path, file_name)
        #print(vdo_file_path)
        frame_count = get_frames(vdo_file_path=vdo_file_path, frame_count=frame_count)
        #total_frames += frame_count
        print(frame_count)
    #print(total_frames)

    """ vdo_file_path = 'D:\\dataset\\rod data\\japan data\\vdo\\clips\\lot1.mp4'
    frame_count = get_frames(vdo_file_path=vdo_file_path, frame_count=frame_count)
    print(frame_count) """


""" video = cv2.VideoCapture(vdo_path)
count = 0
while(video.isOpened()):
    ret , frame = video.read()
    if ret == False:
        break

    count += 1
    cv2.imwrite('./frames/frame_'+str(count)+'.jpg', frame)

    #cv2.namedWindow('video',cv2.WINDOW_NORMAL)
    #cv2.imshow('video',frame)   

    k=cv2.waitKey(1) & 0xFF
    if k==27:
        break
video.release()
cv2.destroyAllWindows() """