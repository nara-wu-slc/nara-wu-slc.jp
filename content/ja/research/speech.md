+++
identifier = 'research__speech'
title = '音声処理'
type = 'docs'
icon = 'fa-solid fa-microphone-lines'
parent = 'research'
weight = 21
hide_summary = true
+++

## **音声認識**
### 音声認識時の書き言葉への整形
{{< cardpane >}}
{{< card >}}
    {{< video src="/videos/2025/matsufuji.mp4" >}}
{{< /card >}}
{{< card header="**研究のポイント**" footer="2025年 人工知能学会全国大会, 音学シンポジウム" >}}
<ul>
<li>フィラー（「あの」「えー」等の表現）を音声認識時に自動的に除去</li>
<li>大規模音声認識モデルOWSMを追加学習（ファインチューニング）</li>
<li>フィラーを出力しないように追加学習することでフィラー除去を実現</li>
<li>今後の課題: フィラー以外も対象にした広範な文字起こしの整形</li>
</ul>
<div align="right">(2025年 人工知能学会全国大会, 音学シンポジウム)</div>
{{< /card >}}
{{< /cardpane >}}

## **音声合成**
### 音楽的制約による音声合成制御
{{< cardpane >}}
{{< card >}}
    {{< video src="/videos/2025/sato.mp4" >}}
{{< /card >}}
{{< card header="**研究のポイント**" footer="2025年 人工知能学会全国大会, 音学シンポジウム" >}}
<ul>
<li>テキスト音声合成の際に部分的に音の高さをコントロール</li>
<li>入力テキストに音の高さを指定する記号を追加</li>
<li>日本語の歌声コーパス (PJS) を利用して記号と音の高さの関係を学習</li>
<li>今後の課題: より広い音高の制御、音高以外の音楽的制約の付与</li>
</ul>
{{< /card >}}
{{< /cardpane >}}
