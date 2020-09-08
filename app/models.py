from datetime import datetime
import re
from app import db

def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern,'-',s)

# Creating table for relations db many to many
# post_tags = db.Table('post_tags',
#                         db.Column('post_id',db.Integer,db.ForeignKey('post.id')),
#                         db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
# )

class War(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    body = db.Column(db.Text)
    image = db.Column(db.String(40),nullable=False,default='default.jpg')
    slug = db.Column(db.String(140), unique=True)
    created = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        super(War, self).__init__(*args, **kwargs)
        self.generate_slug()

    # tags = db.relationship('Tag', secondary=post_tags, backref=db.backref('posts', lazy='dynamic'))

    def generate_slug(self):
        if self.title:
            self.slug = ((slugify(self.title)).lower())

    def __repr__(self):
        return '<Post title: {}, id: {}>'.format(self.title,self.id)

# class Tag(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#     slug = db.Column(db.String(100))
#
#     def __init__(self, *args, **kwargs):
#         super(Tag, self).__init__(*args, **kwargs)
#         self.slug = slugify(self.name)
#
#     def __repr__(self):
#         return '{}'.format(self.name)
#
#
#     def generate_slug(self):
#         if self.name:
#             self.slug = ((slugify(self.name)).lower())
# ### Flask security ###
#
# roles_users = db.Table('roles_users',
#                        db.Column('user_id', db.Integer(), db.ForeignKey("user.id")),
#                        db.Column('role_id', db.Integer(), db.ForeignKey("role.id")))
#
#
#
# class User(db.Model,UserMixin):
#     id = db.Column(db.Integer(), primary_key=True)
#     email = db.Column(db.String(100), unique=True)
#     password = db.Column(db.String(255))
#     active = db.Column(db.Boolean())
#     roles = db.relationship('Role',secondary=roles_users, backref=db.backref('users',lazy='dynamic'))
#
#
#
#
# class Role(db.Model,RoleMixin):
#     id = db.Column(db.Integer(), primary_key=True)
#     name = db.Column(db.String(100), unique=True)
#     description = db.Column(db.String(255))