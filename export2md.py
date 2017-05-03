# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 06:19:01 2017

@author: johri_m
"""

import os
import subprocess

def execute(cmd):
    """
        Purpose  : To execute a command and return exit status
        Argument : cmd - command to execute
        Return   : exit_code
    """  
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (result, error) = process.communicate()

    rc = process.wait() 

    if rc != 0:
        print ("Error: failed to execute command:", cmd)
        print (error )
    return result
# def

#command = "tasklist | grep python"
#print "This process detail: \n", execute(command)

htmlFiles = []
#pdfdir = r"D:\code\LetsExplorePython_pdf"
#os.chdir(pdfdir)
for d in os.walk(r"D:\code\LetsExplorePython"):
    for f in d[2]:
        if f.endswith(".ipynb") and not "-checkpoint" in f:
            print("Processing: ", f)
            file_name = os.path.join(d[0], f)
            execute( "jupyter nbconvert --to Markdown \"" + file_name + "\"")
            file_name_md = os.path.splitext(file_name)[0] + ".md"
#            execute("md2pdf \"{filename}\" --theme=github".format(filename=file_name_md))

for f in htmlFiles:
    print(os.path.f)
