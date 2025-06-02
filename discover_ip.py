import socket
import webbrowser
import subprocess
import time

BROADCAST_PORT = 10000
DISCOVERY_MSG   = b'DISCOVER_PICO'
TIMEOUT         = 2.0  # 秒

def close_all_browsers():
    """
    主要なブラウザプロセスをすべて終了させる。
    - Ubuntu などの Linux 環境で一般的なプロセス名を指定
    """
    # ブラウザ候補をリスト化（必要に応じて追加してください）
    browsers = ['firefox', 'chrome', 'chromium', 'brave', 'opera']
    for name in browsers:
        # pkill コマンドで該当プロセスを強制終了
        subprocess.call(['pkill', '-f', name])

def discover_and_open():
    # UDP ブロードキャスト用ソケットを作成
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.settimeout(TIMEOUT)

    try:
        # ブロードキャスト送信
        sock.sendto(DISCOVERY_MSG, ('255.255.255.255', BROADCAST_PORT))

        # 応答を待つ
        while True:
            try:
                data, addr = sock.recvfrom(1024)
            except socket.timeout:
                print("⚠️ Discovery timeout: Pico が見つかりませんでした")
                return

            if data.startswith(b'PICO_IP:'):
                ip = data.split(b':', 1)[1].decode()
                url = f"http://{ip}"
                print(f"▶ Found Pico at {url}")

                # 既存のブラウザタブをすべて閉じる
                print("→ 既存のブラウザをすべて終了します．．．")
                close_all_browsers()
                time.sleep(0.5)  # 終了が完了するまで少し待機

                # 新たにブラウザで URL を開く
                print("→ ブラウザで開きます．．．")
                webbrowser.open(url)
                return

    finally:
        sock.close()

if __name__ == "__main__":
    # cron などで起動するときに安定化
    time.sleep(1)
    discover_and_open()
