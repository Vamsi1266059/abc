from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")  # Main page with all sections (About, Skills, Projects, etc.)

# Optional: If you want to serve each section as a page (not necessary if it's a single scroll page)
@app.route('/about')
def about():
    return render_template("index.html", section="about")

@app.route('/projects')
def projects():
    return render_template("index.html", section="projects")

@app.route('/contact')
def contact():
    return render_template("index.html", section="contact")

if __name__ == "__main__":
    app.run(debug=True)
