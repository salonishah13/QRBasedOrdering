from flask import Blueprint, render_template,request,redirect,url_for
from flask_login import  login_required, current_user
views= Blueprint('views',__name__)
from website import auth
import qrcode
from io import BytesIO
import base64
import io


@views.route('/')
@login_required
def home():
    return render_template("home.html",user=current_user) #gives info about current user


@views.route("/qrpage")
def index():
    return render_template("index.html")


@views.route("/generate", methods=["POST"])
def generate():
    data = request.form["data"]
    img = qrcode.make(data)
    img_io = io.BytesIO()
    img.save(img_io, "PNG")
    img_io.seek(0)
    return redirect(url_for('views.show_qr', img_uri=img_io.getvalue()))

@views.route("/qr/<img_uri>")
def show_qr(img_uri):
    return render_template("show_qr.html", img_uri=img_uri)












'''@views.route('/qrpage')
def index():
  return  render_template("index.html")

@views.route('/generate', methods=['POST'])
def generate():
    # Get the data from the form
    data = request.form['data']

    # Generate the QR code image
    img = qrcode.make(data)

    # Serve the image as a PNG file
    return serve_pil_image(img)
   



# Define a function to serve a PIL image as a PNG file
def serve_pil_image(pil_img):
    from io import BytesIO
    from flask import send_file
    img_io = BytesIO()
    pil_img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')'''
    