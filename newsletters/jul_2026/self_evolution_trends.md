# Self-Evolving Agents 研究トレンド（2026年7月）

> 7月に活発だった能力カテゴリ（[self-evolution](../../capabilities/adaptation/self-evolution.md), 7本）。各論文の **arXiv HTML 本文**を精読し、framework 図も引用した。6月が「進化をどう評価・防御するか」だったのに続き、7月は **(a) 何を永続させるか＝外在化（重み θ ではなく Σ・知識）**、**(b) 自己進化を支えるシステム基質**、そして **(c) 改善ループの"信頼性"（confidence cliff / discovery-reliability gap）** が焦点になった。

## 3行サマリ
- **「エージェントを複雑化」から「知識を外在化」へ**：Knowledge-Centric は**エージェントを使い捨てにし、共有知識ベースを永続の改善対象**にして、ARC-AGI-1 で **86.7%（HyperAgents 70%）をコスト約1/3**で達成、未知タスクへ 13.3→43.3% 転移。サーベイも自己改善を **θ（重み）更新 vs Σ（足場）更新**へ整理。
- **ボトルネックはアルゴリズムより"システム基質"**：Next-Gen Agentic RL は、実運用の経験を**統治可能・信用割当可能な学習素材**へ変換する ATDP＋制御プレーンを提唱し、「最大の障壁は強い LLM や RL ではなく system substrate」と主張。
- **自己改善ループは"信頼できない"**：Rehearse は最適化が進むほど judge が**自信過剰かつ不正確**になる confidence cliff を示し（selective acc 82.8→56.9 を 83.5 に回復）、RSIBench-Data は「**改善を発見しても 78% はピーク未満で終える**」discovery-reliability gap を定量化。

## なぜ注目か
Self-Evolution は「重みを更新せずに改善するループ」だが、7月は**何を永続資産にするか**の答えが **Σ・知識の外在化**へ収斂し、同時に**そのループ自体の信頼性・インフラ**が主要課題として立ち上がった。[evaluation 号](evaluation_trends.md)・[harness 号](harness_trends.md) と合わせ、「改善ループを厳密に測り・統治する」流れの中核をなす。

## 数字で見るインパクト（各論文の HTML 本文より）

| 論文 | 主な結果 |
|---|---|
| **Knowledge-Centric Self-Improvement** | ARC-AGI-1 **86.7%**（vs 70%）を**コスト約1/3**／未知タスク転移 13.3→**43.3%** |
| **Evidence-in-the-Loop** | 本番精度 **89.52%**（legacy RAG 79.00%）／reranker Hit@1 56.76→**75.68%** |
| **AREX** | BrowseComp 82.5%・GAIA 85.4%・DeepSearchQA 89.9%／ACU +11.8・outer +11.1・**計 +22.9pt** |
| **Rehearse** | selective acc 82.8→56.9 を **83.5 に回復**／同性能到達が **37–46% 高速** |
| **RSIBench-Data** | 初回超えは 58.33% だが、**ピーク超過後は 78.26% が低スコアで終了** |
| **Next-Gen Agentic RL** | 「ボトルネックは system substrate」（ATDP／Evolution Control Plane） |
| **Self-Improvements（Survey）** | 📖 自己改善を **θ更新 vs Σ更新**の二経路に統一 |

---

## 論文紹介（サブテーマ別）

### ① 何を永続させるか＝外在化（θ ではなく Σ・知識）
[Self-Improvements in Modern Agentic Systems: A Survey](https://arxiv.org/abs/2607.13104) 📖
自己改善を **𝒜ₜ=(θₜ, Σₜ)** と定式化し、**Foundation Model Improvement（θ 更新：内因デモ・評価フィードバック・探索経験）** と **Scaffolding Improvement（Σ 更新：プロンプト・メモリ・ツール・制御論理を固定重みのまま refine）** の二経路に整理。**速い in-context 適応と遅い parametric 適応**の統合、mechanism/domain レベルの評価、安全ゲートの必要性を横断的に俯瞰する、今月の見取り図。

![Self-improvement paradigms (θ vs Σ)](../assets/2607.13104-selfimprove-survey.png)
> 図（Survey）：現代エージェントの自己改善パラダイム。Foundation Model Improvement（θ の更新）と Scaffolding Improvement（Σ の更新）を、信号の種類ごとに対比する。（[論文](https://arxiv.org/abs/2607.13104)）

[Knowledge-Centric Self-Improvement](https://arxiv.org/abs/2607.19592)
従来の agent 中心を反転し、**エージェントは汎用・使い捨て、共有された curated 知識ベースを永続の改善対象**にする。task-level forum（証拠付きの主張を投稿）→ cross-task forum（再現する主張を検証）→ distillation（生き残った主張を凝縮）。ARC-AGI-1 **86.7%**（HyperAgents 70%）を $76（vs $234）、SWE-bench Pro 64.0%（DGM 54%）を $208（vs $713）、未知タスク転移 13.3→**43.3%**。「進歩は agent の複雑さより**アクセス可能な情報の質**に依存しうる」。

[Evidence-in-the-Loop: Trace-Driven Optimization for Customer-Service LLM Agents](https://arxiv.org/abs/2607.18039)
本番の顧客対応で、hybrid RAG＋規則由来の証拠に基づき意思決定し、**replay した失敗を「知識ベース／reranker／決定プロンプト／ポリシー」への的を絞った更新**に変換。診断で hybrid recall 96.76% Hit@50、reranker を 56.76→**75.68%**、決定段 DPO で 92.5%、本番で **89.52%（legacy RAG 79.00%）**。「大きな backbone に頼るのではなく、**どこで壊れたか（retrieval/rerank/選択）を診断して層別に直す**」。

### ② システム基質：自己進化を支えるインフラ
[Next-Generation Agentic Reinforcement Learning Systems Enable Self-Evolving Agents](https://arxiv.org/abs/2607.01120)
3本柱：**ATDP**（step-level の RL 級イベントスキーマ：観測・行動・結果・報酬・統治メタデータ）、**Agentic Data Proxy**（LLM・ツール・メモリ・検索の異種本番負荷を横取りし replay 可能な学習素材へ）、**Evolution Control Plane**（軌跡統計と運用制約から、memory 更新／skill パッチ／harness 編集／tool-schema 変更／RL による重み更新の**介入面を自動選択**）。「最大の障壁は強い LLM や RL アルゴリズムではなく、**経験を統治・信用割当可能な学習素材へ変える system substrate の欠如**」。

![AReaL 2.0 architecture](../assets/2607.01120-areal-arch.png)
> 図（Next-Gen Agentic RL / AReaL 2.0）：gateway・router・data proxy・agent-compute worker が、デプロイされたエージェントサービスとオンライン RL 学習を接続するオンライン RL ワークフロー。（[論文](https://arxiv.org/abs/2607.01120)）

### ③ 信頼性：confidence cliff と discovery-reliability gap
[Rehearse: Stepping Back from the Confidence Cliff in Self-Improving Autoresearch](https://arxiv.org/abs/2607.27687)
自己改善オートリサーチでは、最適化が進むほど judge が**自信過剰かつ不正確**になる **confidence cliff** が起きる。**Propose–Predict–Execute** ループで、実行前に候補を strict-consensus のペア比較でランク付けし、**類似の過去試行だけ**を検索する focused outcome store を導入。メモリなしでは selective acc が 82.8→56.9 に落ちるが focused 検索で **83.5 に回復**、nanochat 事前学習で 10.7% 改善（vanilla 7.1%）、4,000 実行で vanilla 性能に **37–46% 速く**到達。

![Rehearse overview](../assets/2607.27687-rehearse-overview.png)
> 図（Rehearse）：Propose–Predict–Execute パイプラインと、類似過去結果だけを引く focused outcome store の全体像。（[論文](https://arxiv.org/abs/2607.27687)）

[RSIBench-Data: Benchmarking Data-Centric Research for Recursive Self-Improvement](https://arxiv.org/abs/2607.25886) ⚖️
学習・評価インフラを固定し、エージェントが**データ中心のポストトレーニング戦略**を反復開発する能力を切り出すベンチ（提案→共有 LoRA SFT→制御フィードバック→checkpoint 選択）。初回超えは **58.33%（14/24）** に達するが、**ピークを超えて探索を続けた場合の 78.26% はより低いスコアで終える**。改善を「発見」できても「維持」できない **discovery-reliability gap** を定量化し、診断枠組みと checkpoint 保全の必要を示す。

### ④ 再帰的自己改善（RSI）
[AREX: Towards a Recursively Self-Improving Agent for Deep Research](https://arxiv.org/abs/2607.21461)
**内側の研究ループ**（証拠収集・回答構築）と**外側の自己改善ループ**（制約検証・的を絞った追調査）を組む二層再帰。長期軌跡を管理する autonomous context-update（ACU）と、決定的に重要な中間行動を強調する step-aware RL。AREX-Base（活性10B）で BrowseComp 82.5%・GAIA 85.4%・DeepSearchQA 89.9%、**ACU +11.8pt・外側ループ +11.1pt・合計 +22.9pt**。discovery-verification の非対称性を再帰的な制約監査で活かす。

![AREX recursive framework](../assets/2607.21461-arex-recursive.png)
> 図（AREX）：内側の research ループが研究状態を保持し暫定回答を確信度付きで外在化、外側の self-improvement ループが確信度と軌跡評価に基づき accept/refine/restart する再帰枠組み。（[論文](https://arxiv.org/abs/2607.21461)）

---

## 論点・未解決課題
1. **外在化の設計**：知識ベース・Σ を永続資産にする流れ（Knowledge-Centric／Survey）。何を・どの粒度で・どう distill するかが鍵。
2. **信頼性（最大の新論点）**：自己改善の**内部 judge が劣化**し（confidence cliff）、改善を**維持できない**（discovery-reliability gap）。→ [verification](../../capabilities/adaptation/verification.md)・[failure-attribution](../../capabilities/adaptation/failure-attribution.md) と直結。
3. **システム基質**：ATDP・制御プレーン等、**経験→統治可能な学習素材**への変換基盤（Next-Gen Agentic RL）。
4. **介入面の選択**：memory / skill / harness / tool-schema / weights のどこを・いつ更新するかの**階層スケジューリング**。
5. **層別診断で直す**：本番は backbone 拡大より「どこで壊れたか」を診断して層別更新（Evidence-in-the-Loop）。

## 次に来るもの（Watch next）
- **信頼できる自己改善**：judge 較正・checkpoint 保全・focused retrieval（Rehearse 型）。
- **外在化知識の標準化**（forum→distill）とクロス LLM 転移。
- **自己進化のシステム基質**（ATDP／Evolution Control Plane）とガバナンス（[governance](../../operations/governance.md)）。
- **RSI の厳密評価**（RSIBench-Data 型）：発見だけでなく"維持"を測る。

---

*本ニュースレターは各論文の **arXiv HTML 本文**を読み取り、framework 図を引用（画像は [`newsletters/assets/`](../assets/) に保存）。[self-evolution.md](../../capabilities/adaptation/self-evolution.md) の2026年7月論文を対象に作成。関連は [評価 号](evaluation_trends.md)・[harness 号](harness_trends.md)・[self-evolution 号（6月）](../jun_2026/self_evolution_trends.md)。*
