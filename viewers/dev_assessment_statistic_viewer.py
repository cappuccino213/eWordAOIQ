"""
@File : dev_assessment_statistic_viewer.py.py
@Date : 2022/8/8 17:05
@Author: 九层风（YePing Zhang）
@Contact : yeahcheung213@163.com
"""
from sanic import Blueprint
from sanic_openapi import openapi

from models.request_schema import *
from models.bug_model import missing_bug_score_statistic, activated_bug_rate_statistic, severity_bug_rate_statistic, \
	BugModel
from controller.response_encapsulate import *
from controller.auth import protected

"""开发考核指标统计"""
dev_as_bp = Blueprint('dev_as_bp', url_prefix='/api/DevAssessmentStatistic')


# 激活缺陷统计
@dev_as_bp.route('ActivatedBugStatistic', methods=['POST'])
@openapi.tag("开发考核指标")
@openapi.summary("激活缺陷统计")
@openapi.body({"application/json": DevBugSta},
			  description="参数均为必填项，其中resolvedBy为string元素的list类型(bug解决者，传用户信息的account)，如：['hdh']、['hdh','xhyx']",
			  required=True)
@protected
async def activated_bug_statistic(request):
	resp = list()
	for resolvedBy in request.json['resolvedBy']:
		request_body = dict(resolvedBy=resolvedBy, activatedBeginDate=request.json['activatedBeginDate'],
							activatedEndDate=request.json['activatedEndDate'])
		resp.append(activated_bug_rate_statistic(request_body))
	if resp:
		return resp_200(resp)
	else:
		return resp_204()


# 激活缺陷详情
@dev_as_bp.route('ActivatedBugDetails', methods=['POST'])
@openapi.tag("开发考核指标")
@openapi.summary("激活缺陷详情")
@openapi.body({"application/json": DevActivatedBugDetails},
			  description="参数均为必填项",
			  required=True)
@protected
async def activated_bug_details_list(request):
	details_obj = BugModel.activated_bug_details(resolvedBy=request.json['resolvedBy'],
												 activatedBeginDate=request.json['activatedBeginDate'],
												 activatedEndDate=request.json['activatedEndDate'])
	if details_obj:
		resp = list()
		for detail_obj in details_obj:
			response_body = dict(ztId=detail_obj.id, severity=detail_obj.severity, title=detail_obj.title,
								 projectId=detail_obj.project,
								 openedBy=detail_obj.openedBy,
								 resolvedBy=detail_obj.resolvedBy,
								 activatedCount=detail_obj.activatedCount,
								 activatedDate=str(detail_obj.activatedDate),
								 accessLink=f"http://192.168.1.43:8086/zentao/bug-view-{detail_obj.id}.html")
			resp.append(response_body)
		return resp_200(resp)
	else:
		return resp_204()


# 严重缺陷统计
@dev_as_bp.route('SeverityBugStatistic', methods=['POST'])
@openapi.tag("开发考核指标")
@openapi.summary("严重缺陷统计")
@openapi.body({"application/json": DevBugSta},
			  description="参数均为必填项，其中resolvedBy为string元素的list类型(bug解决者，传用户信息的account)，如：['hdh']、['hdh','xhyx']",
			  required=True)
@protected
async def severity_bug_statistic(request):
	resp = list()
	for resolvedBy in request.json['resolvedBy']:
		request_body = dict(resolvedBy=resolvedBy, resolvedBeginDate=request.json['resolvedBeginDate'],
							resolvedEndDate=request.json['resolvedEndDate'])
		resp.append(severity_bug_rate_statistic(request_body))
	if resp:
		return resp_200(resp)
	else:
		return resp_204()


# 严重缺陷详情
@dev_as_bp.route('SeverityBugDetails', methods=['POST'])
@openapi.tag("开发考核指标")
@openapi.summary("严重缺陷详情")
@openapi.body({"application/json": DevSeverityBugDetails},
			  description="参数均为必填项",
			  required=True)
@protected
async def severity_bug_details_list(request):
	details_obj = BugModel.severity_bug_details(resolvedBy=request.json['resolvedBy'],
												resolvedBeginDate=request.json['resolvedBeginDate'],
												resolvedEndDate=request.json['resolvedEndDate'])
	if details_obj:
		resp = list()
		for detail_obj in details_obj:
			response_body = dict(ztId=detail_obj.id, severity=detail_obj.severity, title=detail_obj.title,
								 projectId=detail_obj.project,
								 openedBy=detail_obj.openedBy,
								 resolvedBy=detail_obj.resolvedBy,
								 resolvedDate=str(detail_obj.resolvedDate),
								 accessLink=f"http://192.168.1.43:8086/zentao/bug-view-{detail_obj.id}.html")
			resp.append(response_body)
		return resp_200(resp)
	else:
		return resp_204()

# 遗漏缺陷
@dev_as_bp.route('MissingBugStatistic', methods=['POST'])
@openapi.tag("开发考核指标")
@openapi.summary("遗漏缺陷统计")
@openapi.body({"application/json": DevMissingBugSta},
			  description="参数均为必填项，其中resolvedBy为string元素的list类型(bug解决者，传用户信息的account)，如：['hdh']、['hdh','xhyx']",
			  required=True)
@protected
async def missing_bug_statistic(request):
	resp = list()
	for devName in request.json['devName']:
		request_body = dict(devName=devName, openedBeginDate=request.json['openedBeginDate'],
							openedEndDate=request.json['openedEndDate'])
		resp.append(missing_bug_score_statistic(request_body))
	if resp:
		return resp_200(resp)
	else:
		return resp_204()

# 遗漏详情
@dev_as_bp.route('MissingBugDetails', methods=['POST'])
@openapi.tag("开发考核指标")
@openapi.summary("遗漏缺陷详情")
@openapi.body({"application/json": DevMissingBugDetails},
			  description="参数均为必填项",
			  required=True)
@protected
async def missing_bug_details_list(request):
	details_obj = BugModel.missing_bug_details(devName=request.json['devName'],
											   openedBeginDate=request.json['openedBeginDate'],
											   openedEndDate=request.json['openedEndDate'])
	# 处理需要返回的body
	if details_obj:
		resp = list()
		for detail_obj in details_obj:
			response_body = dict(ztId=detail_obj.id, severity=detail_obj.severity, title=detail_obj.title,
								 projectId=detail_obj.project,
								 openedDate=str(detail_obj.openedDate), openedBy=detail_obj.openedBy,
								 assignedTo=detail_obj.assignedTo,
								 resolvedBy=detail_obj.resolvedBy,
								 accessLink=f"http://192.168.1.43:8086/zentao/bug-view-{detail_obj.id}.html")
			resp.append(response_body)
		return resp_200(resp)
	else:
		return resp_204()


if __name__ == "__main__":
	pass
