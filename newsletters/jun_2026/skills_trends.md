# スキル（Skills）研究トレンド（2026年6月）

> 対象：[skills](../../capabilities/action/skills.md) の 2026年6月論文（7本）。各論文の arXiv HTML 本文を読んでまとめた。

## 先月からの差分

ここでいう「スキル」とは、エージェントが繰り返し使える手順のまとまりのことだ。ツールを一回きり呼ぶよりも一段上で、「こういう場面では、こう調べて、こう組み立てる」という、再利用できるやり方を指す。書き足せて、他のモデルにも渡せるのが利点だ。

先月まではスキルを「作って使う」段階が中心だった。6月の差分は、その前後——**どこから作るか（獲得）／別のモデルでも使えるか（転移）／正解なしで良し悪しをどう測るか（検証）**——が、それぞれ具体的な手法として立ち上がったことにある。

- **作る材料が多様になった**：過去の失敗の記録から（SkillAdaptor）、Web 上の文書やコードから（OpenSkill）、研究者の実験ノートから（Notes2Skills）、複数モデルの合議から（OpenClaw-Skill）。
- **別のモデルでも使えることを狙う**：OpenSkill は弱いモデルにも効き、OpenClaw-Skill は「他のモデルでも通じるか」を選ぶ基準に入れ、SkillComposer は本番でも崩れにくいと示す。
- **正解を見ずに良し悪しを測る**：OpenSkill は自前のテストを、Notes2Skills は確からしさの保存を、SkillAdaptor は「もう一度実行して良くなったか確かめる」関門を用意した。

> ※数値はモデルとデータの条件を添えて記す。1本だけの結果は末尾に「要追試」としてまとめた。

## 論文紹介

### スキルをどこから作るか

[SkillAdaptor: Self-Adapting Skills for LLM Agents from Trajectories](https://arxiv.org/abs/2606.01311)
失敗したとき、やみくもに全部やり直すより「どのスキルが原因か」を突き止めて、そこだけ直すほうが速い。SkillAdaptor は失敗の記録から原因のスキルを特定し、直すか新しく作るかを選び、もう一度実行して良くなったときだけ採用する。モデルは訓練しない。地味だが「訓練なしで直せる」点が実務的で、失敗の原因特定（[failure-attribution](../../capabilities/adaptation/failure-attribution.md)）の流れとも重なる。

[OpenSkill: Open-World Self-Evolution for LLM Agents](https://arxiv.org/abs/2606.06741)
本番で困るのは、正解が手元にないことだ。OpenSkill は Web 上の文書やコードから知識を集めてスキルを作り、さらに「正解を見ずに使える自前のテスト」を用意して磨く。正解を教わらないのに成績が上がり、別のモデルにも効いた。ただし Web の情報が古いと質が落ちる、と限界も述べる。

![OpenSkill](../assets/2606.06741-openskill-framework.png)
> 図（OpenSkill）：Web から知識を集めてスキルを作り、正解を見ずに使える自前のテストで磨く。本番の正解は最後まで使わない。（[論文](https://arxiv.org/abs/2606.06741)）

[Notes2Skills: From Lab Notebooks to Certainty-Aware Scientific Agent Skills](https://arxiv.org/abs/2606.11897)
科学の現場では、ノートの「たぶんこうだ」を「確定でこうだ」と取り違えると危ない。Notes2Skills は実験ノートの記述を「事実／判断／提案」に分け、確からしさを保ったままスキルに変換する。曖昧なメモが確定の行動に化けるのを防いだ。ナノポア計測という特定分野での検証で、他分野への一般化はこれから。

[OpenClaw-Skill: Collective Skill Tree Search for Agentic LLMs](https://arxiv.org/abs/2606.16774)
1つのモデルだけでスキルを作ると、そのモデルの癖が出る。複数のモデルに同じ課題を解かせ、出てきた多様なやり方からスキルを合議で選ぶ。しかも「他のモデルでも通じるか」を選ぶ基準に入れる。単一モデル製より偏りが少なく、他のモデルへも渡りやすいスキルになる。

![OpenClaw-Skill](../assets/2606.16774-openclawskill-overview.png)
> 図（OpenClaw-Skill）：課題を小さな課題に分け、複数モデルの合議でスキルを積み上げていく。（[論文](https://arxiv.org/abs/2606.16774)）

### 小さく・安く・崩れにくく選ぶ

[Generative Skill Composition for LLM Agents（SkillComposer）](https://arxiv.org/abs/2606.32025)
スキルが増えると、今度は「どれを・どの順で使うか」の選択が難しくなる。SkillComposer はこれを、ごく小さな専用のモデル（400万パラメータ弱）に任せる。巨大なモデルを訓練し直すやり方に比べ、本番タスクでの崩れが小さく、学習の費用は桁違いに安い。「大きいほど良い」とは限らない好例だ。長い手順のときに少なめに選びがちなのが伸びしろ。

![SkillComposer](../assets/2606.32025-skillcomposer-overview.png)
> 図（SkillComposer）：課題とスキル一覧を読み、どのスキルをどの順で使うかを小さな専用モデルで予測する。（[論文](https://arxiv.org/abs/2606.32025)）

### 応用：データ分析での自己進化

[EvoDS: Self-Evolving Autonomous Data Science Agent](https://arxiv.org/abs/2606.03841)
データ分析を役割分担（掃除・特徴量・モデル化・可視化）で進め、使えるスキルを自分で貯めて再利用し、長くなりすぎたコンテキストは賢く縮める。覚えたスキルの7割ほどを使い回し、長い処理で「コンテキストが溢れて途中で落ちる」事故をなくした。専門知識が要る科学タスクでは、まだ差が残る。

![EvoDS](../assets/2606.03841-evods-framework.png)
> 図（EvoDS）：役割分担のエージェントに、自分でスキルを貯める仕組みと、コンテキストを賢く縮める仕組みを組み合わせる。（[論文](https://arxiv.org/abs/2606.03841)）

---

## この号のまとめ
- **確かなこと**：スキルを作る材料が多様になり（過去の記録・Web・ノート・合議）、モデルを訓練せず・別のモデルにも効く方向が広がった。
- **今月の共通の難所**：正解を見ずに良し悪しを測ること。自前のテストや確からしさの保存で各論文が挑んでいる。
- **1本のみで要追試**：ごく小さな専用モデルが、巨大なモデルの学習より崩れにくくスキルを選ぶ（SkillComposer）／覚えたスキルを7割再利用し途中脱落をなくした（EvoDS）。

## 次に読みたくなる問い
- 正解を見ずに測る検証の精度をどこまで上げられるか（→ [verification](../../capabilities/adaptation/verification.md)）。
- 作ったスキルの、別のモデルへの移りやすさをどう保証するか。
- 長い手順のスキルの組み合わせをどう扱うか（SkillComposer の弱点）。

---

*本ニュースレターは各論文の arXiv HTML 本文を読んで作成。図は [`newsletters/assets/`](../assets/) に保存。関連は [self-evolution（6月）](self_evolution_trends.md)・[tool-use](../../capabilities/action/tool-use.md)。*
