# 対象ページ
https://www.postgresql.org/docs/release/13.XX/

# プロジェクトディレクトリに移動
cd postgres_scraper

# Dockerイメージをビルド
docker build -t postgres-scraper .

# Dockerコンテナを実行
docker run --rm -v $(pwd)/output:/app/output postgres-scraper
