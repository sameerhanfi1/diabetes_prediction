
# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from flask import Flask, redirect, url_for, render_template, request, session



data = pd.read_csv("pima-data.csv")

#data.describe()

data = data.drop(["num_preg","thickness","skin"], axis = 1)



#data.head()
#converting data into float
data1 = data.astype("float32")

#data1.head()

#splitted target values and training data
y = data1["diabetes"]
x = data1.drop("diabetes", axis =1)

#print(y)

#splitting into training and testing data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)


#training and building model
model = LogisticRegression()

model.fit(x_train, y_train)

#predicting data
pred = model.predict(x_test)

#pred


#accurac
accuracy_score(y_test,pred)

#print(type(x_test))

#data1.head()

#glucose_conc = [148]





#DF



#print(pred1[0])



app = Flask(__name__)

app.secret_key = "heyy"

@app.route("/", methods=["POST", "GET"])
def search():
    if request.method == "POST":
        glucose_conc = [request.form["glucose_conc"]]
        diastolic_bp = [request.form["diastolic_bp"]]
        insulin = [request.form["insulin"]]
        bmi = [request.form["bmi"]]
        diab_pred = [request.form["diab_pred"]]
        age = [request.form["age"]]

        DF = pd.DataFrame()
        DF['glucose_conc'] = glucose_conc
        DF['diastolic_bp'] = diastolic_bp
        DF['insulin'] = insulin
        DF['bmi'] = bmi
        DF['diab_pred'] = diab_pred
        DF['age'] = age
        
        pred1 = model.predict(DF)
        
        finalans = int(pred1[0])
        if finalans==1:
            session["home"]="You Have Diabetes!!!!! "
        elif finalans==0:
            session["home"]="Congrats !! You Don't Have Diabetes"
        
        #session["home"] = finalans
            
        return redirect(url_for("final"))
    else:
        return render_template("search.html")

@app.route("/result")
def final():
    if "home" in session:
        home = session["home"]
        return render_template("index.html",content=home)
     
if __name__ == "__main__":
    app.run()







