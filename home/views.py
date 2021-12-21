from django.shortcuts import render,HttpResponse
from django.core.files.storage import FileSystemStorage
from home.models import FeedBacks
from django.contrib import messages
import requests
# from keras.models import load_model
# from keras.preprocessing import image
# import tensorflow.compat.v1 as tf
# from keras.preprocessing.image import img_to_array         
# from keras.preprocessing.image import load_img     
# import json
# from tensorflow import Graph    


# img_height, img_width=224,224
# with open('./models/covidlabels.json','r') as f:
#     labelInfo=f.read()

# labelInfo=json.loads(labelInfo)


# model_graph = Graph()
# with model_graph.as_default():
#     tf_session =tf.compat.v1.Session()
#     with tf_session.as_default():
#         model=load_model('./models/cnncovid5.h5')      


# Create your views here.*args
def index(request):
    data = True
    result = None
    while (data):
        try:
            result = requests.get('https://api.covid19api.com/summary')
            # result2 = requests.get('http://coronavirus-tracker-india-covid-19.p.rapidapi.com/api/getStatewise')
            # js2 = result2.json()
            js = result.json() 
            globaldata = js['Global'] 
            countriesdata = js['Countries']
            # countriesdata = countriesdata1['{"Country":"India"}']
            # print(js2)
            # print(countriesdata)
            data = False
        except:
            data = True

    return render(request,'index.html' ,{'globaldata' : globaldata,'countrydata':countriesdata})
   

def about(request):
    return render(request,'about.html')

def resources(request):
    return render(request,'resources.html')

# def model(request):
#     return render(request,'model.html')


# def predictImage(request):
#     print (request)
#     print (request.POST.dict()) 
#     fileObj=request.FILES['filePath']
#     fs=FileSystemStorage()
#     filePathName=fs.save(fileObj.name,fileObj)
#     filePathName=fs.url(filePathName)
#     testimage='.'+filePathName
#     img = image.load_img(testimage, target_size=(img_height, img_width))
#     x = image.img_to_array(img)
#     x=x/255
#     x=x.reshape(3,img_height, img_width,1)
#     with model_graph.as_default():
#         with tf_session.as_default():
#             predi=model.predict(x)

#     import numpy as np
#     predictedLabel=labelInfo[str(np.argmax(predi[0]))]

#     context={'filePathName':filePathName,'predictedLabel':predictedLabel[1]}
#     return render(request,'index.html',context) 


def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        email =  request.POST.get('email','')
        desc =  request.POST.get('desc','')
        feedback = FeedBacks(name=name,email=email,desc=desc)
        feedback.save()
        messages.success(request, 'Feedback added Successfully')
    return render(request,"resources.html")

















# # img_height, img_width=224,224
# # with open('./models/covidlabels.json','r') as f:
# #     labelInfo=f.read()

# # labelInfo=json.loads(labelInfo)


# model_graph = Graph()
# with model_graph.as_default():
#     tf_session = tf.compat.v1.Session()
#     with tf.compat.v1.Session():
#         model=load_model('./models/cnncovid5.h5')


# def predictImage(request):
#     print (request)
#     print (request.POST.dict())
#     fileObj=request.FILES.POST['filePath']
#     fs=FileSystemStorage()
#     filePathName=fs.save(fileObj.name,fileObj)
#     filePathName=fs.url(filePathName)
#     testimage='.'+filePathName
#     img = image.load_img(testimage, target_size=(img_height, img_width))
#     x = image.img_to_array(img)
#     x=x/255
#     x=x.reshape(1,img_height, img_width,3)
#     with model_graph.as_default():
#         with tf_session.as_default():
#             predi=model.predict(x)

#     # import numpy as np
#     # predictedLabel=labelInfo[str(np.argmax(predi[0]))]

#     context={'filePathName':filePathName,'predictedLabel':predictedLabel[1]}
#     return render(request,'model.html',context) 
