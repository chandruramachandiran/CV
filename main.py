from flask import Flask,render_template,send_file
app=Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')
@app.route('/download',methods=['GET'])
def res():
    return send_file('CV-CHANDRU.pdf',as_attachment=True)
app.run(debug=True)

