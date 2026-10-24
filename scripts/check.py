"""Pre-ship checks for the static manifesto page: balanced HTML, every local asset exists,
no em dashes or prose colons in visible Hebrew text."""
import html.parser, pathlib, re, sys

root = pathlib.Path(__file__).resolve().parent.parent
src = (root / "index.html").read_text(encoding="utf-8")
errors = []

class Balance(html.parser.HTMLParser):
    VOID = {"meta", "link", "img", "br", "input", "source", "circle", "hr"}
    def __init__(self):
        super().__init__(); self.stack = []
    def handle_starttag(self, tag, attrs):
        if tag not in self.VOID: self.stack.append(tag)
    def handle_endtag(self, tag):
        if tag in self.VOID: return
        if self.stack and self.stack[-1] == tag: self.stack.pop()
        else: errors.append(f"unbalanced </{tag}> at line {self.getpos()[0]}")

b = Balance(); b.feed(src)
if b.stack: errors.append(f"unclosed tags: {b.stack[-5:]}")

for ref in re.findall(r'(?:src|href)="(assets/[^"]+)"', src):
    if not (root / ref).exists(): errors.append(f"missing asset {ref}")

body = src[src.index("<body>"):]
body = re.sub(r"<script.*?</script>", "", body, flags=re.S)
text = re.sub(r"<[^>]+>", "\n", body)
for line in text.splitlines():
    if re.search(r"[א-ת]", line) and re.search(r"[—–]|[א-ת]\s*:\s", line):
        errors.append(f"banned punctuation: {line.strip()[:60]}")

if errors:
    print("\n".join(errors)); sys.exit(1)
print("index.html ok")
