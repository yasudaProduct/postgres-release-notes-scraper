FROM python:3.10-slim

# 作業ディレクトリ
WORKDIR /app

# 必要なライブラリをインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p output
RUN mkdir -p input

COPY scraper.py .
COPY input/ input/


# 実行コマンド
CMD ["python", "scraper.py"]
