# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 18:47:56 2021

@author: shane
"""
import os
import subprocess

#once that's done, we generate requirements using pipreqs
def create_reqs(foldername=None):
    if foldername:
        foldername=foldername
    else:
        foldername=os.getcwd()
    comms_list=[]
    x=subprocess.Popen(['pipreqs'],cwd=foldername)
    comms_list.append(x.communicate())

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