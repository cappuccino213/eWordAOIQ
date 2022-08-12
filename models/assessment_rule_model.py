"""
@File : assessment_scorerule.py
@Date : 2022/8/4 16:51
@Author: 九层风（YePing Zhang）
@Contact : yeahcheung213@163.com
"""

from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.sql import or_

from models.db_engine import *
from controller.log_loguru import logging

"""定义考核指标映射"""


class AssessmentScoreRuleModel(Base):
	__tablename__ = 'assessment_scorerule'

	id = Column(Integer, autoincrement=True, primary_key=True)
	indexType = Column(Enum('dev', 'test'))
	indexName = Column(String(255))
	indexID = Column(String(64))
	scoreInterval = Column(String(255))
	rule = Column(String(255))
	deleted = Column(Enum('0', '1'), default='0')

	def __init__(self, fields_dict: dict):
		self.id = fields_dict.get('id')
		self.indexType = fields_dict.get('indexType')
		self.indexName = fields_dict.get('indexName')
		self.indexID = fields_dict.get('indexID')
		self.scoreInterval = fields_dict.get('scoreInterval')
		self.rule = fields_dict.get('rule')
		self.deleted = fields_dict.get('deleted')

	# 用将单条数据列转换成dict
	def to_dict(self):
		return {column.name: getattr(self, column.name, None) for column in
				self.__table__.columns}  # 如果有时间戳需要加处理，https://blog.csdn.net/baidu_36943075/article/details/101053734

	# 将多条数据转化成json
	@staticmethod
	def to_json(all_vendors):
		return [vendor.to_dict() for vendor in all_vendors]

	# 查询是否存在同名（id）的
	@classmethod
	def if_same_exist(cls, index_type: str, index_name: str, index_id: str):
		try:
			with Session() as session:
				return session.query(cls).filter(cls.deleted == '0', cls.indexType == index_type).filter(
					or_(cls.indexName == index_name, cls.indexID == index_id)).first()
		except Exception as e:
			logging.error(str(e))
			return None


"""CRUD的操作"""


# 查询
def multiple_condition_query(condition: dict):
	try:
		with Session() as session:
			result = session.query(AssessmentScoreRuleModel).filter(AssessmentScoreRuleModel.deleted == '0')
			if condition.get('indexType'):
				result = result.filter(AssessmentScoreRuleModel.indexType == condition.get('indexType'))
			if condition.get('indexName'):
				result = result.filter(AssessmentScoreRuleModel.indexName.like(f"%{condition.get('indexName')}%"))
			if condition.get('indexID'):
				result = result.filter(AssessmentScoreRuleModel.indexID == condition.get('indexID'))
			return result.all()
	except Exception as e:
		logging.error(str(e))
		return None


"""计算扣分项函数"""


def calculate_deduction_score(index_type, index_id, index_rate):
	"""
	其中指标的规则从数据库获取，若获取不到，则直接返回None
	:param index_rate: 指标比重，float类型
	:param index_type: 指标类型
	:param index_id:指标id
	:return: 返回扣分值

	指标sample：
	id	indexType	indexName	indexID		scoreInterval	rule
	1	test		无效缺陷		invalidBug	0|1|2|4|10	0|0-1%|2%-5%|6%-10%|11%-100%
	2	test		严重缺陷		severityBug	0|1|2|3		31%-100%|20%-30%|10%-19%|0-9%
	3	test		遗漏缺陷		missingBug	0|1|2|3		31%-100%|20%-30%|10%-19%|0-9%
	4	dev			冒烟测试		smokeTest	0|1|2|3		31%-100%|20%-30%|10%-19%|0-9%
	"""
	# 获取指标规则，若有重复获取第一条
	index_rule_obj = multiple_condition_query(dict(indexType=index_type, indexID=index_id))
	if index_rule_obj:
		index_rule = index_rule_obj[0].to_dict()
		logging.info(f"获取到{index_type}-{index_id}的指标：{index_rule}")
		# 处理规则数据
		score_interval_list = index_rule['scoreInterval'].split('|')
		rule_list = index_rule['rule'].replace('%', '').split('|')
		rule_interval_list = [rule.split('-') for rule in rule_list]
		for rule_interval in rule_interval_list:
			if int(rule_interval[0]) <= index_rate * 100 <= int(rule_interval[1]):
				ind = rule_interval_list.index(rule_interval)
				return score_interval_list[ind]
	else:
		logging.error(f"未获取到{index_type}-{index_id}的指标规则")
		return '-'


if __name__ == "__main__":
	pass
	print(calculate_deduction_score('dev', 'smokeTest', 0))
