# nara-wu-slc.jp

奈良女子大学 音声・言語・コミュニケーション研究室のHugoサイトです。

## 必要な環境

- Hugo Extended 0.164.0
- Go 1.26.x
- Node.js 24.x
- npm

## 初回セットアップ

```sh
hugo mod get
hugo mod npm pack
npm install
```

`go.mod`、`go.sum`、`package.json`、`package-lock.json`はリポジトリへコミットします。

## ローカルプレビュー

```sh
npm ci
hugo server
```

日本語サイトは <http://localhost:1313/ja/>、英語サイトは
<http://localhost:1313/en/> で確認できます。

## 本番ビルド

```sh
hugo --gc --minify
```

生成される `public/` はコミットしません。デフォルトブランチへのpush時に
GitHub Actionsがビルドし、GitHub Pagesへデプロイします。

## Docsyの更新

DocsyはHugo Moduleとしてバージョンを固定しています。更新は専用ブランチで行います。

```sh
hugo mod get github.com/google/docsy/theme@vX.Y.Z
hugo mod tidy
hugo mod npm pack
npm install
hugo --gc --minify
```

更新後は `/ja/` と `/en/`、ナビゲーション、研究紹介の動画、業績一覧を確認してください。

## 業績一覧の更新

`scripts/achievements.py` はresearchmapのJSONLから業績一覧の分類別ページを生成します。
入力JSONLは `.local/` に置き、必要に応じて次を実行します。

```sh
python3 scripts/achievements.py
```


生成された `content/*/research/publications/*.md` はコミットします。各ページの年見出しは
Docsyの右側の目次に自動的に表示されます。

## 研究紹介動画

`video` ショートコードでは、スクリーンリーダー向けの `label` を指定できます。
字幕ファイルを用意した場合は、`track`、`tracklang`、`tracklabel` でWebVTT字幕を追加できます。

```go-html-template
{{</* video src="/videos/example.mp4" label="研究紹介動画" track="/captions/example-ja.vtt" tracklang="ja" tracklabel="日本語" */>}}
```
