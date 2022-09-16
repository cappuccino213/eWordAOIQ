"""
@File : response_encapsulate.py
@Date : 2022/8/4 9:36
@Author: 九层风（YePing Zhang）
@Contact : yeahcheung213@163.com
"""
from sanic import response
from typing import Union

"""响应体封装"""


# 200
def resp_200(data: Union[list, dict, str], message="Success", status=True, token=None):
	return response.json(
		body={'code': 200, 'message': message, 'data': data, 'status': status, 'token': token}
	)


# 204
def resp_204(message="No Content", status=True, token=None):
	return response.json(
		body={'code': 204, 'message': message, 'data': None, 'status': status, 'token': token}
	)


# 204
def resp_422(message="UNPROCESSABLE ENTITY ", status=False, token=None):
	return response.json(
		body={'code': 422, 'message': message, 'data': None, 'status': status, 'token': token}
	)


if __name__ == "__main__":
	pass
