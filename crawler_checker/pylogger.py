# -*- coding: utf-8 -*-
import logging
import sys
import os
from datetime import datetime

from pysys_checker import Pysys
# from beaker.container import logger
class Pylogger: 
    def init_log(self, args):   
        # 创建一个logger 
        logger = logging.getLogger('checker_logger') 
        logger.setLevel(logging.ERROR) 
        
        log_dir=str(Pysys().main(args))
        now = datetime.now().strftime("%m%d%H%M%S")

        try:
            if not os.path.isdir(log_dir):
                os.mkdir(log_dir)
        except OSError, e:
            print 'please mkdir log path!'
            sys.exit(1)
        log_path = log_dir+'/'+str(now)+".log"
        # 创建一个handler，用于写入日志文件 
        fh = logging.FileHandler(log_path) 
        fh.setLevel(logging.ERROR) 
           
    #     # 再创建一个handler，用于输出到控制台 
    #     ch = logging.StreamHandler() 
    #     ch.setLevel(logging.DEBUG) 
           
        # 定义handler的输出格式 
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') 
        fh.setFormatter(formatter) 
    #     ch.setFormatter(formatter) 
        
        # 给logger添加handler 
        logger.addHandler(fh) 
    #     logger.addHandler(ch) 
           
        # 记录一条日志 
    #     logger.info('foorbar') 
        print '##################################################'
        print 'log dir:  '+log_path
        print '##################################################'
        return logger