from cProfile import label
import json
import base64

def modelassist(detectionsList, imgPath, savePath, imgHeight, imgWidth, labelName):
    imgString = get_base64_encoded_image("./model_ast/" + imgPath)
    dct = {"version": "5.0.1",
        "flags": {},
        "shapes":[],
        "imagePath":imgPath,
        "imageData":imgString,
        "imageHeight": imgHeight,
        "imageWidth": imgWidth}
    
    for detection in detectionsList:
        dct['shapes'].append({'label': labelName,'points':detection,"group_id": None,"shape_type": "polygon",
        "flags": {}})
        
    out_file = open(savePath, "w")
  
    json.dump(dct, out_file, indent = 4)
  
    out_file.close()

def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')  