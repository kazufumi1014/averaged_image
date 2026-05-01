# averaged_image

複数のJPEG画像を合成して1枚の画像を生成するツールです。合成方法は引数で切り替えられます。

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

```
uv run mixed_images.py [--mode {average,darkest}] [--input DIR] [--output FILE]
```

### 引数

| 引数 | デフォルト | 説明 |
|------|-----------|------|
| `--mode` | `average` | 合成方法。`average`（平均化）または `darkest`（最も暗いピクセルを採用） |
| `--input` | `images` | 入力画像が格納されたディレクトリ |
| `--output` | モードに依存 | 出力ファイルパス。省略時は `averaged.jpg` または `darkest.jpg` |

### 使用例

**平均化**（各ピクセルのRGB値を全画像で平均する）

```bash
uv run mixed_images.py --mode average
```

**最暗値合成**（各ピクセル・チャンネルごとに最も暗い値を採用する）

```bash
uv run mixed_images.py --mode darkest
```

**入力ディレクトリと出力ファイルを指定する**

```bash
uv run mixed_images.py --mode darkest --input photos --output result.jpg
```

## 注意事項

- 対応フォーマット: `.jpg` / `.jpeg`
- すべての画像は同じサイズである必要があります。サイズが異なる画像はスキップされます。

## （参考）サンプル画像の生成

動作確認用に、赤・緑・青の単色JPEG画像（200x200px）を `images/` ディレクトリに生成できます。

```bash
uv run create_samples.py
```