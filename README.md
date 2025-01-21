## 実行手順
### 1. htmlファイルをinputフォルダへ保存
対象ページ：https://www.postgresql.org/docs/release/XX.XX/

### 2. プロジェクトディレクトリに移動
```
cd postgres_scraper
```

### 3. Dockerイメージをビルド
```
docker build -t postgres-scraper .
```

### 4. Dockerコンテナを実行
```
docker run --rm -v $(pwd)/output:/app/output postgres-scraper
```
