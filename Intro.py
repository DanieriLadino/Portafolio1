import base64
import json
import mimetypes
import os

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Mis Apps de IA", page_icon="🤖", layout="wide")

# =================================================================
# DATOS QUE PUEDES EDITAR
# =================================================================
NOMBRE = "Tu nombre"          # aparece en la barra inferior
CURSO = "Interfaces Multimodales"
ANIO = "2026"
ALTO = 1150                   # alto de la página en píxeles (súbelo si se corta algo)

# Para agregar una clase, copia un bloque {...}.
# Para agregar una app, copia un bloque dentro de "apps".
# "portada" es opcional: nombre de un archivo de imagen en la carpeta
# del proyecto (ej. "clase6.png"). Si es None se muestra el ícono.
# Íconos vectoriales disponibles para "icono":
#   "web", "voz", "texto", "vision", "robot", "datos", "imagen"
CLASES = [
    {
        "numero": "06",
        "fecha": "20 de agosto",
        "corto": "Interfaces multimodales",
        "titulo": "Desarrollo de aplicaciones web para interfaces multimodales",
        "icono": "web",
        "color": "#ffcc33",
        "portada": None,
        "apps": [
            {
                "nombre": "Mi primera app",
                "descripcion": "Primera aplicación web construida con Streamlit.",
                "url": "https://miprimeraapp-3zbnl3hyzf5nuejslpyaxj.streamlit.app/",
            },
            {
                "nombre": "Mi segunda app",
                "descripcion": "Segunda aplicación web con más componentes de interfaz.",
                "url": "https://misegundaapp-oyj7hracz5tumqn8xjvzv2.streamlit.app/",
            },
        ],
    },
    {
        "numero": "07",
        "fecha": "27 de agosto",
        "corto": "Voz a texto",
        "titulo": "Interfaces de voz a texto",
        "icono": "voz",
        "color": "#ff8fc4",
        "portada": None,
        "apps": [
            {
                "nombre": "Voz a texto",
                "descripcion": "Aplicación que convierte la voz en texto.",
                "url": "https://cerrdmufkzjtk7akp8kier.streamlit.app/",
            },
            {
                "nombre": "Traductor",
                "descripcion": "Traductor por voz entre distintos idiomas.",
                "url": "https://traductorr-pmv9hkocmacdasgycsmxtr.streamlit.app/",
            },
            {
                "nombre": "OCR a audio",
                "descripcion": "Extrae el texto de una imagen y lo convierte en audio.",
                "url": "https://ocr-audio-nwetgmm3c4vjgoxkppazvv.streamlit.app/",
            },
        ],
    },
    {
        "numero": "08",
        "fecha": "3 de septiembre",
        "corto": "Lenguaje natural",
        "titulo": "Procesamiento de lenguaje natural",
        "icono": "texto",
        "color": "#7fd1ff",
        "portada": None,
        "apps": [
            {
                "nombre": "Nube de palabras",
                "descripcion": "Genera una nube de palabras a partir de un texto.",
                "url": "https://wordcloud-elrhhykjwcnirxse5g8uj6.streamlit.app/",
            },
            {
                "nombre": "Análisis de sentimientos",
                "descripcion": "Identifica si un texto es positivo, negativo o neutral.",
                "url": "https://sentimenta-bgo4bcp8xljfl5c7ofkz45.streamlit.app/",
            },
            {
                "nombre": "Procesamiento de texto",
                "descripcion": "Aplicación de procesamiento de lenguaje natural.",
                "url": "https://n6enzi7qpshnuye4fjwjea.streamlit.app/",
            },
            {
                "nombre": "TF-IDF en español",
                "descripcion": "Calcula la relevancia de las palabras en documentos en español.",
                "url": "https://tdfesp-9gb836dqji4orzbduzhusc.streamlit.app/",
            },
        ],
    },
    {
        "numero": "09",
        "fecha": "17 de septiembre",
        "corto": "Visión artificial",
        "titulo": "Aplicaciones con visión artificial",
        "icono": "vision",
        "color": "#9be37a",
        "portada": None,
        "apps": [
            {
                "nombre": "Detección de objetos (YOLOv5)",
                "descripcion": "Detecta y clasifica objetos en imágenes con YOLOv5.",
                "url": "https://yolov55-hx8qnmcfsbn8m3rslsxert.streamlit.app/",
            },
            {
                "nombre": "Visión artificial",
                "descripcion": "Aplicación de análisis de imágenes con visión artificial.",
                "url": "https://its4jfemoz2ua72kzqwcen.streamlit.app/",
            },
        ],
    },
]

# =================================================================
# A PARTIR DE AQUÍ NO NECESITAS CAMBIAR NADA
# =================================================================


def imagen_a_data_uri(ruta):
    """Convierte una imagen local en texto para poder mostrarla en el HTML."""
    if not ruta or not os.path.exists(ruta):
        return None
    tipo = mimetypes.guess_type(ruta)[0] or "image/png"
    with open(ruta, "rb") as f:
        return f"data:{tipo};base64,{base64.b64encode(f.read()).decode()}"


clases_html = []
for c in CLASES:
    copia = dict(c)
    copia["portada"] = imagen_a_data_uri(c.get("portada"))
    clases_html.append(copia)

datos = {
    "info": {"nombre": NOMBRE, "curso": CURSO, "anio": ANIO},
    "clases": clases_html,
}
datos_json = json.dumps(datos, ensure_ascii=False).replace("</", "<\\/")

# Quita los márgenes y la barra superior de Streamlit
st.markdown(
    """
    <style>
      header[data-testid="stHeader"], footer, #MainMenu {display: none;}
      .stApp, [data-testid="stAppViewContainer"] {background: #9b6a43;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      iframe {display: block;}
    </style>
    """,
    unsafe_allow_html=True,
)

HTML = r"""
<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="https://fonts.googleapis.com/css2?family=Silkscreen:wght@400;700&family=Nunito:wght@400;600;800;900&display=swap" rel="stylesheet">
<style>
:root{
  --blue:#2f6bea; --blue-d:#1e4fc2; --navy:#1b2f6b; --ink:#21408f;
  --paper:#fbfaf5; --line:#e3e9f4; --pink:#ff5fa8; --yellow:#ffcc33;
}
*{box-sizing:border-box}
html,body{margin:0;height:100%}
body{font-family:'Nunito',sans-serif;color:var(--navy);
  background:repeating-linear-gradient(100deg,#a8744a 0 18px,#9a6840 18px 30px,#b07d52 30px 46px);
  padding:12px}
.pixel{font-family:'Silkscreen',monospace}

/* ---------- tablero azul ---------- */
.board{position:relative;border-radius:16px;overflow:hidden;padding:34px 26px 18px;
  background-color:var(--blue);
  background-image:linear-gradient(rgba(255,255,255,.17) 1px,transparent 1px),
                   linear-gradient(90deg,rgba(255,255,255,.17) 1px,transparent 1px);
  background-size:32px 32px;
  box-shadow:inset 0 0 0 3px rgba(255,255,255,.08),inset 0 0 60px rgba(10,25,80,.35)}

/* ---------- papel ---------- */
.paper{position:relative;background-color:var(--paper);
  background-image:linear-gradient(var(--line) 1px,transparent 1px),
                   linear-gradient(90deg,var(--line) 1px,transparent 1px);
  background-size:18px 18px;border-radius:6px;
  box-shadow:0 6px 0 rgba(0,0,0,.06),0 18px 30px rgba(10,30,90,.35)}
.holes::before{content:"";position:absolute;left:18px;right:18px;top:10px;height:12px;
  background:radial-gradient(circle at 6px 6px,var(--blue-d) 4.5px,transparent 5px) 0 0/26px 12px repeat-x;
  opacity:.9}
.torn::after{content:"";position:absolute;left:0;right:0;bottom:-9px;height:10px;
  background:linear-gradient(135deg,var(--paper) 5px,transparent 0) 0 0/10px 10px,
             linear-gradient(225deg,var(--paper) 5px,transparent 0) 0 0/10px 10px}

/* ---------- clip rosado ---------- */
.clip{position:absolute;top:-15px;left:50%;transform:translateX(-50%);width:44px;height:24px;z-index:3;
  background:var(--pink);border-radius:5px 5px 3px 3px;box-shadow:inset 0 -6px 0 rgba(0,0,0,.14)}
.clip::before{content:"";position:absolute;left:8px;right:8px;top:-15px;height:17px;
  border:3px solid #5b6474;border-bottom:0;border-radius:9px 9px 0 0}

/* ---------- portada ---------- */
.hero{display:grid;grid-template-columns:1.5fr 1fr;gap:26px;padding:44px 40px 36px;transform:rotate(-.6deg)}
.kicker{font-family:'Silkscreen',monospace;font-size:12px;letter-spacing:2px;color:var(--ink);opacity:.7}
.selbox{position:relative;display:inline-block;margin:18px 0 10px;padding:12px 26px 10px;
  border:1.5px solid #8fb1f5}
.selbox i{position:absolute;width:9px;height:9px;background:#fff;border:1.5px solid #8fb1f5}
.selbox i:nth-child(1){left:-5px;top:-5px}.selbox i:nth-child(2){right:-5px;top:-5px}
.selbox i:nth-child(3){left:-5px;bottom:-5px}.selbox i:nth-child(4){right:-5px;bottom:-5px}
.title{margin:0;font-family:'Silkscreen',monospace;font-weight:700;line-height:.92;
  font-size:clamp(46px,8.5vw,104px);color:var(--blue);letter-spacing:2px;
  text-shadow:3px 3px 0 #fff,6px 6px 0 #a9c4ff}
.title span{display:block}
.title span:nth-child(2){padding-left:.6em}
.side{position:absolute;right:-74px;top:4px;font-family:'Silkscreen',monospace;font-weight:700;
  color:var(--pink);font-size:22px;line-height:1.05;transform:rotate(6deg);text-shadow:2px 2px 0 #fff}
.year{position:absolute;left:-30px;bottom:-24px;font-family:'Silkscreen',monospace;font-weight:700;font-size:24px;
  color:#fff;-webkit-text-stroke:1.5px var(--pink);text-shadow:3px 3px 0 var(--pink);transform:rotate(-14deg)}
.cursor{position:absolute;right:-36px;bottom:-40px;width:42px;filter:drop-shadow(2px 3px 0 rgba(0,0,0,.15))}
.topics{list-style:none;padding:0;margin:34px 0 0;display:grid;grid-template-columns:1fr 1fr;gap:4px 18px;
  font-size:13px;font-weight:700;color:var(--ink)}
.topics li::before{content:"";display:inline-block;width:8px;height:8px;background:var(--blue);margin-right:8px}

.note-card{align-self:center;position:relative;background:#fff;border-radius:6px;padding:28px 22px 22px;
  transform:rotate(3deg);box-shadow:0 12px 24px rgba(10,30,90,.25);border:2px solid #f2e3b3}
.note-card::before{content:"";position:absolute;top:-12px;left:50%;transform:translateX(-50%);
  width:64px;height:20px;background:#ffb02e;border-radius:4px;box-shadow:inset 0 -5px 0 rgba(0,0,0,.12)}
.note-card h4{margin:0 0 8px;font-family:'Silkscreen',monospace;color:var(--pink);font-size:15px}
.note-card p{margin:0;font-size:14px;line-height:1.5;color:#33415c}
.note-card .lines{margin-top:12px;height:28px;background:repeating-linear-gradient(transparent 0 13px,#e5e7eb 13px 14px)}

.folder{position:absolute;width:110px;left:-38px;top:-34px;transform:rotate(-14deg);
  filter:drop-shadow(0 8px 10px rgba(0,0,0,.25))}
.pencil{position:absolute;left:30px;bottom:-24px;width:150px;height:16px;transform:rotate(-24deg);
  background:linear-gradient(90deg,#ff9fc9 0 11%,#cbd5e1 11% 17%,#ffcc33 17% 86%,transparent 86%);border-radius:4px 0 0 4px}
.pencil::after{content:"";position:absolute;right:0;top:0;border-left:22px solid #f3d9a8;
  border-top:8px solid transparent;border-bottom:8px solid transparent}
.star{display:inline-block;width:1em;height:1em;vertical-align:-.1em}
.spark{position:absolute;font-size:24px;color:var(--pink);line-height:0}
.spark.b{color:var(--blue)}

/* ---------- clases ---------- */
.contents{position:relative;margin-top:46px}
.head{display:flex;align-items:center;gap:14px;flex-wrap:wrap}
.outline{margin:0;font-family:'Silkscreen',monospace;font-weight:700;font-size:30px;color:#fff;letter-spacing:1px;
  text-shadow:-2px -2px 0 var(--navy),2px -2px 0 var(--navy),-2px 2px 0 var(--navy),2px 2px 0 var(--navy),4px 4px 0 var(--navy)}
.arrows{font-family:'Silkscreen',monospace;font-weight:700;color:#fff;letter-spacing:-2px;font-size:22px;
  text-shadow:2px 2px 0 var(--navy)}
.hint{color:#dbe7ff;font-weight:700;font-size:13px}
.nav{margin-left:auto;display:flex;gap:10px}
.nav button,.mnav button{font-family:'Silkscreen',monospace;font-weight:700;cursor:pointer;border:3px solid var(--navy);
  background:var(--yellow);color:var(--navy);border-radius:6px;box-shadow:3px 3px 0 var(--navy);
  transition:transform .1s,box-shadow .1s}
.nav button{width:44px;height:40px;font-size:16px}
.nav button:active,.mnav button:active{transform:translate(3px,3px);box-shadow:0 0 0 var(--navy)}

.track{display:flex;gap:30px;overflow-x:auto;scroll-snap-type:x mandatory;
  padding:44px 14px 34px;margin:0 -12px;cursor:grab;user-select:none;scrollbar-color:var(--yellow) rgba(255,255,255,.15)}
.track.dragging{cursor:grabbing;scroll-snap-type:none}
.track.dragging .card{pointer-events:none}
.track::-webkit-scrollbar{height:12px}
.track::-webkit-scrollbar-track{background:rgba(255,255,255,.15);border-radius:10px}
.track::-webkit-scrollbar-thumb{background:var(--yellow);border-radius:10px;border:2px solid var(--navy)}

.card{flex:0 0 270px;scroll-snap-align:center;padding:36px 18px 18px;cursor:pointer;outline:none;
  transition:transform .2s ease,box-shadow .2s ease}
.card:nth-child(odd){transform:rotate(-2.2deg)}
.card:nth-child(even){transform:rotate(1.8deg) translateY(14px)}
.card:hover,.card:focus-visible{transform:rotate(0) translateY(-10px);box-shadow:0 26px 36px rgba(10,30,90,.45)}
.thumb{position:relative;height:140px;border-radius:6px;border:3px solid var(--navy);overflow:hidden;
  display:grid;place-items:center;background-color:var(--c);
  background-image:radial-gradient(rgba(255,255,255,.55) 18%,transparent 19%);background-size:16px 16px}
.thumb img{width:100%;height:100%;object-fit:cover}
.thumb .icon{width:116px;height:96px;margin-bottom:12px;filter:drop-shadow(4px 4px 0 rgba(27,47,107,.22))}
.thumb .stamp{position:absolute;left:8px;bottom:8px;background:#fff;border:2px solid var(--navy);
  border-radius:4px;padding:2px 7px;font-size:11px;font-weight:700}
.row{display:flex;justify-content:space-between;align-items:baseline;margin-top:14px}
.num{font-size:26px;font-weight:700;color:var(--blue)}
.date{font-size:12px;font-weight:800;color:var(--pink)}
.card h3{margin:4px 0 2px;font-size:20px;font-weight:900;color:var(--navy)}
.card .sub{margin:0;font-size:13px;color:#5b6b8c;min-height:36px}
.more{display:flex;justify-content:space-between;align-items:center;margin-top:14px;padding-top:10px;
  border-top:2px dashed #c9d6ef;font-size:13px;font-weight:800;color:var(--ink)}
.open{background:var(--blue);color:#fff;padding:4px 10px;border-radius:20px}

/* ---------- barra inferior ---------- */
.bar{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-top:6px;padding:10px 16px;
  background:rgba(20,32,80,.85);border-radius:30px}
.bar .me{color:#fff;font-weight:900;margin-right:6px}
.pill{border:1.5px solid rgba(255,255,255,.5);color:#dbe7ff;border-radius:20px;padding:3px 14px;
  font-size:12px;font-weight:700}

/* ---------- ventana de la clase ---------- */
.overlay{position:fixed;inset:0;z-index:50;display:none;justify-content:center;align-items:flex-start;
  padding:0 16px;background:rgba(12,22,60,.55);backdrop-filter:blur(3px)}
.overlay.show{display:flex}
.sheet{width:min(860px,100%);overflow:auto;padding:46px 30px 26px;animation:pop .25s ease}
@keyframes pop{from{transform:translateY(20px) rotate(-1deg);opacity:0}to{transform:none;opacity:1}}
.close{position:absolute;top:14px;right:14px;width:38px;height:38px;border-radius:50%;border:3px solid var(--navy);
  background:var(--pink);color:#fff;font-weight:900;font-size:16px;cursor:pointer;box-shadow:2px 2px 0 var(--navy)}
.mk{font-family:'Silkscreen',monospace;font-weight:700;color:var(--pink);font-size:14px;letter-spacing:1px}
.sheet h2{margin:6px 0 22px;font-size:clamp(20px,3vw,28px);font-weight:900;color:var(--navy);padding-right:40px}
.apps{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:24px}
.note{position:relative;padding:24px 16px 16px;border-radius:4px;box-shadow:0 8px 16px rgba(10,30,90,.18);
  display:flex;flex-direction:column}
.note.n0{background:#fff3b0;transform:rotate(-1.5deg)}
.note.n1{background:#ffd9ec;transform:rotate(1.2deg)}
.note.n2{background:#d8e7ff;transform:rotate(-.8deg)}
.tape{position:absolute;top:-10px;left:50%;width:70px;height:20px;transform:translateX(-50%) rotate(-3deg);
  background:rgba(255,255,255,.65);border:1px dashed rgba(0,0,0,.12)}
.note h4{margin:0 0 6px;font-size:17px;font-weight:900;color:var(--navy)}
.note p{margin:0 0 14px;font-size:13.5px;line-height:1.45;color:#3d4a66;flex:1}
.btn{align-self:flex-start;text-decoration:none;font-weight:900;font-size:13px;color:#fff;background:var(--blue);
  border:2.5px solid var(--navy);border-radius:6px;padding:6px 12px;box-shadow:3px 3px 0 var(--navy)}
.btn:hover{background:var(--blue-d)}
.mnav{display:flex;justify-content:space-between;margin-top:26px}
.mnav button{padding:8px 14px;font-size:12px}
.mnav button:disabled{opacity:.35;cursor:default;box-shadow:none}

@media (max-width:760px){
  body{padding:8px}
  .board{padding:26px 14px 14px}
  .hero{grid-template-columns:1fr;padding:40px 22px 30px}
  .side{right:-20px;top:-26px;font-size:16px}
  .cursor{display:none}
  .topics{grid-template-columns:1fr}
  .folder{width:80px;left:-20px;top:-26px}
  .card{flex-basis:230px}
  .hint{display:none}
}
</style>
</head>
<body>
<div class="board">

  <span class="spark" style="left:3%;top:2%"><svg class="star" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 0c1 7 5 11 12 12-7 1-11 5-12 12-1-7-5-11-12-12 7-1 11-5 12-12z" fill="currentColor"/></svg></span>
  <span class="spark b" style="right:5%;top:3%"><svg class="star" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 0c1 7 5 11 12 12-7 1-11 5-12 12-1-7-5-11-12-12 7-1 11-5 12-12z" fill="currentColor"/></svg></span>

  <!-- PORTADA -->
  <section class="hero paper holes torn">
    <span class="clip" style="left:auto;right:12%;transform:none"></span>
    <svg class="folder" viewBox="0 0 120 96" aria-hidden="true">
      <path d="M8 18a8 8 0 0 1 8-8h28l10 10h50a8 8 0 0 1 8 8v52a8 8 0 0 1-8 8H16a8 8 0 0 1-8-8z" fill="#e9a812"/>
      <rect x="18" y="20" width="80" height="50" rx="4" fill="#fff"/>
      <rect x="26" y="14" width="74" height="50" rx="4" fill="#5b8def"/>
      <path d="M4 38a8 8 0 0 1 8-8h96a8 8 0 0 1 8 8l-4 42a8 8 0 0 1-8 8H16a8 8 0 0 1-8-8z" fill="#ffcc33"/>
      <rect x="74" y="52" width="24" height="12" rx="3" fill="#fff" opacity=".75"/>
    </svg>
    <div>
      <div class="kicker">PORTAFOLIO · <span id="curso"></span></div>
      <div class="selbox">
        <i></i><i></i><i></i><i></i>
        <h1 class="title"><span>MIS</span><span>APPS</span></h1>
        <div class="side">de IA<br><svg class="star" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 0c1 7 5 11 12 12-7 1-11 5-12 12-1-7-5-11-12-12 7-1 11-5 12-12z" fill="currentColor"/></svg></div>
        <div class="year" id="anio"></div>
        <svg class="cursor" viewBox="0 0 40 48" aria-hidden="true">
          <path d="M4 3l30 22-13 2 8 15-7 3-8-15-10 9z" fill="#ffcc33" stroke="#1b2f6b" stroke-width="2.5" stroke-linejoin="round"/>
        </svg>
      </div>
      <ul class="topics" id="topics"></ul>
    </div>
    <div class="note-card">
      <h4>SOBRE ESTA PÁGINA</h4>
      <p>La inteligencia artificial permite mejorar la toma de decisiones con datos, automatizar
         tareas rutinarias y hacer análisis avanzados en tiempo real. Aquí están las aplicaciones
         que construí en cada clase.</p>
      <div class="lines"></div>
    </div>
    <div class="pencil"></div>
  </section>

  <!-- CLASES -->
  <section class="contents" id="contents">
    <div class="head">
      <h2 class="outline">CLASES</h2>
      <span class="arrows">▶▶▶▶</span>
      <span class="hint">Desliza hacia los lados y haz clic en una clase</span>
      <div class="nav">
        <button id="prev" aria-label="Anterior">◀</button>
        <button id="next" aria-label="Siguiente">▶</button>
      </div>
    </div>
    <div class="track" id="track"></div>
  </section>

  <footer class="bar" id="bar"></footer>
</div>

<!-- VENTANA DE CADA CLASE -->
<div class="overlay" id="overlay">
  <div class="sheet paper holes" id="sheet" role="dialog" aria-modal="true">
    <span class="clip"></span>
    <button class="close" id="close" aria-label="Cerrar">✕</button>
    <div class="mk" id="mk"></div>
    <h2 id="mtitle"></h2>
    <div class="apps" id="apps"></div>
    <div class="mnav">
      <button id="mprev">◀ Anterior</button>
      <button id="mnext">Siguiente ▶</button>
    </div>
  </div>
</div>

<script>
const DATA = __DATA__;
const clases = DATA.clases, info = DATA.info;
const $ = id => document.getElementById(id);
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));


// Íconos vectoriales (mismo estilo: contorno azul marino y colores planos)
const N = '#1b2f6b', B = '#2f6bea', P = '#ff5fa8', Y = '#ffcc33', W = '#fff';
const svg = body => `<svg class="icon" viewBox="0 0 120 100" fill="none" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${body}</svg>`;
const ICONOS = {
  web: svg(`
    <rect x="12" y="12" width="96" height="76" rx="9" fill="${W}" stroke="${N}" stroke-width="4"/>
    <path d="M12 31h96" stroke="${N}" stroke-width="4"/>
    <circle cx="25" cy="21.5" r="3.6" fill="${P}"/><circle cx="36" cy="21.5" r="3.6" fill="${Y}"/><circle cx="47" cy="21.5" r="3.6" fill="${B}"/>
    <path d="M45 48 33 59l12 11M75 48l12 11-12 11" stroke="${B}" stroke-width="5"/>
    <path d="M66 44 54 74" stroke="${P}" stroke-width="5"/>`),
  voz: svg(`
    <path d="M18 38v20M8 44v8M102 38v20M112 44v8" stroke="${W}" stroke-width="5"/>
    <path d="M34 46a26 26 0 0 0 52 0" stroke="${N}" stroke-width="4"/>
    <path d="M60 72v12M46 88h28" stroke="${N}" stroke-width="4"/>
    <rect x="45" y="8" width="30" height="52" rx="15" fill="${W}" stroke="${N}" stroke-width="4"/>
    <path d="M53 24h14M53 34h14M53 44h14" stroke="${B}" stroke-width="3.5"/>`),
  texto: svg(`
    <path d="M16 12h58a9 9 0 0 1 9 9v28a9 9 0 0 1-9 9H38L24 70V58h-8a9 9 0 0 1-9-9V21a9 9 0 0 1 9-9z" fill="${W}" stroke="${N}" stroke-width="4"/>
    <path d="M20 27h46M20 41h30" stroke="${B}" stroke-width="4.5"/>
    <path d="M58 46h46a9 9 0 0 1 9 9v20a9 9 0 0 1-9 9h-2v11L90 84H58a9 9 0 0 1-9-9V55a9 9 0 0 1 9-9z" fill="${P}" stroke="${N}" stroke-width="4"/>
    <circle cx="69" cy="65" r="3.8" fill="${W}"/><circle cx="81" cy="65" r="3.8" fill="${W}"/><circle cx="93" cy="65" r="3.8" fill="${W}"/>`),
  vision: svg(`
    <path d="M8 26V10h16M96 10h16v16M112 74v16H96M24 90H8V74" stroke="${N}" stroke-width="5"/>
    <path d="M18 50c12-19 27-29 42-29s30 10 42 29c-12 19-27 29-42 29S30 69 18 50z" fill="${W}" stroke="${N}" stroke-width="4"/>
    <circle cx="60" cy="50" r="17" fill="${B}" stroke="${N}" stroke-width="4"/>
    <circle cx="60" cy="50" r="7" fill="${N}"/><circle cx="66.5" cy="43.5" r="3.6" fill="${W}"/>`),
  robot: svg(`
    <path d="M60 8v12" stroke="${N}" stroke-width="4"/><circle cx="60" cy="8" r="5" fill="${P}" stroke="${N}" stroke-width="3"/>
    <path d="M18 40v18M102 40v18" stroke="${N}" stroke-width="6"/>
    <rect x="26" y="20" width="68" height="54" rx="13" fill="${W}" stroke="${N}" stroke-width="4"/>
    <circle cx="46" cy="44" r="7.5" fill="${B}"/><circle cx="74" cy="44" r="7.5" fill="${B}"/>
    <path d="M48 61h24" stroke="${N}" stroke-width="4"/>
    <rect x="42" y="78" width="36" height="14" rx="4" fill="${P}" stroke="${N}" stroke-width="4"/>`),
  datos: svg(`
    <rect x="12" y="10" width="96" height="80" rx="9" fill="${W}" stroke="${N}" stroke-width="4"/>
    <rect x="26" y="52" width="16" height="24" rx="2" fill="${B}" stroke="${N}" stroke-width="3"/>
    <rect x="52" y="36" width="16" height="40" rx="2" fill="${P}" stroke="${N}" stroke-width="3"/>
    <rect x="78" y="24" width="16" height="52" rx="2" fill="${Y}" stroke="${N}" stroke-width="3"/>
    <path d="M24 82h72" stroke="${N}" stroke-width="3"/>`),
  imagen: svg(`
    <rect x="12" y="12" width="96" height="76" rx="9" fill="${W}" stroke="${N}" stroke-width="4"/>
    <circle cx="40" cy="36" r="9" fill="${Y}" stroke="${N}" stroke-width="3.5"/>
    <path d="M14 78l28-26 18 16 16-14 30 26" fill="${B}" stroke="${N}" stroke-width="4"/>`),
};
const icono = nombre => ICONOS[nombre] || ICONOS.robot;

// Portada
$('curso').textContent = info.curso.toUpperCase();
$('anio').textContent = info.anio;
$('topics').innerHTML = clases.map(c => `<li>Clase ${esc(c.numero)} · ${esc(c.corto)}</li>`).join('');
const totalApps = clases.reduce((n, c) => n + c.apps.length, 0);
$('bar').innerHTML = `<span class="me">${esc(info.nombre)}</span>
  <span class="pill">${esc(info.curso)}</span>
  <span class="pill">${clases.length} clases</span>
  <span class="pill">${totalApps} apps</span>
  <span class="pill">${esc(info.anio)}</span>`;

// Tarjetas
const track = $('track');
track.innerHTML = clases.map((c, i) => `
  <article class="card paper holes" data-i="${i}" tabindex="0" role="button" aria-label="Abrir clase ${esc(c.numero)}">
    <span class="clip"></span>
    <div class="thumb" style="--c:${esc(c.color)}">
      ${c.portada ? `<img src="${c.portada}" alt="">`
                  : icono(c.icono)}
      <span class="stamp pixel">CLASE ${esc(c.numero)}</span>
    </div>
    <div class="row"><span class="num pixel">${esc(c.numero)}</span><span class="date">${esc(c.fecha)}</span></div>
    <h3>${esc(c.corto)}</h3>
    <p class="sub">${esc(c.titulo)}</p>
    <div class="more"><span>${c.apps.length} app${c.apps.length === 1 ? '' : 's'}</span><span class="open">Abrir ▸</span></div>
  </article>`).join('');

// Botones de desplazamiento
const paso = () => track.clientWidth * 0.8;
$('prev').onclick = () => track.scrollBy({left: -paso(), behavior: 'smooth'});
$('next').onclick = () => track.scrollBy({left: paso(), behavior: 'smooth'});

// Arrastrar con el mouse
let down = false, moved = false, startX = 0, startL = 0;
track.addEventListener('pointerdown', e => {
  if (e.pointerType !== 'mouse') return;
  down = true; moved = false; startX = e.clientX; startL = track.scrollLeft;
});
window.addEventListener('pointermove', e => {
  if (!down) return;
  const dx = e.clientX - startX;
  if (Math.abs(dx) > 6) { moved = true; track.classList.add('dragging'); }
  if (moved) track.scrollLeft = startL - dx;
});
window.addEventListener('pointerup', () => {
  down = false;
  setTimeout(() => track.classList.remove('dragging'), 0);
});

// Rueda del mouse: mueve el carrusel hacia los lados
track.addEventListener('wheel', e => {
  if (Math.abs(e.deltaY) <= Math.abs(e.deltaX)) return;
  const max = track.scrollWidth - track.clientWidth;
  const puede = (e.deltaY > 0 && track.scrollLeft < max - 1) || (e.deltaY < 0 && track.scrollLeft > 0);
  if (puede) { track.scrollLeft += e.deltaY; e.preventDefault(); }
}, {passive: false});

// Abrir clase
track.addEventListener('click', e => {
  if (moved) { moved = false; return; }
  const card = e.target.closest('.card');
  if (card) abrir(+card.dataset.i);
});
track.addEventListener('keydown', e => {
  const card = e.target.closest('.card');
  if (card && (e.key === 'Enter' || e.key === ' ')) { e.preventDefault(); abrir(+card.dataset.i); }
});

const overlay = $('overlay'), sheet = $('sheet');
let actual = 0;

function abrir(i) {
  actual = i;
  const c = clases[i];
  $('mk').textContent = `CLASE ${c.numero} · ${c.fecha}`;
  $('mtitle').textContent = c.titulo;
  $('apps').innerHTML = c.apps.map((a, k) => `
    <div class="note n${k % 3}">
      <span class="tape"></span>
      <h4>${esc(a.nombre)}</h4>
      <p>${esc(a.descripcion)}</p>
      <a class="btn" href="${esc(a.url)}" target="_blank" rel="noopener">Abrir app ↗</a>
    </div>`).join('');
  $('mprev').disabled = i === 0;
  $('mnext').disabled = i === clases.length - 1;

  overlay.classList.add('show');
  const top = Math.max(16, $('contents').offsetTop - 40);
  sheet.style.marginTop = top + 'px';
  sheet.style.maxHeight = (window.innerHeight - top - 16) + 'px';
  sheet.scrollTop = 0;

  const card = track.children[i];
  track.scrollTo({left: card.offsetLeft - (track.clientWidth - card.offsetWidth) / 2, behavior: 'smooth'});
}
function cerrar() { overlay.classList.remove('show'); }

$('close').onclick = cerrar;
overlay.addEventListener('click', e => { if (e.target === overlay) cerrar(); });
$('mprev').onclick = () => actual > 0 && abrir(actual - 1);
$('mnext').onclick = () => actual < clases.length - 1 && abrir(actual + 1);
// Ajusta la altura del marco al contenido (útil en celular)
function ajustarAltura() {
  const h = document.querySelector('.board').offsetHeight + 24;
  window.parent.postMessage({isStreamlitMessage: true, type: 'streamlit:setFrameHeight', height: h}, '*');
}
window.addEventListener('load', ajustarAltura);
window.addEventListener('resize', ajustarAltura);
document.fonts && document.fonts.ready.then(ajustarAltura);

document.addEventListener('keydown', e => {
  if (!overlay.classList.contains('show')) return;
  if (e.key === 'Escape') cerrar();
  if (e.key === 'ArrowLeft') $('mprev').click();
  if (e.key === 'ArrowRight') $('mnext').click();
});
</script>
</body>
</html>
"""

components.html(HTML.replace("__DATA__", datos_json), height=ALTO, scrolling=False)
