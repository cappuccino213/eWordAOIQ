"""
@File : product_viewer.py
@Date : 2022/8/8 16:03
@Author: 九层风（YePing Zhang）
@Contact : yeahcheung213@163.com
"""
from sanic import Blueprint
from sanic_openapi import openapi

from models.product_model import *
from controller.response_encapsulate import *

"""用户相关"""
product_bp = Blueprint('product_bp', url_prefix='/api/product')


# 获取用户列表
@product_bp.route('list', methods=['GET'])
@openapi.tag("产品")  # API标签
@openapi.summary("获取产品列表")  # API信息描述
async def get_products_list(request):
	resp = ProductModel().get_product_list()  # json表示传入的对象时dict
	if resp:
		return resp_200(ProductModel().to_json(resp))
	else:
		return resp_204()


if __name__ == "__main__":
	pass
