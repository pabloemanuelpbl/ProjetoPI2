from application import app
from flask import render_template

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

#dashboard
@app.route("/dashboard")
def dashboard():
    return render_template("user/dashboard.html")

@app.route("/dashboard/clientes")
def listar_clientes():
    return render_template("user/clientes.html")

@app.route("/dashboard/cadastrarclientes")
def cadastrarclientes():
    return render_template("user/cadastrarclientes.html")

@app.post("/dashboard/cadastrarclientes")
def clientes_post():
    return "<script>document.location.href = '/dashboard' </script>"


@app.get("/login")
def login():
    return render_template("user/login.html")

@app.post("/login")
def login_post():
    return "<script>document.location.href = '/dashboard' </script>"