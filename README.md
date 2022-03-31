# neconome-notify

[ネコの目](https://www.neconome.com/)の順番待ち情報を一定時間おきに取得し、順番が近づいたときにデスクトップ通知をしてくれるCUIアプリケーションです。

### ファイル構成
neconome-notify.py - メインスクリプト

### 動作要件
Python 3.10.2で動作を確認。

使用ライブラリ

- [beautifulsoup4 4.10.0](https://pypi.org/project/beautifulsoup4/)
- [plyer 2.0.0](https://pypi.org/project/plyer/)
- [requests 2.27.1](https://pypi.org/project/requests/)

### スクリプト詳細
実行の流れは以下の通りです。

- 自分の整理券番号を入力する(int)
- 指定されたURLのHTMLを取得し、呼び出し中の情報が書かれたspanを取り出す。
- 入力された整理券番号と比較し、順番が近づいたらデスクトップ通知を鳴らす。
- 順番が超過した場合、終了する。

#### 設定項目
INDEX: HTMLに含まれる何番目のspanを順番待ち情報として取得するか設定する。(int)

ALERT_NUM: 何番前になったらデスクトップ通知を鳴らすか設定する。(int)

DURATION: 何秒おきに順番を確認するか設定する。(float)

URL: どの施設の順番待ち情報を取得するか設定する。(string)

### 注意事項
施設によってページに表示される文言が違うため、そのままでは使えない場合があります。適宜改変してください。
