# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 18:47:56 2021

@author: shane
"""
import os
from src.admin import subprocess_cmd

#once that's done, we generate requirements using pipreqs
def create_reqs(foldername=None):
    command="pipreqs .\ "
    if foldername:
        foldername=foldername
    else:
        foldername=os.getcwd()
    subprocess_cmd(command,foldername)

#in the event that there needs to be an update
def req_del():
    try:
        os.remove(os.path.join(os.getcwd(),'requirements.txt'))
    except Exception as e:
        return(e)
    
#this is the event where there needs to en update
def replace_req(foldername=None):
    if foldername:
        os.chdir(foldername)
    try:
        req_del()
    except FileNotFoundError:
        pass
    create_reqs()