from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Users/Lenovo/Desktop/TODOAP/todo.db"
db = SQLAlchemy(app)

# sqlalchemy create table (class yaratmaqla db de tablolar creat olunur)
class Tododb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)

#complete template
@app.route("/complete/<string:id>")
def complete(id):
    todo = Tododb.query.filter_by(id = id).first()

    """if todo.complete == True:
        todo.complete = False
    else:
        todo.complete = True """
    todo.complete = not todo.complete

    db.session.commit()
    return redirect(url_for("index"))       

@app.route("/")
def index():
    #todo.db sqlalchemy (deyelerin hamisi getirilir)
    todos = Tododb.query.all()
    return render_template("index.html", todos = todos)


# add template
@app.route("/add", methods = ["POST"])
def addTodo():
    title = request.form.get('title')
    newTodo = Tododb(title = title , complete = False)

    db.session.add(newTodo)
    db.session.commit()  

    return redirect(url_for("index"))

#delete template
@app.route("/delete/<string:id>")
def delete(id):
    del_todo = Tododb.query.filter_by(id = id).first()

    db.session.delete(del_todo)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)



