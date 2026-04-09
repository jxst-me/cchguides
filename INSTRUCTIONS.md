# CCH Guides Project — Instructions & Navigation Guide

**Carolina Crafted Homes · Frank & Tiffany Hereda**
Last updated: April 2026

---

## What This Project Is

This project generates branded PDF guides and landing pages for Carolina Crafted Homes lead generation. Every guide uses the same visual template — navy/gold branding, Myrtle Beach skyline footer, CCH logo, and clickable contact links — so all guides look consistent and professional.

**The golden rule: Never edit `cch_template.py` for content changes. Only edit the individual guide files.**

---

## Project Structure

```
cch-guides/
├── cch_template.py                    ← Brand standard. DO NOT EDIT for content.
├── assets/
│   ├── cch_logo_clean.png             ← CCH logo (transparent background)
│   └── cch_skyline_clean.png          ← Myrtle Beach skyline (transparent background)
├── guides/
│   ├── output/                        ← Generated PDFs go here
│   ├── guide_01_buying_first_home.py  ← Guide #01
│   └── guide_02_selling_your_home.py  ← Guide #02
└── landing-pages/
    └── buying-guide.html              ← Lead capture landing page (MailerLite)
```

---

## How to Generate a PDF Guide

Run any guide script from the `cch-guides/` folder:

```bash
python guides/guide_01_buying_first_home.py
python guides/guide_02_selling_your_home.py
```

The PDF will be saved to `guides/output/`.

**Requirements:**
- Python 3.8+
- `reportlab` installed: `pip install reportlab`
- Asset files must be in `assets/` folder
- `cch_template.py` must be in the same root folder

---

## How to Create a New Guide (Step by Step)

### Step 1 — Copy an existing guide
```bash
cp guides/guide_02_selling_your_home.py guides/guide_03_investing.py
```

### Step 2 — Open the new file and update the header
```python
"""
guide_03_investing.py
CCH Guide #03 — Investing in Myrtle Beach Real Estate
Output: CCH_Guide_03_Investing.pdf
"""
```

### Step 3 — Update the OUTPUT path
```python
OUTPUT = '/path/to/output/CCH_Guide_03_Investing.pdf'
```

### Step 4 — Update the Cover Banner
```python
story.append(HeaderBanner(
    CW, 220,                                    # width, height (220 fits intro + TOC on one page)
    title    = 'Your New Guide Title Here',     # main headline
    subtitle = 'Subtitle line here',            # smaller line below title
    eyebrow  = 'Carolina Crafted Homes  ·  Free Consumer Guide',  # keep this
))
```

### Step 5 — Update the intro paragraph
Keep it to 2–3 sentences. This sits between the banner and the TOC.

### Step 6 — Update the Table of Contents
```python
story.append(make_toc([
    '01  —  Your First Section Title',
    '02  —  Your Second Section Title',
    '03  —  Your Third Section Title',
    # ... up to 10 sections
], CW))
```

### Step 7 — Add sections
Each section follows this pattern:

```python
# ── SECTION 01 ────────────────────────────────────────────────────────────
story.append(PageBreak())                          # always start sections on a new page
story.append(SectionHeader('01 — Section Title', CW))
story.append(Spacer(1, 10))
story.append(Paragraph('Intro text here.', S['body']))
```

### Step 8 — Always end with the contact card
```python
story.append(ContactCard(CW))
story.append(Spacer(1, 4))
story.append(disclaimer(S))
```

### Step 9 — Build
```bash
python guides/guide_03_investing.py
```

---

## Content Building Blocks

These are all the components available from `cch_template.py`:

### Text Styles — `S['style_name']`

| Style | Use For | Notes |
|-------|---------|-------|
| `S['body']` | Body paragraphs | Justified text |
| `S['body_left']` | Body paragraphs | Left-aligned |
| `S['h2']` | Major headings | Large, bold |
| `S['h3']` | Sub-headings | Medium, bold, navy-mid color |
| `S['bullet']` | Bullet point items | Indented, use with `• ` prefix |
| `S['disc']` | Disclaimer text | Small, italic, grey |

**Example:**
```python
story.append(Paragraph('Your heading here', S['h3']))
story.append(Paragraph('• <b>Bold label:</b> Regular text here.', S['bullet']))
story.append(Paragraph('Body text goes here.', S['body']))
```

---

### Tip Box — `TipBox(text, CW)`
Light blue box with gold left border and "CCH TIP" label. Use for actionable advice.

```python
story.append(TipBox(
    'Your tip text goes here. Keep it to 1–2 sentences for best results.', CW))
```

---

### Section Header — `SectionHeader('XX — Title', CW)`
Navy bar with gold left accent. Always use at the start of each section.

```python
story.append(SectionHeader('03 — Your Section Title', CW))
```

---

### Standard Table — `make_table(data, col_widths)`
Branded table with navy header row, alternating light blue/white rows.

```python
story.append(make_table([
    ['COLUMN 1',  'COLUMN 2',  'COLUMN 3'],   # header row — always ALL CAPS
    ['Row 1 A',   'Row 1 B',   'Row 1 C'],
    ['Row 2 A',   'Row 2 B',   'Row 2 C'],
], [CW*0.30, CW*0.40, CW*0.30]))              # column widths must add up to CW (or close)
```

**Important:** If cell text is long (more than ~40 characters), use `Paragraph` objects inside the table instead of plain strings so text wraps properly:

```python
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT

cell_s = ParagraphStyle('cs', fontName='Helvetica',      fontSize=9, textColor=NAVY, leading=13)
cell_b = ParagraphStyle('cb', fontName='Helvetica-Bold', fontSize=9, textColor=NAVY, leading=13)
hdr_s  = ParagraphStyle('ch', fontName='Helvetica-Bold', fontSize=9, textColor=WHITE, leading=13)

story.append(Table([
    [Paragraph('COLUMN 1', hdr_s), Paragraph('COLUMN 2', hdr_s)],
    [Paragraph('Short text', cell_b), Paragraph('This is a longer sentence that needs to wrap properly across multiple lines', cell_s)],
], colWidths=[CW*0.35, CW*0.65], splitByRow=0))
```

---

### Keep Together — `KeepTogether([...])`
Prevents a heading from being separated from its content across a page break.

```python
story.append(KeepTogether([
    Paragraph('Sub-heading', S['h3']),
    make_table([...], [...]),
]))
```

---

### Page Break
Always add a `PageBreak()` before each section header.

```python
story.append(PageBreak())
story.append(SectionHeader('04 — Next Section', CW))
```

---

### Spacer
Adds vertical space between elements.

```python
story.append(Spacer(1, 10))   # small gap
story.append(Spacer(1, 18))   # medium gap
```

---

### Contact Card — `ContactCard(CW)`
Standard CCH contact card with clickable links. Always use on the last page.
Frank & Tiffany Hereda · (704) 910-9111 · info@carolinacraftedhomes.com
All links (phone, email, website, Facebook, YouTube) are pre-configured.

```python
story.append(ContactCard(CW))
```

---

### Disclaimer — `disclaimer(S)`
Standard legal disclaimer. Always place after the ContactCard.

```python
story.append(disclaimer(S))
```

---

### Table of Contents — `make_toc(sections, CW)`
Standard CCH branded TOC. Pass a list of section title strings.

```python
story.append(make_toc([
    '01  —  Section One',
    '02  —  Section Two',
], CW))
```

---

## Cover Banner Height Guide

The `HeaderBanner` height controls how much space the cover image takes up.

| Height | Best For |
|--------|---------|
| `290` | Cover only — no intro text or TOC on cover page |
| `220` | Intro paragraph + TOC fits on same page as banner |
| `180` | Short intro + long TOC (10 sections) |

---

## Common Patterns

### Bullet list section
```python
story.append(Paragraph('Sub-heading', S['h3']))
for item in [
    '<b>Label:</b> Description of the item here.',
    '<b>Label:</b> Description of the item here.',
    '<b>Label:</b> Description of the item here.',
]:
    story.append(Paragraph(f'• {item}', S['bullet']))
```

### Numbered Q&A (questions with answers)
```python
for i, (q, a) in enumerate([
    ('Question text here?', 'Answer text here.'),
    ('Another question?',   'Another answer.'),
]):
    story.append(KeepTogether([
        Paragraph(f'<b>{i+1}.  {q}</b>', S['h3']),
        Paragraph(a, S['body_left']),
        Spacer(1, 4),
    ]))
```

### Checklist table with tick boxes
```python
tick  = '☐  '
hdr_s = ParagraphStyle('ch', fontName='Helvetica-Bold', fontSize=9, textColor=WHITE, leading=13)
cell_b = ParagraphStyle('cb', fontName='Helvetica-Bold', fontSize=9, textColor=NAVY,  leading=13)
cell_s = ParagraphStyle('cs', fontName='Helvetica',      fontSize=9, textColor=NAVY,  leading=13)

data = [
    [Paragraph('', hdr_s),       Paragraph('TASK', hdr_s),       Paragraph('NOTE', hdr_s)],
    [Paragraph(tick, cell_b),    Paragraph('Task one', cell_s),   Paragraph('Why it matters', cell_s)],
    [Paragraph(tick, cell_b),    Paragraph('Task two', cell_s),   Paragraph('Why it matters', cell_s)],
]
t = Table(data, colWidths=[CW*0.07, CW*0.43, CW*0.50], splitByRow=0)
t.setStyle(TableStyle([
    ('BACKGROUND',    (0,0), (-1,0),  NAVY),
    ('ROWBACKGROUNDS',(0,1), (-1,-1), [WHITE, LIGHT_BLUE]),
    ('GRID',          (0,0), (-1,-1), 0.5, STEEL),
    ('TOPPADDING',    (0,0), (-1,-1), 6),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ('LEFTPADDING',   (0,0), (-1,-1), 8),
    ('VALIGN',        (0,0), (-1,-1), 'TOP'),
]))
story.append(t)
```

---

## Guides Tracker

| # | File | Title | Status | PDF in Drive |
|---|------|-------|--------|--------------|
| 01 | `guide_01_buying_first_home.py` | Buying Your First Home in Myrtle Beach | ✅ Done | ✅ Yes |
| 02 | `guide_02_selling_your_home.py` | Selling Your Home on the Grand Strand | ✅ Done | ⬜ Upload |
| 03 | `guide_03_investing.py` | Investing in Myrtle Beach Real Estate | 📋 Planned | — |
| 04 | `guide_04_building_renovating.py` | Building & Renovating on the Grand Strand | 📋 Planned | — |

---

## Landing Pages Tracker

| Guide | Landing Page File | MailerLite Group | Live URL | PDF Link |
|-------|-------------------|------------------|----------|----------|
| Buying Guide | `buying-guide.html` | Buying Guide Leads (184205290429745140) | jxst-me.github.io/cchguides/buying-guide.html | ✅ Set |
| Selling Guide | `selling-guide.html` | — | — | — |

---

## Quick Checklist When Creating a New Guide

- [ ] Copy an existing guide file and rename it
- [ ] Update the docstring at the top
- [ ] Update `OUTPUT` path
- [ ] Update `HeaderBanner` title, subtitle
- [ ] Update intro paragraph (2–3 sentences)
- [ ] Update `make_toc()` list
- [ ] Write all sections (each starts with `PageBreak()` + `SectionHeader()`)
- [ ] End with `ContactCard(CW)` and `disclaimer(S)`
- [ ] Run the script and check the PDF
- [ ] Upload PDF to Google Drive
- [ ] Update Guides Tracker table above
- [ ] Create landing page for new guide
- [ ] Set up MailerLite automation for new guide

---

## Contact & Support

**Frank & Tiffany Hereda — Carolina Crafted Homes**
- 📞 (704) 910-9111
- 📧 info@carolinacraftedhomes.com
- 🌐 carolinacraftedhomes.com
- 📍 4702 Oleander Dr, Suite 300 · Myrtle Beach, SC 29577
