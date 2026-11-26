#!/usr/bin/env python3
"""Builds the static pages. Run: python3 build.py   (output goes next to this file)
Edit text in the PAGES below or directly in the generated .html files."""
import os
ROOT = os.path.dirname(os.path.abspath(__file__))

FAV = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%231A1816'/%3E%3Ctext x='32' y='44' font-family='Arial' font-weight='700' font-size='34' text-anchor='middle' fill='%23E4532C'%3EF%3C/text%3E%3C/svg%3E"

def head(title, desc, p, cls=""):
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<link rel="icon" href="{FAV}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}style.css">
</head><body class="{cls}">
'''

def nav(p, cur="", dot=None, over=False):
    # Dot, top right: About page -> Home; every other page -> About
    if dot is None:
        dot = ("index.html", "Home") if cur == "about" else ("about.html", "About")
    href, label = dot
    return f'''<header class="site-head{' over' if over else ''}"><a class="name" href="{p}index.html">Filippos Saltsidis</a><a class="dot" href="{p}{href}" aria-label="{label}" title="{label}"></a></header>
'''

def foot(p):
    return '''<footer class="foot2"><a href="mailto:filipposaltsidis@icloud.com">filipposaltsidis@icloud.com</a><a href="tel:+447707354630">(+44) 77 07 35 46 30</a></footer>
</body></html>
'''

def write(path, html):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(html)

# ---------------------------------------------------------------- HOME
home = head("Filippos Saltsidis · UX/UI designer, London",
            "Filippos Saltsidis is a London-based UX/UI designer. Selected work and contact details.", "", "v2") + nav("", "home") + '''
<main class="home">
<a class="card2" href="work/dashboard.html">
<div class="im"><img src="img/home/ccc-cover.jpg" alt="Redesigned Capital City College student dashboard shown on a laptop"></div>
<div class="cap">Capital City College</div></a>
<div class="card2">
<div class="im"></div>
<div class="cap">Next Project</div></div>
</main>
''' + foot("")
write("index.html", home)

# ---------------------------------------------------------------- ABOUT
about = head("About · Filippos Saltsidis", "About Filippos Saltsidis, a London-based UX/UI designer with more than fifteen years of experience.", "", "v2 aboutpage") + nav("", "about") + '''
<main class="ab">
<section class="ab-intro">
<p>I'm Filippos Saltsidis, a London-based UX/UI designer with more than fifteen years of experience in graphic, brand and digital design. I started in print and packaging, ran my own studio, and moved steadily into websites, interfaces and design systems, working with clients and teams in Greece, Berlin and London.</p>
</section>
<section class="ab-body">
<p>I work best at the start of a project, when the problem isn't clear yet. Before I open Figma, I try to understand who the product is for, what they're trying to do and where they get stuck. Then I turn that into structure: clear hierarchy, simple flows and components a team can reuse and build. My background in print and brand shows in the details. Typography, spacing and consistency matter to me, and I design with production in mind. After years of working with developers, marketing teams and clients, I'm used to turning a brief into something that ships.</p>
<ul>
<li>Understand users and define the problem</li>
<li>Map flows and structure information</li>
<li>Design responsive interfaces and prototypes in Figma</li>
<li>Build reusable components and light design systems</li>
<li>Hand over to developers with clear specs and states</li>
</ul>
<p class="contact"><a href="tel:+447707354630">(+44) 77 07 35 46 30</a><br><a href="mailto:filipposaltsidis@icloud.com">filipposaltsidis@icloud.com</a></p>
<p class="credit">Website Programming<br>Filippos Saltsidis</p>
</section>
</main>
''' + "</body></html>\n"
write("about.html", about)

# ---------------------------------------------------------------- SINGER STREET
def pnav(): return nav("../", "work")
ss = head("Singer Street · Print and presentation design · Filip Saltsidis",
          "A strategy deck, data report and community leaflet for a Shoreditch scheme, designed for three different audiences.", "../") + pnav() + '''
<header class="top"><div class="w">
<span class="tag">Print and presentation design · Real estate</span>
<h1>One scheme, three ways to tell its story</h1>
<p class="lead">For the Singer Street scheme in Shoreditch, I designed a data report, a strategy presentation and a community leaflet, each for a different audience. <span class="ph">[Edit: one sentence on your role and the outcome.]</span></p>
<div class="meta">
<div><small>Role</small><span class="ph">[e.g. Senior designer]</span></div>
<div><small>Agency</small><span>AND London</span></div>
<div><small>Client</small><span class="ph">[General Projects, if cleared]</span></div>
<div><small>Year</small><span>2022</span></div>
<div><small>Formats</small><span>Report, deck, leaflet</span></div>
</div></div></header>

<div class="w"><figure><div class="shot"><img src="../img/redesign-01-cover.jpg" alt="Redesigned cover of the Community Wealth Building Strategy"></div><figcaption>Cover of the Community Wealth Building Strategy.</figcaption></figure></div>

<section id="brief"><div class="w"><div class="n">
<div class="k">The brief</div><h2>Explain a planning scheme to people who each care about something different</h2>
<p><span class="ph">[2–3 sentences: what the scheme is, who needed to understand it, and why clear communication mattered.]</span></p></div>
<div class="grid g3">
<div class="card"><h3>The data report</h3><p>For planners and the council. Needed to make dense demographic evidence easy to read.</p></div>
<div class="card"><h3>The strategy deck</h3><p>For decision-makers. Needed to argue the case for community wealth building.</p></div>
<div class="card"><h3>The community leaflet</h3><p>For local people. Needed to be friendly, short and easy to pick up.</p></div>
</div></div></section>

<section id="deck"><div class="w"><div class="n">
<div class="k">01 · Strategy deck</div><h2>Turning pages of numbers into a story</h2>
<p>A presentation arguing the case for community wealth building around the scheme. Each page leads with one headline and one hero number, so a reader gets the point before the detail. <span class="ph">[Edit: add the audience and the outcome if you know it.]</span></p></div>
<figure class="big"><div class="shot"><img src="../img/redesign-02-scheme-overview.png" alt="Scheme Overview slide with statistics grouped into space, economic value and jobs" loading="lazy"></div>
<figcaption><b>Scheme Overview.</b> Eleven figures grouped into three themes, each with one hero number.</figcaption></figure>
<figure class="big"><div class="shot"><img src="../img/redesign-03-target-audience.png" alt="Target Audience slide with headline statistics and comparison charts" loading="lazy"></div>
<figcaption><b>Target Audience.</b> Four headline statistics and two comparison charts, with the study area in orange and the comparison in grey.</figcaption></figure>
<figure class="big"><div class="shot"><img src="../img/redesign-04-community-wealth.png" alt="Community Wealth slide with eight numbered icon cards" loading="lazy"></div>
<figcaption><b>Community Wealth.</b> Eight commitments in numbered cards with one consistent icon style.</figcaption></figure>
</div></section>

<section id="leaflet"><div class="w"><div class="n">
<div class="k">02 · Community leaflet</div><h2>A friendlier voice for local people</h2>
<p>A four-panel leaflet in bright green, with a winding-road illustration that runs across every panel. It speaks to local people, where the deck speaks to decision-makers. <span class="ph">[Edit: who received it and how it was used, only if true.]</span></p></div>
<figure class="big"><div class="empty wide">Leaflet mockup, open and folded<br>(add img/leaflet.png, then replace this box with an img tag)</div></figure>
<div class="grid g3">
<div class="card"><h3>Readable colour</h3><p>Dark text on light backgrounds for a contrast of at least 4.5:1, with bright green kept for large shapes.</p></div>
<div class="card"><h3>Calm type</h3><p>Smaller body text, ragged-right with no hyphenation, and a clear heading level.</p></div>
<div class="card"><h3>One continuous road</h3><p>The illustration runs across all panels, forming one line when the leaflet is open.</p></div>
</div></div></section>

<section id="report"><div class="w"><div class="n">
<div class="k">03 · Housing needs report</div><h2>Making demographic data readable</h2>
<p>A 22-page report on who lives within half a mile of the site. <span class="ph">[Edit: what you designed, such as layout, charts, maps or the illustration.]</span></p></div>
<div class="grid g2">
<div class="empty">Report page: cover or contents<br>(add img/report-1.png)</div>
<div class="empty">Report page: one chart page<br>(add img/report-2.png)</div>
</div></div></section>

<section id="role"><div class="w"><div class="n">
<div class="k">My role</div><h2>What I did, and what I learned</h2>
<p><span class="ph">[Be specific: layout, visual system, charts, illustration, art direction, working with the client and the research team. Name anyone whose work you used.]</span></p></div>
<div class="credit">
<div><small>My work</small><span class="ph">[e.g. layout, system, charts]</span></div>
<div><small>With</small><span class="ph">[research team, client]</span></div>
<div><small>Not mine</small><span class="ph">[photography, stock, partner logos]</span></div>
</div>
<div class="n" style="margin-top:44px"><h3>What this taught me</h3>
<ul class="c"><li>Each audience needs its own tone, but the structure underneath should stay clear.</li><li>Hierarchy matters more than decoration: one headline, one hero number, then detail.</li><li>Accessibility starts in print too: contrast, type size and hyphenation decide whether people read it.</li></ul></div>
</div></section>

<footer><div class="w"><p class="fn">Layouts shown were redesigned in 2026 from work originally produced in 2022 at AND London.</p>
<div class="row"><span><a href="../index.html">← All work</a></span><span><a href="dashboard.html">Next project →</a></span></div></div></footer>
</body></html>
'''
write("work/singer-street.html", ss)

# ---------------------------------------------------------------- DASHBOARD
db = head("Redesigning a college dashboard students actually use · Filippos Saltsidis",
          "Capital City College student dashboard redesign: a UX/UI concept project.", "../", "v2 projectpage") + nav("../", "project", over=True) + '''
<main class="proj">
<img class="phero" src="../img/ccc-hero.jpg" alt="Redesigned Capital City College student dashboard on a laptop">
<h1>Redesigning a college dashboard students actually use</h1>
<div class="intro">
<ul class="meta2">
<li>Role: UX/UI Designer</li>
<li>Project: Concept redesign</li>
<li>Timeline: 4 weeks</li>
<li>Tools: Figma</li>
<li>Platform: Desktop and mobile</li>
</ul>
<div class="lead2">
<p id="lead">Students open the college portal to find their next lesson, but the old dashboard buries it in a wall of tiles. I redesigned the Capital City College student dashboard so students can find their next lesson, messages and attendance quickly, and report an absence without hunting for it.</p>
<button class="more" type="button" aria-controls="lead" aria-expanded="false" hidden>Read more</button>
</div>
</div>
<img class="large" src="../img/ccc-dashboard-large.jpg" alt="The redesigned dashboard: next lesson, student services, attendance overview and the report an absence button" loading="lazy">
</main>
<script>
(function(){
  var p=document.getElementById("lead"), b=document.querySelector(".more");
  if(!p||!b) return;
  function check(){
    if(p.classList.contains("open")) return;
    p.classList.add("clamp");
    b.hidden = !(p.scrollHeight > p.clientHeight + 1);
  }
  b.addEventListener("click",function(){
    var open=p.classList.toggle("open");
    p.classList.toggle("clamp",!open);
    b.setAttribute("aria-expanded",open);
    b.textContent=open?"Read less":"Read more";
  });
  check(); window.addEventListener("resize",check);
  if(document.fonts&&document.fonts.ready) document.fonts.ready.then(check);
})();
</script>
</body></html>
'''
write("work/dashboard.html", db)

# ---------------------------------------------------------------- SIZE GUIDE (not linked from home)
sg = head("Size guide redesign · UX/UI case study · Filip Saltsidis",
          "Redesigning an e-commerce size guide pop-up so shoppers can choose or measure their size with confidence.", "../") + pnav() + '''
<header class="top"><div class="w">
<span class="tag">UX/UI case study · E-commerce</span>
<h1>Helping shoppers find their size without guessing</h1>
<p class="lead">I redesigned the size guide pop-up for <span class="ph">[Client name]</span>, a made-to-order fur store, so customers can choose or measure their size with confidence.</p>
<div class="meta">
<div><small>Role</small><span>UX/UI designer</span></div>
<div><small>Client</small><span class="ph">[real name, if cleared]</span></div>
<div><small>Timeline</small><span class="ph">[e.g. 3 weeks]</span></div>
<div><small>Tools</small><span class="ph">[Figma, ...]</span></div>
<div><small>Platform</small><span>Desktop and mobile web</span></div>
</div></div></header>

<div class="w"><figure><div class="shot"><img src="../img/size-guide-measure.png" alt="Redesigned size guide pop-up showing the guided measuring step"></div><figcaption>The redesigned “Help me measure” step.</figcaption></figure></div>

<section><div class="w"><div class="n">
<div class="k">Summary</div><h2>The short version</h2>
<p><b>Problem.</b> The old size guide mixed photos of models with a table, so shoppers could not tell which size to pick for a piece made to their measurements.</p>
<p><b>What I did.</b> One clear first question, a size chart with cm and inches, and a guided measuring flow with a highlighted illustration. The chosen size then shows on the product page.</p>
<p><b>Result.</b> <span class="ph">[One honest sentence: what shipped, what you measured, or “concept, not yet tested”]</span></p>
</div></div></section>

<section><div class="w"><div class="n">
<div class="k">Solution</div><h2>One question, then the right path</h2>
<p>The pop-up opens with a single choice: <i>I know my size</i> or <i>Help me measure</i>. Shoppers who know their size go straight to the chart. Everyone else is guided.</p></div>
<div class="grid g2">
<figure><div class="shot"><img src="../img/size-guide-know-my-size.png" alt="I know my size: size chips and size chart" loading="lazy"></div><figcaption><b>I know my size.</b> Pick a size chip and see the matching row in the chart.</figcaption></figure>
<figure><div class="shot"><img src="../img/size-guide-measure.png" alt="Help me measure: step by step with highlighted tape on illustration" loading="lazy"></div><figcaption><b>Help me measure.</b> One body part at a time, with the tape shown on the illustration.</figcaption></figure>
</div>
<div class="n" style="margin-top:72px"><h2>The size follows you to the product page</h2>
<p>Once a size is saved, the product page shows a “Your size” card with the measurements and an Edit link.</p></div>
<figure class="big"><div class="shot"><img src="../img/size-guide-product-page.png" alt="Product page with Your size card" loading="lazy"></div></figure>
<div class="mob">
<div class="shot"><img src="../img/size-guide-mobile.png" alt="Mobile bottom sheet version of the size guide" loading="lazy"></div>
<div><h2 style="font-size:30px">Designed for phones too</h2><p>On mobile the pop-up becomes a bottom sheet, so the input and Save button stay on screen.</p>
<ul class="c"><li>Large tap targets</li><li>Numeric input for measurements</li><li>Primary action fixed at the bottom</li></ul></div>
</div></div></section>

<footer><div class="w"><div class="row"><span><a href="../index.html">← All work</a></span></div></div></footer>
</body></html>
'''
write("work/size-guide.html", sg)

# 404
write("404.html", head("Page not found · Filippos Saltsidis", "Page not found.", "", "v2") + nav("", "404", ("index.html","Home")) + '''
<main class="plain"><p>That page doesn't exist. <a href="index.html">Back to the home page</a>.</p></main>
''' + "</body></html>\n")
print("built")
