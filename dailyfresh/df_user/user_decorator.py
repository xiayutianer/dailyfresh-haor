#coding=utf-8
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
import logging
logger=logging.getLogger('django')
#如果未登录则转到登录页面
def login(func):
    def login_fun(request,*args,**kwargs):
        logger.info('hrtest')
        if request.session.has_key('user_id'):
            logger.info('request:')
            logger.info(request)
            logger.info('request.session:')
            logger.info(request.session)
            return func(request,*args,**kwargs)
        else:
            red=HttpResponseRedirect('/user/login/')
            logger.info('red:')
            logger.info(red)
            red.set_cookie('url',request.get_full_path())
            return red
    logger.info('hah')
    return login_fun
'''
http://127.0.0.1
request.path：表示当前路径，为/200/
request.get_full_path()：表示完整路径，为/200/?type=10

'''
