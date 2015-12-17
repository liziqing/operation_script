#!/usr/bin/python 
from pymongo import MongoClient
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')

if os.path.isfile(dotenv_path):
    load_dotenv(dotenv_path)
else:
    dotenv_path = join('/data/scrapyd/', '.env')
    if os.path.isfile(dotenv_path):
        load_dotenv(dotenv_path)

RESULT = float(os.environ.get('RESULT'))
FILE = os.environ.get('FILE')
IP = os.environ.get('IP')
PORT = int(os.environ.get('PORT'))
TODAY = os.environ.get('TODAY')
TOMORROW = os.environ.get('TOMORROW')

connection = MongoClient(IP, PORT)
db = connection.shiji_shop
goods = db.goods

count_result = []

def goods_aggregated_by_scan_date(date):
	datas = goods.aggregate([{'$match': {"scan_date": date}},{'$group': {'_id':"$from_site", 'num':{'$sum':1}}},{'$sort':{'_id':1}}])
	return datas

#datas_today datas_tomorrow are both list
def compare_goods(datas_today, datas_tomorrow):
	for i in range(len(datas_today)):
		data_today = datas_today[i]
		data_tomorrow = datas_tomorrow[i]
		if data_today['_id'] == data_tomorrow['_id']:
			result = float(data_tomorrow['num']) / float(data_today['num'])
			if result > RESULT:
				count_str = data_today['_id']+':'+str(result)
				count_result.append(count_str)

	count_data = '\n'.join(count_result)
	write_into_file(count_data)

def write_into_file(data):
	with open(str(FILE), 'w') as f:
		f.write(str(data))
		f.close()

def get_list_from_cursor(list1, cursor):
	for temp_cursor in cursor:
		list1.append(temp_cursor)
	return list1

datas_today = goods_aggregated_by_scan_date(TODAY)
datas_today_list = []
datas_today_list = get_list_from_cursor(datas_today_list, datas_today)
datas_tomorrow = goods_aggregated_by_scan_date(TOMORROW)
datas_tomorrow_list = []
datas_tomorrow_list = get_list_from_cursor(datas_tomorrow_list, datas_tomorrow)
compare_goods(datas_today_list, datas_tomorrow_list)