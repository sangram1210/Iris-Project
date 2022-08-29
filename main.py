

from flask import Flask,render_template,request

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/get_data',methods=['POST'])
# def get_data():
#     name1 = request.form['var']
#     roll_no = request.form['var1']
#     print(f"{name1=},{roll_no=}")

#     return "data recieved"

# @app.route('/get_data',methods=['GET','POST'])
# def get_data():
#     name1 = request.form['var']
#     roll_no = request.form['var1']
#     print(f"{name1=},{roll_no=}")

#     return "data recieved"    


# @app.route('/get_data',methods=['GET','POST'])
# def get_data():
#     if request.method == 'POST':
#         name1 = request.form['var']
#         roll_no = request.form['var1']
#         print(f"{name1=},{roll_no=}")
#     else:
#         print("Data not received")

#     return "data recieved"

@app.route('/get_data',methods=['GET','POST'])
def get_data():
    name = request.form['var']
    roll_no = request.form['var1']
    subject = request.form['var2']
    print(name,roll_no,subject)

    return 'data received'




if __name__ == "__main__":
    app.run(debug=True)
