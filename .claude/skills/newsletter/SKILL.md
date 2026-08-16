---
name: newsletter
description: >-
  Write a monthly trend newsletter for this ai-agent-papers repo. Use when asked
  to create/update a monthly trend report, summarize a category's recent papers,
  or "make a newsletter". Encodes the house procedure: pick the most active
  categories, read each paper's arXiv HTML in full (background + discussion, not
  just method/numbers), embed real figures, and write a Japanese summary built on
  facts corroborated across multiple papers with numbers made legible to a
  first-time reader.
---

# Newsletter 作成手順（ai-agent-papers）

月次のトレンドニュースレターを作る手順。既存の書式は `newsletters/*/*.md`（特に近い号）を参照する。出力言語は**日本語**。

## 0. 大原則（過去のレビューで確定した必須事項）
1. **arXiv は HTML を読む**（`https://arxiv.org/html/<id>`）。`/abs/` は内容が足りないので使わない。HTML が 404 のときだけ `/abs/` にフォールバックし、その旨を号内に明記。
2. **論文全体を読む**：手法と数値だけを抜くのではなく、**背景・動機（なぜ重要か）・実験・結果・考察(discussion)・限界(limitations)** まで踏まえて要約する。著者の論旨・条件・反証を反映する（数値の羅列にしない）。
3. **図を入れる**：HTML から framework/overview 図を取り出し、実画像を保存して引用する。
4. **複数論文で裏付けたファクトを重視**：単一研究に過剰適合しない。1本だけの結果は「**裏付けは弱め・要追試だがインパクト大**」として別建てで明示する。
5. **数字は初見でも凄さが分かる表現に**：基準・倍率・意味を必ず添える。
6. 各月 **3本** を目安に作る（下記の選定基準）。

## 1. 対象カテゴリの選定
- 対象月の `[Mon YYYY]` タグでカテゴリ別の本数を数える：
  ```bash
  for f in $(find capabilities applications architecture operations -name '*.md'); do
    n=$(grep -cE '\[<Mon> <YYYY>\]' "$f"); [ "$n" -gt 0 ] && printf "%3d  %s\n" "$n" "$f"; done | sort -rn
  ```
- **本数が多く（目安 ≥7本）かつコヒーレントな**カテゴリを 3つ選ぶ。分野混在の受け皿（例 `vertical-agents`）は避け、1テーマ1号にする。
- 各カテゴリの対象論文（当月分）の arXiv ID を抽出：
  ```bash
  grep -E '\[<Mon> <YYYY>\]' <path.md> | grep -oE 'arxiv.org/abs/[0-9v.]+' | sed 's#arxiv.org/abs/##'
  ```

## 2. 各論文を HTML 精読
- 各 ID を `WebFetch https://arxiv.org/html/<id>` で取得。プロンプトは手法/結果だけでなく **背景・動機・考察・限界**も求める。例：
  > 「Extract from the full HTML: (1) title, (2) motivation/background — why this problem matters, (3) core method, (4) experimental setup + key quantitative results with numbers and baselines, (5) discussion/limitations. THEN: FIGURE | <caption of main framework figure> | <img src e.g. 2606.xxxxxvN/xxx.png>. If 404 reply only NO HTML.」
- 404 の場合のみ `/abs/` にフォールバック（号内に「abstract のみ」と注記）。

## 3. 図の取得と埋め込み
- 図の **正確な `<img> src`** を得る（版番号 `vN` に注意。`.../assets/xxx.png` のようにサブディレクトリのことがある）。
- 実画像をダウンロードし、**本当に画像か検証**（HTML 404 は 8KB 程度のテキストが返る）：
  ```bash
  curl -sL "https://arxiv.org/html/<id>vN/<fig>.png" -o "newsletters/assets/<id>-<slug>.png"
  file newsletters/assets/<id>-<slug>.png   # → "PNG image data" ならOK。HTMLなら破棄
  ```
- 保存先は `newsletters/assets/`。1号あたり **3〜4点**、代表的な framework/結果図を選ぶ。
- 埋め込み（相対パス）:
  ```markdown
  ![<label>](../assets/<id>-<slug>.png)
  > 図（<Paper>）：<caption>（[論文](https://arxiv.org/abs/<id>)）
  ```

## 4. 構成（ハウススタイル）
```
# <Theme> 研究トレンド（YYYY年M月）

> 対象カテゴリへのリンク・本数・「arXiv HTML 本文を精読」の一言。

## 3行サマリ
- できるだけ各項目を複数論文で裏付ける。

## クロス論文で見るトレンド（継続 / 明確化 / 単発の注目結果）
**継続する傾向（過去号からの延長）** … 複数論文が共有する方向（過去号にリンク）。
**今月明確になった点（複数論文で裏付け）** … 各項目に **裏付けた論文名を2〜4本明記**。
**単発だがインパクトの大きい結果（裏付けは弱め・要追試）** … 1本のみの striking な結果。「1事例／要追試」と明示。

## 数字で見るインパクト
| 論文 | 数字 | 初見の読み方 |
|---|---|---|
| … | 生の数字 | 基準・倍率・意味（例：「ほぼ据え置き＝進化は効いていない」「大型の9割を約1/25コスト」） |

## 論文紹介（サブテーマ別）
### ① …
[Title](https://arxiv.org/abs/<id>)
2〜4文：**背景/なぜ効くか（考察）** ＋ 手法 ＋ 主要結果（数値） ＋ 限界。
![…](../assets/…)  ＋ 図キャプション

## 論点・未解決課題
番号付きで、**各論点に複数論文を引用**。

## 次に来るもの（Watch next）

---
*本ニュースレターは各論文の arXiv HTML 本文を精読（404 は abstract）。図は `newsletters/assets/` に保存。対象＝<category.md> の YYYY年M月。関連号にリンク。*
```

## 5. 数字を「初見で分かる」ように書くコツ
- 必ず **基準（vs baseline / human / legacy）** か **倍率・割合** を添える。
- 「凄い/残念」の含意を言語化：`+0.6pt →「ほぼ据え置き＝過学習の警告」`、`89.7% at 4% cost →「大型の9割を約1/25の値段」`、`Jaccard=0 →「集約を変えるだけで1位が入れ替わる」`。
- 低い絶対値は「なぜ難しい課題か」を補う（例：`脆弱性検出 6.2% →「従来1%が限界の難題を6倍」`）。

## 6. 仕上げ・検証
- 画像参照がすべて実ファイル（有効 PNG/JPEG）か確認：
  ```bash
  for img in $(grep -rhoE '\(\.\./assets/[^)]+\)' newsletters/*/*.md | sed -E 's#\(\.\./assets/##; s#\)##' | sort -u); do
    { [ -f "newsletters/assets/$img" ] && file "newsletters/assets/$img" | grep -q -E 'PNG|JPEG'; } || echo "BAD $img"; done
  ```
- ファイル名：`newsletters/<mon>_<year>/<theme>_trends.md`（例 `jul_2026/harness_trends.md`）。
- 関連号（前月・関連カテゴリ）に相互リンク。
- コミットは説明的メッセージで。**push はユーザーの明示指示があるときだけ**。

## チェックリスト（提出前）
- [ ] 各論文を `/html/` で読んだ（abs のみは 404 時だけ・注記あり）
- [ ] 背景・考察・限界まで反映（method＋数値の抜き書きになっていない）
- [ ] 図 3〜4点、すべて実画像・出典リンク付き
- [ ] 「今月明確化」は各項目 ≥2 論文で裏付け／単発結果は「要追試」と明示
- [ ] 数字テーブルに「初見の読み方」列があり、基準・倍率・意味が分かる
- [ ] 各月おおむね 3 号（高活動＋コヒーレントなカテゴリ）
