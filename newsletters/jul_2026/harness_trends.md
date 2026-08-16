# Agent Harness 研究トレンド（2026年7月）

> 7月に最も論文数が動いたカテゴリ（[harness](../../architecture/harness.md), 12本）。各論文の **arXiv HTML 本文**を精読して整理した。6月の自己進化が「進化をどう評価・防御するか」へ向かったのに続き、7月の Harness 研究は「**どう進化させるか**」から「**責任を持って進化させ、本当に効くと証明する**」段階へ移った。

## 3行サマリ
- **テスト時・経験駆動の適応が主流**：凍結モデルのまま、無ラベルの実行トレースや経験バンクから harness を適応。TTHE は text-to-SQL を **12%→50%**、Living-Harness は τ²-Bench を **+10.07pp**、MemoHarness は Codex 超えの精度を **$6.89** で達成。
- **しかし「本当に効くのか」への批判が正面化**：Rethinking Evaluation は、**同一計算予算**で比べると harness 進化は単純サンプリングに劣り（72.3% vs 67.4%）、held-out での利得は **+0.6pt** に過ぎず「深刻な過学習」と断じた。
- **工学的規律と診断が前景へ**：Harness Handbook は「どこを直すかの特定が中心的ボトルネック」、From Prompts to Contracts は「**プロンプトはガードレールではない**」、Model or Harness? は失敗を model/harness に **κ=0.76** で帰属。足場は**攻撃・知財**の対象にも（Agent Harness Distillation）。

## クロス論文で見るトレンド（継続 / 明確化 / 単発の注目結果）
単一研究に寄りかからず、**複数論文で裏付けられたファクト**を軸に、単発でもインパクトの大きい結果は別建てで示す。

**継続する傾向（6月からの延長）**
- **凍結モデル＋足場適応で大幅改善**：TTHE・HarnessBank・Living-Harness・MemoHarness・Co-Harness の **5本が独立に**、重み更新なし（または足場主導）で二桁 pt 級の改善を報告。「性能＝モデル＋足場」の見方が定着。

**今月明確になった点（複数論文で裏付け）**
- **テスト時・無ラベル適応が主流化**：TTHE・MemoHarness・Living-Harness の **3本**が、ラベルなしの実行トレース／経験バンクで足場を適応。
- **"モデル特異 vs 転移"の対立が顕在化**：HarnessBank は利得が**モデル特異**（普遍最適足場は無い）と示す一方、Living-Harness・MemoHarness は**クロスモデル転移**を主張。両立条件が次の争点。
- **評価の厳密性が中心争点に**：Rethinking Evaluation（held-out 利得 +0.6pt、単純サンプリング 72.3% > 進化 67.4%）と DataClawEval（LLM judge が採点を膨張、規則ベース採点が不可欠）が、**別々の設定で独立に**「公平比較・決定的採点なしに利得を語るな」を突きつけた（6月 SEAGym とも連続）。

**単発だがインパクトの大きい結果（裏付けは弱め・要追試）**
- **小型モデル＋足場で大型の 89.7% をコスト 4%**（Better Harnesses、7業務タスクの単一研究）。
- **200時間超の自律運用で 8.7× 高速化・クラッシュ自己復旧**（Co-Harness、単一ケーススタディ）。
- **失敗を model/harness に κ=0.76 で帰属**（Model or Harness?、1提案の分類体系）。
- **足場は抽出可能な知財＝新たな攻撃面**（Agent Harness Distillation、1研究の実証）。

## 数字で見るインパクト（各論文の HTML 本文より）

| 論文 | 主な結果 |
|---|---|
| **TTHE** | text-to-SQL 12→**50%**（+38pt）／SWE 20→35%／claw-eval 48.9→69.8%（無ラベル・重み固定） |
| **Co-Harness** | 平均 **+20.4pp**（58.5→78.9）／静的 harness 比 +24.7pp／自律22版で **8.7× 高速化** |
| **Living-Harness** | τ²-Bench 73.0→**83.1%**（+10.07pp）／凍結足場転移で GLM-5 を 0→43.08% |
| **MemoHarness** | Terminal-Bench 0.722→**0.806**／他6モデルへ +0.098／コスト **$6.89**（Codex $10.28 未満） |
| **HarnessBank** | 7ベンチで **+5.1〜15.4%**（AppWorld +15.4, z=6.44）／利得はモデル特異 |
| **Better Harnesses, Smaller Models** | 小型で大型の **89.7%** をコスト **4%**／多様性と効果は ρ=−0.96 |
| **Harness Handbook** | プラン勝率 38.3 vs 28.3（Codex）／トークン **−12.7%**／局所化 F1 +5.0〜18.8pp |
| **Rethinking Evaluation** | held-out 利得 **+0.6pt**／単純サンプリング 72.3% > 進化 67.4% |
| **DataClawEval** | 最強 GPT-5.5 でも **74.9**／MySQL 81.4 vs HiveSQL 61.7（万能モデル不在） |
| **Agent Harness Distillation** | 蒸留後 MMLU-Pro **86.25%（+45pt）**／足場は抽出可能な知財 |

---

## 論文紹介（サブテーマ別）

### ① テスト時・経験駆動の適応（凍結モデル・無ラベル）
[TTHE: Test-Time Harness Evolution](https://arxiv.org/abs/2607.08124)
評価時に**無ラベルの実行トレース**だけで harness（ツール呼び出し・文脈構築・エラー回復を司る実行プログラム）を最適化。G×R の候補集団を agentic proposer が編集し judge が選抜、同一の凍結 LLM 上で「周辺プログラムの変更」として適応する。text-to-SQL を **12%→50%（+38pt）**、SWE-bench 20→35%、claw-eval 48.9→69.8%。ただし「**足場は成功裏に実行しつつ誤った問いに答えうる**」——被覆ギャップ（約15%が未生成）と選択後悔（judge 50% vs プール oracle 64%）が本質的課題。

![TTHE](../assets/2607.08124-tthe-method.png)
> 図（TTHE）：無ラベルバッチ内で、committed harness H_t から G 分岐×R ラウンドで harness を進化させる（[論文](https://arxiv.org/abs/2607.08124)）

[MemoHarness: Agent Harnesses That Learn from Experience](https://arxiv.org/abs/2607.14159)
harness を6つの編集可能次元に分解し、**二層の経験バンク**（ケース別診断＋大域パターン）を保持。テスト時はラベルなしで類似経験を検索し**ケース別構成を生成**。Terminal-Bench 0.722→**0.806**、FinanceAgent 0.60→0.767、他6モデルへ平均 +0.098 転移、コストは **$6.89**（Codex $10.28・Claude Code $9.51 未満）で高精度。ただし held-out は18タスクのみでアブレーション不足と自認。

[HarnessBank: Semantic Gene-Bank Search with Gated Verification](https://arxiv.org/abs/2607.13683)
高性能 harness を**意味座標（どこに・なぜ効くか）で索引する遺伝子バンク**に貯め、再発明・再結合する Quality-Diversity 探索に、評価妥当性→機構活性→有意性（2σ）→性能の**逐次ゲート選別**を重ねる。7ベンチで **+5.1〜15.4%**（AppWorld +15.4, z=6.44）。クロスモデルでは利得が**モデル特異**で、普遍最適足場は見つからないと示す。

[Living-Harness Is an Interactive-Agent Evolver](https://arxiv.org/abs/2607.26598)
**エピソード記憶（トリガ・失敗・回復）と状態グラフ（修復エッジ・遷移規則）**を、rollout→evaluate→update の3相で進化。schema/scope/evidence/constraint/merge の**ゲート**で不正更新を抑える。τ²-Bench を Reflexion 73.02→**83.09%**（+10.07pp）、MultiWOZ +9.91pp、凍結足場の転移で GLM-5 を Taxi 0→43.08%。ただし**単調改善は保証されず**、ロールバックや回帰テストは未整備。

![Living-Harness](../assets/2607.26598-livingharness-overview.png)
> 図（Living-Harness）：各エピソードの軌跡・評価信号を Evolution-SOP が事後証拠へ変換し、episodic memory ℛ と state graph G を更新（tools/base context は凍結）（[論文](https://arxiv.org/abs/2607.26598)）

### ② 効率：小型モデル × 良い足場
[Better Harnesses, Smaller Models: Building 90% Cheaper Agents via Automated Harness Adaptation](https://arxiv.org/abs/2607.08938)
失敗モード（ツール使用・指示追従・知識・長文脈・計画）を harness 適応戦略へ写像し、メタエージェントが編集を探索。**小型モデルで大型の 89.7% をコスト 4%** で回収、21ペア中16で有意改善、7ペアで大型との差を解消。**タスク多様性と効果は ρ=−0.96 の強い負相関**で、「足場は難しさを吸収できるが、欠けた中核能力は代替できない」。

### ③ 重みとの共進化
[Co-Harness: Co-Evolving Harnesses and Model Weights for LLM Agents](https://arxiv.org/abs/2607.22688)
HarnessCritic が失敗軌跡から scaffold の欠陥を診断・修復する第1ループと、改善足場が生む良質軌跡でモデルを微調整する第2ループの**二重ループ**。TIR タスクで平均 **+20.4pp**（58.5→78.9）、HMMT25 で +27.2pp、静的 harness 比 +24.7pp、22版の自律進化でクラッシュ復旧・**8.7× 高速化**・アンサンブル発見。ただし「①足場更新が軌跡品質を上げ、②モデルがそれを内在化し、③強化モデルが新機会を開く」3条件が揃うときのみ複利化し、モデル能力が頭打ちだと飽和する。

![Co-Harness](../assets/2607.22688-coharness-main.png)
> 図（Co-Harness）：HarnessCritic による scaffold 修復ループと、改善足場が生む軌跡でモデルを微調整するループの二重構造（[論文](https://arxiv.org/abs/2607.22688)）

### ④ 批判的検証：その利得は「設計」か「探索」か
[Rethinking the Evaluation of Harness Evolution for Agents](https://arxiv.org/abs/2607.12227)
Parallel Sampling／Sequential Refinement／Harness Evolution／Harness Scaling を**同一推論予算**で比較し、最適化に使ったのと同じベンチではなく held-out で汎化を測る。Terminal-Bench 2.1（89タスク）で、ユニットテストなしでは**単純サンプリング 72.3% > 進化 67.4%**、テストありでも逐次改良 91.8% > 進化 86.2%、そして**held-out 利得はわずか +0.6pt**。「現行の harness 進化は深刻な過学習を示し、公平比較では単純な test-time scaling に劣る」——今月の警鐘。

### ⑤ エンジニアリング：進化する足場を「読める・監査できる」形に
[Harness Handbook: Making Evolving Agent Harnesses Readable, Navigable, and Editable](https://arxiv.org/abs/2607.13285)
静的解析＋LLM で**振る舞いをコード位置へ対応づける**行動中心表現と、L1–L3 の段階的開示（BGPD）。Codex（Rust, 2,267ファイル）でプラン勝率 38.3% vs 28.3%、Terminus-2 で 45.6% vs 26.7%、**トークン −12.7%**、局所化 F1 を **+5.0〜18.8pp**。「**振る舞いの局所化こそ harness 進化の中心的ボトルネック**——正しい編集の生成より、影響箇所を全て見つけることが先」。

[From Prompts to Contracts: Harness Engineering for Auditable Enterprise LLM Agents](https://arxiv.org/abs/2607.08028)
決定的挙動を自然言語の指示から**版管理された成果物（マニフェスト・出典付き claim・トレース）へ移し**、モデルは「claim パッケージを言い換える差し替え可能な層」に限定。韓国5企業群のデータで、契約保全 30/30・故障注入 7/7 検出、3モデル差し替えでもコード側検査 270/270 通過。検証ゲートを外すと prompt のみでは30件の違反、外部ガードレールは過剰拒否（有用性 88/120）だが harness は **120/120 を維持**。「**プロンプトはガードレールではない**」。

### ⑥ 診断：失敗は「モデルか足場か」
[Model or Harness? An Interaction-Centric Taxonomy for Localizing Agent Failures](https://arxiv.org/abs/2607.28802)
失敗を**コンポーネント間のエッジ**として表し、41 の失敗モードに「修復すべき側（fault side）」を付与。回復不能になる**最初の失敗**まで遡って帰属する。4フロンティアの agent-as-judge で、カテゴリ一致 **κ=0.76**（GPT-5.5）、3-of-4 投票で 90% 被覆時に精度 0.83。「同じ可視の失敗でも、由来次第で post-training／scaffolding／環境再設計と対処が変わる」。

![Model or Harness?](../assets/2607.28802-modelorharness-flowchart.png)
> 図（Model or Harness?）：41 の失敗モードをコンポーネント間のエッジへ写像し、fault side を割り当てる相互作用中心の分類（[論文](https://arxiv.org/abs/2607.28802)）

### ⑦ ベンチマークとセキュリティ
[DataClawEval: A Benchmark for Data Engineering Agents in Real Industrial Harness](https://arxiv.org/abs/2607.28033) ⚖️
実運用のデータエンジニアリングコードから5段階 human-in-the-loop で 100 タスクを構築（5エンジン・5業務・英中各50）。成果物70%＋プロセス30%を**決定的採点スクリプト**で評価。最強 GPT-5.5 でも **74.9**、MySQL 81.4 に対し HiveSQL 61.7 と**エンジン間で激変**、万能モデルは不在。**LLM judge は採点を膨張**（プロセス 22.2→75）・非決定的（最大291%の上限超え）で、規則ベース採点が不可欠と実証。

[Agent Harness Distillation: Inference-Time Harness Extraction and Exploitation in Autonomous Multi-Agent Systems](https://arxiv.org/abs/2607.28147)
ブラックボックスの2段階（誘導クエリで実行構造を露出→surrogate と比較する Loop Harness Alignment）で、対象の**推論時 harness を蒸留**。Qwen3.6-Flash で事前蒸留 +12.87〜13.80pp、蒸留後は MMLU-Pro で **86.25%（+45pt）**。**足場は抽出可能な知財**であり、偽の harness 記述を吐かせる**欺瞞防御**を提案。ただし「振る舞い的区別不能」クラスまでしか復元できない。

---

## 論点・未解決課題
1. **評価の厳密性が最重要**：matched-budget・held-out・決定的採点を欠くと利得を過大評価する（Rethinking Evaluation、DataClawEval）。「進化 vs 追加探索」の切り分けが必須。
2. **判定・選択のボトルネック**：無ラベル適応は judge の誤較正が律速（TTHE の selection regret、DataClawEval の judge 膨張）。**検証器の信頼性**が鍵。
3. **モデル特異 vs 転移**：HarnessBank/Better Harnesses は利得がモデル特異、一方 Living-Harness/MemoHarness はクロスモデル転移を主張。特化と汎化のトレードオフ。
4. **可読性・帰属・監査**：どこを直すか（Harness Handbook）、誰の責任か（Model or Harness?）、prompt を契約へ（From Prompts to Contracts）——**運用に耐える工学**が必須条件に。
5. **安全と知財**：足場が抽出・攻撃対象（Agent Harness Distillation）。ガバナンス（gated updates）との統合が急務。

## 次に来るもの（Watch next）
- **公平評価プロトコルの標準化**：matched-budget・held-out・監査クリーン・規則ベース採点を既定に。
- **検証器（judge/verifier）の強化**：無ラベル適応の律速を解く。→ [verification](../../capabilities/adaptation/verification.md)・[evaluation](../../capabilities/trust/evaluation.md) と接続。
- **足場×重みの共進化のスケジューリング**（Co-Harness 起点）：いつ足場を／いつ重みを更新するか。
- **可監査・ガバナンス統合**：contracts 化、gated updates、足場の知財防御。

---

*本ニュースレターは全12本の **arXiv HTML 本文**を読み取り、[harness.md](../../architecture/harness.md) の2026年7月論文を対象に作成。前月の潮流は [self-evolution 号（6月）](../jun_2026/self_evolution_trends.md) を参照。*
