from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        print(f"Message from {name} ({email}): {message}")
    return render_template("contact.html")

@app.route('/resume')
def resume():
    return send_from_directory(directory='.', path='resume.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
