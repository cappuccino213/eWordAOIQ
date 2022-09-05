"""
@File : testtask_model.py
@Date : 2022/8/8 15:48
@Author: 九层风（YePing Zhang）
@Contact : yeahcheung213@163.com
"""
from datetime import date

from sqlalchemy import Column, Integer, String, Enum, Date

from models.db_engine import *
from controller.log_loguru import logging

"""定义测试单映射"""


class TestTaskModel(Base):
	# __bind_key__ = 'zentao'
	__tablename__ = 'zt_testtask'

	id = Column(Integer, autoincrement=True, primary_key=True)
	name = Column(String(90))
	product = Column(Integer)
	project = Column(Integer)
	build = Column(String(30))
	owner = Column(String(30))
	begin = Column(Date)
	end = Column(Date)
	status = Column(Enum('blocked', 'doing', 'wait', 'done'))
	subStatus = Column(String(30))  # 用作是否标记的字段使用
	deleted = Column(Enum('0', '1'))

	# 用将单条数据列转换成dict
	def to_dict(self):
		res_dict = dict()
		for column in self.__table__.columns:
			# 判断字段为date的转化成str，防止之后json序列化报错
			if isinstance(getattr(self, column.name), date):
				res_dict[column.name] = str(getattr(self, column.name))
			else:
				res_dict[column.name] = getattr(self, column.name)
		return res_dict

	# 将多条数据转化成json
	@staticmethod
	def to_json(all_vendors):
		return [vendor.to_dict() for vendor in all_vendors]

	@classmethod
	def get_testtask_list(cls, **kwargs):
		try:
			with Session() as session:
				test_tasks = session.query(cls).filter(cls.deleted == '0')
				if kwargs.get('id'):
					test_tasks = test_tasks.filter(cls.id == kwargs.get('id'))
				if kwargs.get('product'):
					test_tasks = test_tasks.filter(cls.product == kwargs.get('product'))
				if kwargs.get('owner'):
					test_tasks = test_tasks.filter(cls.owner == kwargs.get('owner'))
				if kwargs.get('subStatus'):
					test_tasks = test_tasks.filter(cls.subStatus == kwargs.get('subStatus'))
				if kwargs.get('begin') and kwargs.get('end'):
					test_tasks = test_tasks.filter(
						cls.begin.between(kwargs['begin'], kwargs['end']))
				# logging.info(f"查询对应条件下的bug总数为{test_tasks.scalar()}")
				return test_tasks.all()
		except Exception as e:
			logging.error(str(e))

	# 同步冒烟测试标记结果
	@classmethod
	def sync_mark_smoke_result(cls, test_task_id, result):
		try:
			with Session() as session:
				session.query(cls).filter(cls.id == test_task_id).update({cls.subStatus: result})
				session.commit()
				session.flush()
				logging.info(f"同步测试单{test_task_id},冒烟测试标记subStatus为{result}")
		except Exception as e:
			logging.error(f"更新数据异常，{e}")


if __name__ == "__main__":
	# print(TestTaskModel().get_testtask_list(begin='2022-08-25', end='2022-08-26'))
	TestTaskModel().sync_mark_smoke_result(920,'pass')
