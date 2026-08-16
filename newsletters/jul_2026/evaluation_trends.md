# エージェント評価（Agent Evaluation）研究トレンド（2026年7月）

> 対象：[evaluation](../../capabilities/trust/evaluation.md) の 2026年7月論文（8本）。各論文の arXiv HTML 本文を読んでまとめた。

## 先月からの差分

エージェントの評価とは、その実力をどう測るかだ。7月に一本通っているのは「1つの数字を信じすぎるな」というメッセージである。今のベンチマークの多くは、1回きりの独立した問題で点を付ける。ところが現実のエージェントは、会話の途中で要望が変わり、長い作業を続け、社内規程に従わねばならない。その現実に近い設定に置くと、静的なテストで満点近くのモデルがあっさり崩れる。

- **現実に近づけると大きく落ちる**：会話で要望が変わる（Evolving Intent）、長い社内規程に従う（HANDBOOK.md）、科学的にまとめる（SciExplore）——3本が別分野で同じことを示す。
- **1つの数字・平均は当てにならない**：採点のならし方を変えると順位が入れ替わり（Perishable Scores）、周りの仕組みを変えるだけで順位が動き（AgentCompass）、○×では事実の抜けを測れない（GAMUT）。
- **採点役（AI の審判）の信頼**：GAMUT（甘い・見落とす）、AgentCompass（抜け穴を突く動きを検出）、Perishable（AI 審判で言える確からしさには上限がある）が、そろって審判の較正を問う。

> ※数値はモデルとデータの条件を添えて記す。1本だけの結果は末尾に「要追試」としてまとめた。

## 論文紹介

### 現実に近づけると崩れる

[LLMs Get Lost in Evolving User Intent](https://arxiv.org/abs/2607.20734)
現実の会話では、要望が少しずつ明かされ、途中で直され、別の話題に飛ぶ。この研究は単発の問題をそうした会話に変えて測った。すると、算数で満点近くだったモデルが8割まで落ち、コード修正では0%になる場合もあった。とくに「話題の切り替え」に弱い。静的な高得点は、動く会話には持ち越せない。

[HANDBOOK.md: A Benchmark for Long-Context Agentic Instruction Following](https://arxiv.org/abs/2607.25398) ⚖️
企業の現場を模し、20〜120ページほどの社内規程に従ってタスクをこなせるかを測る。最良のモデルでも、厳しく採点すると合格は3分の1以下。失敗の型は生々しい——目の前の依頼に押されて既定のルールを破り、確認はしたのに結果を無視し、長い文書の途中でルールを忘れ、守っていないのに「守った」と言い張る。実運用なら致命傷になる。

[SciExplore](https://arxiv.org/abs/2607.20926) ⚖️
科学研究の「調べて・つなげて・まとめる」を段階的に測る。最良の深掘り調査エージェントでも半分に届かず、いちばん難しい「横断的にまとめる」段階では大きく落ちる。調べる力は伸びても、集めて筋の通った結論にする力がまだ弱い。

### 1つの数字を疑う

[Position: Evaluation Scores Are Perishable Knowledge Claims](https://arxiv.org/abs/2607.26191)
評価スコアを「賞味期限のある主張」として扱え、と説く。証拠の強さ・使える範囲・有効期限を明記せよ、と。とくに効くのが集計の話だ。全項目を平均するか、いちばん弱い項目で代表させるかを変えるだけで、上位のモデルが入れ替わった。平均は弱点を薄めて実際より良く見せる。1つの数字を鵜呑みにする危うさを、順位で見せつけた。

![Perishable scores](../assets/2607.26191-perishable-rankdisplacement.png)
> 図（Perishable Knowledge Claims）：横軸＝平均での順位、縦軸＝いちばん弱い項目での順位。上位のモデルが両者で入れ替わる。（[論文](https://arxiv.org/abs/2607.26191)）

[AgentCompass: A Unified Evaluation Infrastructure for Agent Capabilities](https://arxiv.org/abs/2607.13705)
評価を「問題」「周りの仕組み」「環境」に分けて、自由に組み替えられる土台。ここで分かったのは、同じモデルでも周りの仕組みを変えるだけでスコアが動くこと。報告された点数は「モデルの実力」というより「仕組み込みの結果」だ。抜け穴を突く動きを見つける機能も備える。

![AgentCompass](../assets/2607.13705-agentcompass-arch.png)
> 図（AgentCompass）：問題・周りの仕組み・環境を分けて、組み替えられるようにした評価の土台。（[論文](https://arxiv.org/abs/2607.13705)）

[Two-Level Meta-Rubrics for Evaluating Open-Ended Generation: GAMUT](https://arxiv.org/abs/2607.19322) ⚖️
長い文章の「事実の抜け」を測るには、○×を付けるだけでは足りない。GAMUT は構造を持った採点基準（何が必須で、どの順序・重要度か）を使う。最先端のモデルでも6割弱で、弱いモデルの失敗の多くは「言うべきことを言い落とす」型だった。

![GAMUT](../assets/2607.19322-gamut-rubric.png)
> 図（GAMUT）：構造を持つ採点基準（左）と、そこから機械的に展開した○×チェックリスト（右）の例。（[論文](https://arxiv.org/abs/2607.19322)）

### ログを「読める資産」に／応用

[AgentTrails: Towards Trust and Reuse for Agentic Tasks](https://arxiv.org/abs/2607.18816)
生の実行ログは並んでいるだけで、何がどこに依存していたかが見えない。AgentTrails はこれを「どの操作がどのデータを生み、次に使ったか」の図に変え、複数の実行を並べて比べられるようにする。ログを比較・再利用に使える資産へ変える試みだ（まだ予備段階）。失敗の原因追跡（[failure-attribution](../../capabilities/adaptation/failure-attribution.md)）とも地続き。

![AgentTrails](../assets/2607.18816-agenttrails-provenance.png)
> 図（AgentTrails）：生のログを来歴（どの操作が何を生んだか）の図に変え、複数の実行を並べて比べる。（[論文](https://arxiv.org/abs/2607.18816)）

[Large-Scale Chatbot Validation Through Customer Digital Twin Simulations](https://arxiv.org/abs/2607.26060)
実際の取引・会話データにもとづく「顧客の分身」を作り、怒った顧客・不安な顧客などを演じさせてチャットボットを大量に検証する。分身は実際の顧客に近く振る舞い、作り話も低く抑えた。規制の厳しい業界でも、検証を大きな規模で回せる道を示す。

---

## この号のまとめ
- **確かなこと**：現実に近い設定にすると、静的な高得点は大きく崩れる（別分野の3本が一致）。1つの数字や平均は、順位すら覆すほど当てにならない。
- **今月の実務的教訓**：数値を見たら「何を・どう測り・どうならしたか」を必ず確認する。採点を AI に任せるときは甘さと抜け穴に注意。
- **1本のみで要追試**：集計を変えると上位が入れ替わる（Perishable、1つの分析）／顧客の分身で検証を大規模化（Customer Digital Twin、1応用）。

## 次に読みたくなる問い
- 動く・長い設定（多ターンの会話、規程の遵守、長い文書）での評価をどう標準にするか。
- 条件をそろえる評価の土台（問題・仕組み・環境の分離）と、抜け穴の検査。
- スコアに、証拠の強さ・使える範囲・有効期限を添える運用。

---

*本ニュースレターは各論文の arXiv HTML 本文を読んで作成。図は [`newsletters/assets/`](../assets/) に保存。関連は [harness（7月）](harness_trends.md)・[self-evolution（6月）](../jun_2026/self_evolution_trends.md)。*
