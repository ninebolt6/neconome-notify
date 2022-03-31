import util

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
ALERT_NUMBER = 6

# 何秒おきに確認するか設定する
DURATION = 180

# 順番待ち情報を取得するURLを指定する
URL = "https://www.neconome.com/XXXXXXX"


# 整理券番号を入力
print("あなたの整理券番号を入力してください: ")
waiting_num = util.to_hankaku(input())

while 1:
  try:
    # 施設の混雑情報を取得
    html = requests.get(URL)
    soup = BeautifulSoup(html.content, "html.parser")

    # 順番待ち情報が入っているspanを取得
    span_list = soup.find_all("span", class_="strong")
    span_text = util.to_hankaku(span_list[INDEX].text)
    current_num = util.extract_number(span_text)

    # 表示
    time_now = datetime.datetime.now()
    print("[{0:%Y年%m月%d日 %H時%M分%S秒}現在]".format(time_now))
    print("あなたの番号:", waiting_num + "番")
    print("現在の呼出番号:", current_num + "番")
    print("")

    # 順番待ちの検証
    alert_num = str(int(waiting_num) - ALERT_NUMBER)

    if waiting_num < current_num :
      print("順番超過 終了します\n")
      notification.notify(
        title="ネコの目通知",
        message="順番が超過しました",
        timeout=5,
      )
      break
    elif alert_num <= current_num :
      print("!!!! " + str(ALERT_NUMBER) + "番前になりました。移動を開始してください !!!!" + "\n")
      notification.notify(
        title="ネコの目通知",
        message=str(ALERT_NUMBER) + "番前になりました。移動を開始してください。",
        timeout=5,
      )

    # 次のループまで待機
    time.sleep(DURATION)
  except KeyboardInterrupt:
    print("プログラムを終了します。")
    break