from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route("/user/<username>")
def show_username(username):
    return f"hello {username}"

@app.route("/success/<name>")
def success(name):
    # return render_template('login.html')
    return render_template("index.html", result=f"welcome {name}")
    # return f"welcome {name}"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for('success', name=user))
    else:
        # return 'test2'
        user = 'test'
        return redirect(url_for('success', name=user))


@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]

            if operation == "add":
                result = num1 + num2
            elif operation == "sub":
                result = num1 - num2
            elif operation == "mul":
                result = num1 * num2
            elif operation == "div":
                result = "Error" if num2 == 0 else num1 / num2
        except:
            result = "Invalid input"
    elif request.method == "GET":
        result = 'This is get method'

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run()
