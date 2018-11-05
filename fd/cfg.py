#!/usr/bin/python2.7

import datetime
import ConfigParser

class StudentInfo(object):
    def __init__(self,filepath):
        self.filepath = filepath
        self.cfg = ConfigParser.ConfigParser()

    def cfg_load(self):
        self.cfg.read(self.filepath)  

    def cfg_dump(self):
        se_list = self.cfg.sections()
        print '=============>'
        for se in se_list:
            print se
            print self.cfg.items(se)
        print '<============='

    def cfg_del_section(self,section):
        self.cfg.remove_section(section)

    def cfg_del_option(self,section,key):
        self.cfg.remove_option(section,key)
	
    def cfg_add_section(self,section):
        self.cfg.add_section(section)

    def cfg_set_item(self,section,option,value):
	self.cfg.set(section,option,value)

    def cfg_save(self):
        fp = open(self.filepath,'w')
        self.cfg.write(fp)
        fp.close()    

if __name__== '__main__':
    info = StudentInfo('imooc')
    info.cfg_load()
    info.cfg_dump() 
    info.cfg_set_item('userinfo','pwd','abc')
    info.cfg_dump()
    info.cfg_add_section('login')
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    info.cfg_set_item('login',nowTime,'20') 
    info.cfg_del_option('study','linux_base')
    info.cfg_dump()
    info.cfg_save()
