'''
Created by auto_sdk on 2016.04.13
'''
from base import RestApi
class FenxiaoGradeUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.grade_id = None
		self.name = None

	def getapiname(self):
		return 'taobao.fenxiao.grade.update'
