"""
@File : test_assessment_statistic_viewer.py
@Date : 2022/8/8 16:56
@Author: 九层风（YePing Zhang）
@Contact : yeahcheung213@163.com
"""
from sanic import Blueprint
from sanic_openapi import openapi

from controller.auth import protected
from models.testtask_project_model import *
from models.request_schema import *
from models.bug_model import invalid_bug_rate_statistic, severity_bug_rate_statistic, test_missing_bug_score_statistic, \
	BugModel
from controller.response_encapsulate import *

"""测试考核指标统计"""
test_as_bp = Blueprint('test_as_bp', url_prefix='/api/TestAssessmentStatistic')


# 项目权重
@test_as_bp.route('ProjectWeight', methods=['POST'])
@openapi.tag("测试考核指标")  # API标签
@openapi.summary("项目权重查询")  # API信息描述
@openapi.body({"application/json": ProjectWeight},
			  description="参数均为必填项，其中owner传测试人员的account",
			  required=True)
@protected
async def project_weight_query(request):
	resp = TestTaskProjectModel().calculate_project_weight(request.json)  # json表示传入的对象时dict
	if resp:
		return resp_200(resp)
	else:
		return resp_204()


# 无效bug统计
@test_as_bp.route('InvalidBugStatistic', methods=['POST'])
@openapi.tag("测试考核指标")
@openapi.summary("无效缺陷统计")
@openapi.body({"application/json": InvalidBug},
			  description="参数均为必填项，其中openedBy为string元素的list类型(bug提出人，传用户信息的account)，如：['zhangl']、['zyp','zhangl']",
			  required=True)
@protected
async def invalid_bug_statistic(request):
	resp = list()
	for opened_by in request.json['openedBy']:
		request_body = dict(openedBy=opened_by, openedBeginDate=request.json['openedBeginDate'],
							openedEndDate=request.json['openedEndDate'])
		resp.append(invalid_bug_rate_statistic(request_body))
	if resp:
		return resp_200(resp)
	else:
		return resp_204()


# 无效bug详情
@test_as_bp.route('InvalidBugDetails', methods=['POST'])
@openapi.tag("测试考核指标")
@openapi.summary("无效缺陷详情")
@openapi.body({"application/json": TestBugDetails},
			  description="参数均为必填项",
			  required=True)
@protected
async def invalid_bug_details_list(request):
	details_obj = BugModel.invalid_bug_details(openedBy=request.json['openedBy'],
											   openedBeginDate=request.json['openedBeginDate'],
											   openedEndDate=request.json['openedEndDate'])
	if details_obj:
		resp = list()
		for detail_obj in details_obj:
			response_body = dict(ztId=detail_obj.id, title=detail_obj.title,
								 projectId=detail_obj.project,
								 openedBy=detail_obj.openedBy,
								 openedDate=str(detail_obj.openedDate),
								 resolvedBy=detail_obj.resolvedBy,
								 resolution=detail_obj.resolution,
								 accessLink=f"http://192.168.1.43:8086/zentao/bug-view-{detail_obj.id}.html")
			resp.append(response_body)
		return resp_200(resp)
	else:
		return resp_204()


# 严重bug统计
@test_as_bp.route('SeverityBugStatistic', methods=['POST'])
@openapi.tag("测试考核指标")
@openapi.summary("严重缺陷统计")
@openapi.body({"application/json": SeverityBug},
			  description="参数均为必填项，其中openedBy为string元素的list类型(bug提出人，传用户信息的account)，如：['zhangl']、['zyp','zhangl']",
			  required=True)
@protected
async def severity_bug_statistic(request):
	resp = list()
	for opened_by in request.json['openedBy']:
		request_body = dict(openedBy=opened_by, openedBeginDate=request.json['openedBeginDate'],
							openedEndDate=request.json['openedEndDate'])
		resp.append(severity_bug_rate_statistic(request_body))
	if resp:
		return resp_200(resp)
	else:
		return resp_204()


# 严重bug详情
@test_as_bp.route('SeverityBugDetails', methods=['POST'])
@openapi.tag("测试考核指标")
@openapi.summary("严重缺陷详情")
@openapi.body({"application/json": TestBugDetails},
			  description="参数均为必填项",
			  required=True)
@protected
async def severity_bug_details_list(request):
	details_obj = BugModel.severity_bug_details(openedBy=request.json['openedBy'],
												openedBeginDate=request.json['openedBeginDate'],
												openedEndDate=request.json['openedEndDate'])
	if details_obj:
		resp = list()
		for detail_obj in details_obj:
			response_body = dict(ztId=detail_obj.id, severity=detail_obj.severity, title=detail_obj.title,
								 projectId=detail_obj.project,
								 openedBy=detail_obj.openedBy,
								 openedDate=str(detail_obj.openedDate),
								 resolvedBy=detail_obj.resolvedBy,
								 accessLink=f"http://192.168.1.43:8086/zentao/bug-view-{detail_obj.id}.html")
			resp.append(response_body)
		return resp_200(resp)
	else:
		return resp_204()


# 遗漏bug统计
@test_as_bp.route('MissingBugStatistic', methods=['POST'])
@openapi.tag("测试考核指标")
@openapi.summary("遗漏缺陷统计")
@openapi.body({"application/json": TestMissingBugSta},
			  description="参数均为必填项，其中openedBy为string元素的list类型(bug解决者，传用户信息的account)，如：['zhangl']、['zhangl','zyp']",
			  required=True)
@protected
async def missing_bug_statistic(request):
	resp = list()
	for openedBy in request.json['openedBy']:
		request_body = dict(openedBy=openedBy, openedBeginDate=request.json['openedBeginDate'],
							openedEndDate=request.json['openedEndDate'])
		resp.append(test_missing_bug_score_statistic(request_body))
	if resp:
		return resp_200(resp)
	else:
		return resp_204()


@test_as_bp.route('MissingBugDetails', methods=['POST'])
@openapi.tag("测试考核指标")
@openapi.summary("遗漏缺陷详情")
@openapi.body({"application/json": TestMissingBugDetails},
			  description="参数均为必填项",
			  required=True)
@protected
async def missing_bug_details(request):
	details_obj = BugModel.missing_bug_details(openedBy=request.json['openedBy'],
											   openedBeginDate=request.json['openedBeginDate'],
											   openedEndDate=request.json['openedEndDate'])
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
