# -*- coding: utf-8 -*-

import click
import os
import re
import datetime
import time

@click.command()
@click.option('--path', default='/root/releases', help='The path of code')

def clear(path):
    if not os.path.isdir(path):
        click.echo(click.style('The path not exist', fg='red'))
        return
    
    now = datetime.datetime.now()
    one_month_ago_datetime = now - datetime.timedelta(days=30)
    one_month_ago = time.mktime(one_month_ago_datetime.timetuple())
    
    dir_name_dict = {}
    
    delete_dir_name_list = []
    stay_dir_name_list = []
    
    for dir_name in  os.listdir(path):
        if re.match(r'^\.', dir_name):
           continue
       
        m = re.match(r'(.+)_(\d+)_bak$', dir_name)
        if m is not None:
            project = m.group(1)
            bak_time = m.group(2)
            
#             if project not in dir_name_dict.keys():
#                 dir_name_dict[project] = []
#                 
#             dir_name_dict[project].append(bak_time) 
            
            bak_datetime = datetime.datetime.strptime(bak_time, '%Y%m%d%H%M%S')
            timestamp = time.mktime(bak_datetime.timetuple())
            
            if timestamp< one_month_ago:
                delete_dir_name_list.append(dir_name)
            else:
                stay_dir_name_list.append(dir_name)
        
    for delete_dir_name in  delete_dir_name_list:
        
        delete_path = os.path.join(path, delete_dir_name)
        
        os.system('rm -Rf "%s"' % delete_path)
        
        #shutil.rmtree(delete_path)
        click.echo(delete_path)
    
    #print stay_dir_name_list
    click.echo(click.style('success', fg='green'))


if __name__ == '__main__':
    clear()