import socket
import os
import json
import pyperclip


def get_current_ip():
    # 先ずはいまのホスト名を取得する
    host = socket.gethostname()
    # ipアドレスを取得
    ip = socket.gethostbyname(host)

    return ip


def create_rss_file(ip):
    folder_path = "cgi-bin/podcast"
    file_path = folder_path + "/podcast.rss"
    # podcastフォルダ作成
    os.makedirs(folder_path, exist_ok=True)

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
    if not os.path.isfile(file_path):
        with open(file_path, mode="w", encoding="utf-8")as f:
            f.write(html_body)
    else:
        print("Don't create podcast.rss, because it already exists.")


def create_json_file(dict):
    # 設定ファイルを作る
    with open("cgi-bin/setting_file.json", mode="w", encoding="utf-8")as f:
        json.dump(dict, f)


def create_user_name_file():
    # ファイルのパス
    file_path = "cgi-bin/user_name.txt"
    # ファイルの内容
    file_body = ("#You can switch login name and password for each video services.\n"
                 "#Enter the login name and password for each services according to the following:\n"
                 "#www.example1.com:username1:password1\n"
                 "#www.example2.com:username2:password2\n")

    # ファイル作成
    if not os.path.isfile(file_path):
        with open(file_path, mode="w", encoding="utf-8")as f:
            f.write(file_body)
    else:
        print("Don't create user_name.txt, because it already exists.")


def main():
    # まずはIPアドレスを取得する
    current_ip = get_current_ip()

    # rss用ダウンロードリンク
    podcast_link = f"http://{current_ip}/podcast/"

    # 登録するURLを表示する
    podcast_file_path = podcast_link + "podcast.rss"

    # 登録するURLの表示ー
    print("Your URL of podcast is")
    print(f"{podcast_file_path}\n")

    # rssファイルを作成する
    create_rss_file(current_ip)

    # youtube_dlのダウンロードフォルダ設定
    podcast_path = os.getcwd().replace("\\", "/") + "/cgi-bin/podcast/"

    # 設定用のjsonファイルを作る
    setting_value = {"podcast_path": podcast_path, "podcast_link": podcast_link}
    create_json_file(setting_value)

    # user_name.txtを作成する
    create_user_name_file()

    # キー入力待ち
    while True:
        temp = input("Press the `Enter` key to exit.")
        if not temp:
            # 登録するURLをクリップボードへコピー
            pyperclip.copy(podcast_file_path)
            break


if __name__ == "__main__":
    main()
