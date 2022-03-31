import requests
import time
import datetime
from bs4 import BeautifulSoup
from plyer import notification

# 何番目のspanを取得するか指定する。
# 施設によって文言が違うため、適宜調整する。
# zero-based index
INDEX = 1

# 何番前になったら通知するか設定する
ALERT_NUM = 6

# 何秒おきに確認するか設定する
DURATION = 180
# 順番待ち情報を取得するURLを指定する
URL = "https://www.neconome.com/XXXXXXXXXXXXXXX"


# 整理券番号を入力
print("あなたの整理券番号を入力してください")
target = int(input())

while 1:
  # 施設の混雑情報を取得
  html = requests.get(URL)
  soup = BeautifulSoup(html.content, "html.parser")

  # 順番待ち情報が入っているspanを取得
  span_list = soup.find_all("span", class_="strong")
  
  current = span_list[INDEX].text

  # 表示
  now = datetime.datetime.now()
  print("[{0:%Y年%m月%d日 %H時%M分%S秒}現在]".format(now))
  print("あなたの番号:", str(target) + "番")
  print("現在の呼出番号:", current)
  print("")


  label = str(target) + "番"
  alert_label = str(target - ALERT_NUM) + "番"
  alert_msg = "!!!! " + str(ALERT_NUM) + "番前になりました。移動を開始してください !!!!"

  if label < current:
    print("順番超過 終了します\n")
    notification.notify(
      title="ネコの目通知",
      message="順番が超過しました",
      timeout=5,
    )
    break
  elif alert_label <= current :
    print(alert_msg + "\n")
    notification.notify(
      title="ネコの目通知",
      message=str(ALERT_NUM) + "番前になりました。移動を開始してください。",
      timeout=5,
    )

  # 次のループまで待機
  time.sleep(DURATION)