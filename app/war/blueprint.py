from app import app,db,my_background_task
from models import War
from .forms import WarForm
from werkzeug.utils import secure_filename
from flask_uploads import configure_uploads, IMAGES, UploadSet
from flask import Blueprint, render_template,request,redirect,url_for
import time
war = Blueprint('war', __name__, template_folder="templates")
images = UploadSet('war',IMAGES)
configure_uploads(app, images)

@war.route('/news',methods=['GET','POST'])
def create_news():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        description = request.form['description']
        file = request.files['image']
        if file.filename != '':
            filename = secure_filename(file.filename)
            file.filename = f'{str(time.time())}_.{filename}'
            # my_background_task(1, 1).delay()
            images.save(file)
            news = War(title=title,body=body,description=description,image=file.filename)
            db.session.add(news)
            db.session.commit()
        return redirect(url_for('index'))
    form = WarForm()
    return render_template('war/index.html',form=form)

# @war.route('/')
# def displayed():
#     file_path = "static/images/war/"
#     q = request.args.get('q')
#     page = request.args.get('page')
#
#     if page and page.isdigit():
#         page = int(page)
#     else:
#         page = 1
#
#     if q:
#         posts = War.query.filter(War.title.contains(q) | War.body.contains(q))#.all()
#     else:
#         posts = War.query.order_by(War.created.desc())
#     pages = posts.paginate(page=page,per_page=1)
#     return render_template('war/displaying_news.html',war=war,pages=pages,file_path=file_path)

@war.route('/<int:page_num>')
def displayed(page_num):
    file_path = "static/images/war/"
    war = War.query.paginate(page=page_num,per_page=1,error_out=True)
    return render_template('war/displaying_news.html',war=war,file_path=file_path)