from flask import Flask, request, Response, render_template
from flask_restful import Api


app=Flask(__name__)
api=Api(app)


@app.route("/")
def Home():
	return render_template("index.html")



if __name__=='__main__':
	app.run(debug=True)
