#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from base.service import *
from time import sleep

def main():
    ok = okexFuture()
    print(ok.future_ticker())

