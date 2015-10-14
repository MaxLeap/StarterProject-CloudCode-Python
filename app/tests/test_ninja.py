#coding:utf-8

import ML
import function.ninja
import hook.hooks
import job.job
import json
from nose.tools import with_setup
from ML import Server

def setup_func():
    ML.init("","")
