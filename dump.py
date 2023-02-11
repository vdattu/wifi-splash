from flask import Flask,request
import json,time
import os
import wget 
app = Flask(__name__)
#@app.route('/',methods=["GET","POST","DELETE"])
@app.route('/<string:id>',methods=["GET","POST","DELETE"])
def dat_traf(id):
    if request.method=='POST':
        data=request.data
        dat_lst=eval(data)
        print(dat_lst)
        if dat_lst:
            pat=os.path.join("path/image",id)
            os.remove(pat)
            for j in dat_lst:
                wget.download(j,'path//image')
                print("list downloaded")
            return "--successfully downloaded-----"
        else:
            return "NO Data Found"
    return "This App is Running & FIles Downloading Successfully"
        
    
if (__name__)=="__main__":
    app.run(host='0.0.0.0',port='5002')

