"""
@File : bug_model.py
@Date : 2022/8/9 13:45
@Author: 九层风（YePing Zhang）
@Contact : yeahcheung213@163.com
"""
from sqlalchemy import Column, Integer, String, SmallInteger, Enum, DateTime
from sqlalchemy import func
from sqlalchemy.sql import or_

from models.db_engine import *
from models.assessment_rule_model import calculate_deduction_score_rate, calculate_deduction_score
from controller.log_loguru import logging

"""缺陷映射"""


class BugModel(Base):
	__bind_key__ = 'zentao'
	__tablename__ = 'zt_bug'

	id = Column(Integer, primary_key=True)
	# product = Column(Integer)
	project = Column(Integer)
	# story = Column(Integer)
	# task = Column(Integer)
	title = Column(String)
	severity = Column(Integer)
	confirmed = Column(SmallInteger)
	activatedCount = Column(SmallInteger)
	activatedDate = Column(DateTime)
	type = Column(String)
	status = Column(Enum('active', 'resolved', 'closed'))
	openedBy = Column(String)
	openedDate = Column(DateTime)
	assignedTo = Column(String)
	# assignedDate = Column(DateTime)
	# closedBy = Column(String)
	closedDate = Column(DateTime)
	# deadline = Column(Date)
	# testtask = Column(Integer)  # 测试单
	resolvedBy = Column(String)  # 解决人
	resolution = Column(String)  # 解决方案

	# resolvedBuild = Column(String)  # 解决版本
	resolvedDate = Column(DateTime)  # 解决日期
	deleted = Column(Enum('0', '1'))  # 测试单

	# 用将单条数据列转换成dict
	def to_dict(self):
		return {column.name: getattr(self, column.name, None) for column in
				self.__table__.columns}

	# 根据测试人员、开发人员、时间计算缺陷总数
	@classmethod
	def bug_total(cls, condition: dict):
		try:
			with Session() as session:
				total_count = session.query(func.count(cls.id)).filter(cls.deleted == '0')
				if condition.get('openedBy'):
					total_count = total_count.filter(cls.openedBy == condition.get('openedBy'))
				if condition.get('openedBeginDate') and condition.get('openedEndDate'):
					total_count = total_count.filter(
						cls.openedDate.between(condition['openedBeginDate'], condition['openedEndDate']))
				if condition.get('resolvedBy'):
					total_count = total_count.filter(cls.resolvedBy == condition.get('resolvedBy'))
				if condition.get('resolvedBeginDate') and condition.get('resolvedEndDate'):
					total_count = total_count.filter(
						cls.resolvedDate.between(condition['resolvedBeginDate'], condition['resolvedEndDate']))
				if condition.get('activatedBeginDate') and condition.get('activatedEndDate'):
					total_count = total_count.filter(
						cls.resolvedDate.between(condition['activatedBeginDate'], condition['activatedEndDate']))
				logging.info(f"查询对应条件下的bug总数为{total_count.scalar()}")
				return total_count.scalar()
		except Exception as e:
			logging.error(str(e))

	# 无效bug数统计
	@classmethod
	def invalid_bug_count(cls, condition: dict):
		try:
			with Session() as session:
				count = session.query(func.count(cls.id)).filter(cls.deleted == '0',
																 cls.resolution.in_(['bydesign', 'duplicate'])).filter(
					cls.openedBy == condition['openedBy'],
					cls.openedDate.between(condition['openedBeginDate'], condition['openedEndDate'])).scalar()
				logging.info(f"查询对应条件下的无效bug数为{count}")
				return count
		except Exception as e:
			logging.error(str(e))

	# 严重bug数统计
	@classmethod
	def severity_bug_count(cls, condition: dict):
		try:
			with Session() as session:
				count = session.query(func.count(cls.id)).filter(cls.deleted == '0', cls.severity.in_(['1', '2']))
				# 根据是传值判断是开发或是测试的统计
				if condition.get('openedBy'):
					count = count.filter(
						cls.openedBy == condition['openedBy'],
						cls.openedDate.between(condition['openedBeginDate'], condition['openedEndDate'])).scalar()
				else:
					count = count.filter(cls.deleted == '0',
										 cls.resolvedBy == condition['resolvedBy'],
										 cls.resolvedDate.between(condition['resolvedBeginDate'],
																  condition['resolvedEndDate'])).scalar()
				logging.info(f"查询对应条件下的严重bug数为{count}")
				return count
		except Exception as e:
			logging.error(str(e))

	# 激活bug数统计
	@classmethod
	def activated_bug_count(cls, condition: dict):
		try:
			with Session() as session:
				count = session.query(func.count(cls.id)).filter(cls.deleted == '0',
																 cls.confirmed == 1,
																 cls.activatedCount > 0,
																 cls.activatedDate.between(
						condition['activatedBeginDate'], condition['activatedEndDate'])).filter(
					or_(cls.resolvedBy == condition['resolvedBy'], cls.assignedTo == condition['resolvedBy'])).scalar()
				logging.info(f"查询对应条件下的激活bug数为{count}")
				return count
		except Exception as e:
			logging.error(str(e))

	# 遗漏bug数统计
	@classmethod
	def missing_bug_count(cls, condition: dict):
		try:
			with Session() as session:
				count = session.query(func.count(cls.id)).filter(cls.deleted == '0', cls.type == 'missingbug',
																 cls.openedDate.between(
																	 condition['openedBeginDate'],
																	 condition['openedEndDate'])).filter(
					or_(cls.assignedTo == condition['devName'], cls.resolvedBy == condition['devName'])).scalar()
				logging.info(f"查询对应条件下的遗漏bug数为{count}")
				return count
		except Exception as e:
			logging.error(str(e))

	@classmethod
	def test_missing_bug_count(cls, condition: dict):
		try:
			with Session() as session:
				count = session.query(func.count(cls.id)).filter(cls.deleted == '0', cls.type == 'missingbug',
																 cls.openedDate.between(
																	 condition['openedBeginDate'],
																	 condition['openedEndDate'])).filter(
					or_(cls.openedBy == condition['openedBy'])).scalar()
				logging.info(f"查询对应条件下的遗漏bug数为{count}")
				return count
		except Exception as e:
			logging.error(str(e))

	# 遗漏bug详情
	# 尝试使用不定参数**kwargs
	@classmethod
	def missing_bug_details(cls, **kwargs):
		try:
			if kwargs.get('openedBy'):
				with Session() as session:
					details = session.query(cls).filter(cls.deleted == '0', cls.type == 'missingbug',
														cls.openedDate.between(
															kwargs['openedBeginDate'],
															kwargs['openedEndDate'])).filter(
						or_(cls.openedBy == kwargs['openedBy'])).all()
					return details
			elif kwargs.get('devName'):
				with Session() as session:
					details = session.query(cls).filter(cls.deleted == '0', cls.type == 'missingbug',
														cls.openedDate.between(
															kwargs['openedBeginDate'],
															kwargs['openedEndDate'])).filter(
						or_(cls.assignedTo == kwargs['devName'], cls.resolvedBy == kwargs['devName'])).all()
					return details
			else:
				return None
		except Exception as e:
			logging.error(str(e))

	# 严重bug的详情查询
	@classmethod
	def severity_bug_details(cls, **kwargs):
		try:
			if kwargs.get('openedBy'):
				with Session() as session:
					details = session.query(cls).filter(cls.deleted == '0', cls.severity.in_(['1', '2']),
														cls.openedDate.between(
															kwargs['openedBeginDate'],
															kwargs['openedEndDate'])).filter(
						or_(cls.openedBy == kwargs['openedBy'])).all()
					return details
			elif kwargs.get('resolvedBy'):
				with Session() as session:
					details = session.query(cls).filter(cls.deleted == '0',
														cls.severity.in_(['1', '2']),
														cls.resolvedBy == kwargs['resolvedBy'],
														cls.resolvedDate.between(
															kwargs['resolvedBeginDate'],
															kwargs['resolvedEndDate'])).all()
					return details
			else:
				return None
		except Exception as e:
			logging.error(str(e))

	# 激活缺陷详情
	@classmethod
	def activated_bug_details(cls, **kwargs):
		try:
			with Session() as session:
				details = session.query(cls).filter(cls.deleted == '0',
													cls.confirmed == 1,
													cls.activatedCount > 0,
													cls.activatedDate.between(
														kwargs['activatedBeginDate'],
														kwargs['activatedEndDate'])).filter(
					or_(cls.resolvedBy == kwargs['resolvedBy'], cls.assignedTo == kwargs['resolvedBy'])).all()
				return details
		except Exception as e:
			logging.error(str(e))

	# 无效缺陷详情
	@classmethod
	def invalid_bug_details(cls, **kwargs):
		try:
			with Session() as session:
				details = session.query(cls).filter(cls.deleted == '0',
													cls.resolution.in_(['bydesign', 'duplicate']),
													cls.openedBy == kwargs['openedBy'],
													cls.openedDate.between(
														kwargs['openedBeginDate'],
														kwargs['openedEndDate'])).all()
				return details
		except Exception as e:
			logging.error(str(e))


# 无效率考核统计
def invalid_bug_rate_statistic(param: dict):
	# 定义初始化数据
	statistic_result = dict(openedBy=param['openedBy'], invalidBugCount=BugModel.invalid_bug_count(param),
							bugTotal=BugModel.bug_total(param))
	# 计算无效率
	if statistic_result['bugTotal']:
		statistic_result['invalidBugRate'] = round(statistic_result['invalidBugCount'] / statistic_result['bugTotal'],
												   4)
	else:
		statistic_result['invalidBugRate'] = 0
	# 计算扣分
	statistic_result['deductPoint'] = calculate_deduction_score_rate('test', 'invalidBug',
																	 statistic_result['invalidBugRate'])
	logging.info(f"获得无效bug统计结果：{statistic_result}")
	return statistic_result


# 严重率统计
def severity_bug_rate_statistic(param: dict):
	# 定义初始化数据
	# 根据是传值判断是开发或是测试的统计
	if param.get('openedBy'):
		result = dict(openedBy=param['openedBy'], severityBugCount=BugModel.severity_bug_count(param),
					  bugTotal=BugModel.bug_total(param))
		# 计算严重占比
		if result['bugTotal']:
			result['severityBugRate'] = round(result['severityBugCount'] / result['bugTotal'], 4)
		else:
			result['severityBugRate'] = 0
		# 计算扣分
		result['deductPoint'] = calculate_deduction_score_rate('test', 'severityBug', result['severityBugRate'])
	else:
		result = dict(resolvedBy=param['resolvedBy'], severityBugCount=BugModel.severity_bug_count(param),
					  bugTotal=BugModel.bug_total(param))
		# 计算严重占比
		if result['bugTotal']:
			result['severityBugRate'] = round(
				result['severityBugCount'] / result['bugTotal'], 4)
		else:
			result['severityBugRate'] = 0
		# 计算扣分
		result['deductPoint'] = calculate_deduction_score_rate('dev', 'severityBug',
															   result['severityBugRate'])

	logging.info(f"获得严重bug统计结果：{result}")
	return result


# 激活率考核统计
def activated_bug_rate_statistic(param: dict):
	# 定义初始化数据
	statistic_result = dict(resolvedBy=param['resolvedBy'], activatedBugCount=BugModel.activated_bug_count(param),
							bugTotal=BugModel.bug_total(param))
	# 计算严重占比
	if statistic_result['bugTotal']:
		statistic_result['activatedBugRate'] = round(
			statistic_result['activatedBugCount'] / statistic_result['bugTotal'],
			4)
	else:
		statistic_result['activatedBugRate'] = 0
	# 计算扣分
	statistic_result['deductPoint'] = calculate_deduction_score_rate('dev', 'activatedBug',
																	 statistic_result['activatedBugRate'])
	logging.info(f"获得激活bug统计结果：{statistic_result}")
	return statistic_result


# 遗漏缺陷统计
def missing_bug_score_statistic(param: dict):
	statistic_result = dict(devName=param['devName'], missingBugCount=BugModel.missing_bug_count(param))

	# 计算扣分
	statistic_result['deductPoint'] = calculate_deduction_score('dev', 'missingBug',
																statistic_result['missingBugCount'])
	logging.info(f"获得遗漏bug统计结果：{statistic_result}")
	return statistic_result


def test_missing_bug_score_statistic(param: dict):
	statistic_result = dict(devName=param['openedBy'], missingBugCount=BugModel.test_missing_bug_count(param))

	# 计算扣分
	statistic_result['deductPoint'] = calculate_deduction_score('test', 'missingBug',
																statistic_result['missingBugCount'])
	logging.info(f"获得遗漏bug统计结果：{statistic_result}")
	return statistic_result


if __name__ == "__main__":
	# BugModel().bug_total(dict(openedBy='zyp', openedBeginDate='2022-01-01', openedEndDate='2022-08-09'))
	# BugModel().bug_total(dict(resolvedBy='hdh', resolvedBeginDate='2022-01-01', resolvedEndDate='2022-08-09'))
	# BugModel().invalid_bug_count(dict(openedBy='yp', openedBeginDate='2022-01-01', openedEndDate='2022-08-09'))
	# BugModel().activated_bug_count(dict(resolvedBy='hdh', resolvedBeginDate='2022-01-01', resolvedEndDate='2022-08-09'))
	# invalid_bug_rate_statistic(dict(openedBy='zyp', openedBeginDate='2022-01-01', openedEndDate='2022-08-09'))
	# BugModel().severity_bug_count(dict(openedBy='zyp', openedBeginDate='2022-01-01', openedEndDate='2022-08-09'))
	# BugModel().severity_bug_count(dict(resolvedBy='hdh', resolvedBeginDate='2022-01-01', resolvedEndDate='2022-08-09'))
	# activated_bug_rate_statistic(dict(resolvedBy='hdh', resolvedBeginDate='2022-01-01', resolvedEndDate='2022-08-09'))
	# test_missing_bug_score_statistic(dict(openedBy='zyp', openedBeginDate='2022-01-01', openedEndDate='2022-08-24'))

	md = BugModel.missing_bug_details(devName='chengjk', openedBeginDate='2022-01-01', openedEndDate='2022-08-24')
	# md = BugModel.missing_bug_details(openedBy='zyp', openedBeginDate='2022-01-01', openedEndDate='2022-08-24')
	print([d.to_dict() for d in md])
