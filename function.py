import cv2
import math
import numpy as np


#每t秒随机取n帧
def method_one(dataPath,savePath,t,n):

    cap = cv2.VideoCapture(dataPath)
    if cap.isOpened():
        rval = True
    else:
        rval = False

    #cv2直接get到的时间是小数，因此通过fps来间接计算t秒内包含的帧数来设置间隔转化为方法2的方式
    fps = round(cap.get(5))
    length = cap.get(7)
    gap = fps*t
    print(fps,length,gap)

    headF=0
    tailF=gap
    currentF=0
    tmp = np.random.randint(headF, tailF, n)
    print(tmp)


    while rval:
        rval, frame = cap.read()

        if currentF in tmp:
            cv2.imwrite(savePath + str(currentF) + '.jpg', frame)
            print(currentF)
        if currentF == tailF:
            headF += gap
            tailF += gap
            # 由于按秒取的话间隔过长，若丢掉尾部可能会遗漏关键信息,因此对尾部加以保留
            if tailF > length and headF<length:
                tmp = np.random.randint(headF, length, n)
            #若头部超限则上次尾部必定超限，因此在上一个间隔内必定已经读完视频，所以不会存在头部超限的情况
            else:
                tmp = np.random.randint(headF, tailF, n)
            print(tmp)

        currentF += 1


    return


#m等分，每个区间随机取n帧
def method_two(dataPath,savePath,m,n):
    cap = cv2.VideoCapture(dataPath)

    if cap.isOpened():
        rval = True
    else:
        rval = False

    # cv2的get方法，参数为目标所对应的编号，这里取长度对应的编号是7
    length=cap.get(7)
    print("length: "+str(length))

    gap=math.floor(length/m)

    print("gap: " +str(gap))

    headF = 0
    tailF = gap
    if tailF > length:
        tailF = length

    currentF = 0

    tmp = np.random.randint(headF,tailF,n)
    print(tmp)
    while rval:


        rval,frame = cap.read()

        if currentF in tmp:
            cv2.imwrite(savePath+str(currentF)+'.jpg',frame)
            print(currentF)
        if currentF==tailF:
            headF+=gap
            tailF+=gap
            #因为总长度除间隔后向下取整的小数会有导致剩下几帧在末尾，丢掉无影响
            if tailF > length:
                break
            else:
                tmp = np.random.randint(headF, tailF, n)
            print(tmp)


        currentF+=1
        #cv2.waitKey(1)

    return

#每隔n帧取1帧
def method_three(dataPath,savePath,n):

    cap = cv2.VideoCapture(dataPath)
    if cap.isOpened():
        rval=True
    else:
        rval=False

    #cv2的get方法，参数为目标所对应的编号，这里取长度对应的编号是7
    length=cap.get(7)
    print("length: "+str(length))

    gap=n

    print("gap: " +str(gap))
    currentF = 0
    tmp=0

    while rval:


        rval,frame = cap.read()

        if tmp == gap:
            tmp=0

        if tmp == 0:
            cv2.imwrite(savePath+str(currentF)+'.jpg',frame)
            print(currentF)

        currentF+=1
        tmp+=1
        #cv2.waitKey(1)

    return
