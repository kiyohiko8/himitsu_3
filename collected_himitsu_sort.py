import os, csv
import random
import himitsu_data_gd_3
import pandas as pd
import numpy as np




#csvを読み込んでデータ作成	
def read_csv(csv_data):
	collected = []
	# ファイルを読み込みモードでオープン
	with open(csv_data, 'r', encoding = "shift-jis") as f:
		# 行ごとのリストを処理する
		for row in f:
			row = row.rstrip()
			row = row.replace('\"', '')
			row = row.replace(' ', '')
			row = row.replace('インスタントミニュチュア製造カメラ', 'インスタントミニチュア製造カメラ')
			row = row.replace('かならず実現するメモ帳', 'かならず実現する予定メモ帳')
			row = row.replace('穴掘り機', '穴ほり機')
			row = row.replace('重量ペンキ', '重力ペンキ')
			line = row.split(",")
			collected.append(line)
			
			
	return collected


#カウントをする
def count_sort(collected, words):
	cntlist = []
	for word in words:
		cnt = 0
		for collection in collected:
			if word in collection:
				cnt += 1
		index = [cnt, word]
		cntlist.append(index)
	
	cntlist.sort()
		
		
	return cntlist
		
if __name__ == "__main__":


	
	himitsu  = himitsu_data_gd.mk_allword_list()
	collected =read_csv("himitsu_data.csv")
	cntlist = count_sort(collected, himitsu)
	for item in cntlist:
		print(item)
		
		
























