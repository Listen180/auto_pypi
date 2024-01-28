#!/Users/leisen/anaconda3/bin/python3
# -*- coding: UTF-8 -*-

# ********************************************************
# * Author        : LEI Sen
# * Email         : sen.lei@outlook.com
# * Create time   : 2018-11-30 11:14
# * Last modified : 2018-11-30 11:14
# * Filename      : __init__.py
# * Description   : 
# *********************************************************

import time
import platform
import subprocess

class avatar(object):
    def __init__(self):
        self._judge()
        if self.n == 1:
            self.type_1()
        elif self.n == 2:
            self.type_2()
        elif self.n == 3:
            self.type_3()

    def _judge(self):
        OS_TYPE = platform.platform().split('-')[0]
        if OS_TYPE == 'Darwin':
            self.n = 1
        elif OS_TYPE == 'Linux':
            self.n = 2
        elif OS_TYPE == 'Windows':
            self.n = 3
        else:
            self.n = 2

    def type_1(self):
        info = '''
 █████╗ ██╗   ██╗████████╗ ██████╗     ██████╗ ██╗   ██╗██████╗ ██╗
██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗    ██╔══██╗╚██╗ ██╔╝██╔══██╗██║
███████║██║   ██║   ██║   ██║   ██║    ██████╔╝ ╚████╔╝ ██████╔╝██║
██╔══██║██║   ██║   ██║   ██║   ██║    ██╔═══╝   ╚██╔╝  ██╔═══╝ ██║
██║  ██║╚██████╔╝   ██║   ╚██████╔╝    ██║        ██║   ██║     ██║
╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝     ╚═╝        ╚═╝   ╚═╝     ╚═╝

                    Copyright 2018-2024 Sen LEI 
                       All Rights Reserved
                '''
        print(info)
        time.sleep(1)

    def type_2(self):
        info = '''
 █████╗ ██╗   ██╗████████╗ ██████╗     ██████╗ ██╗   ██╗██████╗ ██╗
██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗    ██╔══██╗╚██╗ ██╔╝██╔══██╗██║
███████║██║   ██║   ██║   ██║   ██║    ██████╔╝ ╚████╔╝ ██████╔╝██║
██╔══██║██║   ██║   ██║   ██║   ██║    ██╔═══╝   ╚██╔╝  ██╔═══╝ ██║
██║  ██║╚██████╔╝   ██║   ╚██████╔╝    ██║        ██║   ██║     ██║
╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝     ╚═╝        ╚═╝   ╚═╝     ╚═╝

                    Copyright 2018-2024 Sen LEI 
                       All Rights Reserved
                '''
        print(info)
        time.sleep(1)

    def type_3(self):
        info = '''
 █████╗ ██╗   ██╗████████╗ ██████╗     ██████╗ ██╗   ██╗██████╗ ██╗
██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗    ██╔══██╗╚██╗ ██╔╝██╔══██╗██║
███████║██║   ██║   ██║   ██║   ██║    ██████╔╝ ╚████╔╝ ██████╔╝██║
██╔══██║██║   ██║   ██║   ██║   ██║    ██╔═══╝   ╚██╔╝  ██╔═══╝ ██║
██║  ██║╚██████╔╝   ██║   ╚██████╔╝    ██║        ██║   ██║     ██║
╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝     ╚═╝        ╚═╝   ╚═╝     ╚═╝

                    Copyright 2018-2024 Sen LEI 
                       All Rights Reserved
                '''
        print(info)
        time.sleep(1)


avatar()
