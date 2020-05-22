import os, sys, time, dlib, face_recognition, cv2
import numpy as np
from PIL import Image
import pkg_resources

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
    if path == none:
        image = Image.open(filename)
        return image
    else:
        new_path = os.path.join(path, filename)
        image = Image.open(new_path)
        return image

def facedetection(unknownimage, knownimage, path=None, save_path=None):
    """ """
    haar_xml = pkg_resources.resource_filename(
        'cv2', 
        'data/haarcascade_frontalface_default.xml'
        )
    faces_cascade = cv2.CascadeClassifier(haar_xml)
    img = cv2.imread(unknownimage, 0)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faces_cascade.detectMultiScale(gray, 1.1, 4)
    if len(faces) !=0 : #If the haar algorithm finds a face, it fill fill the array-> faces!=0
        facerecognition(unknownimage, knownimage, path)

        for (x, y, w, h) in faces: # Draws rectangles around the faces
            cv2.rectangle(img, (x ,y), (x+w ,y+h), (0, 255, 0), 2)
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    #implement a save picture function

def facerecognition(unknownimage, knownimage, path):
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
        return f'The recognitiontest is {result} for the two images.'

folder = '/Users/andreasevensen/Desktop/Uni/Programming/Enterprises/Known_faces/Admin'
andreas = 'Andreas.png'
unknown = '/Users/andreasevensen/Desktop/Uni/Programming/Enterprises/Known_faces/Admin/'

facedetection(unknown, andreas, folder)