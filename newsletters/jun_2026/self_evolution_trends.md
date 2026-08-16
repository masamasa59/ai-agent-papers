# Self-Evolving Agents 研究トレンド（2026年6月）

> 6月に最も論文数が動いた能力カテゴリ（[self-evolution](../../capabilities/adaptation/self-evolution.md), 10本）。各論文の **arXiv HTML 本文**（一部 abstract）を精読して整理した。今月の自己進化研究は「**どう進化させるか**」から「**進化をどう評価・信頼・防御するか**」へ重心が明確に移っている。

## 3行サマリ
- **学習対象の外在化が定着**：モデル重みを凍結したまま、Context・Playbook・Prompt など外部知識を進化させ、Git 管理・モデル横断転移する流れ。UCE は ALFWorld を **75.4%→96.3%**、EvoHunt は脆弱性検出を **1.1%→6.2%（6×）** に。
- **評価が最大の焦点**：SEAGym は「検証で伸びても held-out には転移しない」「利得は更新機構に強く依存」を定量化。Meta-Agent Challenge は、自律的なエージェント開発で **3,939 構成中 人間超えは 55 のみ**と、現状の限界を突きつけた。
- **安全・ガバナンスが前景化**：MLAS 行列は自己進化で **25セル中17が有効防御なし**・攻撃が世代を越えて持続すると警告。Red Queen Gödel Machine は**評価器を共進化**させて評価バイアス（AI論文を人間の1.91倍で過剰採択）を補正した。

## クロス論文で見るトレンド（継続 / 明確化 / 萌芽）
単一研究の主張に寄りかからず、**複数論文で裏付けられたファクト**に絞って整理する。

**継続する傾向（過去号からの延長）**
- **改善対象の外在化**：重みでなく Context/Playbook/知識を進化させる流れが継続。UCE（context）・EvoHunt（playbook）・AgentX（prompt を SGPO で最適化）の **3本が独立に**、モデル凍結のまま改善を示す（1〜4月の self-evolution 号からの延長）。
- **転移性の重視**：UCE（別アクター構造へ 73.1→97.8%）と EvoHunt（弱モデルへ 2.7–4×）が、**進化成果を他モデルへ移す**方向を共有。

**今月明確になった点（複数論文で裏付け）**
- **利得は"普遍的でない"**：SEAGym（GPT→GLM で −7.3pp の非対称・「更新機構に強く依存」）と Meta-Agent Challenge（3,939 構成中 人間超えは 55 のみ）が、**別設定で独立に**「自己進化は条件依存で脆い」を示した。
- **焦点は"評価"へ**：SEAGym（評価環境）・Rubrics サーベイ（評価基準の共進化）・Red Queen（評価器の共進化）の **3本**が揃って「何をどう測るか」を主題化。

**別角度から複数が示唆する萌芽**
- **"評価器・安全機構が最適化対象になる"問題**：MLAS（optimizer–optimizee collapse で静的防御は構造的に不十分）を軸に、Rubrics（低品質・機械生成ルーブリックが判断を悪化）・Red Queen（最強評価器が AI 論文を人間の 1.91 倍で過剰採択）が、**別角度から同じ核**を示唆。

**単発だがインパクトの大きい結果（裏付けは弱め・要追試）**
- **自己進化系の攻撃は"系統持続"する**：MLAS の事例研究で evolution-native な Hermes は攻撃持続率 100%（40/40）・併設スキャナ阻止 2.5%。単一フレームワークの比較ゆえ一般化は要検証だが、影響は大きい。
- **産業での compounding**：AgentX が Kuaishou の単一デプロイで年 RMB 1億超・人手比 3.7×。1事例だが、本番自己進化の桁感を示す。

## 数字で見るインパクト（各論文の本文より）

| 論文 | 数字 | 初見の読み方 |
|---|---|---|
| **UCE** | ALFWorld 75.4→**96.3%**／別アーキへ 73.1→**97.8%** | 失敗が約1/7に激減。しかも**別のエージェント構造に載せ替えても効く**＝手法がモデル非依存 |
| **EvoHunt** | "実際に動く攻撃"の検出 1.1→**6.2%**／弱モデルへ **2.7–4×** | 絶対値は低いが**従来1%が限界の難題を6倍**に。強モデルで一度学べば安モデルが実行 |
| **SEAGym** | 自タスク **+17.1pp** ／未知タスク +6.3pp／他モデル **−7.3pp** | 「自分のタスクでは伸びるが**使い回すと効かない・悪化**」＝進化の成果は転移しにくい実証 |
| **Meta-Agent Challenge** | 3,939 通り中、人間超えは **55（約1.4%）** | **エージェントに自律的にエージェントを作らせるのは現状ほぼ無理**、という厳しい現実 |
| **Safety / MLAS** | 25攻撃面中 **17 は防御ゼロ**／攻撃成功 **100% が持続** | 自己進化系は**ほぼ丸腰**で、一度侵入されると**世代を越えて残る** |
| **AgentX** | 3週で年 **RMB 1億超**・人手比 **3.7×** | 実サービス1本で**エンジニア手作業の約4倍の事業価値**＝自己進化の実利を初めて桁で提示 |
| **Red Queen** | トークン **1.35–1.72× 減**／論文採択 **1.78–1.86×** | **評価器を一緒に育てる**と、より少ない計算で質（採択率ほぼ倍）も上がる |

---

## 論文紹介（サブテーマ別）

### ① 学習対象の外在化：凍結モデル上で「文脈・手順」を進化させる
[Unified Context Evolution for LLM Agents](https://arxiv.org/abs/2606.02304)
経験を4型（Memory／Strategy／Workflow／Skill）の **Evolvable Context Units (ECU)** として型付きライブラリに蓄積し、評価→収集→予算配分(KYS)→生成→整理の5フェーズで**勾配なしに文脈を進化**させる。ALFWorld を ReAct 75.4%→**96.3%**（+20.9pp）、WebShop を +16.2pp、さらに Plan-and-Act/ReflAct など**別アクター構造へ 73.1%→97.8% で転移**。細粒度の属性選択タスクでは頭打ちで、RL 併用が課題と明言。

![UCE](../assets/2606.02304-uce-architecture.png)
> 図（UCE）：1サイクル5フェーズ（evaluate→collect→KYS→generate→cleanup）で型付き知識(ECU)を勾配なしに進化させるアーキテクチャ（[論文](https://arxiv.org/abs/2606.02304)）

[Transferable Self-Evolving Playbooks for Agentic Security Auditing（EvoHunt）](https://arxiv.org/abs/2606.16420)
モデルと harness を固定し、**Git テキストで版管理される監査プレイブック**（ワークフロー・脆弱性別戦略・検証ゲート・誤検知制御）だけを進化させる。取得段で target-match を 1.1%→**6.2%（6×）**、凍結プレイブックの転移で弱いモデルを **2.7–4×** 改善、**28件の脆弱性を確認開示**。フロンティアモデルが一度だけ進化を回し（約$1,400）、以降は安価なモデルが手順を実行するコストモデルを提示。

[AgentX: Towards Agent-Driven Self-Iteration of Industrial Recommender Systems](https://arxiv.org/abs/2606.26859)
Brainstorm→Developing→Evaluation の閉ループ・マルチエージェントが推薦アルゴリズム反復を自動化し、**Semantic-Gradient Prompt Optimization (SGPO)** で自らの harness を進化。Kuaishou で3週間、3ワーカ運用し **374案→10 投入**、週次スループット倍増、人手比 **3.7× の事業価値**、**年換算 RMB 1億超**。ただし本番はオフライン指標では不十分で**実オンライン A/B と admission gate の人手レビュー**が必須と結論。

![AgentX](../assets/2606.26859-agentx-workflow.png)
> 図（AgentX）：Brainstorm→Developing→Evaluation の閉ループと、SGPO による harness 進化の全体フレーム（[論文](https://arxiv.org/abs/2606.26859)）

### ② 自己進化を「正しく評価する」
[SEAGym: An Evaluation Environment for Self-Evolving LLM Agents](https://arxiv.org/abs/2606.17546)
静的ベンチを自己進化用の動的環境へ変換し、進化を MDP として定式化。**update-validation／ID-OOD 転移／replay（忘却）／cost** の多視点で測る。AHE は検証で **+17.1pp** でも OOD は +6.3pp に留まり、GPT で進化した harness が GLM の ID を **−7.3pp** 悪化させるなど**転移は非対称**。「**自己進化の利得は更新機構とタスク分布・バックエンドに強く依存**し、普遍的に有益ではない」と結論づける、今月の評価論の中核。

![SEAGym](../assets/2606.17546-seagym.png)
> 図（SEAGym）：静的ベンチを自己進化用の動的環境へ変換し、train バッチのサンプリング→エピソード実行→軌跡と検証器フィードバックの記録→自己進化エージェントの状態更新→凍結スナップショットでの評価、という流れ（[論文](https://arxiv.org/abs/2606.17546)）

[The Meta-Agent Challenge: Are Current Agents Capable of Autonomous Agent Development?](https://arxiv.org/abs/2606.04455)
コードエージェント（メタエージェント）がサンドボックス内で**タスク特化エージェントを自律設計・実装・最適化**できるかを、開発フェーズ＋保護テストで測る。5ドメインの **3,939 構成中、人間ベースラインを超えたのは 55 のみ**（44 はプロプライエタリ）、33% は標準偏差 >0.1 と高分散、reward hacking の試みも検出。**自律的なエージェント開発は依然困難**で、閉/開モデル差が大きいことを実証。

[From Holistic Evaluation to Structured Criteria: Rubrics Across the Evolving LLM Landscape](https://arxiv.org/abs/2606.08625) 📖
ルーブリック（明示性・構造性・分解可能性・検証可能性）を統一枠組みとして整理したサーベイ。**明示的基準→整合ガイド→推論足場→実行可能報酬→自己進化機構**という5段階の共進化を跡付ける。低品質ルーブリックは沈黙せず**むしろ判断を悪化**させ、機械生成ルーブリックは一貫性が劣化、「固定ルーブリック集合では複雑な報酬関数を完全には捉えられない」表現力ギャップを指摘。評価基準が外部ツールから**内在的な自己監督機構**へ移りつつある。

### ③ 評価器を「共進化」させる
[The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators](https://arxiv.org/abs/2606.26294)
固定ベンチを前提とせず、**エポック内は安定・エポック境界で効用が進化**する非定常評価のもとで、エージェントと評価器を共進化させつつ**エポック単位の自己改善保証**を与える。コーディングでトークン **1.35–1.72× 削減**、論文執筆で採択率 **1.78–1.86×**、証明採点で **+9%** 精度。最強ベースライン評価器が AI 論文を**人間の 1.91 倍で過剰採択**する偏りを、敵対的目的で補正した点が示唆的（work-in-progress）。

### ④ 自己進化の「安全・ガバナンス」
[Safety in Self-Evolving LLM Agent Systems: Threats, Amplification, and Case Studies](https://arxiv.org/abs/2606.23075)
5モジュール（Brain／Cognitive Resource／Execution／Self-Design／Collective）×5ライフサイクル（Bootstrap/Propose/Evaluate/Commit/Serve）の **MLAS 行列（25セル）** で攻撃面を体系化。**17セルは有効な防御が存在せず**、evolution-native な Hermes は **攻撃持続率 100%**（40/40）、併設スキャナは **2.5%（1/40）** しか阻止できない。自己進化は「全ての既知攻撃を**セッション境界から系統持続へ**変換」し、安全機構自体が最適化対象になる **optimizer–optimizee collapse** により**静的防御は構造的に不十分**と結論。

---

## 論点・未解決課題
1. **評価の妥当性**：検証での伸びが held-out に転移しない（SEAGym）。ID/OOD/replay・matched 設定・監査クリーンを前提にしないと利得を過大評価する。
2. **更新機構への強依存**：利得はタスク分布・バックエンド・更新則に強く依存し、**モデル横断転移は非対称**。「普遍的に良い進化」は成立しにくい。
3. **optimizer–optimizee collapse**：自己進化下では安全機構・評価器そのものが攻撃・最適化の対象になり、静的な分離が崩れる（Safety/MLAS、Rubrics の評価器バイアス）。
4. **外在化 vs 重み更新**：Context/Playbook/Prompt の外在化は転移性・可監査性で有利だが、細粒度タスクは頭打ちで RL 併用が要る（UCE）。
5. **本番ガバナンス**：産業展開は compounding だが、causal attribution・admission gate・人手レビューが不可欠（AgentX）。

## 次に来るもの（Watch next）
- **進化対応の評価プロトコル/環境**（SEAGym 系）の標準化：ID/OOD/replay/cost を既定に。
- **評価器の共進化・非定常評価**（RQGM 方向）＝評価指標の攻略（reward hacking）への構造的対処。
- **進化対応セキュリティ**：longitudinal monitoring、自己改変系の formal verification、系統横断の防御。
- **外在化知識の型・ライフサイクル自動設計**（UCE の ECU 型は現状手設計）。

---

*本ニュースレターは各論文の **arXiv HTML 本文**（Red Queen Gödel Machine のみ abstract）を読み取り、[self-evolution.md](../../capabilities/adaptation/self-evolution.md) の2026年6月論文を対象に作成。関連動向は [evaluation.md](../../capabilities/trust/evaluation.md)・[safety.md](../../capabilities/trust/safety.md)・[experience.md](../../capabilities/adaptation/experience.md) も参照。*
