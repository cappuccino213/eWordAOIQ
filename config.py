"""
@File : config.py
@Date : 2022/8/3 11:13
@Author: 九层风（YePing Zhang）
@Contact : yeahcheung213@163.com
"""

from urllib.parse import quote_plus as urlquote

"""定义配置文件"""

# 数据库配置
PASSWORD = urlquote('p@ssw0rd')  # 防止带有特殊字符被转义

DATABASE_CONFIG = {
	"DATABASE_URL": "mysql+pymysql://test:123456@192.168.1.43:3306/zentao",
	"SQLALCHEMY_BINDS": {'zentao': "mysql+pymysql://test:123456@192.168.1.43:3306/zentao?charset=UTF8MB4",
						 'eWordRDM_dev': f"mssql+pymssql://sa:{PASSWORD}@192.168.1.45:1433/eWordRDM_dev"},
	"SQL_ECHO": True  # 是否输出执行语句
}

# API文档设置
SWAGGER_DOC = {
	"VERSION": "v1.0.0",
	"TITLE": "考核客观指标查询API",
	"ACCESS_LOG": False
}

# 授权设置
AUTH = {"IF_AUTH": False,
		"SECRET": "eWordAOIQ_TomTaw@HZ"}

# 运行配置
RUN_CONFIG = {
	"RUN_FILE_NAME": "main",  # 运行主函数文件名
	"PORT": 8088,  # 运行监听的端口号
	"WORKERS": 4,  # 进程数
	"RELOAD": True  # 是否重载
}

if __name__ == "__main__":
	pass
