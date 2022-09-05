"""
@File : db_engine.py
@Date : 2022/8/3 15:40
@Author: 九层风（YePing Zhang）
@Contact : yeahcheung213@163.com
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

from config import DATABASE_CONFIG
from controller.log_loguru import logging

# 创建引擎
engine = create_engine(url=DATABASE_CONFIG.get('DATABASE_URL'), echo=DATABASE_CONFIG.get('SQL_ECHO'), future=True)

# 定义会话生成器
Session = sessionmaker(engine, autocommit=False, autoflush=False)

# 声明映射
Base = declarative_base()

"""会话操作"""


# 根据id查询
def query_by_id(primary_id: int, db_model: Base):
	try:
		with Session() as session:
			result = session.query(db_model).filter(db_model.id == primary_id).first()
			logging.info(f"查询id为{primary_id}的成功")
			return result
	except Exception as e:
		logging.error(f"通过id查询异常，{e}")


# 增加
def create(db_model):
	try:
		with Session() as session:
			session.add(db_model)
			session.commit()
			session.refresh(db_model)
			logging.info("增加记录成功")
	except Exception as e:
		logging.error(f"增加记录异常，{e}")


# 批量增加
def create_batch(db_model_list):
	"""
	批量insert
	:param db_model_list:
	:return:
	"""
	try:
		with Session() as session:
			session.add_all(db_model_list)
			session.commit()
			for db_model in db_model_list:
				session.refresh(db_model)
				session.expunge(db_model)
			logging.info("增加记录成功")
	except Exception as e:
		logging.error(f"增加记录异常，{e}")
		session.rollback()
		session.flush()


# 修改
def update(update_dict: dict, db_model: Base):
	result = query_by_id(update_dict['id'], db_model)
	if result:
		try:
			with Session() as session:
				session.query(db_model).filter(db_model.id == update_dict['id']).update(update_dict)
				session.commit()
				session.flush()
				logging.info(f"更新数据成功，数据{update_dict}")
				return update_dict
		except Exception as e:
			logging.error(f"更新数据异常，{e}")


# 逻辑删除
def logical_delete(primary_id: int, db_model: Base):
	result = query_by_id(primary_id, db_model)
	if result:
		try:
			with Session() as session:
				session.query(db_model).filter(db_model.id == primary_id).update({'deleted': '1'})
				session.commit()
				session.flush()
				logging.info(f"删除数据{result.to_dict()}成功")
				return result.to_dict()
		except Exception as e:
			logging.error(f"删除数据异常，{e}")


# 物理删除
def physical_delete(primary_id: int, db_model: Base):
	# result = query_by_id(primary_id, db_model)
	# if result:
	try:
		with Session() as session:
			delete_data = session.query(db_model).filter(db_model.id == primary_id)
			resp_data = delete_data.first()  # 用于返回删除的数据
			if delete_data.all():
				delete_data.delete()
				session.commit()
				session.flush()
				logging.info(f"删除数据{resp_data.to_dict()}成功")
				return resp_data.to_dict()
			else:
				logging.error(f"删除的数据不存在")
	except Exception as e:
		logging.error(f"删除数据异常，{e}")


if __name__ == "__main__":
	pass
	from assessment_rule_model import AssessmentScoreRuleModel

	# logging.info(query_by_id(2, AssessmentScoreRuleModel))

	# logical_delete(14, AssessmentScoreRuleModel)
	physical_delete(39, AssessmentScoreRuleModel)
