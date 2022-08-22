"""
@File : version_info_viewer.py
@Date : 2022/8/17 16:56
@Author: 九层风（YePing Zhang）
@Contact : yeahcheung213@163.com
"""
from sanic import Blueprint
from sanic_openapi import openapi

from config import VERSION_INFO
from controller.response_encapsulate import *

"""版本信息"""
version_bp = Blueprint('version_bp', url_prefix='/api/VersionInfo')


# 获取用户列表
@version_bp.route('/', methods=['get'])
@openapi.tag("版本信息")  # API标签
@openapi.summary("获取版本信息")  # API信息描述
async def get_version_info(request):
	return resp_200(VERSION_INFO)


if __name__ == "__main__":
	pass
