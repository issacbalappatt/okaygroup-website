from pathlib import Path
import json
from html import escape
from urllib.parse import urlsplit

from catalogue_content import APPLICATION_DETAILS, DISTRICTS, GUIDES, PRODUCT_DETAILS, SUPPLY_DETAILS

SITE = 'https://okaygroup.org/'
EMAIL = 'okaygroup@live.com'
ROOT = Path(__file__).resolve().parents[1]
PAGES = []
MAP = 'https://www.google.com/maps/search/?api=1&amp;query=Manorama+Oxygen+Major+Industrial+Estate+Kalamassery'
INDIAMART = 'https://www.indiamart.com/manorama-oxygen-pvtltd/'
nav = [('index.html', 'Home'), ('products.html', 'Our gases'), ('industries.html', 'Industries'),
       ('supply.html', 'Supply & quality'), ('locations.html', 'Coverage'), ('companies.html', 'About')]
icons = {
    'arrow': '<path d="M4 12h15m-6-6 6 6-6 6"/>',
    'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m4 7 8 6 8-6"/>',
    'pin': '<path d="M20 10c0 5-8 10-8 10s-8-5-8-10a8 8 0 1 1 16 0Z"/><circle cx="12" cy="10" r="2.5"/>',
    'menu': '<path d="M4 6h16M4 12h16M4 18h16"/>',
    'factory': '<path d="M3 21V11l6-4v5l6-5v5h3l1-8h2v17H3Zm4-4h2m3 0h2m3 0h2"/>',
    'medical': '<path d="M9 3h6v6h6v6h-6v6H9v-6H3V9h6V3Z"/>',
    'truck': '<path d="M3 5h11v12H3zM14 9h4l3 4v4h-7"/><circle cx="7" cy="18" r="2" fill="currentColor" stroke="none"/><circle cx="17" cy="18" r="2" fill="currentColor" stroke="none"/>',
    'shield': '<path d="m12 2 8 4v6c0 5-5 8-8 10-3-2-8-5-8-10V6l8-4Z"/><path d="m8 12 3 3 5-6"/>',
    'flask': '<path d="M9 3h6m-5 0v7L4 19a1 1 0 0 0 1 2h14a1 1 0 0 0 1-2l-6-9V3M7 16h10"/>',
    'food': '<path d="M4 3v5a3 3 0 0 0 6 0V3M7 3v18M17 21V3c-3 2-4 5-4 9h4"/>',
    'spark': '<path d="M3 17h8v4H3zM7 17V9h9m2-6v6m3-3h-6m4 6 2 3m-6-2-1 4"/>',
    'snow': '<path d="M12 2v20M3 7l18 10M3 17 21 7M9 5l3 3 3-3M9 19l3-3 3 3M5 10l4-1-1-4m8 14-1-4 4-1m-14 0 4 1-1 4m8-14-1 4 4 1"/>',
    'cylinder': '<rect x="7" y="7" width="10" height="14" rx="3"/><path d="M10 7V3h4v4m-5-4h6"/>',
}

def icon(name):
    return f'<svg class="icon" viewBox="0 0 24 24" aria-hidden="true">{icons[name]}</svg>'

def public_url(path):
    return '/' if path == 'index.html' else '/' + path

def local_href(href):
    if href.startswith(('/', '#')) or urlsplit(href).scheme:
        return href
    return public_url(href)

def button(href, title, style='', symbol='arrow'):
    return f'<a class="button {style}" href="{local_href(href)}">{title} {icon(symbol)}</a>'

def link(href, title):
    return f'<a class="text-link" href="{local_href(href)}">{title} {icon("arrow")}</a>'

def shot(name, alt='', lazy=True):
    loading = ' loading="lazy"' if lazy else ''
    return f'<img src="/assets/{name}.webp" alt="{alt}"{loading} decoding="async">'

def brand():
    return '<a class="brand" href="/" aria-label="Okay Group home"><span class="brand-main">OKAY</span><span class="brand-small">GROUP</span></a>'

def nav_links(current):
    return ''.join(f'<a href="{public_url(url)}"{" aria-current=\"page\"" if current == url else ""}>{escape(label)}</a>' for url, label in nav)

def render(file, title, description, content, social='gas-facility', extra_schema=None, trail=(), article=False):
    canonical = SITE.rstrip('/') + public_url(file)
    schema = []
    if file in {'index.html', 'companies.html'}:
        schema.append({
            '@type': 'Organization', '@id': SITE + '#organization', 'name': 'Okay Group',
            'url': SITE, 'email': EMAIL, 'foundingDate': '1996',
            'areaServed': {'@type': 'State', 'name': 'Kerala'},
            'address': {
                '@type': 'PostalAddress', 'streetAddress': 'Major Industrial Estate, Kalamassery',
                'addressLocality': 'Ernakulam', 'addressRegion': 'Kerala', 'addressCountry': 'IN',
            },
        })
    if file == 'index.html':
        schema.append({
            '@type': 'WebSite', '@id': SITE + '#website', 'name': 'Okay Group',
            'url': SITE, 'inLanguage': 'en-IN', 'publisher': {'@id': SITE + '#organization'},
        })
    if extra_schema:
        schema.append(extra_schema)
    crumbs = ''
    if trail:
        full_trail = (('index.html', 'Home'),) + trail
        schema.append({
            '@type': 'BreadcrumbList',
            'itemListElement': [
                {'@type': 'ListItem', 'position': i, 'name': name, 'item': SITE.rstrip('/') + public_url(path)}
                for i, (path, name) in enumerate(full_trail, 1)
            ],
        })
        anchors = ''.join(f'<li><a href="{public_url(path)}">{escape(name)}</a></li>' for path, name in full_trail[:-1])
        crumbs = f'<nav class="breadcrumb wrap" aria-label="Breadcrumb"><ol>{anchors}<li aria-current="page">{escape(full_trail[-1][1])}</li></ol></nav>'
    structured_data = ''
    if schema:
        graph = json.dumps({'@context': 'https://schema.org', '@graph': schema}, ensure_ascii=False)
        structured_data = f'<script type="application/ld+json">{graph}</script>'
    noindex = '<meta name="robots" content="noindex">' if file == '404.html' else ''
    canonical_tag = f'<link rel="canonical" href="{canonical}">' if not noindex else ''
    og_type = 'article' if article else 'website'
    site = f'''<!doctype html>
<html lang="en-IN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(description)}">
  <meta name="theme-color" content="#101a29">
  {noindex}{canonical_tag}
  <meta property="og:type" content="{og_type}">
  <meta property="og:locale" content="en_IN">
  <meta property="og:site_name" content="Okay Group">
  <meta property="og:title" content="{escape(title)}">
  <meta property="og:description" content="{escape(description)}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{SITE}assets/{social}.webp">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="/assets/site.css">
  <link rel="stylesheet" href="/assets/motion.css">
  <script src="/assets/site.js" defer></script>
  <script type="module" src="/assets/motion.js"></script>
{structured_data}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="masthead">
  <div class="wrap mast-row">
    {brand()}
    <nav class="nav-row" id="main-nav" aria-label="Main navigation">{nav_links(file)}</nav>
    <div class="mast-actions">
      {button('contact.html', 'Enquire', 'nav-enquire')}
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="main-nav" aria-label="Menu" hidden>{icon('menu')}</button>
    </div>
  </div>
</header>
<main id="main">
{crumbs}
{content}
</main>
<footer class="footer">
  <div class="wrap footer-grid">
    <div>{brand()}<p>Industrial and medical gas supply<br>Kalamassery, Kerala</p></div>
    <div><h2>Explore</h2><nav aria-label="Footer navigation"><a href="/products.html">Our gases</a><a href="/industries.html">Industries and applications</a><a href="/supply.html">Supply and quality</a><a href="/guides.html">Gas buying guides</a><a href="/manorama-oxygen.html">Manorama Oxygen Pvt. Ltd.</a></nav></div>
    <div><h2>Get in touch</h2><address>Major Industrial Estate, Kalamassery<br>Ernakulam, Kerala, India</address><a href="mailto:{EMAIL}">{EMAIL}</a><a href="/contact.html">Enquiries and directions</a><a href="/locations.html">Kerala branches and delivery</a></div>
  </div>
  <div class="wrap footer-bottom"><p>© Okay Group</p></div>
</footer>
</body>
</html>
'''
    output = ROOT / file
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(site, encoding='utf-8')
    if not noindex:
        PAGES.append(canonical)

def page_head(label, heading, intro, action=''):
    return f'<section class="page-head"><div class="wrap"><p class="eyebrow">{label}</p><h1>{heading}</h1><p class="intro">{intro}</p>{action}</div></section>'

def callout(heading='Get a gas supply quote', desc='Share the gas, grade, quantity and delivery postcode with our team.', enquiry='contact.html'):
    return f'<section class="callout"><div class="wrap"><div><h2>{heading}</h2><p>{desc}</p></div>{button(enquiry, "Make an enquiry")}</div></section>'

products = {
    'industrial-oxygen': ('Industrial oxygen', 'O₂', 'Oxygen supports industrial processes such as oxy-fuel cutting and combustion. Ask about the industrial grade and cylinder format required for your process.'),
    'nitrogen': ('Nitrogen', 'N₂', 'Gaseous nitrogen is used for inerting, purging and blanketing. Liquid nitrogen serves applications such as cryogenic cooling and freezing. Specify the form and grade you need.'),
    'argon': ('Argon', 'Ar', 'An inert gas commonly used to shield welds in TIG and MIG processes. Enquire about commercial, high-purity or liquid argon, depending on your specification.'),
    'carbon-dioxide': ('Carbon dioxide', 'CO₂', 'Enquire about gaseous or liquid CO₂ for applications such as beverage carbonation and welding. Specify the grade your process requires.'),
    'acetylene': ('Dissolved acetylene', 'C₂H₂', 'A fuel gas for oxy-fuel cutting and fabrication. Ask the team about current availability and cylinder format.'),
    'helium': ('Helium', 'He', 'Helium has applications in leak detection and analytical work. Contact us about cylinder supply and the required specification.'),
    'medical-oxygen': ('Medical oxygen', 'O₂', 'Supply enquiries for hospitals and healthcare facilities. Contact us about the required grade and documentation, including cylinder and Dura cylinder options.'),
    'oxygen-equipment': ('Oxygen equipment', 'O₂', 'Portable oxygen cylinder kits and concentrators are listed by Manorama Oxygen. Ask about models and availability.'),
    'liquid-nitrogen-equipment': ('Liquid nitrogen containers', 'LN₂', 'Enquire about cryocans and liquid nitrogen tanks. Include the container type, capacity and application.'),
    'dry-ice': ('Dry ice', 'CO₂', 'Solid carbon dioxide in block form. Enquire about quantities, timing and collection or delivery for cold-chain and temperature-controlled transport applications.'),
}
industrial = list(products)[:6]
medical = ['medical-oxygen', 'oxygen-equipment']
specialty = ['liquid-nitrogen-equipment', 'dry-ice']
product_specs = {
    'industrial-oxygen': ('Compressed gas', 'Industrial cylinders', 'Cutting and metalworking', 'fabrication'),
    'nitrogen': ('Gas and cryogenic liquid', 'Cylinder or liquid enquiry', 'Purging and cooling', 'laboratories'),
    'argon': ('Gas and cryogenic liquid', 'Commercial and high purity', 'Welding and laboratory uses', 'welding'),
    'carbon-dioxide': ('Gas and liquid', 'Cylinder or liquid enquiry', 'Beverage and fabrication uses', 'food'),
    'acetylene': ('Dissolved fuel gas', 'Cylinder availability enquiry', 'Oxy-fuel cutting', 'welding'),
    'helium': ('Compressed gas', 'Cylinder enquiry', 'Leak detection and analytical uses', 'laboratories'),
    'medical-oxygen': ('Medical oxygen', 'Cylinder and Dura cylinder enquiries', 'Healthcare procurement', 'healthcare'),
    'oxygen-equipment': ('Equipment', 'Portable kits and concentrators', 'Healthcare equipment enquiries', 'healthcare'),
    'liquid-nitrogen-equipment': ('Cryogenic equipment', 'Cryocans and tanks', 'Cryogenic storage', 'laboratories'),
    'dry-ice': ('Solid carbon dioxide', 'Blocks', 'Temperature-controlled transport', 'cold-chain'),
}
product_art = {
    'industrial-oxygen': 'cylinder-oxygen', 'nitrogen': 'cylinder-nitrogen', 'argon': 'cylinder-argon',
    'carbon-dioxide': 'cylinder-co2', 'acetylene': 'cylinder-acetylene', 'helium': 'cylinder-helium',
    'medical-oxygen': 'cylinder-oxygen', 'oxygen-equipment': 'medical',
    'dry-ice': 'dry-ice', 'liquid-nitrogen-equipment': 'gas-facility',
}

def cylinders(keys, panel):
    return f'<div class="cylinder-grid" id="preview-{panel}" data-panel="{panel}">' + ''.join(
        f'<a class="cylinder-card" href="/gases/{key}.html"><span class="cylinder-art {"photo-art" if not product_art[key].startswith("cylinder-") else ""}">{shot(product_art[key])}<span class="formula" aria-hidden="true">{products[key][1]}</span></span><span class="cylinder-body"><span><strong>{products[key][0]}</strong><small>{product_specs[key][1]}</small></span>{icon("arrow")}</span></a>'
        for key in keys) + '</div>'

sectors = [
    ('fabrication', 'Manufacturing<br>and fabrication', 'factory', 'Industrial oxygen and dissolved acetylene are used in oxy-fuel cutting. Argon and carbon dioxide can be used in shielding gas applications. Match the grade and gas to your welding or cutting process.', 'industrial'),
    ('healthcare', 'Hospitals<br>and healthcare', 'medical', 'Enquire about medical oxygen and oxygen equipment for healthcare facilities. Share the required supply format, usage and delivery location when you contact us.', 'healthcare'),
    ('laboratories', 'Laboratories<br>and research', 'flask', 'Nitrogen, argon and helium may be used in analytical and research settings. Give us the instrument or application and its required gas specification.', 'argon'),
    ('food', 'Food<br>and beverage', 'food', 'Common applications include carbonation with carbon dioxide and cooling with liquid nitrogen. Confirm the required food-contact grade before ordering.', 'carbon-dioxide'),
    ('welding', 'Cutting<br>and welding', 'spark', 'Tell us the material, welding or cutting process, and required gas or mix, so we can discuss an appropriate supply option.', 'acetylene'),
    ('cold-chain', 'Cold chain<br>and transport', 'snow', 'Dry ice blocks can be used in temperature-controlled packing and transport. Enquire about the amount, collection or delivery, and timing.', 'dry-ice'),
]
sector_strip = '<section class="sector-band"><div class="wrap"><div class="split-title"><div><p class="eyebrow">Industries</p><h2>Find gases by application</h2></div>' + link('industries.html', 'View all applications') + '</div><ul class="sector-grid">' + ''.join(
    f'<li><a href="/applications/{key}.html">{icon(s)}<span>{title}</span></a></li>' for key,title,s,_,_ in sectors
) + '</ul></div></section>'
tiles = [
    ('industrial-cylinders', 'Packaged gas', 'Cylinder enquiries for workshops, laboratories and hospitals.', '/supply/cylinder-supply.html'),
    ('gas-facility', 'Liquid &amp; bulk', 'Discuss cryogenic liquids, storage and recurring deliveries.', '/supply/bulk-liquid.html'),
    ('dry-ice', 'Dry ice', 'Block dry ice for cold-chain handling and transport.', '/supply/dry-ice-supply.html'),
]
tile_grid = ''.join(f'<a class="tile" href="{url}">{shot(pic)}<h3>{head}</h3><p>{body}</p>{icon("arrow")}</a>' for pic,head,body,url in tiles)

render('index.html', 'Industrial & Medical Gas Supplier in Kerala | Okay Group',
       'Okay Group and Manorama Oxygen supply industrial gases, medical oxygen and dry ice, with branches and delivery across all 14 districts of Kerala.', f'''
<section class="hero">
  <picture><source media="(max-width: 780px)" srcset="assets/cylinder-studio-mobile.webp"><img src="assets/cylinder-studio.webp" alt="" fetchpriority="high" decoding="async"></picture>
  <div class="wrap hero-copy">
    <p class="eyebrow">Okay Group · Manorama Oxygen</p>
    <h1>Industrial gases.<br><span>Medical oxygen.</span></h1>
    <p class="intro">Industrial and medical gas supply for manufacturers, hospitals and businesses, with branches and delivery across Kerala.</p>
    <div class="hero-actions">{button("#gas-range", "Explore gases")}{button("contact.html", "Get a quote", "outline")}</div>
  </div>
  <p class="hero-note">Illustrative cylinder imagery</p>
</section>
<section class="catalogue" id="gas-range">
  <div class="wrap">
    <div class="split-title">
      <div><p class="eyebrow">Product range</p><h2>Explore our gases</h2></div>
      <div class="filters" role="group" aria-label="Gas category" hidden><button type="button" data-category="industrial" aria-controls="preview-industrial" aria-pressed="true">Industrial gases</button><button type="button" data-category="medical" aria-controls="preview-medical" aria-pressed="false">Medical oxygen</button><button type="button" data-category="specialty" aria-controls="preview-specialty" aria-pressed="false">Dry ice &amp; equipment</button></div>
    </div>
    {cylinders(industrial, "industrial")}
    {cylinders(medical, "medical")}
    {cylinders(specialty, "specialty")}
    <div class="catalogue-end"><p>Cylinder images and colours are illustrative.</p>{link("products.html", "View full catalogue")}</div>
  </div>
</section>
{sector_strip}
<section class="section applications">
  <div class="wrap">
    <div class="split-title"><div><p class="eyebrow">Supply formats</p><h2>From cylinders to bulk liquid</h2></div>{link("supply.html", "Explore supply options")}</div>
    <div class="tile-grid">{tile_grid}</div>
  </div>
</section>
<section class="coverage-band">
  <div class="wrap coverage-row">
    <div><p class="eyebrow">Delivery coverage</p><h2>Delivering across all 14 districts of Kerala</h2>
    <p>Share your postcode to find the branch that serves your site and arrange delivery.</p></div>
    {button('locations.html', 'Explore Kerala coverage')}
  </div>
</section>
<section class="about-preview">
  <div class="wrap about-grid">
    <figure class="about-photo">{shot("industrial-cylinders", "Illustration of cylinders in an industrial warehouse")}<figcaption>Illustrative warehouse image</figcaption></figure>
    <div><p class="eyebrow">About Okay Group</p><h2>Based in Kalamassery since 1996</h2><p class="intro">Manorama Oxygen began in Kalamassery with medical oxygen supply. Today its catalogue includes industrial gases, dry ice and cryogenic equipment for customers across Kerala.</p>{link("manorama-oxygen.html", "About Manorama Oxygen")}</div>
  </div>
</section>
{callout()}''', 'cylinder-studio')

def product_card(key):
    title, formula, copy = products[key]
    form, supply_format, application, sector = product_specs[key]
    return f'''<article class="info-card product-card" id="{key}">
      <div class="product-heading"><span class="chem" aria-hidden="true">{formula}</span><h3><a href="/gases/{key}.html">{title}</a></h3></div>
      <p>{copy}</p>
      <dl class="product-spec"><div><dt>Form</dt><dd>{form}</dd></div><div><dt>Supply enquiry</dt><dd>{supply_format}</dd></div>
      <div><dt>Application</dt><dd><a href="/applications/{sector}.html">{application}</a></dd></div></dl>
      {link("contact.html?product="+key, "Enquire about "+title.lower())}
    </article>'''

groups = [('industrial', 'Industrial gases', industrial), ('healthcare', 'Medical oxygen and equipment', medical),
          ('specialty', 'Dry ice and cryogenic equipment', specialty)]
jumps = ''.join(f'<a href="#{key}">{title}</a>' for key,title,_ in groups)
details = ''.join(f'<section class="content-group" id="{key}"><h2>{title}</h2><div class="content-grid">{"".join(map(product_card, keys))}</div></section>' for key,title,keys in groups)
render('products.html', 'Industrial Gases, Medical Oxygen & Dry Ice | Okay Group',
       'Explore industrial and medical oxygen, nitrogen, argon, carbon dioxide, acetylene, helium, dry ice and cryogenic equipment from Okay Group and Manorama Oxygen.',
       page_head('Product catalogue', 'Gases, dry ice and equipment', 'Explore our industrial and healthcare range. Enquire about your required grade, supply format and availability.') +
       f'''<div class="wrap page-content"><nav class="jump" aria-label="Product categories">{jumps}</nav>{details}
       <section class="content-group feature" id="special-gas-enquiries">
         <h2>Looking for a specific gas or grade?</h2>
         <p>For nitrous oxide, specialty mixtures or an unlisted grade, send your specification and required volume so our team can check sourcing and availability.</p>
         {link('contact.html?product=other-gases', 'Ask about a specific gas or grade')}
       </section></div>''' + callout())

def sector_card(key, title, symbol, body, _product):
    name = title.replace('<br>', ' ')
    return f'<article class="info-card" id="{key}">{icon(symbol)}<h3>{name}</h3><p>{body}</p>{link(f"applications/{key}.html", "Gases for " + name.lower())}</article>'


sector_cards = ''.join(sector_card(*sector) for sector in sectors)
render('industries.html', 'Industries and Gas Applications | Okay Group',
       'Industrial and medical gas applications for metal fabrication, hospitals, laboratories, food and beverage and cold-chain operations in Kerala.',
       page_head('Industries and applications', 'Gas for your application', 'Explore common applications and tell us what your operation needs.') +
       f'<section class="wrap page-content"><div class="content-grid">{sector_cards}</div></section>' + callout(), 'fabrication')

supply = [
    ('cylinders', 'cylinder', 'Cylinder supply', 'For workshops, laboratories and healthcare facilities. Tell us the gas, required cylinder format, consumption and how often you need supply.', 'supply/cylinder-supply.html', 'Cylinder supply and exchanges'),
    ('liquids', 'truck', 'Liquid and bulk enquiries', 'For cryogenic or recurring requirements, include the gas, expected usage, delivery location and any existing storage. Discuss options for your site.', 'supply/bulk-liquid.html', 'Liquid and bulk supply'),
    ('dry-ice-supply', 'snow', 'Dry ice blocks', 'Share the amount of dry ice you need, dispatch date and preferred collection or delivery location.', 'supply/dry-ice-supply.html', 'Dry ice ordering and delivery'),
]
supply_cards = ''.join(f'<article class="info-card" id="{key}">{icon(symbol)}<h3>{title}</h3><p>{body}</p>{link(url, label)}</article>' for key,symbol,title,body,url,label in supply)
render('supply.html', 'Gas Supply Formats, Quality & Documentation | Okay Group',
       'Enquire about cylinder gas, bulk and cryogenic supply, or dry ice. Request the specification, safety data sheet or documentation for your order.',
       page_head('Supply and quality', 'Gas supply formats', 'Tell us what you use, where you need it and how often you need replenishment.') + f'''
<div class="wrap page-content">
  <section class="content-group" id="formats"><h2>Ways to source your gas</h2><div class="content-grid">{supply_cards}</div></section>
  <section class="content-group feature" id="quality"><p class="eyebrow">Safety and quality</p><h2>Product documentation</h2><p>Ask for the current product specification, safety data sheet and any quality documentation you need for purchasing. Include your application and required grade so the documents match the product you are ordering.</p><p>For healthcare procurement, list the documentation your facility requires when you enquire.</p>{link('supply/product-documentation.html', 'Request specifications or safety data sheets')}</section>
  <section class="content-group"><h2>Plan your delivery</h2><p>Okay Group operates branches across Kerala and delivers to all 14 districts.</p>
  <div class="inline-links">{link('locations.html', 'View Kerala delivery coverage')}{link('guides.html', 'Read the gas buying guides')}</div></section>
</div>
{callout()}''')

associated = [
    ('Manorama Carbonic Pvt. Ltd.', 'U31908KL1985PTC004154', 'Udyogamandal is listed in historical company records.'),
    ('Roopresmi Private Limited', 'U28113KL1995PTC009634', 'Corporate records document common directors with Manorama Oxygen.'),
    ('Ajay Oxygen Private Limited', 'U24111KL2011PTC027679', 'Corporate records list the same registered address as Manorama Oxygen.'),
]
associated_cards = ''.join(f'<article class="info-card"><h3>{name}</h3><p>{desc}</p><small>{cin}</small></article>' for name,cin,desc in associated)
render('companies.html', 'About Okay Group | Manorama Oxygen and Associated Companies',
       'Learn about Okay Group, Manorama Oxygen and associated companies. Based in Kalamassery, Ernakulam, Kerala since 1996.',
       page_head('About us', 'Okay Group', 'Our beginnings in Kalamassery and the companies associated with the group.') + f'''
<div class="wrap page-content">
  <section class="feature content-group" id="manorama-oxygen"><p class="eyebrow">Group company</p><h2>Manorama Oxygen Private Limited</h2><p>Manorama Oxygen was incorporated in 1996 and began with medical oxygen supply in Kalamassery. It manufactures and supplies industrial and medical gases and lists dry ice, cryogenic containers and oxygen equipment.</p>{link('manorama-oxygen.html', 'Explore Manorama Oxygen')}</section>
  <section class="content-group"><h2>Associated companies</h2><div class="content-grid">{associated_cards}</div></section>
  <section class="content-group"><h2>Branches and delivery across Kerala</h2><p class="intro">Okay Group began in Kalamassery and now operates branches across Kerala, with deliveries available in all 14 districts.</p>{link('locations.html', 'Find the branch serving your area')}</section>
</div>
{callout('Contact the Kalamassery office')}''')

render('manorama-oxygen.html', 'Manorama Oxygen Pvt. Ltd. | Gas Supplier in Kalamassery, Kochi',
       'Manorama Oxygen Private Limited, part of Okay Group, supplies industrial gases, medical oxygen, dry ice and gas equipment from Kalamassery, Kochi.',
       page_head('An Okay Group company', 'Manorama Oxygen Private Limited', 'Industrial and medical gas supply from Major Industrial Estate, Kalamassery, Kochi.') + f'''
<div class="wrap page-content">
  <div class="about-grid">
    <div><p class="eyebrow">Kalamassery, Kerala</p><h2>Supplying gases since 1996</h2><p class="intro">Manorama Oxygen began supplying medical oxygen from Kalamassery. Its product range includes industrial and medical oxygen, nitrogen, carbon dioxide, argon, helium, dry ice and related equipment.</p>
    <dl class="facts"><div><dt>Company identification number</dt><dd>U24111KL1996PTC010661</dd></div><div><dt>GSTIN</dt><dd>32AABCM6073D1ZV</dd></div></dl>
    {link('products.html', 'Browse the gas catalogue')}</div>
    <figure class="about-photo">{shot("industrial-cylinders", "Illustration of cylinders in an industrial warehouse")}<figcaption>Illustrative warehouse image</figcaption></figure>
  </div>
</div>
{callout('Enquire with Manorama Oxygen')}''',
       extra_schema={'@type':'Organization', 'name':'Manorama Oxygen Private Limited', 'url':SITE+'manorama-oxygen.html',
                     'taxID':'32AABCM6073D1ZV', 'foundingDate':'1996-08-19', 'parentOrganization':{'@type':'Organization', 'name':'Okay Group', 'url':SITE}})

options = ''.join(f'<option value="{key}">{title}</option>' for key,(title,_,_) in products.items())
district_options = ''.join(f'<option>{district}</option>' for district in DISTRICTS)
render('contact.html', 'Enquiries & Directions | Okay Group, Kalamassery',
       'Contact the Okay Group and Manorama Oxygen office in Kalamassery, Ernakulam for gas supply, quotes, availability and product documentation.',
       page_head('Contact', 'Talk to our team', 'Request a quote, confirm your nearest branch or arrange delivery anywhere in Kerala.') + f'''
<section class="wrap page-content two-column">
  <div class="feature contact-details"><p class="eyebrow">Corporate office</p><h2>Kalamassery</h2>
    <address>Major Industrial Estate<br>Kalamassery, Ernakulam<br>Kerala, India</address>
    {link('mailto:'+EMAIL, EMAIL)}{link(MAP, 'Get directions')}{link(INDIAMART+'enquiry.html', 'Enquire via IndiaMART')}
    {link('locations.html', 'Kerala branches and delivery')}
  </div>
  <div class="form-card"><h2>Supply enquiry</h2>
    <p>Include your required grade, quantity and delivery date if known.</p>
    <form id="enquiry-form" data-email="{EMAIL}" hidden>
      <div class="form-grid">
        <label>Name<input name="name" autocomplete="name" required maxlength="120"></label>
        <label>Company or facility<input name="company" autocomplete="organization" maxlength="120"></label>
        <label>Email<input name="email" type="email" autocomplete="email" required maxlength="160"></label>
        <label>Delivery district<select name="district"><option value="">Select a district</option>{district_options}</select></label>
        <label>Delivery town or suburb<input name="location" autocomplete="address-level2" maxlength="120"></label>
        <label>Delivery PIN code<input name="postcode" inputmode="numeric" autocomplete="postal-code" pattern="[1-9][0-9]{{5}}" maxlength="6" title="Enter a six-digit Indian PIN code"></label>
        <label class="wide">Product or enquiry<select name="product"><option value="general">General supply</option>{options}<option value="bulk-liquid">Liquid or bulk supply</option><option value="other-gases">Specialty gas or specific grade</option><option value="documentation">Product documentation</option><option value="delivery">Branch or delivery enquiry</option></select></label>
        <label class="wide">Requirements<textarea name="requirements" rows="4" required maxlength="700"></textarea></label>
      </div>
      <div class="form-actions"><button class="button" type="submit">Open email draft {icon('mail')}</button><button class="button outline" type="button" id="copy-enquiry" hidden>Copy enquiry</button></div>
      <p class="form-status" id="enquiry-status" role="status">Review and send the draft from your email app.</p>
    </form>
    <noscript><a class="button navy" href="mailto:{EMAIL}?subject=Supply%20enquiry">Email Okay Group</a></noscript>
  </div>
</section>''')

render('404.html', 'Page not found | Okay Group', 'The requested page could not be found.',
       page_head('404', 'Page not found', 'Use the links below to get back to the website.') +
       f'<section class="wrap page-content">{button("/", "Back to home")} {button("/products.html", "Browse products", "navy")}</section>')

def body_sections(sections):
    return ''.join(f'<section><h2>{escape(heading)}</h2><p>{escape(copy)}</p></section>' for heading, copy in sections)


def related_products(keys):
    return [(f'gases/{key}.html', products[key][0]) for key in keys]


def detail_body(sections, related, related_title='Explore related pages'):
    links = ''.join(f'<li>{link(path, escape(name))}</li>' for path, name in related)
    return f'''<div class="wrap page-content detail-layout">
  <article class="detail-copy">{body_sections(sections)}</article>
  <aside class="detail-aside" aria-label="{related_title}">
    <h2>{related_title}</h2><ul>{links}</ul>
  </aside>
</div>'''


for key, (heading, description, sections, related) in PRODUCT_DETAILS.items():
    name, _, intro = products[key]
    category = product_specs[key][3]
    path = f'gases/{key}.html'
    path_enquiry = f'contact.html?product={key}'
    sector_title = next(title.replace('<br>', ' ') for slug, title, *_ in sectors if slug == category)
    related_links = related_products(related) + [
        (f'applications/{category}.html', sector_title),
        ('locations.html', 'Kerala delivery coverage'),
    ]
    render(
        path, heading + ' | Okay Group', description,
        page_head('Our gases', escape(heading), escape(intro), button(path_enquiry, 'Request a quote'))
        + detail_body(sections, related_links, 'Related products and applications')
        + callout(f'Enquire about {name.lower()}', enquiry=path_enquiry),
        product_art[key],
        extra_schema={
            '@type': 'Product', '@id': SITE + path + '#product',
            'name': name, 'url': SITE + path, 'description': description,
        },
        trail=(('products.html', 'Our gases'), (path, name)),
    )


for key, (heading, description, sections, related) in APPLICATION_DETAILS.items():
    path = f'applications/{key}.html'
    short_title = next(title.replace('<br>', ' ') for slug, title, *_ in sectors if slug == key)
    photo = {'fabrication': 'fabrication', 'healthcare': 'medical', 'welding': 'fabrication', 'cold-chain': 'dry-ice'}.get(key, 'gas-facility')
    render(
        path, heading + ' | Okay Group', description,
        page_head('Industries and applications', escape(heading), escape(description))
        + detail_body(sections, related_products(related) + [('guides/request-a-gas-quote.html', 'How to request a gas quote')], 'Relevant gases and equipment')
        + callout(),
        photo,
        trail=(('industries.html', 'Industries'), (path, short_title)),
    )


for key, (heading, description, sections, related, enquiry, photo) in SUPPLY_DETAILS.items():
    path = f'supply/{key}.html'
    render(
        path, heading + ' | Okay Group', description,
        page_head('Supply and quality', escape(heading), escape(description))
        + detail_body(sections, related_products(related) + [('locations.html', 'Kerala delivery coverage'), ('guides.html', 'Gas buying guides')])
        + callout(enquiry=f'contact.html?product={enquiry}'),
        photo,
        trail=(('supply.html', 'Supply and quality'), (path, heading)),
    )


guide_cards = ''.join(
    f'<article class="info-card"><h3><a href="/guides/{key}.html">{escape(heading)}</a></h3><p>{escape(description)}</p></article>'
    for key, (heading, description, _, _) in GUIDES.items()
)
render(
    'guides.html', 'Industrial Gas Buying and Supply Guides | Okay Group',
    'Practical industrial gas buying guides for Kerala customers. Learn how to specify grade, compare supply formats, request a quote and plan regular delivery.',
    page_head('Buyer resources', 'Gas buying guides', 'Plan gas orders, compare cylinder and liquid supply, and send a complete enquiry to the team.')
    + f'<section class="wrap page-content"><h2 class="resource-heading">Purchasing and delivery</h2><div class="content-grid">{guide_cards}</div></section>'
    + callout(),
    trail=(('guides.html', 'Gas buying guides'),),
)

linked_titles = {
    'locations.html': 'Kerala branches and delivery',
    **{f'supply/{key}.html': entry[0] for key, entry in SUPPLY_DETAILS.items()},
    **{f'applications/{key}.html': entry[0] for key, entry in APPLICATION_DETAILS.items()},
    **{f'gases/{key}.html': entry[0] for key, entry in products.items()},
}
for key, (heading, description, sections, related) in GUIDES.items():
    path = f'guides/{key}.html'
    render(
        path, heading + ' | Okay Group', description,
        page_head('Gas buying guides', escape(heading), escape(description))
        + detail_body(sections, [(path, linked_titles[path]) for path in related])
        + callout(),
        extra_schema={
            '@type': 'Article', 'headline': heading, 'description': description,
            'mainEntityOfPage': SITE + path, 'inLanguage': 'en-IN',
            'author': {'@type': 'Organization', '@id': SITE + '#organization', 'name': 'Okay Group', 'url': SITE},
        },
        trail=(('guides.html', 'Gas buying guides'), (path, heading)),
        article=True,
    )


districts = ''.join(f'<li>{district}</li>' for district in DISTRICTS)
render(
    'locations.html', 'Kerala Gas Delivery & Branch Coverage | Okay Group',
    'Okay Group operates branches across Kerala and delivers to all 14 districts. Find your nearest branch and request industrial gas, medical oxygen or dry ice delivery.',
    page_head('Statewide coverage', 'Gas delivery across Kerala', 'Okay Group operates branches across Kerala and delivers to all 14 districts. Tell us your delivery PIN code to find the branch serving your site.')
    + f'''<div class="wrap page-content">
  <section class="content-group" aria-labelledby="district-heading">
    <h2 id="district-heading">Districts we deliver to</h2><ul class="district-grid">{districts}</ul>
  </section>
  <section class="content-group two-column" aria-label="Branches and order details">
    <div class="feature contact-details"><p class="eyebrow">Corporate office</p><h2>Kalamassery, Kochi</h2>
    <address>Major Industrial Estate<br>Kalamassery, Ernakulam<br>Kerala, India</address>
    {link(MAP, 'Get directions to the corporate office')}{link('mailto:' + EMAIL, EMAIL)}</div>
    <div class="detail-copy"><section><h2>Find the branch serving your site</h2>
    <p>Send the town, district and PIN code, along with the gas and quantity. Our team can confirm the branch serving your address, availability and the delivery arrangements for your order.</p></section>
    <section><h2>Arrange a regular delivery</h2><p>For recurring orders, share how much you use, when you can receive supplies and whether you have multiple delivery locations.</p>
    {link('guides/planning-recurring-delivery.html', 'Plan recurring deliveries')}</section></div>
  </section>
</div>'''
    + callout('Enquire about your nearest branch or delivery', enquiry='contact.html?product=delivery'),
    extra_schema={
        '@type': 'Service', 'name': 'Industrial and medical gas delivery in Kerala',
        'url': SITE + 'locations.html',
        'provider': {'@id': SITE + '#organization'},
        'areaServed': {'@type': 'State', 'name': 'Kerala'},
    },
    trail=(('locations.html', 'Kerala branches and delivery'),),
)


(ROOT / 'sitemap.xml').write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + ''.join(f'  <url><loc>{url}</loc></url>\n' for url in sorted(PAGES))
    + '</urlset>\n',
    encoding='utf-8',
)
