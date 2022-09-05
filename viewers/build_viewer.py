"""
@File : build_viewer.py
@Date : 2022/9/2 17:34
@Author: 九层风（YePing Zhang）
@Contact : yeahcheung213@163.com
"""

from sanic import Blueprint
from sanic_openapi import openapi

from controller.response_encapsulate import *
from controller.auth import protected
from models.build_model import BuildModel

"""获取测试程序版本信息"""
build_bp = Blueprint('build_bp', url_prefix='/api/build')


# 查询版本信息
@build_bp.route('GetInfo', methods=['GET'])
@openapi.tag("程序版本信息")
@openapi.summary("查询")
@openapi.parameter("id", int, location="query")
@protected
async def get_build_info(request):
	resp = BuildModel().get_info(request.args.get('id'))
	if resp:
		return resp_200(resp.to_dict(), f"查询到id:{resp.id}的版本信息")
	else:
		return resp_200({}, message=f"暂未查询到id:{resp.id}的版本信息", status=False)


if __name__ == "__main__":
	pass
