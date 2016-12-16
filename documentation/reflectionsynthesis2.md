# Project Daydream
# Review 2

![alt tag](https://i.ytimg.com/vi/j3xq7CVpsB0/hqdefault.jpg)

## Synthesis & Reflection

### Issues raised
- **Object Recognition**
 - We raised the problem of the bounding box of the target object  changes if the object spins which makes the recognition process using the aspect ratio harder. We are trying to use the keypoint recognition method to make it work. Reasons for this decision:
   - Should work better than the simple bounding box approach
 - For the recognition process using the contour, to recognize a square object is easier than to recognize round objects.
 - Since the size and solidity of objects are not fixed enough under different conditions, we decide to abandon those factors in our object recognition process.


- **.GIF Compatibility**
 - We raised the issue of there not being a reliable way to display .gif files in live video stream. Resolved this by trying to doing a frame-by-frame approach. Reasons for this include:
  - Existing approaches already exist for this
  - Does not require extensive “hacks” and workarounds
  - The CV toolbox prepared us well for this approach
 - Things to look out for:
    - Frame rate going too fast to update the images for each one
    - Having to store each of the images to make a .gif


## Process reflection

Overall, this review went relatively well. However, the discussion seemed to take on a circular approach at times. We were also forced to kill the idea of machine learning in favor of a heuristic approach that could possibly allow us to target a specific area of interest with growing accuracy, due to a lack of time. Comments were also brought back on Indico during the review, despite being abandoned since the end of Review I.

We also adhered better to our agenda this time, mostly due to our use of slides. However, we spent a lot more time discussing object recognition than working on gif compatibility, another equally important element of our project with which we were struggling.

The answers to our questions on occasion generated more questions for our team. For example, we still have to grapple with how to effectively use aspect ratio for rectangular objects at an angle, which is an aspect of this code that we had not considered before. We also have to determine the tolerance for using color detection, which we think can be an effective tool for object recognition.

The feedback has certainly helped us realize how daunting the tasks ahead of us are going to be.

We felt that our audience had a firm enough grasp of our project that they could comprehend and provide appropriate feedback for our questions.
