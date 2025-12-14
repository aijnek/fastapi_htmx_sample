# FastAPI + HTMX + Ollama サンプル

Ollamaを使ったリアルタイムLLMテキスト生成のデモアプリケーション。

## 必要環境

- Python 3.13以上
- uv (パッケージ管理)
- Ollama (ローカル実行中)

## セットアップ

依存パッケージのインストール:
```bash
uv sync
```

## 実行方法

アプリケーションの起動:
```bash
uv run uvicorn main:app --reload
```

ブラウザで `http://localhost:8000` にアクセス

## 設定

[main.py](main.py) で以下を変更可能:
- `OLLAMA_URL`: Ollama APIのエンドポイント (デフォルト: http://localhost:11434/api/generate)
- `OLLAMA_MODEL`: 使用するモデル (デフォルト: gpt-oss:20b)

## 技術スタック

- **FastAPI**: バックエンドWebフレームワーク
- **HTMX**: フロントエンドの動的更新
- **Ollama**: ローカルLLMエンジン
- **Server-Sent Events**: ストリーミングレスポンス
