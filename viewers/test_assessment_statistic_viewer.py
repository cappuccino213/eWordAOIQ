"""
@File : test_assessment_statistic_viewer.py
@Date : 2022/8/8 16:56
@Author: 九层风（YePing Zhang）
@Contact : yeahcheung213@163.com
"""
from sanic import Blueprint
from sanic_openapi import openapi

from models.testtask_project_model import *
from models.request_schema import ProjectWeight, InvalidBug, SeverityBug
from models.bug_model import invalid_bug_rate_statistic, severity_bug_rate_statistic
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


# 严重bug统计
@test_as_bp.route('SeverityBugStatistic', methods=['POST'])
@openapi.tag("测试考核指标")
@openapi.summary("严重缺陷统计")
@openapi.body({"application/json": SeverityBug},
			  description="参数均为必填项，其中openedBy为string元素的list类型(bug提出人，传用户信息的account)，如：['zhangl']、['zyp','zhangl']",
			  required=True)
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


if __name__ == "__main__":
	pass
