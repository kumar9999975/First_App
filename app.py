from flask import Flask, request, session, redirect, url_for, Response

app = Flask(__name__)
app.secret_key = "super-secret-key"  # Change this to a random secret value for production
app.secret_key = "change-this-to-a-random-secret-value"  # required for sessions

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "admin":
            session["username"] = username
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid username or password", mimetype="text/html")

    return '''
    <h2>Login Form</h2>
    <form method="POST">
        UserName:<input type="text" name="username"><br><br>
        Password:<input type="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
    '''

@app.route("/welcome")
def welcome():
    if "username" in session:
        return f'''
        <h2>Welcome, {session['username']}!</h2>
        <a href="{url_for("logout")}">Logout</a>
        '''
    else:
        return redirect(url_for("login"))
    
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)