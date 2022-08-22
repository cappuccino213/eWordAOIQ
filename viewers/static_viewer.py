"""
@File : static_viewer.py
@Date : 2022/8/11 11:27
@Author: 九层风（YePing Zhang）
@Contact : yeahcheung213@163.com
"""
from sanic import Blueprint

"""静态资源相关"""
sbp = Blueprint('sbp', url_prefix='/')
sbp.static("/login", "./index.html")
sbp.static("/static/js", "./static/js", content_type="text/javascript")
sbp.static("/static/css", "./static/css")
sbp.static("/static/img", "./static/img")
#
# @sbp.route('/')
# async def index_request(request):
# 	return await response.file('../static/index.html')


if __name__ == "__main__":
	pass
