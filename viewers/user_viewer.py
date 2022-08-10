"""
@File : user_viewer.py
@Date : 2022/8/3 17:32
@Author: 九层风（YePing Zhang）
@Contact : yeahcheung213@163.com
"""
from sanic import Blueprint
from sanic_openapi import openapi

from models.user_model import *
from models.request_schema import UserBody, LoginBody
from controller.response_encapsulate import *

"""用户相关"""
user_bp = Blueprint('user_bp', url_prefix='/api/user')


async def get_user_info():
	pass


# 获取用户列表
@user_bp.route('list', methods=['POST'])
@openapi.tag("用户")  # API标签
@openapi.summary("获取用户列表")  # API信息描述
@openapi.body({"application/json": UserBody},
			  description="所有参数都是可选项，可以不传或者传空字符，dev=3，开发，dev=4测试",
			  required=True)
async def get_user_list(request):
	resp = UserModel().multiple_condition_query(request.json)  # json表示传入的对象时dict
	if resp:
		return resp_200(UserModel().to_json(resp))
	else:
		return resp_204()


# 登录接口
@user_bp.route('login', methods=['POST'])
@openapi.tag("用户")
@openapi.summary("用户登录")
@openapi.body({"application/json": LoginBody},
			  description="用户密码不能为空",
			  required=True)
async def user_login(request):
	user_info = UserModel().get_userinfo_by_account(request.json['account'])
	if user_info:
		if UserModel().if_password_match(request.json['password'],user_info.password):
			return resp_200(user_info.to_dict(), message="登录成功")
		else:
			return resp_200({}, message="用户名或密码错误",status=False)
	else:
		return resp_200({}, message="用户名或密码错误",status=False)


if __name__ == "__main__":
	pass
