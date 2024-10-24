from flask import Flask, render_template, request, redirect, url_for
from backend import converter, file_validator

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files['file']
        format = request.form['format']
        file.save(file.filename)

        valid, message = file_validator.validate_file(file.filename)
        if not valid:
            return message, 400

        if format in ['jpeg', 'png', 'gif']:
            output_file = converter.convert_image(file.filename, format)
        elif format in ['mp3', 'wav', 'flac']:
            output_file = converter.convert_audio(file.filename, format)
        else:
            output_file = converter.convert_video(file.filename, format)

        return redirect(url_for('download_file', filename=output_file))

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
