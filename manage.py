# 启动文件
from ccms import app
from ccms.view import SystemView


if __name__ == '__main__':
    app.run(port=8080, debug=True)

