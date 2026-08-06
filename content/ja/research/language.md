+++
identifier = 'research__languageh'
title = '言語処理'
type = 'docs'
icon = 'fa-solid fa-language'
parent = 'research'
weight = 22
hide_summary = true
+++

## **機械翻訳**
### 同時機械翻訳の遅延と精度の関係
{{< cardpane >}}
{{< card >}}
    {{< video src="/videos/2025/ogura.mp4" >}}
{{< /card >}}
{{< card header="**研究のポイント**" footer="2025年 人工知能学会全国大会" >}}
<ul>
<li>語順が似ている日本語と韓国語の間の高速な同時機械翻訳</li>
<li>データから同時翻訳において待つタイミングを自動学習するBS-SiMTを使用</li>
<li>語順が似ていても精度を保つためにはある程度待つ必要があることを確認</li>
<li>今後の課題: 高速化のための言い換え等訳出戦略の高度化</li>
</ul>
{{< /card >}}
{{< /cardpane >}}

### 読み情報を追加で与える日英機械翻訳
{{< cardpane >}}
{{< card >}}
    {{< video src="/videos/2025/yamada.mp4" >}}
{{< /card >}}
{{< card header="**研究のポイント**" footer="2025年 人工知能学会全国大会" >}}
<ul>
<li>万葉歌碑解説文を対象に大規模言語モデルを用いて機械翻訳</li>
<li>解説文中の人名・地名に頻出する難読語の読み情報を与え機械翻訳を改善</li>
<li>難読語を大規模言語モデルに抽出させ、人手で読み情報を付与</li>
<li>今後の課題: 難読語の読み情報資源の自動作成と拡張</li>
</ul>
{{< /card >}}
{{< /cardpane >}}

## **言語解析**
### 日本語固有表現抽出のためのデータ拡張
{{< cardpane >}}
{{< card >}}
    {{< video src="/videos/2025/okazaki.mp4" >}}
{{< /card >}}
{{< card header="**研究のポイント**" footer="2025年 人工知能学会全国大会" >}}
<ul>
<li>文章中のキーワードとなる固有表現（固有名詞や数量等）を見つける</li>
<li>固有表現を同種の別のものに言い換えたデータを自動作成し追加学習</li>
<li>大規模言語モデルを用いて効果的に言い換えデータを作成できる</li>
<li>今後の課題: 文体や文脈を踏まえたデータ拡張の高度化</li>
</ul>
{{< /card >}}
{{< /cardpane >}}

## **自然言語処理応用**
### メンタルヘルス不調者のSNS投稿分析
{{< cardpane >}}
{{< card >}}
    {{< video src="/videos/2025/takabatake.mp4" >}}
{{< /card >}}
{{< card header="**研究のポイント**" footer="2025年 人工知能学会全国大会" >}}
<ul>
<li>SNS投稿から精神的不調に関わることばの表現を抽出</li>
<li>大規模言語モデルを用い精神的不調を持つ人に特徴的と思われるキーワードを抽出</li>
<li>大規模なSNS投稿データからの抽出結果を分析</li>
<li>今後の課題: より長い表現の抽出と投稿全体の意味推定</li>
</ul>
<div align="right">※静岡大学 狩野芳伸先生との共同研究</div>
{{< /card >}}
{{< /cardpane >}}

### 文章の推敲提案
{{< cardpane >}}
{{< card >}}
    {{< video src="/videos/2025/sawada.mp4" >}}
{{< /card >}}
{{< card header="**研究のポイント**" footer="2025年 人工知能学会全国大会" >}}
<ul>
<li>大規模言語モデルを用いて人が書く文章の推敲を支援</li>
<li>日本語の学術論文の概要を対象に修正すべき点を大規模言語モデルが提案</li>
<li>3種類のプロンプトと100件弱の論文概要を用いて検証</li>
<li>今後の課題: 学術論文以外の文章を対象にした推敲</li>
</ul>
{{< /card >}}
{{< /cardpane >}}

