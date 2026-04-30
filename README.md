# averaged_image

複数のJPEG画像を平均化して1枚の画像を生成するツールです。

## セットアップ

### 1. uvのインストール

**Mac**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows（PowerShell）**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. 依存パッケージのインストール

プロジェクトディレクトリで以下を実行します。

```bash
uv sync
```

## 使い方

### 基本的な使い方

`images/` ディレクトリ内のJPEG画像を平均化し、`averaged.jpg` として保存します。

```bash
uv run average_images.py
```

## 注意事項

- 対応フォーマット: `.jpg` / `.jpeg`
- すべての画像は同じサイズである必要があります。サイズが異なる画像はスキップされます。
