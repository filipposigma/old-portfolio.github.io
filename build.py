#!/usr/bin/env python3
"""Builds the static pages. Run: python3 build.py   (output goes next to this file)
Edit text in the PAGES below or directly in the generated .html files."""
import os
ROOT = os.path.dirname(os.path.abspath(__file__))

FAV = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%231A1816'/%3E%3Ctext x='32' y='44' font-family='Arial' font-weight='700' font-size='34' text-anchor='middle' fill='%23E4532C'%3EF%3C/text%3E%3C/svg%3E"

def head(title, desc, p):
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<link rel="icon" href="{FAV}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}style.css">
</head><body>
'''

def nav(p, cur=""):
    a = lambda k, href, label: f'<a href="{href}"' + (' aria-current="page"' if cur == k else '') + f'>{label}</a>'
    return f'''<nav><div class="w"><a class="logo" href="{p}index.html">Filip Saltsidis</a>
{a("work", p + "index.html#work", "Work")}{a("about", p + "about.html", "About")}<a class="btn" href="{p}index.html#contact">Get in touch</a></div></nav>
'''

def foot(p):
    return f'''<footer><div class="w"><div class="row"><span>© 2026 Filip Saltsidis · London</span>
<span><a href="mailto:hello@filipposaltsidis.com">Email</a> · <a href="https://www.linkedin.com/in/your-profile">LinkedIn</a> · <a href="{p}index.html#work">Work</a></span></div></div></footer>
</body></html>
'''

def write(path, html):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(html)

CONTACT = '''<section id="contact"><div class="w"><div class="contact-box">
<div class="k" style="color:#ffd36b">Contact</div>
<h2>Let’s talk about your product</h2>
<p>I’m looking for my first full-time UX/UI or product design role in tech, fintech or a startup. <span class="ph">[Edit: one line on what you’re open to, e.g. London, hybrid, remote.]</span></p>
<a class="btn" href="mailto:hello@filipposaltsidis.com">hello@filipposaltsidis.com</a>
</div></div></section>
'''

# ---------------------------------------------------------------- HOME
home = head("Filip Saltsidis · UX/UI designer, London",
            "UX/UI designer with 15+ years in digital and print design. Case studies in product, dashboards and fintech.", "") + nav("") + '''
<header class="hero"><div class="w">
<span class="tag">UX/UI designer · London</span>
<h1>I design clear, trustworthy products for people who just want to get things done</h1>
<p class="lead">15+ years in graphic and digital design, now focused on UX and product design. <span class="ph">[Edit: one line on what you want to be hired for, e.g. fintech and startup products.]</span></p>
<div class="cta"><a class="btn" href="#work">See my work</a><a class="btn ghost" href="about.html">About me</a></div>
</div></header>

<section id="work"><div class="w">
<div class="k">Selected work</div><h2>Case studies</h2>
<div class="projects">

<a class="project" href="work/dashboard.html">
<div class="pimg"><img src="img/dashboard-redesign.jpg" alt="Redesigned student dashboard for Capital City College" loading="lazy"></div>
<div><span class="tag">UX/UI · Education · Dashboard</span><h3>Redesigning a college dashboard students actually use</h3>
<p>Research with students, a new information structure and a simpler dashboard, including a feature to report an absence in two taps.</p><span class="more">Read case study →</span></div></a>

<a class="project" href="work/singer-street.html">
<div class="pimg"><img src="img/redesign-02-scheme-overview.png" alt="Redesigned Scheme Overview slide" loading="lazy"></div>
<div><span class="tag">Presentation and print · Real estate</span><h3>One scheme, three ways to tell its story</h3>
<p>A strategy deck, a data report and a community leaflet for a Shoreditch scheme, each designed for a different audience.</p><span class="more">Read case study →</span></div></a>

<div class="project soon">
<div class="pimg">Next project: a fintech case study</div>
<div><span class="tag">Coming soon</span><h3>A mobile fintech project</h3>
<p><span class="ph">[Replace this card with your next project when it is ready, or delete it.]</span></p></div></div>

</div></div></section>

<section id="about"><div class="w"><div class="about-grid">
<div><div class="k">About</div><h2>From print and brand to product</h2></div>
<div><p>I’m a designer with more than 15 years’ experience across print, brand and digital work, including a senior design role at AND London. I’m now building on that foundation with UX research, interaction design and front-end skills.</p>
<p><span class="ph">[Edit: two sentences on how you work, e.g. start with evidence, test early, explain every decision.]</span></p>
<div class="chips"><span class="chip">UX research</span><span class="chip">Interaction design</span><span class="chip">Design systems</span><span class="chip">Figma</span><span class="chip">HTML and CSS</span></div>
<p style="margin-top:24px"><a href="about.html"><b>More about me →</b></a></p></div>
</div></div></section>
''' + CONTACT + foot("")
write("index.html", home)

# ---------------------------------------------------------------- ABOUT
about = head("About · Filip Saltsidis", "About Filip Saltsidis, UX/UI designer in London.", "") + nav("", "about") + '''
<header class="top"><div class="w">
<span class="tag">About</span>
<h1>Designer first, now building products end to end</h1>
<p class="lead"><span class="ph">[Edit: a short, personal intro in your own voice, 2–3 sentences.]</span></p></div></header>

<section><div class="w"><div class="about-grid">
<div><div class="k">My story</div><h2>How I got here</h2></div>
<div>
<p>I started in graphic design and spent over 15 years working in print, brand and digital, rising to a senior design role at AND London.</p>
<p><span class="ph">[Edit: why you moved towards UX and product design, what you’ve learned, and what you want to do next. Keep it honest and specific.]</span></p>
<p>I’m studying computer science alongside design, so I can talk to developers in their own language and build working prototypes. <span class="ph">[Check this line is still right for you.]</span></p>
</div></div></div></section>

<section><div class="w"><div class="k">What I do</div><h2>Skills</h2>
<div class="grid g3">
<div class="card"><h3>Research</h3><p>Interviews, surveys, usability tests and heuristic reviews, with honest counts of what I did.</p></div>
<div class="card"><h3>Design</h3><p>Information architecture, wireframes, interface design and design systems in Figma.</p></div>
<div class="card"><h3>Build</h3><p>HTML, CSS and prototypes, so ideas can be checked in a browser, not only on a canvas.</p></div>
</div></div></section>
''' + CONTACT + foot("")
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
<div class="row"><span><a href="../index.html#work">← All work</a></span><span><a href="dashboard.html">Next project →</a></span></div></div></footer>
</body></html>
'''
write("work/singer-street.html", ss)

# ---------------------------------------------------------------- DASHBOARD
db = head("College dashboard redesign · UX/UI case study · Filip Saltsidis",
          "Redesigning the Capital City College student dashboard: research, structure, interface and a report-an-absence feature.", "../") + pnav() + '''
<header class="top"><div class="w">
<span class="tag">UX/UI case study · Education · Dashboard</span>
<h1>Redesigning a college dashboard students actually use</h1>
<p class="lead">I redesigned the Capital City College student dashboard so students can find their next lesson, messages and attendance quickly, and report an absence without hunting for it. <span class="ph">[Edit: make this one honest sentence about what is a concept and what is real.]</span></p>
<div class="meta">
<div><small>Role</small><span>UX/UI designer</span></div>
<div><small>Type</small><span class="ph">[e.g. self-initiated concept]</span></div>
<div><small>Timeline</small><span class="ph">[e.g. 6 weeks]</span></div>
<div><small>Tools</small><span>Figma <span class="ph">[+ others]</span></span></div>
<div><small>Platform</small><span>Desktop and mobile web</span></div>
</div></div></header>

<div class="w"><figure><div class="shot"><img src="../img/dashboard-redesign.jpg" alt="Redesigned Capital City College student dashboard"></div><figcaption>The redesigned dashboard.</figcaption></figure></div>

<section><div class="w"><div class="n">
<div class="k">Summary</div><h2>The short version</h2>
<p><b>Problem.</b> <span class="ph">[What was hard for students: where things were, how long tasks took, what they missed.]</span></p>
<p><b>What I did.</b> <span class="ph">[Research you really ran, the structure you changed, the key screens and the absence feature.]</span></p>
<p><b>Result.</b> <span class="ph">[One honest sentence: tested with how many people, what you learned, or “concept, not yet tested”.]</span></p>
</div></div></section>

<section id="research"><div class="w"><div class="n">
<div class="k">01 · Research</div><h2>What students told me</h2>
<p><span class="ph">[Explain your survey and interviews: how many responses, how you reached people, and what patterns you found. Use only real numbers.]</span></p></div>
<div class="grid g3">
<div class="card"><div class="num">1</div><h3>Survey</h3><p><span class="ph">[Responses and main findings]</span></p></div>
<div class="card"><div class="num">2</div><h3>Interviews</h3><p><span class="ph">[How many people, what they said]</span></p></div>
<div class="card"><div class="num">3</div><h3>Old portal review</h3><p><span class="ph">[What the existing portal did poorly]</span></p></div>
</div>
<div class="quote">“<span class="ph">[A real quote from a student]</span>”<small>Source: <span class="ph">[who / how collected]</span></small></div>
</div></section>

<section id="design"><div class="w"><div class="n">
<div class="k">02 · Design</div><h2>One screen, clear priorities</h2>
<p>The new dashboard puts the next lesson, messages and attendance first, with student services one tap away. <span class="ph">[Edit: explain two or three decisions and the evidence behind each.]</span></p></div>
<div class="grid g2">
<div class="card"><div class="num">1</div><h3>Next lesson first</h3><p>The most common question, “where do I need to be?”, is answered at the top right with date, time and room.</p></div>
<div class="card"><div class="num">2</div><h3>Attendance at a glance</h3><p>Two simple bars and a status label replace a table of numbers.</p></div>
<div class="card"><div class="num">3</div><h3>Report an absence in two taps</h3><p>The action sits with attendance, where students think about it.</p></div>
<div class="card"><div class="num">4</div><h3>Student services as a short list</h3><p>Five clear links with a one-line description each.</p></div>
</div></div></section>

<section id="outcome"><div class="w"><div class="n">
<div class="k">03 · Outcome</div><h2>What happened and what I learned</h2>
<p><span class="ph">[Be honest about testing and results. Add prototypes, GIFs or test findings here.]</span></p>
<h3 style="margin-top:36px">What I would do next</h3>
<ul class="c"><li><span class="ph">[e.g. test the absence flow with more students]</span></li><li><span class="ph">[e.g. explore an AI help feature]</span></li></ul></div>
</div></section>

<footer><div class="w"><div class="row"><span><a href="singer-street.html">← Previous project</a></span><span><a href="../index.html#work">All work →</a></span></div></div></footer>
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

<footer><div class="w"><div class="row"><span><a href="../index.html#work">← All work</a></span></div></div></footer>
</body></html>
'''
write("work/size-guide.html", sg)

# 404
write("404.html", head("Page not found · Filip Saltsidis", "Page not found.", "") + nav("") + '''
<header class="hero"><div class="w"><span class="tag">404</span><h1>That page doesn’t exist</h1><p class="lead">Try the <a href="index.html">home page</a> or my <a href="index.html#work">work</a>.</p></div></header>
''' + foot(""))
print("built")
