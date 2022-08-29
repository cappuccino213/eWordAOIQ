"""
@File : assessment_rule_viewer.py
@Date : 2022/8/5 9:17
@Author: 九层风（YePing Zhang）
@Contact : yeahcheung213@163.com
"""
from sanic import Blueprint
from sanic_openapi import openapi

from models.assessment_rule_model import *
from models.request_schema import AssessmentRuleAdd, AssessmentRuleQuery, AssessmentRuleUpdate
from controller.response_encapsulate import *
from controller.auth import protected

"""考核客观指标设置"""
ass_rule_bp = Blueprint('ass_rule_bp', url_prefix='/api/AssessmentRule')


# 增加指标
@ass_rule_bp.route('add', methods=['POST'])
@openapi.tag("考核客观指标")  # API标签
@openapi.summary("增加")  # API信息描述
@openapi.body({"application/json": AssessmentRuleAdd},
			  description="所有参数必填",
			  required=True)
@protected
async def add_assessment_rule(request):
	data = AssessmentScoreRuleModel(request.json)
	if not data.if_same_exist(request.json['indexType'], request.json['indexID']):
		create(data)
		if data.id:
			return resp_200(data.to_dict(), message="增加考核指标规则成功")
		else:
			return resp_200({}, message="增加考核指标规则失败", status=False)
	else:
		return resp_200({}, message="增加考核指标规则失败,同类型指标已存在相同的指标名称或指标id", status=False)


# 查询指标
@ass_rule_bp.route('query', methods=['POST'])
@openapi.tag("考核客观指标")  # API标签
@openapi.summary("查询")  # API信息描述
@openapi.body({"application/json": AssessmentRuleQuery},
			  description="参数条件可选，可不入参或者参数值为空",
			  required=True)
@protected
async def query_assessment_rule(request):
	resp = multiple_condition_query(request.json)
	if resp:
		return resp_200([column.to_dict() for column in resp])
	else:
		return resp_204()


# 更新指标
@ass_rule_bp.route('update', methods=['PUT'])
@openapi.tag("考核客观指标")  # API标签
@openapi.summary("修改")  # API信息描述
@openapi.body({"application/json": AssessmentRuleUpdate},
			  description="所有参数均为必填项,indexType是枚举值：dev或test",
			  required=True)
@protected
async def update_assessment_rule(request):
	data = AssessmentScoreRuleModel(request.json)
	if not data.if_same_exist(request.json['indexType'], request.json['indexID'],
							  request.json['id']):
		resp = update(request.json, AssessmentScoreRuleModel)
		if resp:
			return resp_200(resp, "更新考核指标规则成功")
		else:
			return resp_200({}, message="更新考核指标规则失败", status=False)
	else:
		return resp_200({}, message="修改考核指标规则失败,同类型指标已存在相同的指标id", status=False)


# 删除指标
@ass_rule_bp.route('delete', methods=['DELETE'])
@openapi.tag("考核客观指标")  # API标签
@openapi.summary("删除")  # API信息描述
@openapi.parameter("id", int, location="query")
@protected
async def delete_assessment_rule(request):
	resp = logical_delete(request.args.get('id'), AssessmentScoreRuleModel)
	if resp:
		return resp_200(resp, "删除考核指标规则成功")
	else:
		return resp_200({}, message="删除考核指标规则失败", status=False)


if __name__ == "__main__":
	pass
