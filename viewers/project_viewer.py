"""
@File : project_viewer.py
@Date : 2022/8/8 16:03
@Author: 九层风（YePing Zhang）
@Contact : yeahcheung213@163.com
"""
from sanic import Blueprint
from sanic_openapi import openapi

from models.project_model import *
from controller.response_encapsulate import *
from controller.auth import protected

"""用户相关"""
project_bp = Blueprint('project_bp', url_prefix='/api/project')


# 获取用户列表
@project_bp.route('list', methods=['GET'])
@openapi.tag("项目")  # API标签
@openapi.summary("获取项目列表")  # API信息描述
@protected
async def get_projects_list(request):
	resp = ProjectModel().get_project_list()  # json表示传入的对象时dict
	if resp:
		return resp_200(ProjectModel().to_json(resp))
	else:
		return resp_204()


if __name__ == "__main__":
	pass
