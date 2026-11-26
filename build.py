#!/usr/bin/env python3
"""Builds the static pages. Run: python3 build.py   (output goes next to this file)"""
import os
ROOT = os.path.dirname(os.path.abspath(__file__))
EMAIL = "filipposaltsidis@icloud.com"
TEL_HREF = "tel:+447707354630"
TEL = "(+44) 77 07 35 46 30"
FAV = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%23000'/%3E%3Ctext x='32' y='44' font-family='Arial' font-weight='700' font-size='34' text-anchor='middle' fill='%23fff'%3EF%3C/text%3E%3C/svg%3E"

def head(title, desc, p, cls=""):
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<link rel="icon" href="{FAV}">
<link rel="stylesheet" href="{p}style.css">
</head><body class="{cls}">
'''

def nav(p, current=False):
    """Header: name on the left, 'Info' in the second column (plain text when already on the Info page)."""
    right = '<span aria-current="page">Info</span>' if current else f'<a href="{p}about.html">Info</a>'
    return f'<header class="site-head"><a href="{p}index.html">Filippos Saltsidis</a>{right}</header>\n'

def write(path, html):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(html)

INTRO = ("I'm a London-based UX/UI designer with more than fifteen years of experience in graphic, brand and digital design. "
         "I started in print and packaging, ran my own studio, and moved steadily into websites, interfaces and design systems, "
         "working with clients and teams in Greece, Berlin and London.")

# ---------------------------------------------------------------- HOME
CARD_PH = '<div class="card"><div class="im"></div><p class="cap">{}</p></div>'
home = head("Filippos Saltsidis · UX/UI designer, London",
            "Filippos Saltsidis is a London-based UX/UI designer. Selected work.", "", "home-page") + nav("") + f'''<main>
<p class="intro">{INTRO}</p>
<div class="cards">
<a class="card" href="work/dashboard.html"><div class="im"><img src="img/home/ccc-cover.jpg" alt="Redesigned Capital City College student dashboard shown on a laptop"></div><p class="cap">Capital City College</p></a>
{CARD_PH.format("Next Project")}
{CARD_PH.format("Next Project")}
{CARD_PH.format("Next Project")}
</div>
<div class="home-end"></div>
</main>
</body></html>
'''
write("index.html", home)

# ---------------------------------------------------------------- ABOUT (Info)
about = head("Info · Filippos Saltsidis",
             "Filippos Saltsidis is a London-based UX/UI designer with more than fifteen years of experience in graphic, brand and digital design.", "", "aboutpage") + nav("", current=True) + f'''<main class="ab">
<div class="col1">
<p>I'm Filippos Saltsidis, a London-based UX/UI designer with more than fifteen years of experience in graphic, brand and digital design. I started in print and packaging, ran my own studio, and moved steadily into websites, interfaces and design systems, working with clients and teams in Greece, Berlin and London.</p>
<p>I work best at the start of a project, when the problem isn't clear yet. Before I open Figma, I try to understand who the product is for, what they're trying to do and where they get stuck. Then I turn that into structure: clear hierarchy, simple flows and components a team can reuse and build. My background in print and brand shows in the details. Typography, spacing and consistency matter to me, and I design with production in mind. After years of working with developers, marketing teams and clients, I'm used to turning a brief into something that ships.</p>
</div>
<div class="col2">
<p><a href="{TEL_HREF}">{TEL}</a><a href="mailto:{EMAIL}">{EMAIL}</a></p>
<p>Website Programming<br>Filippos Saltsidis</p>
</div>
</main>
</body></html>
'''
write("about.html", about)

# ---------------------------------------------------------------- CAPITAL CITY COLLEGE
LEAD = "Students open the college portal to find their next lesson, but the old dashboard buries it in a wall of tiles. I redesigned the Capital City College student dashboard so students can find their next lesson, messages and attendance quickly, and report an absence without hunting for it."
db = head("Redesigning a college dashboard students actually use · Filippos Saltsidis",
          "Capital City College student dashboard redesign: a UX/UI concept project.", "../", "cspage") + nav("../") + f'''<main>
<h1 class="cs-title">Redesigning a college dashboard students actually use</h1>
<div class="cs-lead">
<p id="lead">{LEAD}</p>
<button class="more" type="button" aria-controls="lead" aria-expanded="false" hidden>read more</button>
</div>
<div class="cs-blocks">
<figure class="blk b1" style="margin-top:0"><img src="../img/ccc-dashboard-large.jpg" alt="The redesigned dashboard: next lesson, student services, attendance overview and the report an absence button"></figure>
<!-- Placeholders from the Figma layout: replace with project images -->
<div class="blk b2" role="presentation"></div>
<div class="pair"><div class="blk" role="presentation"></div><div class="blk" role="presentation"></div></div>
<div class="blk b3" role="presentation"></div>
</div>
<ul class="cs-meta">
<li>Role: UX/UI Designer</li>
<li>Project: Concept redesign</li>
<li>Timeline: 4 weeks</li>
<li>Tools: Figma</li>
<li>Platform: Desktop and mobile</li>
</ul>
</main>
<script>
(function(){{
  var p=document.getElementById("lead"), b=document.querySelector(".more");
  if(!p||!b) return;
  function check(){{
    if(p.classList.contains("open")) return;
    p.classList.add("clamp");
    b.hidden = !(p.scrollHeight > p.clientHeight + 1);
  }}
  b.addEventListener("click",function(){{
    var open=p.classList.toggle("open");
    p.classList.toggle("clamp",!open);
    b.setAttribute("aria-expanded",open);
    b.textContent=open?"read less":"read more";
  }});
  check(); window.addEventListener("resize",check);
  if(document.fonts&&document.fonts.ready) document.fonts.ready.then(check);
}})();
</script>
</body></html>
'''
write("work/dashboard.html", db)

# ---------------------------------------------------------------- 404
nf = head("Page not found · Filippos Saltsidis", "Page not found.", "/", "") + nav("/") + '''<main class="ab"><div class="col1"><p>Page not found.</p><p><a href="/index.html">Back to the work</a></p></div></main>
</body></html>
'''
write("404.html", nf)
print("built")
