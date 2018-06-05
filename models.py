# the solders in the Storm Winds listen to me
from flask_sqlalchemy import SQLAlchemy

from manage import app

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(20))

    phone = db.Column(db.String(12))

    def __repr__(self):
        return '\n{} {} {}'.format(self.id, self.name, self.phone)


class Music(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    name = db.Column(db.String(50))  # 歌曲名
    singer = db.Column(db.String(20))  # 歌手信息

    brand = db.Column(db.String(50))  # 歌曲流派

    mp3_path = db.Column(db.String(100))  # 歌曲路径

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    user = db.relationship('User', backref=db.backref('music', lazy=True))


class Image(db.Model):  # 图库模型目前和用户没有关系
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    name = db.Column(db.String(50))  # 图片的名称

    url = db.Column(db.String(200))  # 图片的路径

    # 建立和用户的多对多关系， 一个用户可以收藏图片，一张图片可以被多个用户收藏
    # 建立第三方表，这个多对多得自己建立一张表


class Collect(db.Model):  # 图片收藏类
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    img_id = db.Column(db.Integer, db.ForeignKey('image.id'))



# mysql数据库配置命令
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/flask'
# # SQlALCHEMY_TRACK_MODIFICATIONS = False



















