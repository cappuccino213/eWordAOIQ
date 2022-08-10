"""
@File : request_schema.py
@Date : 2022/8/4 14:53
@Author: 九层风（YePing Zhang）
@Contact : yeahcheung213@163.com
"""
from datetime import date


# 用户
class UserBody:
	id = str
	dept = str
	account = str
	role = str
	gender = str


class LoginBody:
	account = str
	password = str


# 指标
class AssessmentRuleAdd:
	indexType = str
	indexName = str
	indexID = str
	scoreInterval = str
	rule = str


class AssessmentRuleQuery:
	indexType = str
	indexName = str
	indexID = str


class AssessmentRuleUpdate:
	id = int
	indexType = str
	indexName = str
	indexID = str
	scoreInterval = str
	rule = str


# 测试统计
class ProjectWeight:
	owner = str
	beginDate = date
	endDate = date


class InvalidBug:
	openedBy = [str]
	openedBeginDate = date
	openedEndDate = date


class SeverityBug:
	openedBy = [str]
	openedBeginDate = date
	openedEndDate = date


# 研发统计
class DevBugSta:
	resolvedBy = [str]
	resolvedBeginDate = date
	resolvedEndDate = date


if __name__ == "__main__":
	pass
