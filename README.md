# Facial Recognition - Facial Alignment part 2

This repository is a continuation of the [face_align_1](https://github.com/CodeSaint98/face_align_1).

# Requirements and Installation 

I used dlib python library in this project. To install the dlib library make sure you're using a virtual environment first. If you are wondering how to set up a virtual environment, you can refer to [face_align_1](https://github.com/CodeSaint98/face_align_1). To install dlib type in the following commands into your terminal:
 
```
    pip install dlib
```


# Working

I used dlib's frontal face detector to capture facial landmarks(only the eyes) of the face in the image. I then unskewed the image by horizontally aligning the line drawn between the left and right eye.