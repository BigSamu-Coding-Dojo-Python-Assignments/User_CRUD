from flask import Flask, render_template, request, redirect
# import the class from friend.py
from user import User
app = Flask(__name__)

@app.route('/users')
def index():
    all_users = User.get_all()
    return render_template("index.html", users_info = all_users)

@app.route('/users/<int:id>')
def show_user(id):
    data = {
        "id": id
    }
    selected_user = User.get_one(data)
    return render_template("show_user.html", user_info = selected_user)

@app.route('/users/new', methods=["GET","POST"])
def create_user():

    if(request.method == "POST"):
        data = {
            "first_name": request.form["first_name"],
            "last_name" : request.form["last_name"],
            "email" : request.form["email"]
        }
        User.save(data)
        return redirect('/users')

    return render_template("new_user.html")

@app.route('/users/<int:id>/edit', methods=["GET","POST"])
def edit_user(id):
    
    if(request.method == "POST"):
        data = request.form
        print(data)
        User.update(data)
        return redirect('/users')

    data = {
        "id": id
    }
    selected_user = User.get_one(data)
    return render_template("edit_user.html", user_info = selected_user)

@app.route('/users/<int:id>/delete')
def delete_user(id):
    
    data = {
        "id": id
    }
    selected_user = User.destroy(data)
    return redirect('/users')
            
if __name__ == "__main__":
    app.run(debug=True)

