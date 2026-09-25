# Visión desde Cero

Curso abierto de matemáticas, machine learning y deep learning orientado a visión por computadora.

## Publicación

Los Markdown de clase se guardan en `notion/`. `course_pages.json` registra las páginas del curso y sus rutas. `python3 scripts/build_pages.py` genera páginas de Just the Docs. El flujo `.github/workflows/pages.yml` compila con Jekyll y publica en GitHub Pages.

## Sincronización automática desde Notion

El flujo puede revisar Notion a los minutos 17 y 47 de cada hora. Consulta **solo los cinco IDs de matemáticas registrados** en `course_pages.json`, guarda las versiones Markdown, genera el sitio y hace commit si hubo cambios. El mismo flujo publica la versión nueva en GitHub Pages. También puedes iniciarlo manualmente desde Actions.

Para activarlo:

1. En Notion, abre **Configuración → Conexiones** y sigue la [guía oficial para crear una conexión interna](https://www.notion.com/es/help/create-integrations-with-the-notion-api). Llámala, por ejemplo, `Visión desde Cero · publicación` y dale solo la capacidad **Read content**.
2. En Notion, abre `Visión desde Cero → 01 Matemáticas`, usa `••• → Connections → Add connection` y comparte **solo esa página y sus hijas** con la conexión. No hace falta compartir la página general ni el curso de Álgebra Lineal.
3. En GitHub, abre `wowito68/vision-desde-cero → Settings → Secrets and variables → Actions` y crea un secreto de repositorio llamado `NOTION_TOKEN` con el token de instalación. No pongas el token en un archivo, commit, URL ni mensaje.
4. Comprueba una primera ejecución manual del flujo **Deploy Jekyll site to Pages** y revisa el commit de sincronización. Después crea la variable de repositorio `NOTION_SYNC_ENABLED` con valor `true` para habilitar la ejecución periódica.

Hasta que exista esa variable, las ejecuciones programadas se omiten y los push normales siguen publicando el sitio. La conexión da acceso de lectura a `01 Matemáticas` y sus páginas hijas; solo los IDs enumerados en el manifiesto se copian al sitio. Para publicar una clase nueva, añade su página a `course_pages.json`.

El sincronizador detiene la publicación si Notion devuelve contenido incompleto o medios que necesitan un tratamiento especial. Por ahora soporta los textos, listas, enlaces, tablas y código usados en las clases 01–04. Las imágenes cargadas en Notion necesitan descargarse como archivos permanentes antes de publicarlas; el sincronizador las rechaza para evitar enlaces temporales rotos.

Editar una de las páginas registradas en Notion implica publicar ese contenido en el sitio público en la siguiente revisión. Conserva en ellas solo material destinado a publicarse.

## Desarrollo local

- `python3 -m unittest discover -s tests`
- `python3 scripts/build_pages.py`
- `bundle install && bundle exec jekyll serve`

El token de Notion nunca es necesario para compilar el sitio desde los Markdown ya guardados.
