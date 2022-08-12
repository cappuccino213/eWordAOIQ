"""
@File : dev_assessment_statistic_viewer.py.py
@Date : 2022/8/8 17:05
@Author: 九层风（YePing Zhang）
@Contact : yeahcheung213@163.com
"""
from sanic import Blueprint
from sanic_openapi import openapi

from models.request_schema import DevBugSta
from models.bug_model import activated_bug_rate_statistic, severity_bug_rate_statistic
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
		request_body = dict(resolvedBy=resolvedBy, resolvedBeginDate=request.json['resolvedBeginDate'],
							resolvedEndDate=request.json['resolvedEndDate'])
		resp.append(activated_bug_rate_statistic(request_body))
	if resp:
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


if __name__ == "__main__":
	pass
