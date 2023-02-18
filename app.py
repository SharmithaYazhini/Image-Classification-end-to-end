from flask import Flask, render_template, request
#from keras.models import load_model
#from keras.preprocessing import image

app = Flask(__name__)

dic = {0:"Positive",1:"Negative"}

#model = load_model("model.h5")

#model.make_predict_function()

#def predict_label(image_path):
    #i= image.load_img(image_path,target_size=(100,100))
    #i= image.img_to_array(i)/255.0
    #i=i.reshape(1,100,100,3)
    #p =model.predict_classes(i)
    #return dic[p[0]]

@app.route("/",methods=["GET"])
def hello_world():
    return render_template("index.html")

@app.route("/submit",methods=["POST"])
def predict():
    imagefile=request.files["my_image"]
    image_path="./static/" + imagefile.filename
    imagefile.save(image_path)
    #p=predict_label(image_path)
    
    return "Running"
    #return render_template("index.html",prediction=p,img_path=image_path)
    
if __name__ =='__main__':
	#app.debug = True
	app.run(port=3000, debug = True)