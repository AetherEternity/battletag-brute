#!/usr/bin/env python3
# coding: utf-8
# AetherEternity, Jul 2017
# https://github.com/AetherEternity/battletag-brute
# GPLv3
 
# Enable dialogue mode
switch=1
if (switch):
	print('Enter nickname:')
	targetName=input()
	print('')
	print('Enter region:')
	print('1=US, 2=EU, 3=KR, 5=CN')
	targetRegion=input()
	print('')
	print('Stop on success? (1/0)')
	allvars=int(input())
	print('')
else:
	# Nickame (String before #)
	targetName='Kripp'
	# Region (1=US, 2=EU, 3=KR, 5=CN)
	targetRegion=2
	# Try all variants?
	allvars=0
success=0

import requests 
for val in range(10000):
	r = requests.get('https://api.hotslogs.com/Public/Players/'+str(targetRegion)+'/'+targetName+'_'+str(targetRegion)+str(val))
	if r.text!='null':
		print('Found: '+targetName+'#')+str(targetRegion)+str(val)
		success=1
		if allvars:
			exit()
if success==0:
	print('Failed')
