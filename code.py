from flask import Flask, render_template

app = Flask(__name__)

@app.route("/form")
def student_app():
    name = "Sukruthi"
    return render_template("index.html", name = name)

app.run(debug=True)