from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template
from flask_cache import Cache
# from flask.ext.cache import Cache

app = Flask(__name__)

# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/flask'
# SQlALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_DATABASE_URI = 'sqlite:////root/flask/modelsflask/users.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

app.config.from_object(__name__)

# 初始化Bootstrap
Bootstrap(app)

# 创建Cache对象
cache = Cache(app, config={"CACHETYPE": 'simple' })

@cache.cached(timeout=60)
@app.route('/')
def home():
    print('index 查询用户')
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
