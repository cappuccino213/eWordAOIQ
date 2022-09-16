"""
@File : smoke_test_record_viewer.py
@Date : 2022/9/2 9:17
@Author: 九层风（YePing Zhang）
@Contact : yeahcheung213@163.com
"""
from sanic import Blueprint
from sanic_openapi import openapi

from models.smoke_test_record_model import *
from models.testtask_model import TestTaskModel
from models.request_schema import SmokeTestRecordAdd, SmokeTestRecordUpdate, SmokeTestRecordList
from controller.response_encapsulate import *
from controller.auth import protected

"""冒烟测试记录视图"""
smoke_test_bp = Blueprint('smoke_test_bp', url_prefix='/api/SmokeTestRecord')


# 获取测试单列表
@smoke_test_bp.route('list', methods=['POST'])
@openapi.tag("冒烟测试记录")  # API标签
@openapi.summary("获取冒烟列表")  # API信息描述
@openapi.body({"application/json": SmokeTestRecordList}, description="参数均为选填", required=True)
@protected
async def get_testtask_list(request):
	resp_list = SmokeTestRecordModel.get_smoke_test_list(testTaskID=request.json['testTaskID'],
														 product=request.json['product'],
														 tester=request.json['tester'],
														 smokeResult=request.json['smokeResult'],
														 relatedPerson=request.json['relatedPerson'],
														 begin=request.json['begin'],
														 end=request.json['end'])

	if resp_list:
		smoke_list = []
		for resp in resp_list:
			smoke_list.append(resp.to_dict())
		return resp_200(smoke_list)
	else:
		return resp_204()


# 增加冒烟记录
@smoke_test_bp.route('add', methods=['POST'])
@openapi.tag("冒烟测试记录")  # API标签
@openapi.summary("增加")  # API信息描述
@openapi.body({"application/json": SmokeTestRecordAdd}, description="所有参数均必填", required=True)
@protected
async def add_smoke_test(request):
	data = SmokeTestRecordModel(request.json)
	if not data.if_same_testtask_exist(request.json['testTaskID']):
		create(data)
		if data.id:
			# 同时更新测试单中subStatus(此字段无用，被用来做smokeflag记录的标记使用)标记
			TestTaskModel().sync_mark_smoke_result(request.json['testTaskID'], request.json['smokeResult'])
			return resp_200(data.to_dict(), message="增加冒烟测试记录成功")
		else:
			return resp_200({}, message="增加冒烟测试记录失败", status=False)
	else:
		return resp_200({}, message=f"增加冒烟测试记录失败,已存在相同测试单{request.json['testTaskID']}的数据", status=False)


# 批量增加
@smoke_test_bp.route('AddBatch', methods=['POST'])
@openapi.tag("冒烟测试记录")  # API标签
@openapi.summary("批量增加")  # API信息描述
@openapi.body({"application/json": [SmokeTestRecordAdd]}, description="参数为单次增加的body的list", required=True)
@protected
async def add_batch_smoke_test(request):
	if not request.json:
		return resp_422(message="入参格式有误，请检查确认")
	else:
		data_list = [SmokeTestRecordModel(data) for data in request.json]
		# 判断是否是有已存在的测试单id
		exist_list = []
		for data in data_list:
			if data.if_same_testtask_exist(data.testTaskID):
				exist_list.append(data.testTaskID)
		# 批量增加
		if not exist_list:
			create_batch(data_list)
			for data in data_list:
				TestTaskModel().sync_mark_smoke_result(data.testTaskID, data.smokeResult)
			return resp_200(TestTaskModel().to_json(data_list), message="批量增加冒烟测试记录成功")
		else:
			return resp_200({}, message=f"增加冒烟测试记录失败,已存在相同测试单{exist_list}的数据", status=False)


# 更新
@smoke_test_bp.route('update', methods=['PUT'])
@openapi.tag("冒烟测试记录")  # API标签
@openapi.summary("修改")  # API信息描述
@openapi.body({"application/json": SmokeTestRecordUpdate}, description="所有参数均为必填", required=True)
@protected
async def update_smoke_test(request):
	data = SmokeTestRecordModel(request.json)
	# 判断是否存在需要修改的记录
	original_data = data.if_same_testtask_exist(request.json['testTaskID'])
	if original_data:
		# update需要主键id
		request.json['id'] = original_data.id
		# 修改时也要同步状态
		TestTaskModel().sync_mark_smoke_result(request.json['testTaskID'], request.json['smokeResult'])
		resp = update(request.json, SmokeTestRecordModel)
		if resp:
			return resp_200(resp, "更新冒烟测试记录成功")
		else:
			return resp_200({}, message="更新冒烟测试记录失败", status=False)
	else:
		return resp_200({}, message=f"测试单{data.testTaskID}冒烟记录不存在，修改失败", status=False)


# 删除指标
@smoke_test_bp.route('delete', methods=['DELETE'])
@openapi.tag("冒烟测试记录")  # API标签
@openapi.summary("删除")  # API信息描述
@openapi.parameter("testTaskID", int, location="query")
@protected
async def delete_smoke_test(request):
	"""
	删除符合测试单id的所有冒烟记录
	:param request:测试单id
	:return: 删除的记录list
	"""
	# 获取需要删除的数据
	data_list = SmokeTestRecordModel.query_by_testtaskid(request.args.get('testTaskID'))
	if data_list:
		resp_list = []
		for data in data_list:
			resp = physical_delete(data.id, SmokeTestRecordModel)
			# 删除也要同步状态为NA（未标记）
			TestTaskModel().sync_mark_smoke_result(data.testTaskID, 'NA')
			resp_list.append(resp)
		if resp_list:
			return resp_200(resp_list, "删除冒烟测试记录成功")
		else:
			return resp_200({}, message="删除冒烟测试记录失败", status=False)
	else:
		return resp_200({}, message=f"测试单{request.args.get('testTaskID')}冒烟记录不存在，删除失败", status=False)


if __name__ == "__main__":
	pass
