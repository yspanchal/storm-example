#!/usr/bin/python

import os
import commands

f = ["appgridlicense", ".com.google.Chrome.OCpZnm", "hsperfdata_tomcat7", "hsperfdata_yogesh", ".ICE-unix", "orbit-yogesh", "pulse-PKdhtXMmr18n", "ssh-NFomEpaIIpYT", "sublime-pylint.log", "tmpe3Ccmc", "unity_support_test.0", ".X0-lock", ".X11-unix", "remove.py"]

for i in os.listdir("."):
	if i not in f:
		cmd = "rm -rf " + i
		commands.getstatusoutput(cmd)
