"""
@File : static_viewer.py
@Date : 2022/8/11 11:27
@Author: 九层风（YePing Zhang）
@Contact : yeahcheung213@163.com
"""
from sanic import Blueprint, response

"""静态资源相关"""
sbp = Blueprint('sbp', url_prefix='/')
sbp.static("/", "./static/index.html")
sbp.static("/assets", "./static/assets", content_type="*/*")
#
# @sbp.route('/')
# async def index_request(request):
# 	return await response.file('../static/index.html')


if __name__ == "__main__":
	pass
