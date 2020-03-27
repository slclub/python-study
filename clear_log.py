#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import commands
import sys
# 学习使用 commands 与sys 执行 shell 命令

# 遍历相应的文件夹  执行操作
def gci(filepath):
        files = os.listdir(filepath)
        for fi in files:
                fi_d = os.path.join(filepath,fi)
                if os.path.isdir(fi_d):
                        print(os.path.join(filepath,fi_d), '###', fi_d)
                        clear_log( os.path.join(filepath,fi_d) )
                else:
                        print(os.path.join(filepath,fi_d))

# 删除操作，根据相应的规则删除服务的日志文件
def clear_log(path_full):
        cmd = ''
        if 'proxy_java' in path_full :
                cmd = 'rm -rf ' + path_full + "/proxy.log.*"

        if 'center_service1' in path_full :
                cmd = 'rm -rf ' + path_full + "/center_service1.*.log"

        if 'game_service' in path_full :
                cmd = "rm -rf " + path_full + "/game_service*.*.log"

        if 'gate_java' in path_full :
                cmd = "rm -rf " + path_full + "/gate.log.*"

        if 'map_service1' in path_full :
                cmd = "rm -rf " + path_full + "/map_service1.*.log"

        if 'platform_proxy_service1' in path_full :
                cmd = "rm -rf " + path_full + "/platform_proxy_service1.*.log"

        if 'platform_service1' in path_full :
                cmd = "rm -rf " + path_full + "/platform_service1.*.log"

        print(cmd)
        os.system(cmd)

#递归遍历用户服务日志目录下所有文件
# 获取命令对应的返回值
def bash_get(cmd):
        #p = os.popen(cmd)
        #rtn = p.read()
        #p.close()
        rtn = commands.getstatusoutput(cmd)
        return rtn[1]
# 获取服务路径
def get_log_path(input_path):
        home_path=bash_get("echo $HOME")
        if input_path == '' :
                input_path='server/log/'

        rtn = str(home_path) + '/' + input_path
        return rtn

# 主函数
def main(argvs):
        param_arg=''
        if len(argvs) > 1:
                param_arg = argvs[1]
        log_path = get_log_path(param_arg)
        print(log_path)
        gci(log_path)

main(sys.argv)
#gci('/root')
