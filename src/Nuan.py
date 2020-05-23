import os, sys, time, dlib, face_recognition, cv2
import numpy as np
from PIL import Image
import pkg_resources
from threading import Timer

def importfile(filename, path=None):
    """This imports any file to the current directory."""
    if path == None:
        file = open(filename)
        return file
    else:
        new_path = os.path.join(path, filename)
        file = open(new_path)
        return file

def importimage(filename, path=None):
    """ This imports any image to the current directory """
    if path == None:
        image = Image.open(filename)
        return image
    else:
        new_path = os.path.join(path, filename)
        image = Image.open(new_path)
        return image

def facedetection(unknownimage, knownimage, path=None, save_path=None):
    """ Takes an unknown image and looks for faces. """
    haar_xml = pkg_resources.resource_filename(
        'cv2', 
        'data/haarcascade_frontalface_default.xml'
        )
    faces_cascade = cv2.CascadeClassifier(haar_xml)
    unknown_image = os.path.join(path, unknownimage)
    img = cv2.imread(unknown_image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faces_cascade.detectMultiScale(gray, 1.1, 4)
    if len(faces) != 0 : #If the haar algorithm finds a face, it fill fill the array-> faces!=0
        facerecognition(unknownimage, knownimage, path)

        for (x, y, w, h) in faces: # Draws rectangles around the faces
            cv2.rectangle(img, (x ,y), (x+w ,y+h), (0, 255, 0), 2)
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        if save_path != None:
            cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
            filename = time.ctime()
            os.chdir(save_path)
            cv2.imwrite(f'{filename}', cv2image)


def facerecognition(unknownimage, knownimage, path):
    """ This takes an unknown image and compare it with an known image. If the face_recognition deems them to be the same person you will return true """
    if path == None:
        pass #wer're in the same directory as the files
    else:
        file_for_unknown = os.path.join(path, unknownimage)
        file_for_known = os.path.join(path, knownimage)
        unknown = face_recognition.load_image_file(file_for_unknown)
        known = face_recognition.load_image_file(file_for_known)
        unknown_encoding = face_recognition.face_encodings(unknown)[0]
        known_encoding = face_recognition.face_encodings(known)[0]

        result = face_recognition.compare_faces([known_encoding], unknown_encoding)
        return f'The face-recognition test was {result}.', result




    
def video_recognition(camera, reference_image = None, path = None, path_to_save = None):
    """Takes the input camera and saves the regonized file to the path of which you want to save,
    if no path is specified then it saves to the current directory."""
    if path_to_save == None:
        directory = os.getcwd()
        os.chdir(directory)
    else:
        os.chdir(path_to_save)
    if image_to_checkwith == None:
        pass # well write a code to fetch a random image.
    
    cap = cv2.VideoCapture(camera)
    ret, frame = cap.read()



folder = '/Users/andreasevensen/Documents/GitHub/Nuan'
reference = 'Andreas.jpeg'

#video_facedetection(0)