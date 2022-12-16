from flask import Flask, render_template


app = Flask(__name__)



# shipment list
@app.route("/index", methods= ["GET","POST"])
def index():
	print("hello")
	return render_template("index.html")	



app.run(debug=True)