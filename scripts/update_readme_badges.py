#!/usr/bin/env python3
"""Annotate the README category index with recent-activity badges.

Every category link gets ` (+N)` = papers added in the last two months
(auto-detected from the `[Mon YYYY]` tags), and 🔥 when N is high. Cluster
headings (and the flat Architecture / Operations layers) get the **sum** of
their children, so you can see at a glance which parts of the field are moving.
Idempotent — re-run after each weekly update.

    python scripts/update_readme_badges.py
"""
import glob
import re

MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
MI = {m: i for i, m in enumerate(MONTHS, 1)}
CATDIRS = ('capabilities/', 'applications/', 'architecture/', 'operations/')
HOT = 10  # 🔥 threshold for the 2-month count

tag = re.compile(r'\[([A-Z][a-z]{2}) (20\d{2})\]')
link_re = re.compile(r'\]\(([^)#]+\.md)([^)]*)\)')
badge_re = re.compile(r' \(\+\d+\)(?: 🔥)?')
legend_re = re.compile(r'^> 🔄 Badges show.*\n', re.MULTILINE)


def category_files():
    fs = set()
    for pat in ("capabilities/**/*.md", "applications/**/*.md",
                "architecture/*.md", "operations/*.md"):
        fs |= set(glob.glob(pat, recursive=True))
    return fs


def window():
    ym = set()
    for f in category_files():
        for m in tag.finditer(open(f).read()):
            ym.add((int(m.group(2)), MI[m.group(1)]))
    return sorted(ym)[-2:]


def count(path, win):
    if not any(path.startswith(d) for d in CATDIRS):
        return None
    try:
        lines = open(path).read().split("\n")
    except FileNotFoundError:
        return None
    n = 0
    for l in lines:
        if l.startswith("* "):
            m = tag.search(l)
            if m and (int(m.group(2)), MI[m.group(1)]) in win:
                n += 1
    return n


def badge(n):
    return f" (+{n})" + (" 🔥" if n >= HOT else "")


def main():
    win = window()
    lines = [badge_re.sub('', l) for l in open("README.md").read().split("\n")]

    # pass 1: leaf counts + roll up into the enclosing cluster / flat layer
    leaf = {}                 # idx -> count
    group_sum = {}            # idx -> subtree sum
    layer_has_direct = {}     # layer idx -> bool
    cur_layer = cur_cluster = None
    for i, l in enumerate(lines):
        s = l.strip()
        m = link_re.search(l)
        if s.startswith("- **"):                       # top-level layer
            cur_layer, cur_cluster = i, None
            group_sum.setdefault(i, 0); layer_has_direct[i] = False
        elif s.startswith("- *"):                      # cluster / axis
            cur_cluster = i; group_sum.setdefault(i, 0)
        elif m and any(m.group(1).startswith(d) for d in CATDIRS):
            n = count(m.group(1), win) or 0
            leaf[i] = n
            if cur_cluster is not None:
                group_sum[cur_cluster] += n
            elif cur_layer is not None:
                group_sum[cur_layer] += n
                if n:
                    layer_has_direct[cur_layer] = True

    # pass 2: annotate
    out = []
    for i, l in enumerate(lines):
        if i in leaf and leaf[i]:
            l += badge(leaf[i])
        elif i in group_sum and group_sum[i]:
            s = l.strip()
            is_cluster = s.startswith("- *") and not s.startswith("- **")
            if is_cluster or layer_has_direct.get(i):   # clusters + flat layers only
                l += badge(group_sum[i])
        out.append(l)
    text = "\n".join(out)

    label = f"{MONTHS[win[0][1] - 1]}–{MONTHS[win[1][1] - 1]} {win[1][0]}"
    legend = (f"> \U0001F504 Badges show papers added in the last 2 months "
              f"({label}); cluster headings show the sum: `(+N)` recent additions, "
              f"\U0001F525 = high activity. Regenerate: "
              f"`python scripts/update_readme_badges.py`.")
    # Idempotently place the legend right above the TAXONOMY pointer, clearing
    # any previous legend / orphaned '>' separator lines above it.
    rows = text.split("\n")
    p = next((i for i, l in enumerate(rows)
              if l.startswith("> \U0001F4C2 See [**TAXONOMY.md**]")), None)
    if p is not None:
        j = p - 1
        while j >= 0 and (rows[j].startswith("> \U0001F504 Badges")
                          or rows[j].strip() == ">"):
            del rows[j]; j -= 1; p -= 1
        rows[p:p] = [legend, ">"]
    open("README.md", "w").write("\n".join(rows))
    print(f"window={win}  leaves + cluster totals updated.")


if __name__ == "__main__":
    main()
