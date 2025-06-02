
---

## 必要環境

- Linux（Ubuntu などの一般的なディストリビューションを想定）  
- Python 3.x  
- pip（Python パッケージ管理ツール）  

---

## 依存ライブラリのインストール

今回のスクリプトでは、外部ライブラリは使用せず標準ライブラリのみで実装しています。必要な場合は別途追加してください。

```bash
# リポジトリをクローン
git clone https://github.com/hiroki077/discover_ip.git
cd <YourRepo>

# 必要があれば仮想環境を作成して有効化
python3 -m venv venv
source venv/bin/activate

# （現状、requirements.txt は不要ですが、将来的にライブラリを追加する場合はここを利用）
pip install -r requirements.txt


#run on the terminal
crontab -e
# 毎日午前5時に Pico 検出スクリプトを実行（ブラウザタブは一度すべて閉じてから開く）
0 5 * * * /usr/bin/python3 /full/path/to/discover_ip.py >> /full/path/to/discover_ip.log 2>&1