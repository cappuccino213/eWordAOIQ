"""
@File : product_model.py
@Date : 2022/8/8 15:48
@Author: 九层风（YePing Zhang）
@Contact : yeahcheung213@163.com
"""
from sqlalchemy import Column, Integer, String, Enum

from models.db_engine import *
from controller.log_loguru import logging

"""定义产品映射"""


class ProductModel(Base):
	# __bind_key__ = 'zentao'
	__tablename__ = 'zt_product'

	id = Column(Integer, autoincrement=True, primary_key=True)
	name = Column(String(90))
	code = Column(String(45))
	status = Column(String(30))
	desc = Column(String(256))
	PO = Column(String(30))
	QD = Column(String(30))
	RD = Column(String(30))
	deleted = Column(Enum('0', '1'))

	# 用将单条数据列转换成dict
	def to_dict(self):
		return {column.name: getattr(self, column.name, None) for column in
				self.__table__.columns}

	# 将多条数据转化成json
	@staticmethod
	def to_json(all_vendors):
		return [vendor.to_dict() for vendor in all_vendors]

	# 获取未被关闭且未被删除的产品列表
	@classmethod
	def get_product_list(cls):
		try:
			with Session() as session:
				return session.query(cls).filter(cls.status == 'normal', cls.deleted == '0').all()
		except Exception as e:
			logging.error(str(e))


if __name__ == "__main__":
	print(ProductModel().get_product_list())
