"""
@File : main.py
@Date : 2022/8/3 10:11
@Author: 九层风（YePing Zhang）
@Contact : yeahcheung213@163.com
"""
import uvicorn

from sanic import Sanic, response
from sanic_openapi import openapi3_blueprint
from sanic_cors import CORS

# from config import AUTH

from viewers.user_viewer import user_bp
from viewers.assessment_rule_viewer import ass_rule_bp
from viewers.product_viewer import product_bp
from viewers.project_viewer import project_bp
from viewers.build_viewer import build_bp
from viewers.testtask_viewer import testtask_bp
from viewers.smoke_test_record_viewer import smoke_test_bp
from viewers.test_assessment_statistic_viewer import test_as_bp
from viewers.dev_assessment_statistic_viewer import dev_as_bp
from viewers.version_info_viewer import version_bp
from viewers.static_viewer import sbp

from config import *

# 声明应用
app = Sanic(__name__)

# 添加token秘钥
app.config.SECRET = AUTH.get("SECRET")

# 解决跨域问题
CORS(app)

# 应用级的上下文对象，且使用方法与 请求上下文 一致， 这有效的避免了命名冲突可能导致的潜在问题
# app.ctx.db = DataBase()

# 注册swagger文档
app.blueprint(openapi3_blueprint)

# 注册用户蓝图
app.blueprint(user_bp)

# 注册考核指标规则
app.blueprint(ass_rule_bp)

# 注册产品
app.blueprint(product_bp)

# 注册项目
app.blueprint(project_bp)

# 注册测试单
app.blueprint(testtask_bp)

# 提交测试的程序版本信息
app.blueprint(build_bp)

# 注册冒烟记录
app.blueprint(smoke_test_bp)

# 注册测试考核指标路由
app.blueprint(test_as_bp)

# 注册开发考核指标路由
app.blueprint(dev_as_bp)

# 产品版本信息
app.blueprint(version_bp)

app.blueprint(sbp)

# 配置swagger文档
app.config.API_VERSION = SWAGGER_DOC.get("VERSION")
app.config.API_TITLE = SWAGGER_DOC.get("TITLE")
app.config.ACCESS_LOG = SWAGGER_DOC.get("ACCESS_LOG")


@app.route('/')
async def index_request(request):
	return await response.file('./index.html')


if __name__ == "__main__":
	# uvicorn.run(app=f'main:app', host='0.0.0.0', port=8112, workers=4, reload=True)

	uvicorn.run(app=f'{RUN_CONFIG.get("RUN_FILE_NAME")}:app', host='0.0.0.0', port=RUN_CONFIG.get("PORT"),
				workers=RUN_CONFIG.get("WORKERS"), reload=RUN_CONFIG.get("RELOAD"))
