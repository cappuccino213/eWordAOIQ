"""
@File : request_schema.py
@Date : 2022/8/4 14:53
@Author: 九层风（YePing Zhang）
@Contact : yeahcheung213@163.com
"""
from datetime import date

"""用于openapi文档中请求或响应对象的说明"""


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


class TestMissingBugSta:
	openedBy = [str]
	openedBeginDate = date
	openedEndDate = date


class TestMissingBugDetails:
	openedBy = str
	openedBeginDate = date
	openedEndDate = date


class TestBugDetails:
	openedBy = str
	openedBeginDate = date
	openedEndDate = date


# 研发统计
class DevBugSta:
	resolvedBy = [str]
	activatedBeginDate = date
	activatedEndDate = date


class DevMissingBugSta:
	devName = [str]
	openedBeginDate = date
	openedEndDate = date


class DevMissingBugDetails:
	devName = str
	openedBeginDate = date
	openedEndDate = date


class DevSeverityBugDetails:
	resolvedBy = str
	resolvedBeginDate = date
	resolvedEndDate = date


class DevActivatedBugDetails:
	resolvedBy = str
	activatedBeginDate = date
	activatedEndDate = date


if __name__ == "__main__":
	pass
