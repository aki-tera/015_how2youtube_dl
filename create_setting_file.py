import socket
import os
import json


def get_current_ip():
    # 先ずはいまのホスト名を取得する
    host = socket.gethostname()
    # ipアドレスを取得
    ip = socket.gethostbyname(host)

    return ip


def create_rss_file(ip):
    # podcastフォルダ作成
    os.makedirs("cgi-bin/podcast", exist_ok=True)

    html_body = ('<?xml version="1.0" encoding="utf-8"?>\n'
                 '<rss xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" version="2.0">\n'
                 '  <channel>\n'
                 '    <title>My Podcast</title>\n'
                 '    <itunes:owner/>\n' +
                 f'    <itunes:image href="http://{ip}/art-work/001.png"/>\n' +
                 '    <itunes:category text="video"/>\n'
                 '  </channel>\n'
                 '</rss>\n')

    # rssファイルの作成
    with open("cgi-bin/podcast/podcast.rss", mode="w", encoding="utf-8")as f:
        f.write(html_body)


def create_json_file(dict):
    # 設定ファイルを作る
    with open("cgi-bin/setting_file.json", mode="w", encoding="utf-8")as f:
        json.dump(dict, f)


def main():
    # まずはIPアドレスを取得する
    current_ip = get_current_ip()

    # 現在のipアドレスを表示する
    print(f"The ip address of this computer is {current_ip}")

    # rssファイルを作成する
    create_rss_file(current_ip)
    print("create podcast.rss")

    # youtube_dlのダウンロードフォルダ設定
    podcast_path = os.getcwd().replace("\\", "/") + "/cgi-bin/podcast/"

    # rss用ダウンロードリンク
    podcast_link = f"http://{current_ip}/podcast/"

    # 設定用のjsonファイルを作る
    setting_value = {"podcast_path": podcast_path, "podcast_link": podcast_link}
    create_json_file(setting_value)
    print("create setting_file.json")


if __name__ == "__main__":
    main()
