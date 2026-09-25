from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'notion'
PAGES = [
    (SOURCE / 'Visión desde Cero.md', ROOT / 'index.md', 'Inicio', None, 1, '/'),
    (SOURCE / '01 Matemáticas' / '00 Programa de matemáticas.md', ROOT / 'matematicas' / 'index.md', '01 · Matemáticas', None, 2, '/matematicas/'),
    (SOURCE / '01 Matemáticas' / '01 Números variables y funciones.md', ROOT / 'matematicas' / '01-numeros-variables-y-funciones.md', '01 · Números, variables y funciones', '01 · Matemáticas', 1, '/matematicas/numeros-variables-y-funciones/'),
]

for source, target, title, parent, order, permalink in PAGES:
    content = source.read_text(encoding='utf-8').strip()
    if source.name == 'Visión desde Cero.md':
        content += '\n\n[Comenzar por matemáticas]({{ "/matematicas/" | relative_url }})\n'
    elif source.name == '00 Programa de matemáticas.md':
        content += '\n\n[Ir a la primera clase]({{ "/matematicas/numeros-variables-y-funciones/" | relative_url }})\n'
    front = ['---',f'title: "{title}"',f'layout: {"home" if permalink == "/" else "default"}',f'nav_order: {order}',f'permalink: {permalink}']
    if parent:
        front.append(f'parent: "{parent}"')
    front.extend(['---',''])
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text('\n'.join(front)+content+'\n',encoding='utf-8')
    print(target.relative_to(ROOT))
