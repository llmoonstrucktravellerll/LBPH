# LBPH

 Tools Used 

We utilized the OpenCV library to implement LBPH, which provided an accessible and efficient framework for face recognition tasks.

LBPH analyzes local features of an image and constructs a histogram to represent facial features. It is renowned for its robustness under varying lighting conditions and lower computational demands compared to deep learning methods.

Three primary parts make up the face recognition project:


 face_recogniser.py, face_train.py, and face_taker.py.

 The modules each have their own purposes and were built using OpenCV and Python. Some of the techniques used are Local Binary Patterns Histograms (LBPH) for face recognition and Haar Cascade classifiers for face detection.


Functions performed by Modules
1.face_recognizer.py:
This module is in charge of recognizing faces using a pre-trained LBPH model.


2.face_train.py:
This module is responsible for training the face recognizer model using images stored in a specified directory.


3.face_taker.py:
This module is responsible for capturing images of faces from the webcam and saving them for training. In addition, it assigns unique identifiers to users and saves the names of those users.



In conclusion, succesfully implemented a method of creating a face recognition system using LBPH for the recognition and Haar Cascade feature to detect a face. The system has implemented separate modules to recognise faces, train the model, and take pictures of your face.


The implementation of these methodologies and technologies allows for fairly accurate and efficient recognition of faces. This shows that the system is quite robust, and provides a fairly reliable possibility for solving a variety of problems.



Advantages:

Reduced Computational Load: The LBPH method significantly lowered the computational requirements, enabling faster processing and real-time face recognition capabilities.

Hardware Efficiency: The algorithm performed efficiently on our existing hardware, delivering satisfactory results without the need for extensive computational resources.

The transition to the LBPH algorithm proved beneficial, addressing the issues we encountered with TensorFlow and FaceNet. Its robustness and efficiency make it a suitable choice for our face recognition needs.

Drawbacks:


Although the face recognition project shows how well LBPH and Haar Cascade classifiers may be implemented, the present methodology and code implementation have a number of flaws. The system's scalability, accuracy, and performance may be impacted by these constraints.

1.Accuracy threshold and Confidence 

2.Obsolete Face Detection Method

3.Limited Scalability

4.Lack of Data Augmentation

5.No Deep Learning-Based Approaches Were Used

6.Privacy and Security Concerns



Conclusion:
The  project demonstrates a functional implementation using traditional computer vision techniques. However, it has several limitations and drawbacks that affect its accuracy, scalability, and usability. Future improvements could include adopting deep learning-based methods, implementing data augmentation, enhancing the user interface, and addressing privacy and security concerns to create a more robust and efficient face recognition system.




