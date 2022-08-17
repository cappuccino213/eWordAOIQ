"""
@File : user_model.py
@Date : 2022/8/3 14:19
@Author: 九层风（YePing Zhang）
@Contact : yeahcheung213@163.com
"""
from sqlalchemy import Column, Integer, String, Enum

from models.db_engine import *
from controller.log_loguru import logging

import hashlib

"""定义用户模型"""


class UserModel(Base):
	__tablename__ = 'zt_user'

	id = Column(Integer, autoincrement=True, primary_key=True)
	dept = Column(Integer)
	account = Column(String(30), unique=True)
	password = Column(String(32))
	role = Column(String(10))
	realname = Column(String(100))
	nickname = Column(String(60))
	gender = Column(Enum('f', 'm'))
	mobile = Column(String(11))
	email = Column(String(90))
	qq = Column(String(20))
	address = Column(String(120))
	deleted = Column(Enum('0', '1'))

	# 用将单条数据列转换成dict
	def to_dict(self):
		return {column.name: getattr(self, column.name, None) for column in
				self.__table__.columns}  # 如果有时间戳需要加处理，https://blog.csdn.net/baidu_36943075/article/details/101053734

	# 将多条数据转化成json
	@staticmethod
	def to_json(all_vendors):
		return [vendor.to_dict() for vendor in all_vendors]

	# 验证密码是否匹配
	@staticmethod
	def if_password_match(cleartext_password, cipher_password):
		ciphertext = hashlib.md5(cleartext_password.encode('utf-8')).hexdigest()
		if cipher_password == ciphertext:
			logging.info("密码匹配")
			return True
		else:
			logging.error("密码不匹配")
			return False

	"""CRUD的操作"""

	# 根据账号查询用户信息
	@classmethod
	def get_userinfo_by_account(cls, account: str):
		try:
			with Session() as session:
				return session.query(cls).filter(cls.account == account, cls.deleted == '0').first()
		except Exception as e:
			logging.error(str(e))
			return None

	# 查询用户列表
	@classmethod
	def multiple_condition_query(cls, condition: dict):
		try:
			with Session() as session:
				result = session.query(cls).filter(cls.deleted == '0', cls.role != 'ud')  # 过滤掉角色是ui设计的，以防止没有数据报错
				if condition.get('id'):
					result = result.filter(cls.id == condition.get('id'))
				if condition.get('dept'):
					result = result.filter(cls.dept == condition.get('dept'))
				if condition.get('account'):
					result = result.filter(cls.account == condition.get('account'))
				if condition.get('role'):
					result = result.filter(cls.role == condition.get('role'))
				if condition.get('gender'):
					result = result.filter(cls.gender == condition.get('gender'))
				return result.all()
		except Exception as e:
			logging.error(str(e))
			return None


if __name__ == "__main__":
	m = UserModel()
	# print(um.get_userinfo_by_account('zhangl'))
	res = m.multiple_condition_query({"account": "zyp"})
