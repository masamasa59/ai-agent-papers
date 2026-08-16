#!/usr/bin/env python3
"""Annotate README category links with recent-activity badges.

For every category link in README.md, count how many paper entries carry a
`[Mon YYYY]` tag falling in the **latest two months** present in the repo, and
append ` (+N)` (plus 🔥 when N is high) to that link. Idempotent — re-run any
time (e.g. after the weekly update) to refresh the numbers.

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


def main():
    win = window()
    out = []
    for line in open("README.md").read().split("\n"):
        m = link_re.search(line)
        if m and any(m.group(1).startswith(d) for d in CATDIRS):
            line = badge_re.sub('', line)
            n = count(m.group(1), win)
            if n:
                line += f" (+{n})" + (" 🔥" if n >= HOT else "")
        out.append(line)
    text = "\n".join(out)

    label = f"{MONTHS[win[0][1] - 1]}–{MONTHS[win[1][1] - 1]} {win[1][0]}"
    legend = (f"> \U0001F504 Badges show papers added in the last 2 months "
              f"({label}): `(+N)` recent additions, \U0001F525 = high activity. "
              f"Regenerate: `python scripts/update_readme_badges.py`.\n")
    text = legend_re.sub('', text)
    text = text.replace("> \U0001F4C2 See [**TAXONOMY.md**]",
                        legend + ">\n> \U0001F4C2 See [**TAXONOMY.md**]", 1)
    open("README.md", "w").write(text)
    print(f"window={win}  badged links updated.")


if __name__ == "__main__":
    main()
