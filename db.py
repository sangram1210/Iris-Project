
from flask import Flask,render_template,request,jsonify

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/student_detail',methods=['POST'])
def student_detail():
    s_name = request.form['student_name']
    s_rollno = request.form['student_rollno']
    sub1 = request.form['sub_1']
    sub2 = request.form['sub_2']
    sub3 = request.form['sub_3']

    print(f'Student Name {s_name}')
    return jsonify(s_name)

if __name__ == "__main__":
    app.run(debug=True)