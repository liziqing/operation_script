# -*- coding: utf-8 -*-
import redis
import os

class HandlingImageService:

	DIR = '/home/transdoing/Temp/crawler_image'
	FILE = '/home/transdoing/Temp/crawler_image/image.txt'
	REDIS_KEY_JOBS = 'bq:crawler_handle_image:jobs'
	REDIS_KEY_KEYS = 'bq:crawler_handle_image:failed'

	DEL_KEY = [
		'bq:crawler_handle_image:stallTime',
		# 'bq:crawler_handle_image:stalling',
		# 'bq:crawler_handle_image:failed',
		# 'bq:crawler_handle_image:id',
		# 'bq:crawler_handle_image:jobs',
		# 'bq:crawler_handle_image:active'
		]

	final_crawler_handle_image = {}

	def __init__(self, host="localhost", port=6379, password=None, db=0):
	    self.conn = redis.StrictRedis(host=host, password=password, port=port, db=db)

	def process_image(self):
		if not os.path.isdir(self.DIR):
			os.mkdir(self.DIR)
			if not os.path.isfile(self.FILE):
				os.mknod(self.FILE)
		crawler_handle_image_keys_list = list(self.conn.smembers(self.REDIS_KEY_KEYS))
		crawler_handle_image_jobs_dict = dict(self.conn.hgetall(self.REDIS_KEY_JOBS))
		for crawler_handle_image_key in crawler_handle_image_keys_list:
			# crawler_handle_image_key = int(crawler_handle_image_key)
			try:
				# import pdb;pdb.set_trace()
				crawler_handle_image_str = crawler_handle_image_jobs_dict[crawler_handle_image_key]
				crawler_handle_image_value = eval(crawler_handle_image_str)['data']
				self.final_crawler_handle_image[crawler_handle_image_key] = crawler_handle_image_value
			except KeyError :
				print "KeyError: can not find key: "+str(crawler_handle_image_key)
		self.persist_data(self.final_crawler_handle_image)
		self.delete_keys()

	def persist_data(self, data):
		with open(self.FILE, 'w') as f:
			f.write(str(data))
			f.close()
				
	def delete_keys(self):
		for key in self.DEL_KEY:
			self.conn.delete(key)

if __name__ == "__main__":
	HandlingImageService().process_image()

