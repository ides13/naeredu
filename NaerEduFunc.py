# -*- coding: utf-8 -*-
"""
Created on Thu May 31 12:23:54 2018

@author: ides13
"""
import urllib.parse
#import urllib
import pandas as pd
import sys
import webbrowser


def naeredu():
    rooturl='http://terms.naer.edu.tw/search/?q={}&field=ti&op=AND&match=&group=&num=30'
    url = ''
    
    while True:
        word = input("在【學術名詞】查詢：")
        if word=="q":
#            sys.exit()
            break
        elif word =="openurl":
            webbrowser.open(url) 
        else:
            word = urllib.parse.quote(word, safe='') 
    		#如上，中文網址需要編碼，例如try and error的英文“詞”也需要。
            url = rooturl.format(word)
            #print (url)
            try:
                myhtml = pd.read_html(url)
        #        print ("1111111111111")
                table = myhtml[0]
                table = table.drop(['INFO', '全選'], axis=1)
                print (table)
        
                print('\n')
            except (IndexError, ValueError):
                print("在學術名詞網中，找不到這個詞，請重新輸入")
    return 
 
if __name__ == "__main__":
    naeredu()                
