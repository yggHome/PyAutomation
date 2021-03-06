__author__ = 'Administrator'
'''
1）新建一个unittest类，对获取用户信息接口进行单元测试
2）runcase循环类，修改函数，引入测试套件
3）注意super写法
'''

from Frame5.runcase import Runcase
from Frame5.database import Database
from Frame5.HttpRequest import HttpRequest
from Frame5.mode import Mode

#定义主函数
if __name__ == "__main__" :
    path_http = "http.conf"
    path_db = "db.conf"
    path_mode = "mode.conf"

    http = HttpRequest(path_http)
    cnn = Database(path_db).connect_db()
    mode = Mode(path_mode)

    runcase = Runcase()
    runcase.run_Case(http, cnn, mode)