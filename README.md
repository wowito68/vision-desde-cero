# Visión desde Cero

Curso abierto de matemáticas, machine learning y deep learning orientado a visión por computadora. La primera clase muestra cómo convertir una operación matemática en una transformación de píxeles.

## Fuentes y publicación

Los Markdown limpios para Notion están en `notion/`. `python3 scripts/build_pages.py` genera las páginas Jekyll con metadatos de navegación. El sitio usa Just the Docs y el flujo oficial de GitHub Pages mediante Actions. Después de editar una clase en Notion, exportaremos el módulo a Markdown y revisaremos ecuaciones, imágenes y enlaces antes de regenerar el sitio. La sincronización automática se añadirá una vez validado el primer ciclo de exportación real.

Para ejecutar localmente, instala Bundler y usa `bundle install` y `bundle exec jekyll serve`.
