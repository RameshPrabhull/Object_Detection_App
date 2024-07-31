import streamlit as sl
import cv2 as c
from objectdetection_tf import objectDetection
sl.title("Data Extraction from Image and Enhancement")
cont1=sl.container()
with cont1:
    sl.header("Select Image to Extract Data")
    im_path=sl.text_input("Path",placeholder="Enter Image Path",label_visibility="hidden")
obj=objectDetection(im_path)
if(not im_path==""):
        try:
            originalArray=c.imread(im_path)
            originalArray=c.cvtColor(originalArray,c.COLOR_BGR2RGB)
            im_arr,data,dList,dataPoints=obj.inputImage()
            dList=list(dList)
            cont2=sl.container()
            cont2.image(im_arr,channels="RGB")
            cont3=sl.container()
            with cont3:
                sl.header("Data Extracted from the above image")
                sl.dataframe(data)
            cont4=sl.container()
            cont5=sl.container()
            with cont4:
                sl.header("Select Object for further enhancement")
                def expand(object):
                    for i,x in enumerate(dataPoints[object]):
                        extImg=originalArray[x[1]:x[3],x[0]:x[2]]
                        extImg=c.GaussianBlur(extImg,(5,5),0)
                        cont4.image(extImg)
                for l in dList:
                    sl.button(l,on_click=expand,args=(l,))
        except(KeyError):
            print(KeyError)
            sl.header("Oops!! The image path seems to be incorrect...Try Other Images")

            


