"""
@File : testtask_project_model.py
@Date : 2022/8/8 17:41
@Author: 九层风（YePing Zhang）
@Contact : yeahcheung213@163.com
"""
from sqlalchemy import Column, Integer, String, Date, FLOAT
from sqlalchemy import func, cast

from models.db_engine import *
from controller.log_loguru import logging

"""定义测试单项目映射"""


class TestTaskProjectModel(Base):
	# __bind_key__ = 'zentao'
	__tablename__ = 'assessment_statistic_project_weight'

	id = Column(Integer, autoincrement=True, primary_key=True)
	name = Column(String(90))
	begin = Column(Date)
	end = Column(Date)
	projectId = Column(Integer)
	projectName = Column(String(90))
	owner = Column(String(30))

	# deleted = Column(Enum('0', '1'))

	# 用将单条数据列转换成dict
	def to_dict(self):
		return {column.name: getattr(self, column.name, None) for column in
				self.__table__.columns}

	# 将多条数据转化成json
	@staticmethod
	def to_json(all_vendors):
		return [vendor.to_dict() for vendor in all_vendors]

	# 计算权重值
	@classmethod
	def calculate_project_weight(cls, condition: dict):
		try:
			with Session() as session:
				# 计算测试单总和
				total_count = session.query(func.count(cls.id)).filter(cls.owner == condition.get('owner'),
																	   cls.begin.between(condition['beginDate'],
																						 condition['endDate'])).scalar()
				# 查询权重，label表示给列取别名，*10把权重合转化成10
				weight_result = session.query(cls.projectId, cls.projectName,
											  # decimal的类型无法json序列话，故转成FLOAT类型
											  cast((func.count(cls.id) / total_count * 10), FLOAT).label(
												  'projectWeight')).filter(
					cls.owner == condition.get('owner'),
					cls.begin.between(condition['beginDate'],
									  condition['endDate'])
				).group_by(cls.projectId).all()
				# 处理返回结果
				return [dict(wr._mapping) for wr in weight_result]
		except Exception as e:
			logging.error(str(e))
			return None


if __name__ == "__main__":
	pass
	print(TestTaskProjectModel().calculate_project_weight(
		{'owner': 'zhangl', 'beginDate': '2022-06-01', 'endDate': '2022-08-31'}))
