"""
@File : auth.py
@Date : 2022/8/12 11:10
@Author: 九层风（YePing Zhang）
@Contact : yeahcheung213@163.com
"""
from functools import wraps

from sanic import text

from config import AUTH

import jwt


def check_token(request):
	"""校验token是否有效，有效会返回解密数据"""
	if not request.token:
		return False
	try:
		jwt.decode(
			request.token, request.app.config.SECRET, algorithms=["HS256"]
		)
	except jwt.exceptions.InvalidTokenError:
		return False
	else:
		return True


def protected(wrapped):
	"""token校验装饰器"""
	def decorator(f):
		@wraps(f)
		async def decorated_function(request, *args, **kwargs):
			"""根据配置文件是否开启授权"""
			if AUTH.get('IF_AUTH'):
				is_authenticated = check_token(request)
				if is_authenticated:
					response = await f(request, *args, **kwargs)
					return response
				else:
					return text("未获得授权", 401)
			else:
				return await f(request, *args, **kwargs)
		return decorated_function

	return decorator(wrapped)


if __name__ == "__main__":
	pass
