"""
@File : smoke_test_record_model.py
@Date : 2022/9/2 15:48
@Author: 九层风（YePing Zhang）
@Contact : yeahcheung213@163.com
"""
from datetime import date

from sqlalchemy import Column, Integer, String, Enum, Date
from sqlalchemy import func

from models.db_engine import *
from controller.log_loguru import logging
from models.assessment_rule_model import calculate_deduction_score

"""定义冒烟测试记录映射"""


class SmokeTestRecordModel(Base):
	# __bind_key__ = 'zentao'
	__tablename__ = 'assessment_smoketestrecord'

	id = Column(Integer, autoincrement=True, primary_key=True)
	testTaskID = Column(Integer)
	title = Column(String(255))
	product = Column(Integer)
	project = Column(Integer)
	build = Column(String(30))
	tester = Column(String(30))
	smokeResult = Column(Enum('pass', 'fail'), default='pass')
	failedReason = Column(String(255))
	relatedPerson = Column(String(30))
	begin = Column(Date)
	end = Column(Date)

	def __init__(self, fields_dict: dict):
		self.id = fields_dict.get('id')
		self.testTaskID = fields_dict.get('testTaskID')
		self.title = fields_dict.get('title')
		self.product = fields_dict.get('product')
		self.project = fields_dict.get('project')
		self.build = fields_dict.get('build')
		self.tester = fields_dict.get('tester')
		self.smokeResult = fields_dict.get('smokeResult')
		self.failedReason = fields_dict.get('failedReason')
		self.relatedPerson = fields_dict.get('relatedPerson')
		self.begin = fields_dict.get('begin')
		self.end = fields_dict.get('end')

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

	# 查询是否为相同的测试单id数据
	@classmethod
	def if_same_testtask_exist(cls, test_task_id: int):
		try:
			with Session() as session:
				return session.query(cls).filter(cls.testTaskID == test_task_id).first()
		except Exception as e:
			logging.error(str(e))
			return None

	# 根据测试单id查询
	@classmethod
	def query_by_testtaskid(cls, test_task_id: int):
		try:
			with Session() as session:
				return session.query(cls).filter(cls.testTaskID == test_task_id).all()
		except Exception as e:
			logging.error(str(e))

	# 冒烟失败数
	@classmethod
	def smoke_test_fail_count(cls, **kwargs):
		try:
			with Session() as session:
				count = session.query(func.count(cls.id)).filter(cls.smokeResult == 'fail',
																 cls.relatedPerson == kwargs['relatedPerson'],
																 cls.begin.between(
																	 kwargs['begin'],
																	 kwargs['end'])).scalar()
				logging.info(f"查询冒烟测试失败的数量：{count}")
				return count
		except Exception as e:
			logging.error(str(e))

	# 冒烟失败详情
	@classmethod
	def smoke_test_fail_details(cls, **kwargs):
		try:
			with Session() as session:
				return session.query(cls).filter(cls.smokeResult == 'fail',
												 cls.relatedPerson == kwargs['relatedPerson'],
												 cls.begin.between(
													 kwargs['begin'],
													 kwargs['end'])).all()
		except Exception as e:
			logging.error(str(e))


# 冒烟测试失败率统计
def smoke_test_fail_statistic(**kwargs):
	statistic_result = dict(relatedPerson=kwargs['relatedPerson'],
							smokeTestFailCount=SmokeTestRecordModel.smoke_test_fail_count(**kwargs))

	# 计算扣分
	statistic_result['deductPoint'] = calculate_deduction_score('dev', 'smokeTest',
																statistic_result['smokeTestFailCount'])
	logging.info(f"获得冒烟统计结果：{statistic_result}")
	return statistic_result


if __name__ == "__main__":
	pass
	# SmokeTestRecordModel.smoke_test_fail_count(relatedPerson='wangj',begin='2022-08-05',end='2022-08-06')
	# std = SmokeTestRecordModel.smoke_test_fail_details(relatedPerson='wangj', begin='2022-08-05', end='2022-08-06')
	# print([d.to_dict() for d in std])
	smoke_test_fail_statistic(relatedPerson='wangj', begin='2022-08-02', end='2022-08-06')
