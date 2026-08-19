import os
import requests

# Configuración inicial
token = os.getenv('GITHUB_TOKEN')
repo_privado = os.getenv('GITHUB_REPOSITORY') # Detecta el repo automáticamente
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}

# 1. Obtener lenguajes
resp_lang = requests.get(f'https://api.github.com/repos/{repo_privado}/languages', headers=headers)
lenguajes = resp_lang.json() if resp_lang.status_code == 200 else {}
total_bytes = sum(lenguajes.values()) if lenguajes else 1
lang_md = ""

colores = {
    'JavaScript': '🟡', 'Python': '🔵', 'CSS': '🟣', 'HTML': '🟠', 
    'TypeScript': '🟦', 'Ruby': '🔴', 'Dockerfile': '🐳', 'Mako': '🟤',
    'Shell': '🟢', 'Java': '☕', 'C++': '🔵', 'C': '⚫'
}

for lang, bytes_count in lenguajes.items():
    pct = (bytes_count / total_bytes) * 100
    icono = colores.get(lang, '⚪')
    lang_md += f"* {icono} **{lang}:** {pct:.1f}%\n"

# 2. Obtener estadísticas detalladas vía Commits
commits_url = f'https://api.github.com/repos/{repo_privado}/commits?per_page=100'
conteo_autores = {}
total_commits_repo = 0

# Diccionario para formatear los nombres del equipo
nombres_equipo = {
    "LGhosn": "Ghosn, Lautaro Gabriel",
    "axel-zielonka": "Zielonka, Axel",
    "FelipeAscencio": "Ascencio, Felipe Santino",
    "marttinguerrero": "Guerrero, Martín"
}

print(f"🔍 [LOG] Iniciando conteo crudo de commits y líneas sin merges...")

while commits_url:
    resp_commits = requests.get(commits_url, headers=headers)
    if resp_commits.status_code != 200:
        print(f"⚠️ Error obteniendo commits: Status {resp_commits.status_code}")
        break
    
    commits_page = resp_commits.json()
    if not commits_page:
        break
        
    for commit in commits_page:
        
        # 1. FILTRO DE MERGES: Ignorar commits con más de 1 padre
        if len(commit.get('parents', [])) > 1:
            continue
            
        # Identificar al autor
        author = None
        if commit.get('author'):
            author = commit['author']['login']
        else:
            author = commit.get('commit', {}).get('author', {}).get('name', '')
            
        # 2. FILTRO DE BOTS: Omitir si no hay autor, si es un bot o un action
        if not author:
            continue
            
        author_lower = author.lower()
        if 'bot' in author_lower or 'action' in author_lower:
            continue
            
        # Si pasa los filtros, lo sumamos al total real del equipo
        total_commits_repo += 1    
        sha = commit['sha']
        
        # Inicializar al usuario si es su primer commit analizado
        if author not in conteo_autores:
            conteo_autores[author] = {'commits': 0, 'additions': 0, 'deletions': 0}
            
        # Hacemos una petición extra para ver cuántas líneas tocó en este commit individual
        resp_detalle = requests.get(f'https://api.github.com/repos/{repo_privado}/commits/{sha}', headers=headers)
        if resp_detalle.status_code == 200:
            stats = resp_detalle.json().get('stats', {'additions': 0, 'deletions': 0})
            conteo_autores[author]['commits'] += 1
            conteo_autores[author]['additions'] += stats.get('additions', 0)
            conteo_autores[author]['deletions'] += stats.get('deletions', 0)

    # Paginación para seguir buscando si hay más de 100 commits
    link_header = resp_commits.headers.get('Link')
    commits_url = None
    if link_header:
        links = link_header.split(',')
        for link in links:
            if 'rel="next"' in link:
                commits_url = link[link.find('<')+1 : link.find('>')]
                break

print(f"✅ [LOG] Total de commits de los integrantes: {total_commits_repo}")

# Armar la tabla de contribuidores ordenados
contrib_md = ""
if conteo_autores:
    # Ordenar de mayor a menor cantidad de commits
    autores_ordenados = sorted(conteo_autores.items(), key=lambda x: x[1]['commits'], reverse=True)
    
    for user, data in autores_ordenados:
        nombre_completo = nombres_equipo.get(user)
        
        # Si está en nuestro diccionario, le damos el formato profesional
        if nombre_completo:
            display_name = f"**{nombre_completo}** (`{user}`)"
        else:
            display_name = f"**{user}**"
            
        # Formateamos los números grandes con puntos (ej: 5.876)
        add_str = f"{data['additions']:,}".replace(',', '.')
        del_str = f"{data['deletions']:,}".replace(',', '.')
        
        contrib_md += f"| {display_name} | {data['commits']} | {add_str} | {del_str} |\n"
else:
    contrib_md = "| No se encontraron datos de los integrantes | - | - | - |\n"

# 3. Obtener Issues y PRs cerrados
resp_issues = requests.get(f'https://api.github.com/repos/{repo_privado}/issues?state=closed&per_page=100', headers=headers)
issues_data = resp_issues.json() if resp_issues.status_code == 200 else []
prs_cerrados = len([i for i in issues_data if 'pull_request' in i])
issues_cerrados = len(issues_data) - prs_cerrados

# 4. Generar el contenido Markdown final
markdown_content = f"""---
layout: default
title: Métricas de la implementación
nav_order: 99
---

# 📊 Métricas de la implementación (Automáticas)

Este espacio está destinado a medir el trabajo, la participación y el progreso del equipo en el desarrollo de esta documentación. Estos datos se actualizan automáticamente mediante el avance del desarrollo.

## Resumen del repositorio

* **Actividad de commits:** ![Commits](https://img.shields.io/badge/Commits_Totales-{total_commits_repo}-blue)
* **Pull Requests cerrados:** ![PRs](https://img.shields.io/badge/PRs_Cerrados-{prs_cerrados}-purple)
* **Issues resueltos:** ![Issues](https://img.shields.io/badge/Issues_Resueltos-{issues_cerrados}-green)

## Composición del código (Lenguajes)

Basado en el análisis automático del repositorio, la distribución tecnológica es la siguiente:

{lang_md}
## Distribución del trabajo (Contributors)

A continuación se detalla la participación de cada miembro del equipo basándonos en la estadística de "Contributors", la cual contempla tanto la cantidad de commits como el volumen de código impactado:

| Miembro del equipo (GitHub User) | Commits Totales | Líneas Agregadas (++) | Líneas Eliminadas (--) |
| :--- | :---: | :---: | :---: |
{contrib_md}
*(Nota: Cualquier diferencia entre el total de commits del repositorio y la suma de los aportes individuales corresponde a operaciones de mantenimiento automatizado realizadas por herramientas como dependabot).*
"""

# Guardar el archivo generado
with open('metricas_generadas.md', 'w', encoding='utf-8') as f:
    f.write(markdown_content)
print("Archivo metricas_generadas.md creado exitosamente.")
