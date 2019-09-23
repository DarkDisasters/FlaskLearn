from flask import Flask
# from config import DEBUG

app = Flask(__name__)
app.config.from_object('config')        #载入配置文件
print(app.config)



# 使用装饰器来注册路由
@app.route('/hello')
def hello():
    #基于类的视图
    # 1/0
    return '咳咳'

# 另一种注册路由得方式
# app.add_url_rule('/hello', view_func=hello)

# 将debug设置为True开启flask的调试模式，使得程序自动程序，避免每次修改后都要重启python程序
if __name__ == '__main__':
    # 在生产环境通常由 nginx+uwsgi 部署项目(nginx作为前置服务器接受浏览器发来的请求，然后发给uwsgi)，
    # 不会用Flask自带的Web服务器，这个文件不再是入口文件，而是作为被config.pyuwsgi加载的模块
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)