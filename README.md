# averaged_image

複数のJPEG画像を平均化して1枚の画像を生成するツールです。

## 前提条件

- Python 3.13以上がインストールされていること

## セットアップ

### 1. uvのインストール

```bash
pip install uv
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

## （参考）サンプル画像の生成

動作確認用に、赤・緑・青の単色JPEG画像（200x200px）を `images/` ディレクトリに生成できます。

```bash
uv run create_samples.py
```