from flask import render_template,Blueprint , request , session ,flash , redirect , url_for
from data import add_blogs , get_blogs
import os
from werkzeug.utils import secure_filename
blog_bp=Blueprint("blogs",__name__)

folder_name_for_image="static/image_folder"
#folder_name_for_audio="static/audio_folder"
# create folders if not exist
os.makedirs(folder_name_for_image, exist_ok=True)
#os.makedirs(folder_name_for_audio, exist_ok=True)
# Allowed extensions
allowed_image_extensions = {"png", "jpg", "jpeg", "gif"}
allowed_audio_extensions = {"mp3", "mp4", "wav", "m4a"}
def allowed_file(file_name,extensions):
    if file_name.rsplit(".",1)[1].lower() in extensions:
        return file_name
    else:
        return False
@blog_bp.route("/blogs" , methods=["GET","POST"])
def blogs():
    if request.method=="POST" :
        if session.get("is_user")==True:
            title=request.form["title"]
            content=request.form.get("content")
            image_file=request.files.get("image_file")
            audio_file=request.files.get("audio_file")
            image_path=None
            audio_path=None
            #save photos
            if image_file and allowed_file(image_file.filename,allowed_image_extensions):
                secure_image= secure_filename(image_file.filename)         
                image_file.save(os.path.join(folder_name_for_image,secure_image))
                # image_path=os.path.join(folder_name_for_image,secure_image)
                image_path=secure_image
             #save audio
            if audio_file and allowed_file(audio_file.filename,allowed_audio_extensions):
                secure_audio=secure_filename(audio_file.filename)
                audio_file.save(os.path.join(folder_name_for_audio,secure_audio))
                # audio_path=os.path.join(folder_name_for_audio,secure_audio)
                audio_path=secure_audio
            add_blogs(title=title , content=content , image=image_path , audio=audio_path )
            return redirect(url_for("blogs.blogs"))
        else:
            flash("You must log in first" , "blogs")
            return redirect(url_for("blogs.blogs"))
    return render_template("blogs.html" , blogs= get_blogs())

