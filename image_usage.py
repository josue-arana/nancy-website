import pathlib
import re
root = pathlib.Path('.')
all_imgs = sorted(str(p) for p in root.glob('images/**') if p.is_file())
used = set()
pattern = re.compile(r'images/[^\)"\'\"]+')
for p in root.rglob('*'):
    if p.is_file() and p.suffix.lower() in {'.html', '.css', '.js'}:
        text = p.read_text(encoding='utf-8', errors='ignore')
        used |= set(pattern.findall(text))
print('ALL:', len(all_imgs))
print('USED:', len(used))
unused = [p for p in all_imgs if p not in used]
print('DIFF:', len(unused))
for p in unused:
    print(p)
