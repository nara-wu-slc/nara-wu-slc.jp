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

## お知らせの追加・編集

お知らせはHugoのコンテンツとして1件ずつ管理し、記事ページにはDocsyのブログ用テンプレートを使用します。

- 日本語の記事: `content/ja/news/`
- 英語の記事: `content/en/news/`

既存の記事を編集する場合は、そのMarkdownファイルだけを変更します。新しい記事は、リポジトリのルートで次のように作成できます。

```sh
hugo new content --kind news content/ja/news/2026-10-13-example.md
hugo new content --kind news content/en/news/2026-10-13-example.md
```

生成されたファイルの `title`、`date` と本文を編集してください。日付はお知らせの掲載日とし、発表予定を案内する場合は開催日を本文に書き、公表済みの開催案内やプログラムへのリンクを添えます。日本語・英語の記事を同じファイル名にすると、記事ページの言語選択で相互に移動できます。

新規記事は `draft = true` の下書きとして作成されます。下書きは `hugo server -D` で確認でき、公開する際は `draft = false` に変更します。通常のビルドでは、下書きと掲載日が未来の記事は表示されません。`toc_hide = true` は個別記事をサイドバーに列挙しないための設定です。

トップページは `latest-news` ショートコードから掲載日の新しい順に日付・タイトルのリンクを自動表示します。記事を追加してもトップページのMarkdownを編集する必要はありません。表示件数は `hugo.toml` の `[params] news_limit = 5` で設定でき、10件にしたい場合は `10` に変更します。

過去のお知らせは `/ja/news/` と `/en/news/` の一覧から閲覧できます。

## 研究紹介の論文リンク

研究紹介の `card` ショートコードでは、`footer` にMarkdownのリンクを指定できます。DOIが確認できた論文は `https://doi.org/…` を使い、DOIが確認できないものは出版社・学会の書誌ページへリンクします。PDFへの直接リンクよりも、論文情報を確認できるページを優先してください。

## メンバーの個人Webページ

`member` ショートコードに `website` を指定すると、名前の下に個人Webページへのリンクが表示されます。教員・学生ともに同じ形式で使用できます。指定しない場合はリンクを表示しません。

```go-html-template
{{</* member name="氏名" role="博士前期課程1年" website="https://example.com/" */>}}
```

リンクの表示名は日本語ページでは「個人Webページ」、英語ページでは「Personal website」になります。日英それぞれの `members.md` にURLを指定してください。

## 研究紹介動画

`video` ショートコードでは、スクリーンリーダー向けの `label` を指定できます。
字幕ファイルを用意した場合は、`track`、`tracklang`、`tracklabel` でWebVTT字幕を追加できます。

```go-html-template
{{</* video src="/videos/example.mp4" label="研究紹介動画" track="/captions/example-ja.vtt" tracklang="ja" tracklabel="日本語" */>}}
```
