# Project Daydream
# Technical Review 2

![alt tag](https://raw.githubusercontent.com/kwinter213/TeamDayDream/master/images/SDUML.png)

## Preparation and Framing

### Background and Context
- Basic knowledge of our Project
- Basic understanding of what OpenCV is
  - What it is used for

### Key Questions
- We would like to try to stir some creative juices in terms of object recognition
- An outside perspective might be helpful in terms of determining which objects we want to use/how to identify said objects
- We would like to search for alternatives to how we are inserting our gifs

### Agenda for Technical Review Session
- *Establish a progressive review of work*
  - What has been done so far (5 minutes)
    - Github branching and structure clean-up
    - Selection of OpenCV as primary medium
    - OpenCV experimentation
      - Using heuristics and feature analysis
      - Training Haar samples
      - Single object identification
    - Started a website
- *What’s upcoming (5 minutes)*
  - Figure out new methods for identifying Areas of Interest (AOI)
  - Consistency in object identification
  - Superimposition of animations in a video frame
  - Animation creation

- *Discuss key discoveries (10 minutes)*
  - Object recognition approach
    - Current strategy
      - Aspect ratio
      - Size
      - Contour
      - Solidity
    - Possible strategies
      - *Keypoint recognition*
        - SURF (Speeded Up Robust Features) (algorithm) and FLANN (Fast Library for Approximate Nearest Neighbours) (api based on SURF algorithm)
      - *Feature tracking*
        - KLT (Kanade-Lucas-Tomasi) Algorithm

  - Animation display approach
    - Tkinter
    - ImageMagick
    - PIL (Python Imaging Library)
    - FreeImage
