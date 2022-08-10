"""
@File : log_loguru.py
@Date : 2022/8/3 11:30
@Author: 九层风（YePing Zhang）
@Contact : yeahcheung213@163.com
"""

import time

from pathlib import Path

from loguru import logger


class Logging:
	__instance = None

	project_path = Path.cwd()
	log_path = project_path / 'log'
	log_time = time.strftime('%Y%m%d')

	logger.add(f"{log_path}/{log_time}.log", rotation="50MB", encoding="utf-8", enqueue=True, retention="10 days")

	# 参数定义参考 loguru官网 http://loguru.readthedocs.io/
	# https://cloud.tencent.com/developer/article/1849382?from=article.detail.1640693
	# https://cloud.tencent.com/developer/article/1664382
	def __new__(cls, *args, **kwargs):
		if not cls.__instance:
			cls.__instance = super(Logging, cls).__new__(cls, *args, **kwargs)

		return cls.__instance

	@classmethod
	def info(cls, msg):
		return logger.info(msg)

	@classmethod
	def debug(cls, msg):
		return logger.debug(msg)

	@classmethod
	def warning(cls, msg):
		return logger.warning(msg)

	@classmethod
	def error(cls, msg):
		return logger.error(msg)


logging = Logging()

if __name__ == "__main__":
	logging.info("中文test")
	logging.debug("中文test")
	logging.warning("中文test")
	logging.error("中文test")
