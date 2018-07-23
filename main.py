#!/usr/bin/env  python
# -*- coding: utf-8 -*-
import sys
if len(sys.argv) >= 2:
    SCRIPT_SELECT = sys.argv[1]
else:
    from base.settings import SCRIPT_SELECT

import importlib
print('开始运行app目录下的{0}.py脚本下的main函数'.format(SCRIPT_SELECT))

try:
    run = importlib.import_module('app.' + SCRIPT_SELECT)
except:
    print('app目录下不存在{0}.py文件'.format(SCRIPT_SELECT))


run.main()


