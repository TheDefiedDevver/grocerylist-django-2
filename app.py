from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)       # Creates instance for file class

# STATIC ROUTE

# @app.route("/")
# def index():
#     return "This is the home page '/' "

# @app.route("/hello")
# def hello():
#     return "This is the '/hello' route!"

# # DYNAMIC ROUTE (CHANGEABLE ANGLE BRACKETS!)

# @app.route("/hello/<name>")
# def hellothere(name):
#     return f"Hello, {name}!"

# @app.route("/post/<int:post_id>")
# def show_post(post_id):
#     return f"Post {post_id}"

# Grocer's List App

groceryList = ["Fries"]

@app.route("/", methods=["GET"])       # GET = Retrieve something
def index():
    return render_template('index.html', groceryList = groceryList, enumerate=enumerate)

@app.route("/add_groceryItem", methods=["POST"])
def add_groceryItem():
    groceryItem = request.form["item"]
    groceryList.append(groceryItem)
    return redirect(url_for("index"))

@app.route("/delete_groceryItem/<int:item_index>", methods=["POST"])
def delete_groceryItem(item_index):
    groceryList.pop(item_index)
    return redirect(url_for("index"))



if __name__ == "__main__":
    app.run(debug=True) ;   # for detailed automatic error when changes are made

