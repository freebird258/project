
#!/usr/bin/python
#coding=utf-8
import  xml.dom.minidom
import ast,os,sys,time
import mustaine
import random
from common import callapi
from common import postget  
from common import xmlanal
from common.callapi import env_get, createtxt, addtxt, gettoken, getuserid,savelog
from common.postget import login_post, req_post, req_get
from mustaine.client import HessianProxy
reload(sys)
sys.setdefaultencoding('utf-8')
# fronturl=env_get("")
fronturl="http://10.43.1.127:9200/pe_engine/service/"
xmlname="req_hessian"
#
now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))   
lastdir=os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
# print lastdir
# print "xmlname:"+xmlname
txtfile=os.path.join(lastdir,"pytemplate","result",str(now+xmlname+".txt"))
createtxt(txtfile,now)
print r"生成报告成功!!  "+txtfile
xmlfile=os.path.join(lastdir,"pytemplate","data",str(xmlname+".xml"))
# print xmlfile
dom = xml.dom.minidom.parse(xmlfile)
root = dom.documentElement
itemlist = root.getElementsByTagName('testcase')

def SaveDict(savedict,dataid):        
    dataid=dataid
##
    if savedict['req'][0]['RequestType']== "string" :
                   print r"API请求参数类型为"+savedict['req'][0]['RequestType']
                   dictlist=savedict['req']
                   urldata=dictlist[2]['parm']
                   service_get= dictlist[1]['url'].split('.',2)
                   print urldata
                   tcp_url=fronturl+service_get[0]
                   print tcp_url
                   service = HessianProxy(tcp_url)
                   service.method= service_get[2]                 
                   resplog="resplog=service."+service_get[1]+"(long(urldata[1]),urldata[0])."+service_get[2]
                   print resplog
                   exec(resplog)
                   print resplog
                   savelog(txtfile,dataid,urldata,resplog)
                   
    elif savedict['req'][0]['RequestType']== "json" :
                   print r"API请求参数类型为"+savedict['req'][0]['RequestType']
                   dictlist=savedict['req']
                   urldata=dictlist[2]['parm']
                   service_get= dictlist[1]['url'].split('.',2)
                   print urldata
                   tcp_url=fronturl+service_get[0]
                   print tcp_url
                   service = HessianProxy(tcp_url)
                   service.method= service_get[1]                 
                   resplog="resplog=service."+service_get[1]+"(urldata)."+service_get[2]
                   print resplog
                   exec(resplog)
                   print resplog
                   savelog(txtfile,dataid,urldata,resplog)
                           
    elif savedict['req'][0]['RequestType']== "mix" :
                   print r"API请求参数类型为"+savedict['req'][0]['RequestType']
                   dictlist=savedict['req']
                   urldata=dictlist[2]['parm']
                   service_get= dictlist[1]['url'].split('.',2)
                   print urldata
                   tcp_url=fronturl+service_get[0]
                   print tcp_url
                   service = HessianProxy(tcp_url)
                   service.method= service_get[1]                 
                   resplog="resplog=service."+service_get[1]+"(urldata[0],urldata[1],urldata[2],urldata[3],urldata[4])."+service_get[2]
                   exec(resplog)
                   print resplog
                   savelog(txtfile,dataid,urldata,resplog)

        
        
for item in itemlist:
    addtxt(txtfile,item.getAttribute("id"),item.getAttribute("name"),item.getAttribute("description"))
#item=testcase
#type = item.getElementsByTagName('data')[0]
#print "Type: %s" % type.childNodes[0].data
    for datainfo in  item.getElementsByTagName('data')   :
        datadict=datainfo.childNodes[0].data
        datadict=str(datadict).replace("null", '"null"').replace("false", '"false"').replace("true", '"true"')
        print r"==============↓↓以下为data id="+datainfo.getAttribute("id")+r"接口执行情况：=================="#######取data id 
#id值传到下面的函数里
        datadict=eval(datadict)
#解析字典：
        SaveDict(datadict,datainfo.getAttribute("id"))
        
        
        
        
        
        
        
# 随机数代码
# 
#     b_list = range(9999,9999999)
#     blist_random=[]
#     blist_random = random.sample(b_list, 1)

#                    if urldata.get("clientId")=="randmon_clientid":
#                        urldata["clientId"]=blist_random[0]
#                    for k,v in urldata.items():
#                            if urldata.get(k)=="random":
#                                urldata[k]=blist_random[0]
