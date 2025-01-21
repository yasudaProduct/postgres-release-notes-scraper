import requests
from bs4 import BeautifulSoup
import os

input_folder = "input"
output_folder = "output"

# URL
# url = "https://www.postgresql.org/docs/release/13.14/"

def fetch_changes(input_file):
    try:
        # response = requests.get(url)
        # response.raise_for_status()
        
        # soup = BeautifulSoup(response.content, "html.parser")

        # 入力HTMLファイルを読み込む
        with open(input_file, "r", encoding="utf-8") as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, "html.parser")
        
        # 変更点のセクションを取得
        ul = soup.find("ul", class_="itemizedlist")

        # 結果を格納するリスト
        output_lines = []
        
        if ul:
            li_items = ul.find_all("li", class_="listitem")
            for li in li_items:
                text = li.get_text()
    
                formatted_text = f"\"{text}\""
    
                # リストに追加
                output_lines.append(formatted_text)
        else:
            output_lines.append("該当するulタグが見つかりませんでした。")

        return output_lines
    except Exception as e:
        print(f"エラーが発生しました: {e}")

def save_changes(changes, output_file):
    # ディレクトリが存在しない場合は作成
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as file:
        file.write("\n".join(changes))
    print(f"変更点を {output_file} に保存しました。")

def process_html_files():
    # 入力フォルダ内のすべてのHTMLファイルに対して処理を行う
    for input_file in os.listdir(input_folder):
        # HTMLファイルのみを対象
        if input_file.endswith(".html"):
            input_file_path = os.path.join(input_folder, input_file)
            
            print(f"{input_file} を処理中...")
            
            # 変更点を取得
            changes = fetch_changes(input_file_path)
            
            if changes:
                # 出力ファイルのパスを設定（ファイル名に _output を付ける）
                output_file_path = os.path.join(output_folder, f"{os.path.splitext(input_file)[0]}_output.txt")
                save_changes(changes, output_file_path)
            else:
                print(f"{input_file} の変更点の取得に失敗しました。")

if __name__ == "__main__":
    print("変更点を取得中...")
    process_html_files()