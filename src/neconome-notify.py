import requests
import time
import datetime
from bs4 import BeautifulSoup
from plyer import notification

import util

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
        req = requests.get(URL)

        if req.status_code != requests.codes.ok:
            print("ページが取得できませんでした。URLをご確認ください。")
            print(f"{str(req.status_code)}: {str(URL)}")
            break

        soup = BeautifulSoup(req.content, "html.parser")
        time_now = datetime.datetime.now()

        # 順番待ち情報が入っているspanを取得
        span_list = soup.find_all("span", class_="strong")

        if len(span_list) == 0:
            print(f"[{util.format_date(time_now)}現在]")
            print(f"順番待ち情報が取得できないか、まだ診察が始まっていません。{str(DURATION)}秒後に再試行します。\n")

            # ページの内容を一部表示
            content = soup.find("p", class_="more-contents")
            for line in content.get_text("\n").splitlines():
                print(f"> {line}")

            # 次のループまで待機
            time.sleep(DURATION)
        elif len(span_list) <= int(INDEX):
            print(f"INDEXが不正です。設定できるのは{str(len(span_list))}までですが、{str(INDEX)}が設定されました。")
            break

        span_text = util.to_hankaku(span_list[INDEX].text)
        current_num = util.extract_number(span_text)

        # 表示
        print(f"[{util.format_date(time_now)}現在]")
        print(f"あなたの番号:{waiting_num}番")
        print(f"現在の呼出番号:{current_num}番")
        print("")

        if current_num.isdigit():
            # 順番待ちの検証
            alert_num = int(waiting_num) - ALERT_NUMBER

            if int(waiting_num) < int(current_num):
                print("順番超過 終了します\n")
                notification.notify(
                    title="ネコの目通知",
                    message="順番が超過しました",
                    timeout=5,
                )
                break
            elif alert_num <= int(current_num):
                print(f"!!!! {str(ALERT_NUMBER)}番前になりました。移動を開始してください !!!!" + "\n")
                notification.notify(
                    title="ネコの目通知",
                    message=f"{str(ALERT_NUMBER)}番前になりました。移動を開始してください。",
                    timeout=5,
                )

        # 次のループまで待機
        time.sleep(DURATION)
    except KeyboardInterrupt:
        print("プログラムを終了します。")
        break
