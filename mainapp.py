from flask import Flask, request, render_template
import os

from text_model import analyze_text
from image_model import analyze_image 
from url_checker import check_url

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def index():
    result = {}

    if request.method == "POST":
        text = request.form.get("news")
        url = request.form.get("url")
        image = request.files.get("image")

        if text:
            result["text"] = analyze_text(text)

        if url:
            result["url"] = check_url(url)

        if image:
            path = os.path.join(UPLOAD_FOLDER, image.filename)
            image.save(path)
            result["image"] = analyze_image(path)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
