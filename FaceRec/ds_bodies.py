# import the necessary packages
from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
import sqlite3
import time
import mysql.connector
import os


def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            if f.endswith('.mp4') or f.endswith(".mkv"):
                print('{}{}'.format(subindent, f))


def list_dirs(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        print(subindent)


def crop_videos(file, show):
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    cam = 0
    orig = 0
    cam = cv2.VideoCapture(file)
    fileName = str(file.split('/')[-1])[:-4]

    directory = 'unidentified/bodies/'
    while (True):

        ret, image = cam.read()
        cv2.waitKey(5)
        begin.readCount += 1
        print('read: ', begin.readCount, 'saved: ', begin.count)
        if image is None:
            cam.release()
            break
        orig = image.copy()
        image = imutils.resize(image, width=(int(image.shape[1] / 4)))
        (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
                                                padding=(8, 8), scale=1.05)
        for (x1, y1, x2, y2) in rects:
            begin.count += 1
            # cv2.putText(orig, str(i+1), (x1*4 + 75, y1*4 + 75), cv2.FONT_HERSHEY_COMPLEX_SMALL, 5,
            #             (0, 100, 0), 2),
            if not os.path.exists(directory + fileName):
                os.makedirs(directory + fileName)
            cv2.imwrite(directory + fileName + '/' + str(begin.count) + ".jpg",
                        orig[(y1 * 4):(y1 * 4) + (y2 * 4), (x1 * 4):(x1 * 4) + (x2 * 4)])

            # cv2.rectangle(orig, (x1 * 4, y1 * 4), ((x1 * 4) + (x2 * 4), (y1 * 4) + (y2 * 4)), (0, 0, 255), 2)
        rects = np.array([[x1, y1, x1 + x2, y1 + y2] for (x1, y1, x2, y2) in rects])
        pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
        for (xA, yA, xB, yB) in pick:
            cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)
        if show:
            cv2.imshow("before", image)
            cv2.moveWindow("before", 0, 300)

            cv2.waitKey(1)
    while False:
        cam.release()


def crop_images(path, show):
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    directory = 'unidentified/bodies/'
    for subdir, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.jpg') or file.endswith('.png'):
                print(subdir + file)
                begin.readCount += 1
                print('read: ', begin.readCount, 'saved: ', begin.count)
                image = cv2.imread(subdir + '/' + file)
                print(file)
                orig = image.copy()
                image = imutils.resize(image, width=(int(image.shape[1] / 4)))
                (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
                                                        padding=(8, 8), scale=1.05)
                for (x1, y1, x2, y2) in rects:
                    begin.count += 1
                    cv2.imwrite(directory + subdir.split('/')[-1] + '/' + str(begin.count) + ".jpg",
                                orig[(y1 * 4):(y1 * 4) + (y2 * 4), (x1 * 4):(x1 * 4) + (x2 * 4)])
                    cv2.rectangle(orig, (x1 * 4, y1 * 4), ((x1 * 4) + (x2 * 4), (y1 * 4) + (y2 * 4)), (0, 0, 255), 2)
                rects = np.array([[x1, y1, x1 + x2, y1 + y2] for (x1, y1, x2, y2) in rects])
                pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
                for (xA, yA, xB, yB) in pick:
                    cv2.rectangle(image, (xA, yA), (xB, yB), (0, 0, 0), 2)

                if show:
                    cv2.imshow("before", image)
                    cv2.moveWindow("before", 0, 0)
                    cv2.waitKey(1)


def produce(path, show, choice):
    if choice == 3 or choice == 4:
        if choice == 3:
            crop_videos(path, show)
        elif choice == 4:
            crop_videos(path, show)


    elif choice == 1 or choice == 2:
        for subdir, dirs, files in os.walk(path):
            for file in files:
                filepath = subdir + os.sep + file
                if choice == 1:
                    if filepath.endswith(".mkv") or filepath.endswith(".mp4"):
                        print(filepath)
                        crop_videos(filepath, show)
                else:
                    if filepath.endswith('jpg') or filepath.endswith('png'):
                        crop_images(subdir, show)


def begin():
    begin.count = 0
    begin.readCount = 0
    os.system('cls' if os.name == 'nt' else 'clear')
    showWork = input('Crop bodies from source '
                     'do you want to see pictures '
                     'while its working? \n\n'
                     'Y/N or YES/NO\n'
                     '_____________________________\n').lower()

    if showWork != 'y' and showWork != 'n' and showWork != 'no' and showWork != 'yes':
        os.system('cls' if os.name == 'nt' else 'clear')
        begin()
    else:
        if (showWork == 'y' or showWork == 'yes'):
            showWork = True
        else:
            showWork = False

        os.system('cls' if os.name == 'nt' else 'clear')
        choice = int(input('Input a number 1-4:\n'
                           '1. Crop all videos in subdirectories\n'
                           '2. Crop all images in subdirectories\n'
                           '3. Crop images in a specific directory\n'
                           '4. Crop video\n'))

        if choice > 4 or choice < 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            begin()

        if choice == 1 or choice == 2:
            produce('./', showWork, choice)
        else:

            if choice == 3:
                dir = input('list all relevant directories?\n'
                            '______________________________\n'
                            'Y/N or YES/NO\n').lower()
                if dir != 'y' and dir != 'n' and dir != 'no' and dir != 'yes':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    begin()
                else:
                    if (dir == 'y' or dir == 'yes'):
                        list_dirs('./')
                    else:
                        dir = False
                    dir = './' + str(input('write path ./ + {path}\n'))

                crop_images(dir, showWork)
            if choice == 4:
                dir = input('list all relevant directories?\n'
                            '______________________________\n'
                            'Y/N or YES/NO\n').lower()
                if dir != 'y' and dir != 'n' and dir != 'no' and dir != 'yes':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    begin()
                else:
                    if (dir == 'y' or dir == 'yes'):
                        list_files('./videos')
                    else:
                        dir = False
                    dir = str(
                        input('write path example: \n./videos/movie.mp4\nor \nrtsp://username:password@IP:PORT/SRC\n'))
                    crop_videos(dir, showWork)


begin()
cv2.destroyAllWindows()
