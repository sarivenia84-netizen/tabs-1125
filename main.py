from pathlib import Path

# 404 tabs: closure not found.
Path('/output').mkdir(parents=True,exist_ok=True)
Path('/output/entry.txt').write_text('404',encoding='utf-8')
