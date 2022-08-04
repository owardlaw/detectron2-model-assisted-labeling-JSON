# detectron2-model-assisted-labeling-JSON

This is an example of model assisted labeling for detectron2. This function will take a 2D array of (X,Y) cordinates per detection and write them and a base64 image into JSON similar to the output of labelme. For example, polygon cordinates can be appeneded to a 2D array and then used as the detectionsList. 

!! Cordinates must be added in a clockwise or counter clockwise manner or JSON will output an issue !!

```       Ex.
    <--------
    * * * * *   ^
| *           * |
| *           * |
| *           * |
V   * * * * * 
    -------->
```

You can check the output with LabelMe. 

# Usage
def modelassist(detectionsList, imgPath, savePath, imgHeight, imgWidth, labelName):

detectionsList = 2D array of polygon cordinates
imgPath = path to image (used for base64 encoding)
savePath =  where to save JSON output 
imgHeight = image height
imgWidth = image width
labelName = string, class of label (ex. car, house, dog)
