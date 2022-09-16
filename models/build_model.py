"""
@File : build_model.py
@Date : 2022/9/2 17:31
@Author: 九层风（YePing Zhang）
@Contact : yeahcheung213@163.com
"""

from sqlalchemy import Column, Integer, String, Enum
from models.db_engine import *

"""版本信息映射"""


class BuildModel(Base):
	__tablename__ = "zt_build"

	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(150))

	branch = Column(Integer, default=0)
	product = Column(Integer)
	project = Column(Integer)
	scmPath = Column(String(255), default='')
	filePath = Column(String(255), default='')
	# date = Column(Date, default=date.today())
	# stories = Column(Text, default='')
	# bugs = Column(Text, default='')
	builder = Column(String(30))
	desc = Column(String(255))
	deleted = Column(Enum('0', '1'), default='0')

	def to_dict(self):
		return {column.name: getattr(self, column.name, None) for column in
				self.__table__.columns}

	# 将多条数据转化成json
	@staticmethod
	def to_json(all_vendors):
		return [vendor.to_dict() for vendor in all_vendors]

	# 通过id获取版本信息
	@classmethod
	def get_info(cls, _id):
		try:
			with Session() as session:
				return session.query(cls).filter(cls.deleted == '0', cls.id == _id).first()
		except Exception as e:
			logging.error(str(e))
			return None

	@classmethod
	def get_build_info_list(cls):
		try:
			with Session() as session:
				return session.query(cls).filter(cls.deleted == '0').all()
		except Exception as e:
			logging.error(str(e))
			return None


if __name__ == "__main__":
	print(BuildModel().get_build_info_list())
