# Skills 研究トレンド（2026年6月）

> 6月に活発だった能力カテゴリ（[skills](../../capabilities/action/skills.md), 7本）。各論文の **arXiv HTML 本文**を精読し、主要な **framework 図も引用**した。今月のスキル研究は「スキル＝**自己進化し・モデルを跨いで転移し・検証可能な再利用資産**」という像を固めつつあり、焦点は **(a) どう獲得するか、(b) どう転移させるか、(c) どう構成・選択するか、(d) どう検証するか** に整理できる。

## 3行サマリ
- **獲得元が多様化**：軌跡（SkillAdaptor）・オープンワールド文書/Web（OpenSkill）・実験ノート（Notes2Skills）・複数モデルの集合知（OpenClaw-Skill）から、スキルを抽出。
- **転移と検証が主戦場**：OpenSkill は**答えを見ずに仮想検証器**を作り closed-world 比 **+8.9pt**・他モデルへ 5.5–14.8% 転移、SkillComposer は **3.9M の小型モデル**でスキル選択を担い SkillsBench を **+23.1pt**（SFT 比 **154× 省パラメータ**）。
- **応用でも自己進化が結実**：EvoDS はデータサイエンスで **279 スキルを 69% 再利用**、DataMind-14B 比 **+28.9%** と、スキル×文脈圧縮の統合が効いた。

## なぜ注目か
スキルは Tool Use を包含する上位概念として、エージェントの「再利用可能な手続き」を担う。6月は**獲得・転移・検証**の各段が具体化し、[self-evolution](../../capabilities/adaptation/self-evolution.md)（改善ループ）と [tool-use](../../capabilities/action/tool-use.md) の橋渡しとして機能し始めた。特に **step-level の失敗帰属**でスキルを直す SkillAdaptor は [failure-attribution](../../capabilities/adaptation/failure-attribution.md) の潮流とも接続する。

## 数字で見るインパクト（各論文の HTML 本文より）

| 論文 | 主な結果 |
|---|---|
| **SkillAdaptor** | WebShop +1.7pp／Claw-Eval +1.8（訓練不要・**ステップ帰属**でスキル修正） |
| **OpenSkill** | SkillsBench **43.6%**(Opus)、closed-world 比 **+8.9pt**／仮想検証器の一致 60.7%／転移 5.5–14.8% |
| **Notes2Skills** | 指令検出 F1=**0.737**／149指令を**確信度100%一致**で保存／FLAG recall 85.7–100% |
| **OpenClaw-Skill** | QwenClawBench 34.5→**44.9**（+10.4）／PinchBench 68.2%（vs 61.1%） |
| **SkillComposer** | Set F1 **73.9%**／実タスク劣化 11pp（SFT 27.5pp）／SkillsBench **+23.1pt**／**154× 省パラメータ** |
| **EvoDS** | DataMind-14B 比 **+28.9%**／**279スキル・再利用69%**／out-of-token 失敗を根絶 |

---

## 論文紹介（サブテーマ別）

### ① スキルの獲得：軌跡・オープンワールド・ノート・集合知
[SkillAdaptor: Self-Adapting Skills for LLM Agents from Trajectories](https://arxiv.org/abs/2606.01311)
訓練不要で外部スキルを適応する3段（**Attribution → Modification → Qualification**）。失敗軌跡から**最初の実行可能な誤りステップを局所化**し、責任のあるスキルを重み付き帰属して「誤誘導なら改訂／不足なら新規生成」、再実行で性能が上がるときのみ採用。WebShop +1.7pp、Claw-Eval +1.8 を3モデルで一貫達成。軌跡に観測可能な中間信号が出る構造化タスクで特に有効。

[OpenSkill: Open-World Self-Evolution for LLM Agents](https://arxiv.org/abs/2606.06741)
デプロイ後に、**文書・リポジトリ・Web** から接地知識を得てスキルと**検証信号**を構築（対象タスクの答えは見ない）。独立に検証可能な事実へ紐づく**仮想テスト**でスキルを反復精緻化し、**leakage barrier** で最終評価まで監督を隔離。SkillsBench で Opus 43.6%・GPT 42.1%、closed-world 比 **+8.9/+8.8pt**、仮想検証器は正解と **60.7% 一致**（正解未参照）、他モデルへ 5.5–14.8% 転移。

![OpenSkill framework](../assets/2606.06741-openskill-framework.png)
> 図（OpenSkill Fig.2）：base agent が外部資源からオープンワールド知識を獲得→sandbox で生成・実行・精緻化し、仮想タスク検証器と診断リトリーバでバグ/知識ギャップを修復。leakage barrier が対象監督をスキル構築から隔離する。（[論文](https://arxiv.org/abs/2606.06741)）

[Notes2Skills: From Lab Notebooks to Certainty-Aware Scientific Agent Skills](https://arxiv.org/abs/2606.11897)
実験ノートから**確信度を保ったまま**指令を抽出。Stage1 で実行可能文を **FACT/JUDGMENT/SUGGESTION** に分類（F1=0.737）、Stage2 で出典と確信度に紐づく **MetaSkill**（Markdown＋JSON）へコンパイルし、決定的 executor が「確信度＋証拠」の二重整合を要求。**149指令を確信度100%一致**で保存し、**uncertainty laundering（曖昧な注記が確定行動化）と directive loss（確定文の無視）を回避**（FLAG recall 85.7–100%）。ただしナノポア電気泳動の**ドメイン特化**で、指令密な領域は Stage1 精度が課題。

[OpenClaw-Skill: Collective Skill Tree Search for Agentic LLMs](https://arxiv.org/abs/2606.16774)
**複数モデルが同一サブタスクを解いて多様な軌跡を生成**し、品質＋転移可能性で評価（CSN-Gen/Assess）、選抜スキルを**木構造**（層＝サブタスク、経路＝合成手順）に組織。さらに CSRL でスキル条件付き軌跡を group-relative に最適化。QwenClawBench で 9B が 34.5→**44.9（+10.4）**、PinchBench 68.2%。**skill fragmentation・limited diversity・poor transferability** を集合知で緩和する。

![OpenClaw-Skill overview](../assets/2606.16774-openclawskill-overview.png)
> 図（OpenClaw-Skill Fig.2）：複雑なタスクをサブタスクへ分解し、各サブタスクに対して collective にスキルノードを反復構築する CSTS ＋ CSRL の全体像。（[論文](https://arxiv.org/abs/2606.16774)）

### ② スキルの構成・選択（効率）
[Generative Skill Composition for LLM Agents（SkillComposer）](https://arxiv.org/abs/2606.32025)
スキル選択を「閉じたライブラリ上の**タスク条件付きスキル系列予測**」と定式化。**3.9M パラメータの小型デコーダ**が、どのスキルを・何個・どの順で使うかを自己回帰生成（凍結エンコーダ＋基数/集合ヘッド＋検索拡張復号）。In-dist で Set F1 73.9%（SFT 71.1%）、**実タスクでの劣化はわずか 11pp**（SFT は 27.5pp）、SkillsBench を **+23.1pt**（Codex）とオラクル検索に匹敵しつつプロンプトトークン削減。SFT 比 **154× 省パラメータ・25× 省計算**。長鎖（≥3スキル）で過少予測する short-sequence bias が伸びしろ。

![SkillComposer overview](../assets/2606.32025-skillcomposer-overview.png)
> 図（SkillComposer Fig.3）：タスク–ライブラリ文脈を符号化し、可変長・順序付きのスキル系列を「凍結エンコーダ＋制約付き自己回帰デコーダ＋検索拡張復号」で予測する。（[論文](https://arxiv.org/abs/2606.32025)）

### ③ 応用での自己進化（データサイエンス）
[EvoDS: Self-Evolving Autonomous Data Science Agent with Skill Learning and Context Management](https://arxiv.org/abs/2606.03841)
**階層マルチエージェント**（Manager/Cleaner/Featurizer/Modeler/Visualizer）＋**自律スキル獲得（ASA）**＋**適応的文脈圧縮（ACC）**を、SFT→GRPO で共同最適化。4ベンチ平均 **0.424**（DataMind-14B 比 **+28.9%**）、MLE-Dojo で 0.311（最良ベースライン 0.136）、**279スキルを69%再利用**、**out-of-token 失敗を全廃**。ScienceAgentBench の専門的発見では基盤モデルの科学知識不足で差が残る。

![EvoDS framework](../assets/2606.03841-evods-framework.png)
> 図（EvoDS Fig.1）：階層マルチエージェント＋自律スキル獲得＋適応的文脈圧縮の全体像（a）と、SFT＋agentic RL によるタスク実行・スキル獲得・文脈管理の同時最適化（b）。（[論文](https://arxiv.org/abs/2606.03841)）

---

## 論点・未解決課題
1. **検証（答えなし）**：デプロイ後の自己進化は「正解を見ずにスキル品質をどう測るか」が核心。仮想検証器は 60.7% 一致に留まり、易しすぎる仮想タスクで過大評価も（OpenSkill）。
2. **転移 vs 特化**：集合知・小型コンポーザは転移を志向（OpenClaw-Skill/SkillComposer）する一方、ドメイン特化（Notes2Skills）は汎化が限定的。
3. **失敗帰属の粒度**：スキル修正は**ステップ帰属**が効くが、疎なフィードバックや外部状態依存では弱い（SkillAdaptor）。→ [failure-attribution](../../capabilities/adaptation/failure-attribution.md)。
4. **確信度・安全**：ノート由来スキルの uncertainty laundering 回避など、**確信度の保存**が科学応用で不可欠（Notes2Skills）。
5. **構成の長鎖化**：スキル系列が長くなると選択が過少に（SkillComposer の short-sequence bias）。

## 次に来るもの（Watch next）
- **答えなし検証器**の高精度化（self-verification / virtual test）→ [verification](../../capabilities/adaptation/verification.md)。
- **クロスモデル転移**の定量化と、集合知的スキル生成のスケール。
- **スキル×文脈圧縮**の統合（EvoDS 型）で長期・省トークン運用。
- **確信度・出所を保つスキル表現**（科学・企業応用の監査可能性）。

---

*本ニュースレターは各論文の **arXiv HTML 本文**を読み取り、framework 図を引用（画像は [`newsletters/assets/`](../assets/) に保存）。[skills.md](../../capabilities/action/skills.md) の2026年6月論文を対象に作成。*
