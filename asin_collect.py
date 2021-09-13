import sys, os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import configparser
import json

# 実行ファイルのディレクトリパスを取得
directory_path = os.path.dirname(os.path.abspath(sys.argv[0]))

# 引数があれば引数をディレクトリパスに設定
if len(sys.argv) > 1:
    directory_path = sys.argv[1]

# Chromedriver設定
options = Options()
# options.add_argument('--headless')
chromedriver_path = directory_path + os.sep +'chromedriver'

# OSがウィンドウズなら拡張子「.exe」を追加
if os.name == 'nt':
    chromedriver_path = chromedriver_path + '.exe'
driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=options)
time.sleep(2)

# キーワード（商品名）
goods_name = 'Echo Show 5 (エコーショー5) スマートディスプレイ with Alexa、チャコール'
# google検索URL
google_search_url = 'https://www.google.com/'

# 検索ページを開く
driver.get(google_search_url)
# 検索ボックス要素を取得
search_box = driver.find_element_by_name('q')
# 検索ボックスにキーワードを入力
search_box.send_keys(goods_name)
# エンターキー押下
search_box.send_keys(Keys.RETURN)

time.sleep(2)

# 検索結果の取得
element_g_list = driver.find_elements_by_class_name('g')
# for element_g in element_g_list:
#     print(element_g)

elem = element_g_list[0]
a_list = elem.find_elements_by_tag_name('a')

for elem_a in a_list:
    url = elem_a.get_attribute('href')
    if url.startswith('https://www.amazon.co.jp/'):
        print(os.path.basename(url))

#ブラウザを閉じる
driver.quit()