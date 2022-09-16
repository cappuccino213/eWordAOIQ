"""
@File : product_viewer.py
@Date : 2022/8/8 16:03
@Author: 九层风（YePing Zhang）
@Contact : yeahcheung213@163.com
"""
from sanic import Blueprint
from sanic_openapi import openapi

from models.testtask_model import *
from models.request_schema import TestTaskList
from controller.response_encapsulate import *
from controller.auth import protected

"""测试单"""
testtask_bp = Blueprint('testtask_bp', url_prefix='/api/TestTaskList')


# 获取测试单列表
@testtask_bp.route('list', methods=['POST'])
@openapi.tag("测试单")  # API标签
@openapi.summary("获取测试单列表")  # API信息描述
@openapi.body({"application/json": TestTaskList}, description="参数均为选填", required=True)
@protected
async def get_testtask_list(request):
	resp = TestTaskModel().get_testtask_list(id=request.json['id'],
											 product=request.json['product'],
											 owner=request.json['owner'],
											 subStatus=request.json['subStatus'],
											 begin=request.json['begin'],
											 end=request.json['end'])
	if resp:
		return resp_200(TestTaskModel().to_json(resp))
	else:
		return resp_204()


if __name__ == "__main__":
	pass
