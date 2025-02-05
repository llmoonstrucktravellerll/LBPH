import numpy as np
import json
import cv2
import os


def create_directory(directory: str) -> None:
    """
    Create a directory if it doesn't exist.

    Parameters:
        directory (str): The path of the directory to be created.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_face_id(directory: str) -> int:
    """
    Get the first identifier available.

    Parameters:
        directory (str): The path of the directory of images.
    """
    user_ids = []
    for filename in os.listdir(directory):
        parts = os.path.split(filename)[-1].split("-")
        if len(parts) > 1:
            try:
                number = int(parts[1])
                user_ids.append(number)
            except ValueError:
                continue  # Ignore files that don't match the expected format
    user_ids = sorted(list(set(user_ids)))
    max_user_ids = 1 if len(user_ids) == 0 else max(user_ids) + 1
    for i in sorted(range(0, max_user_ids)):
        if i not in user_ids:
            return i
    return max_user_ids

def save_name(face_id: int, face_name: str, filename: str) -> None:
    """
    Save name on JSON of names.

    Parameters:
        face_id (int): The identifier of the user.
        face_name (str): The user name.
        filename (str): The file name where to save the pair identifier - name.
    """
    names_json = None
    if os.path.exists(filename):
        with open(filename, 'r') as fs:
            names_json = json.load(fs)
    if names_json is None:
        names_json = {}
    names_json[face_id] = face_name
    with open(filename, 'w') as fs:
        json_dump = json.dumps(names_json, ensure_ascii=False, indent=4)
        fs.write(json_dump)

if __name__ == '__main__':
    directory = 'images'
    cascade_classifier_filename = 'haarcascade_frontalface_default.xml'
    names_json_filename = 'names.json'

    create_directory(directory)
    
    faceCascade = cv2.CascadeClassifier(cascade_classifier_filename)
    
    cam = cv2.VideoCapture(0)
    
    if not cam.isOpened():
        print("Error: Could not open webcam.")
        exit()
    
    cam.set(3, 640)
    cam.set(4, 480)
    
    count = 0
    face_name = input('\nEnter user name and press <return> -->  ')
    face_id = get_face_id(directory)
    save_name(face_id, face_name, names_json_filename)
    print('\n[INFO] Initializing face capture. Look at the camera and wait...')

    while True:
        ret, img = cam.read()
        
        if not ret or img is None or img.size == 0:
            print("Error: Failed to capture image. Exiting...")
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            count += 1
            cv2.imwrite(f'./images/Users-{face_id}-{count}.jpg', gray[y:y+h, x:x+w])
            cv2.imshow('image', img)
    
        k = cv2.waitKey(100) & 0xff
        if k == 27:  # ESC key
            break
    
        elif count >= 30:
            break
    
    print('\n[INFO] Success! Exiting Program.')
    
    cam.release()
    cv2.destroyAllWindows()
