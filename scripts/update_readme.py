#!/usr/bin/env python3
"""Refresh the 'Recently shipped' block of README.md. Stdlib only."""
import json
import os
import re
import sys
import urllib.request

USER = "googlarz"
LIMIT = 6
START, END = "<!-- RECENT:START -->", "<!-- RECENT:END -->"
README = sys.argv[1] if len(sys.argv) > 1 else "README.md"


def api(path):
    req = urllib.request.Request(
        f"https://api.github.com{path}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": f"{USER}-readme-updater",
            "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def oneline(text):
    text = " ".join((text or "").split())
    return text if len(text) <= 100 else text[:97].rstrip() + "..."


def collect():
    repos = api(f"/users/{USER}/repos?type=owner&sort=pushed&per_page=100")
    repos = [r for r in repos if not r["fork"] and not r["archived"] and r["name"] != USER]
    items = []
    for r in repos:
        rels = api(f"/repos/{USER}/{r['name']}/releases?per_page=5")
        rel = next((x for x in rels if not x["draft"] and not x["prerelease"]), None)
        if rel:
            items.append((rel["published_at"], f"{r['name']} {rel['tag_name']}",
                          rel["html_url"], r["description"]))
    items.sort(reverse=True)
    items = items[:LIMIT]
    if len(items) < LIMIT:  # fall back to recently pushed repos with a description
        seen = {i[1].split()[0] for i in items}
        for r in repos:
            if len(items) >= LIMIT:
                break
            if r["name"] not in seen and r["description"]:
                items.append((r["pushed_at"], r["name"], r["html_url"], r["description"]))
    return items


def render(items):
    return "\n".join(
        f"- [{name}]({url}) — {oneline(desc) or 'No description'} · {ts[:10]}"
        for ts, name, url, desc in items
    )


def main():
    with open(README, encoding="utf-8") as f:
        text = f.read()
    pat = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if not pat.search(text):
        sys.exit(f"markers not found in {README}")
    block = f"{START}\n{render(collect())}\n{END}"
    new = pat.sub(lambda _: block, text, count=1)
    if new != text:
        with open(README, "w", encoding="utf-8") as f:
            f.write(new)
        print("README updated")
    else:
        print("README unchanged")


if __name__ == "__main__":
    main()
