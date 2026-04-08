"""
cch_template.py
───────────────────────────────────────────────────────────────
Carolina Crafted Homes — PDF Guide Standard Template
───────────────────────────────────────────────────────────────
Import this file in every guide script. Never edit this file
unless you are updating the CCH brand standard.

Usage in a guide script:
    from cch_template import *
    
    def build():
        out = '/path/to/output.pdf'
        doc = make_doc(out)
        S, CW = make_styles(), doc_content_width()
        story = []
        # ... add content ...
        doc.build(story, onFirstPage=cch_footer, onLaterPages=cch_footer)

    build()
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    HRFlowable, Table, TableStyle, KeepTogether
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import Flowable

# ── Page size ─────────────────────────────────────────────────────────────────
W, H = letter

# ── Brand Colors ──────────────────────────────────────────────────────────────
NAVY       = colors.HexColor('#1e3350')
NAVY_MID   = colors.HexColor('#2e4a6b')
STEEL      = colors.HexColor('#6b8cae')
LIGHT_BLUE = colors.HexColor('#ddedf8')
WHITE      = colors.white
GOLD       = colors.HexColor('#c9a84c')

# ── Asset Paths ───────────────────────────────────────────────────────────────
# Update these paths if assets are moved
SKYLINE_PATH = '/home/claude/cch_skyline_clean.png'
LOGO_PATH    = '/home/claude/cch_logo_clean.png'

# ── Footer dimensions ─────────────────────────────────────────────────────────
SKYLINE_W    = W
SKYLINE_H    = int(W * 300 / 1280)   # ~143pt — preserves aspect ratio
FOOTER_BAR_H = 40
GOLD_LINE_H  = 3


# ── Standard Footer ───────────────────────────────────────────────────────────
# Layering: navy bar → gold line → skyline (50% opacity) → white text
def cch_footer(canvas, doc):
    canvas.saveState()
    # 1 — Navy bar
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, W, FOOTER_BAR_H, fill=1, stroke=0)
    # 2 — Gold accent line
    canvas.setFillColor(GOLD)
    canvas.rect(0, FOOTER_BAR_H, W, GOLD_LINE_H, fill=1, stroke=0)
    # 3 — Skyline at 50% opacity
    canvas.saveState()
    canvas.setFillAlpha(0.5)
    canvas.setStrokeAlpha(0.5)
    canvas.drawImage(SKYLINE_PATH, 0, 0,
                     width=SKYLINE_W, height=SKYLINE_H,
                     preserveAspectRatio=False, mask='auto')
    canvas.restoreState()
    # 4 — Footer text with outline for readability
    label      = 'Carolina Crafted Homes  ·  Myrtle Beach, SC  ·  (704) 910-9111'
    page_label = f'Page {doc.page}'
    canvas.setFont('Helvetica-Bold', 8)
    canvas.setFillColor(NAVY)
    for dx, dy in [(-0.6,0),(0.6,0),(0,-0.6),(0,0.6)]:
        canvas.drawString(inch*0.75 + dx, 14 + dy, label)
        canvas.drawRightString(W - inch*0.75 + dx, 14 + dy, page_label)
    canvas.setFillColor(WHITE)
    canvas.drawString(inch*0.75, 14, label)
    canvas.drawRightString(W - inch*0.75, 14, page_label)
    canvas.restoreState()


# ── Document factory ──────────────────────────────────────────────────────────
def make_doc(output_path):
    """Create a standard CCH SimpleDocTemplate."""
    return SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=0.75*inch,
        rightMargin=0.75*inch,
        topMargin=0.55*inch,
        bottomMargin=0.6*inch,
    )

def doc_content_width():
    return W - 1.5*inch


# ── Custom Flowables ──────────────────────────────────────────────────────────

class HeaderBanner(Flowable):
    """Cover page hero banner with logo, title, subtitle, eyebrow."""
    def __init__(self, width, height, title, subtitle, eyebrow):
        Flowable.__init__(self)
        self.width    = width
        self.height   = height
        self.title    = title
        self.subtitle = subtitle
        self.eyebrow  = eyebrow

    def wrap(self, aW, aH):
        return self.width, self.height

    def draw(self):
        c = self.canv
        c.setFillColor(NAVY)
        c.rect(0, 0, self.width, self.height, fill=1, stroke=0)
        c.setFillColor(GOLD)
        c.rect(0, self.height - 6, self.width, 6, fill=1, stroke=0)

        # Logo right side
        logo_size = 170
        logo_x = self.width - logo_size - 20
        logo_y = (self.height - logo_size) / 2 - 10
        c.drawImage(LOGO_PATH, logo_x, logo_y,
                    width=logo_size, height=logo_size,
                    preserveAspectRatio=True, mask='auto')

        text_w = self.width - logo_size - 60
        tx = 36

        # Eyebrow
        c.setFillColor(STEEL)
        c.setFont('Helvetica', 9)
        c.drawString(tx, self.height - 48, self.eyebrow.upper())

        # Title
        c.setFillColor(WHITE)
        c.setFont('Helvetica-Bold', 26)
        words = self.title.split()
        lines, line = [], []
        for w in words:
            test = ' '.join(line + [w])
            if c.stringWidth(test, 'Helvetica-Bold', 26) < text_w:
                line.append(w)
            else:
                lines.append(' '.join(line))
                line = [w]
        if line:
            lines.append(' '.join(line))
        y = self.height - 82
        for ln in lines:
            c.drawString(tx, y, ln)
            y -= 34

        # Subtitle
        c.setFillColor(LIGHT_BLUE)
        c.setFont('Helvetica', 11)
        c.drawString(tx, y - 6, self.subtitle)

        # Bottom brand line
        c.setFillColor(GOLD)
        c.rect(0, 0, self.width, 3, fill=1, stroke=0)
        c.setFillColor(colors.HexColor('#a0b8cc'))
        c.setFont('Helvetica', 8)
        label = 'carolinacraftedhomes.com  ·  (704) 910-9111  ·  Myrtle Beach, SC'
        lw = c.stringWidth(label, 'Helvetica', 8)
        c.drawString(tx, 10, label)
        c.linkURL('https://www.carolinacraftedhomes.com/', (tx, 6, tx + lw, 20), relative=1)


class SectionHeader(Flowable):
    """Navy bar with gold left accent — use at the start of every section."""
    def __init__(self, text, width):
        Flowable.__init__(self)
        self.text  = text
        self.width = width
        self.height = 34

    def wrap(self, aW, aH):
        return self.width, self.height

    def draw(self):
        c = self.canv
        c.setFillColor(NAVY)
        c.roundRect(0, 0, self.width, self.height, 4, fill=1, stroke=0)
        c.setFillColor(GOLD)
        c.rect(0, 0, 5, self.height, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont('Helvetica-Bold', 11)
        c.drawString(18, 11, self.text.upper())


class TipBox(Flowable):
    """Light blue tip box with gold left border. Auto-sizes to text."""
    def __init__(self, text, width):
        Flowable.__init__(self)
        self.text  = text
        self.width = width
        chars_per_line = int((width - 32) / 5.2)
        n_lines = max(2, -(-len(text) // chars_per_line))
        self.height = 24 + n_lines * 14

    def wrap(self, aW, aH):
        return self.width, self.height

    def draw(self):
        c = self.canv
        c.setFillColor(LIGHT_BLUE)
        c.roundRect(0, 0, self.width, self.height, 5, fill=1, stroke=0)
        c.setFillColor(GOLD)
        c.rect(0, 0, 5, self.height, fill=1, stroke=0)
        c.setFillColor(NAVY_MID)
        c.setFont('Helvetica-Bold', 8)
        c.drawString(16, self.height - 14, 'CCH TIP')
        c.setFillColor(NAVY)
        c.setFont('Helvetica', 9)
        words = self.text.split()
        lines, line = [], []
        for w in words:
            test = ' '.join(line + [w])
            if c.stringWidth(test, 'Helvetica', 9) < self.width - 28:
                line.append(w)
            else:
                lines.append(' '.join(line))
                line = [w]
        if line:
            lines.append(' '.join(line))
        y = self.height - 28
        for ln in lines:
            c.drawString(16, y, ln)
            y -= 13


class ContactCard(Flowable):
    """
    Standard CCH contact card with fully clickable links.
    Always appears on the last page of every guide.
    """
    def __init__(self, width):
        Flowable.__init__(self)
        self.width  = width
        self.height = 200

    def wrap(self, aW, aH):
        return self.width, self.height

    def draw(self):
        c = self.canv
        # Header
        c.setFillColor(NAVY)
        c.rect(0, self.height - 40, self.width, 40, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont('Helvetica-Bold', 12)
        c.drawCentredString(self.width/2, self.height - 26, 'READY TO GET STARTED?')
        # Body background
        c.setFillColor(LIGHT_BLUE)
        c.rect(0, 0, self.width, self.height - 40, fill=1, stroke=0)
        # Names
        c.setFillColor(NAVY)
        c.setFont('Helvetica-Bold', 14)
        c.drawCentredString(self.width/2, self.height - 68, 'Frank Hereda & Tiffany Hereda')
        # Company
        c.setFont('Helvetica-Bold', 11)
        c.drawCentredString(self.width/2, self.height - 88, 'Carolina Crafted Homes')
        # Address
        c.setFont('Helvetica', 10)
        c.drawCentredString(self.width/2, self.height - 106,
                            '4702 Oleander Dr, Suite 300  ·  Myrtle Beach, SC 29577')
        c.setFillColor(NAVY_MID)
        # Phone
        phone = '(704) 910-9111'
        pw = c.stringWidth(phone, 'Helvetica', 10)
        px = self.width/2 - pw/2
        py = self.height - 122
        c.drawString(px, py, phone)
        c.linkURL('tel:+17049109111', (px, py-2, px+pw, py+12), relative=1)
        # Email
        email = 'info@carolinacraftedhomes.com'
        ew = c.stringWidth(email, 'Helvetica', 10)
        ex = self.width/2 - ew/2
        ey = self.height - 138
        c.drawString(ex, ey, email)
        c.linkURL('mailto:info@carolinacraftedhomes.com', (ex, ey-2, ex+ew, ey+12), relative=1)
        # Website
        site = 'carolinacraftedhomes.com'
        sw = c.stringWidth(site, 'Helvetica', 10)
        sx = self.width/2 - sw/2
        sy = self.height - 154
        c.drawString(sx, sy, site)
        c.linkURL('https://www.carolinacraftedhomes.com/', (sx, sy-2, sx+sw, sy+12), relative=1)
        # Facebook
        c.setFillColor(NAVY)
        c.setFont('Helvetica', 9)
        fb = 'Facebook: /CarolinaCraftedHomes'
        fbw = c.stringWidth(fb, 'Helvetica', 9)
        fbx = self.width/2 - fbw/2
        fby = self.height - 170
        c.drawString(fbx, fby, fb)
        c.linkURL('https://www.facebook.com/CarolinaCraftedHomes', (fbx, fby-2, fbx+fbw, fby+11), relative=1)
        # YouTube
        yt = 'YouTube: @carolinacraftedhomes'
        ytw = c.stringWidth(yt, 'Helvetica', 9)
        ytx = self.width/2 - ytw/2
        yty = self.height - 184
        c.drawString(ytx, yty, yt)
        c.linkURL('https://www.youtube.com/@carolinacraftedhomes', (ytx, yty-2, ytx+ytw, yty+11), relative=1)


# ── Styles ────────────────────────────────────────────────────────────────────
def make_styles():
    base = dict(fontName='Helvetica', fontSize=10, leading=16,
                textColor=NAVY, spaceAfter=8)
    return {
        'body':      ParagraphStyle('body',      **base, alignment=TA_JUSTIFY),
        'body_left': ParagraphStyle('body_left', **base, alignment=TA_LEFT),
        'h2':        ParagraphStyle('h2',  fontName='Helvetica-Bold', fontSize=15,
                                    textColor=NAVY, spaceBefore=18, spaceAfter=6, leading=20),
        'h3':        ParagraphStyle('h3',  fontName='Helvetica-Bold', fontSize=11,
                                    textColor=NAVY_MID, spaceBefore=12, spaceAfter=4, leading=15),
        'bullet':    ParagraphStyle('bullet', fontName='Helvetica', fontSize=10,
                                    textColor=NAVY, leftIndent=18, bulletIndent=6,
                                    spaceBefore=2, spaceAfter=2, leading=15),
        'disc':      ParagraphStyle('disc', fontName='Helvetica-Oblique', fontSize=8,
                                    textColor=STEEL, alignment=TA_CENTER, leading=13),
    }


# ── Table builder ─────────────────────────────────────────────────────────────
def make_table(data, col_widths, header_bg=NAVY):
    """Standard CCH branded table. Never splits across pages."""
    t = Table(data, colWidths=col_widths, splitByRow=0)
    t.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,0),  header_bg),
        ('TEXTCOLOR',     (0,0), (-1,0),  WHITE),
        ('FONTNAME',      (0,0), (-1,0),  'Helvetica-Bold'),
        ('FONTSIZE',      (0,0), (-1,-1), 9),
        ('TEXTCOLOR',     (0,1), (-1,-1), NAVY),
        ('ROWBACKGROUNDS',(0,1), (-1,-1), [WHITE, LIGHT_BLUE]),
        ('GRID',          (0,0), (-1,-1), 0.5, STEEL),
        ('TOPPADDING',    (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('LEFTPADDING',   (0,0), (-1,-1), 10),
        ('VALIGN',        (0,0), (-1,-1), 'TOP'),
    ]))
    return t


# ── Standard TOC builder ──────────────────────────────────────────────────────
def make_toc(sections, content_width):
    """
    Build a standard CCH table of contents.
    sections = list of strings e.g. ['01  —  Are You Ready to Buy?', ...]
    """
    rows = ["WHAT'S INSIDE THIS GUIDE"] + sections
    toc = Table([[r] for r in rows], colWidths=[content_width], splitByRow=0)
    toc.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,0),  NAVY),
        ('TEXTCOLOR',     (0,0), (-1,0),  WHITE),
        ('FONTNAME',      (0,0), (-1,0),  'Helvetica-Bold'),
        ('FONTSIZE',      (0,0), (-1,0),  11),
        ('ROWBACKGROUNDS',(0,1), (-1,-1), [LIGHT_BLUE, WHITE]),
        ('TEXTCOLOR',     (0,1), (-1,-1), NAVY),
        ('FONTNAME',      (0,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE',      (0,1), (-1,-1), 10),
        ('TOPPADDING',    (0,0), (-1,-1), 9),
        ('BOTTOMPADDING', (0,0), (-1,-1), 9),
        ('LEFTPADDING',   (0,0), (-1,-1), 16),
    ]))
    return toc


# ── Standard disclaimer ───────────────────────────────────────────────────────
def disclaimer(styles):
    return Paragraph(
        'This guide was prepared by Carolina Crafted Homes for educational purposes. '
        'Content draws on resources from the Coastal Carolinas Association of REALTORS® '
        'and the National Association of REALTORS®. For personalized advice, consult '
        'a licensed real estate professional.',
        styles['disc']
    )
