"""
guide_01_buying_first_home.py
───────────────────────────────────────────────────────────────
CCH Guide #01 — Buying Your First Home in Myrtle Beach
───────────────────────────────────────────────────────────────
To generate the PDF, run:
    python guide_01_buying_first_home.py

Template: cch_template.py  (do not edit for content changes)
Output:   CCH_Guide_01_Buying_Your_First_Home.pdf
"""

from cch_template import *

OUTPUT = '/mnt/user-data/outputs/CCH_Guide_01_Buying_Your_First_Home.pdf'

def build():
    doc = make_doc(OUTPUT)
    S   = make_styles()
    CW  = doc_content_width()
    story = []

    # ── COVER ─────────────────────────────────────────────────────────────────
    story.append(HeaderBanner(
        CW, 290,
        title    = 'Buying Your First Home in Myrtle Beach',
        subtitle = 'A Step-by-Step Guide for Grand Strand Homebuyers',
        eyebrow  = 'Carolina Crafted Homes  ·  Free Consumer Guide',
    ))
    story.append(Spacer(1, 20))
    story.append(Paragraph(
        'Buying your first home is one of the most exciting — and most significant — '
        'financial decisions you will ever make. The Myrtle Beach market offers incredible '
        'opportunity, but navigating it successfully requires the right knowledge and the '
        'right team. This guide was created by Frank & Tiffany Hereda at Carolina Crafted '
        'Homes to give you a clear, honest roadmap from your very first question to closing day.',
        S['body']))
    story.append(Spacer(1, 14))
    story.append(make_toc([
        '01  —  Are You Ready to Buy?',
        '02  —  Getting Pre-Approved for a Mortgage',
        '03  —  Finding the Right Home',
        '04  —  Making an Offer & Negotiating',
        '05  —  From Contract to Closing',
        '06  —  Protecting Your Investment',
        '07  —  10 Questions to Ask Your Agent',
        '08  —  Your Carolina Crafted Homes Team',
    ], CW))

    # ── SECTION 01 ────────────────────────────────────────────────────────────
    story.append(PageBreak())
    story.append(SectionHeader('01 — Are You Ready to Buy?', CW))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        'Before you start browsing listings, honestly assess your financial readiness. '
        'These factors determine not just whether you <i>can</i> buy, but whether now is the '
        '<i>right time</i> for you.', S['body']))

    story.append(Paragraph('Financial Checklist', S['h3']))
    for item in [
        '<b>Credit Score:</b> Most conventional loans require 620+. FHA may accept 580+. The higher your score, the better your rate.',
        '<b>Debt-to-Income Ratio (DTI):</b> Lenders generally want total monthly debts under 43% of gross monthly income.',
        '<b>Down Payment Savings:</b> Conventional loans require 3–20%. FHA requires 3.5%. VA loans (veterans) may require 0%.',
        '<b>Emergency Fund:</b> Keep 3–6 months of living expenses in reserve even after your down payment.',
        '<b>Stable Employment:</b> Most lenders want at least 2 years of consistent employment history.',
    ]:
        story.append(Paragraph(f'• {item}', S['bullet']))

    story.append(Spacer(1, 10))
    story.append(TipBox(
        'South Carolina offers several first-time buyer assistance programs. Contact us about '
        'SC Housing loan programs that can help with your down payment and closing costs.', CW))

    story.append(Paragraph('Personal Readiness', S['h3']))
    story.append(Paragraph(
        'Beyond finances, ask yourself: How long do you plan to stay in the area? Buying generally '
        'makes more financial sense if you plan to stay at least 3–5 years. Are you prepared for '
        'the ongoing costs of homeownership, including maintenance, property taxes, and insurance?',
        S['body']))

    story.append(Paragraph('9 Questions to Help You Decide', S['h3']))
    for q in [
        'Do I have a stable income I expect to continue?',
        'Have I saved enough for a down payment and closing costs?',
        'Is my credit in good shape, or do I need time to improve it?',
        'Am I planning to stay in this area for at least 3–5 years?',
        'Do I have an emergency fund separate from my down payment?',
        'Am I comfortable with the responsibility of maintaining a home?',
        'Have I researched the neighborhoods I\'m interested in?',
        'Do I understand all costs beyond the mortgage payment?',
        'Have I spoken with a trusted real estate professional?',
    ]:
        story.append(Paragraph(f'• {q}', S['bullet']))

    # ── SECTION 02 ────────────────────────────────────────────────────────────
    story.append(PageBreak())
    story.append(SectionHeader('02 — Getting Pre-Approved for a Mortgage', CW))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        'Pre-approval is one of the most important steps before searching for a home. '
        'It tells sellers you\'re a serious buyer and gives you a clear picture of what you can afford.',
        S['body']))

    story.append(Paragraph('Pre-Qualification vs. Pre-Approval', S['h3']))
    story.append(KeepTogether([Paragraph('Pre-Qualification vs. Pre-Approval', S['h3']), make_table([
        ['', 'PRE-QUALIFICATION', 'PRE-APPROVAL'],
        ['Based on',  'Self-reported info',  'Verified documents'],
        ['Strength',  'Informal estimate',   'Strong commitment'],
        ['Time',      '~10 minutes',         '1–3 business days'],
        ['Best for',  'Early planning',      'Active home search'],
    ], [CW*0.28, CW*0.36, CW*0.36])]))
    story.append(Spacer(1, 10))

    story.append(Paragraph('Documents You\'ll Need', S['h3']))
    for item in [
        'Government-issued photo ID',
        'Last 2 years of W-2s or tax returns (self-employed: 2 years of returns)',
        'Last 30 days of pay stubs',
        'Last 2–3 months of bank statements',
        'List of all debts (car loans, student loans, credit cards)',
        'Proof of any additional income (rental income, alimony, etc.)',
    ]:
        story.append(Paragraph(f'• {item}', S['bullet']))

    story.append(Spacer(1, 10))
    story.append(TipBox(
        'Get pre-approved by a local lender who knows the Myrtle Beach market. '
        'Local lenders often close faster and can be more flexible than big national banks.', CW))

    story.append(KeepTogether([Paragraph('Understanding Your Loan Options', S['h3']), make_table([
        ['LOAN TYPE',         'DOWN PAYMENT', 'BEST FOR'],
        ['Conventional',      '3–20%',        'Good credit, stable income'],
        ['FHA',               '3.5%',         'Lower credit scores'],
        ['VA',                '0%',           'Veterans & active military'],
        ['USDA',              '0%',           'Rural/suburban areas'],
        ['Renovation (203k)', '3.5%',         'Fixer-upper buyers'],
    ], [CW*0.33, CW*0.27, CW*0.40])]))

    # ── SECTION 03 ────────────────────────────────────────────────────────────
    story.append(PageBreak())
    story.append(SectionHeader('03 — Finding the Right Home', CW))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        'Once you\'re pre-approved, the fun begins. The Grand Strand offers incredible variety '
        'of communities, property types, and price points. Here\'s how to navigate your search.',
        S['body']))

    story.append(KeepTogether([Paragraph('Myrtle Beach Area Neighborhoods at a Glance', S['h3']), make_table([
        ['AREA',               'CHARACTER',                    'GREAT FOR'],
        ['Myrtle Beach',       'Vibrant, walkable, beachfront', 'Primary & vacation homes'],
        ['North Myrtle Beach', 'Quieter, family-oriented',     'Families, retirees'],
        ['Conway',             'Historic, affordable',         'First-time buyers'],
        ['Socastee',           'Suburban, growing',            'Young families'],
        ['Surfside Beach',     'Small-town charm',             'Retirees, investors'],
        ['Carolina Forest',    'Master-planned, great schools', 'Families'],
        ['Market Common',      'Walkable, mixed-use',          'Active lifestyle'],
    ], [CW*0.28, CW*0.38, CW*0.34])]))
    story.append(Spacer(1, 10))

    story.append(Paragraph('What to Look for When Touring Homes', S['h3']))
    for item in [
        '<b>Location & Commute:</b> Proximity to work, schools, and daily errands matters even in a beach market.',
        '<b>HOA Rules & Fees:</b> Many Grand Strand communities have HOAs. Understand what\'s covered and what restrictions apply.',
        '<b>Flood Zone Status:</b> Coastal properties can carry flood risk. Check FEMA maps and factor in flood insurance costs.',
        '<b>Age & Condition:</b> Note roof, HVAC, plumbing, and electrical age — these are major expenses.',
        '<b>Rental Potential:</b> If considering short-term rentals, check local ordinances and HOA rules first.',
    ]:
        story.append(Paragraph(f'• {item}', S['bullet']))

    story.append(Spacer(1, 10))
    story.append(TipBox(
        'Use the CCMLS (Coastal Carolinas MLS) to search current listings. We can set up '
        'automated alerts so you\'re first to know when a matching home hits the market.', CW))

    # ── SECTION 04 ────────────────────────────────────────────────────────────
    story.append(PageBreak())
    story.append(SectionHeader('04 — Making an Offer & Negotiating', CW))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        'When you find the right home, moving quickly and strategically is essential — '
        'especially in a competitive market. We\'ll guide you through crafting a compelling offer.',
        S['body']))

    story.append(Paragraph('What Goes Into an Offer', S['h3']))
    for item in [
        '<b>Purchase Price:</b> Based on comparable sales (comps) in the area.',
        '<b>Earnest Money Deposit:</b> Typically 1–2% of the purchase price, deposited into escrow to show good faith.',
        '<b>Contingencies:</b> Conditions that must be met — commonly inspection, financing, and appraisal contingencies.',
        '<b>Closing Date:</b> When you plan to take possession. Flexibility here can make your offer more attractive.',
        '<b>Seller Concessions:</b> You may request the seller cover some closing costs or complete repairs.',
    ]:
        story.append(Paragraph(f'• {item}', S['bullet']))

    story.append(Paragraph('Buyer\'s Market vs. Seller\'s Market', S['h3']))
    story.append(Paragraph(
        'In a <b>seller\'s market</b> (more buyers than homes), you may need to offer at or above '
        'asking price, limit contingencies, and move fast. In a <b>buyer\'s market</b> (more homes '
        'than buyers), you have more negotiating power. We\'ll assess current conditions and '
        'advise you accordingly.', S['body']))

    story.append(Spacer(1, 10))
    story.append(TipBox(
        'A pre-approval letter from a local lender included with your offer signals you\'re ready '
        'and qualified — this can make the difference in a multiple-offer situation.', CW))

    # ── SECTION 05 ────────────────────────────────────────────────────────────
    story.append(PageBreak())
    story.append(SectionHeader('05 — From Contract to Closing', CW))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        'Once your offer is accepted, you\'ve entered the "under contract" phase. '
        'There are several important steps between signing and getting the keys.', S['body']))

    steps = [
        ('Home Inspection',     '3–7 days',        'A licensed inspector evaluates the property\'s condition. You can request repairs or credits based on findings.'),
        ('Appraisal',           '1–2 weeks',        'Required by your lender to confirm the home\'s value supports the loan amount.'),
        ('Title Search',        'During escrow',    'A title company verifies the seller has legal right to sell and there are no liens on the property.'),
        ('Final Loan Approval', '2–3 weeks',        'Your lender finalizes your mortgage. Avoid major purchases or credit changes during this period.'),
        ('Final Walk-Through',  '24–48 hrs before', 'Confirm the home is in agreed condition and any requested repairs have been completed.'),
        ('Closing Day',         'As agreed',        'You sign documents, pay closing costs, and receive the keys to your new home!'),
    ]
    cell_s = ParagraphStyle('cs', fontName='Helvetica',      fontSize=9, textColor=NAVY,  leading=13)
    cell_b = ParagraphStyle('cb', fontName='Helvetica-Bold', fontSize=9, textColor=NAVY,  leading=13)
    hdr_s  = ParagraphStyle('ch', fontName='Helvetica-Bold', fontSize=9, textColor=WHITE, leading=13)
    step_data = [
        [Paragraph('STEP', hdr_s), Paragraph('TIMING', hdr_s), Paragraph('WHAT HAPPENS', hdr_s)]
    ] + [
        [Paragraph(s[0], cell_b), Paragraph(s[1], cell_s), Paragraph(s[2], cell_s)]
        for s in steps
    ]
    st = Table(step_data, colWidths=[CW*0.26, CW*0.22, CW*0.52], repeatRows=1, splitByRow=0)
    st.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,0),  NAVY),
        ('ROWBACKGROUNDS',(0,1), (-1,-1), [WHITE, LIGHT_BLUE]),
        ('GRID',          (0,0), (-1,-1), 0.5, STEEL),
        ('TOPPADDING',    (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('LEFTPADDING',   (0,0), (-1,-1), 8),
        ('VALIGN',        (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(st)
    story.append(Spacer(1, 10))
    story.append(TipBox(
        'Protect yourself from wire fraud: Always verify wiring instructions by calling your title '
        'company or us directly — never rely solely on email for transferring closing funds.', CW))

    # ── SECTION 06 ────────────────────────────────────────────────────────────
    story.append(PageBreak())
    story.append(SectionHeader('06 — Protecting Your Investment', CW))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        'Owning a home in coastal South Carolina comes with unique considerations. '
        'Protect your investment with the right coverage and knowledge.', S['body']))

    story.append(Paragraph('Insurance You\'ll Need', S['h3']))
    for item in [
        '<b>Homeowners Insurance:</b> Required by most lenders. Covers fire, theft, wind, and liability. Shop multiple providers for the best rate.',
        '<b>Flood Insurance:</b> Separate from homeowners insurance and often required in coastal/flood-prone areas. Available through FEMA\'s NFIP or private insurers.',
        '<b>Wind/Hurricane Insurance:</b> Standard policies may exclude wind damage in coastal SC. Verify your coverage and consider a separate wind policy.',
    ]:
        story.append(Paragraph(f'• {item}', S['bullet']))

    story.append(Paragraph('Property Taxes in South Carolina', S['h3']))
    story.append(Paragraph(
        'South Carolina has one of the lowest effective property tax rates in the nation. '
        'As a primary resident, you may qualify for the <b>4% assessment ratio</b> (owner-occupied). '
        'Non-primary/investment properties are assessed at 6%. We can connect you '
        'with a local tax professional for details.', S['body']))

    story.append(Paragraph('HOA Considerations', S['h3']))
    story.append(Paragraph(
        'Many Myrtle Beach communities are governed by Homeowners Associations. Before buying, '
        'review the HOA\'s CC&Rs, financial statements, and meeting minutes. '
        'Understand monthly fees and any special assessments.', S['body']))

    story.append(Spacer(1, 10))
    story.append(TipBox(
        'Request a copy of the HOA\'s reserve fund study. A well-funded HOA signals a well-managed '
        'community — underfunded HOAs can lead to surprise special assessments.', CW))

    # ── SECTION 07 ────────────────────────────────────────────────────────────
    story.append(PageBreak())
    story.append(SectionHeader('07 — 10 Questions to Ask Your Agent', CW))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        'Choosing the right agent is one of the most important decisions in your homebuying '
        'journey. Here are the questions you should ask — and what good answers look like.',
        S['body']))

    for i, (q, a) in enumerate([
        ('How long have you been working in the Myrtle Beach market?',
         'Local experience matters. Look for agents who know the neighborhoods, pricing trends, and local contractors.'),
        ('How many buyers did you represent last year?',
         'An active agent with recent transactions will have current market knowledge.'),
        ('What is your communication style?',
         'Make sure their availability and preferred contact method matches yours.'),
        ('How will you help me find homes before they\'re listed?',
         'Top agents have networks and strategies beyond the MLS.'),
        ('How do you handle multiple-offer situations?',
         'Strategy and creativity in competitive situations can win you the home.'),
        ('Can you recommend lenders, inspectors, and other professionals?',
         'A strong referral network saves time and connects you with trusted experts.'),
        ('What total costs should I budget for beyond the purchase price?',
         'Closing costs, inspection fees, insurance, and moving costs all add up.'),
        ('How do you negotiate on behalf of your buyers?',
         'Look for specific strategies, not vague assurances.'),
        ('What happens if I want to back out of a contract?',
         'Understand your contingency rights and when you can exit without losing your deposit.'),
        ('Why should I choose you over another agent?',
         'Confidence and a clear value proposition matter.'),
    ]):
        story.append(KeepTogether([
            Paragraph(f'<b>{i+1}.  {q}</b>', S['h3']),
            Paragraph(a, S['body_left']),
            Spacer(1, 4),
        ]))

    # ── SECTION 08 ────────────────────────────────────────────────────────────
    story.append(PageBreak())
    story.append(SectionHeader('08 — Your Carolina Crafted Homes Team', CW))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        'At Carolina Crafted Homes, Frank & Tiffany Hereda specialize in helping buyers find '
        'the perfect home on the Grand Strand — whether you\'re buying your first home, '
        'investing in a vacation property, or building from the ground up.', S['body']))

    story.append(Paragraph('What Sets Us Apart', S['h3']))
    for item in [
        '<b>Local Expertise:</b> We live and work in Myrtle Beach. We know every neighborhood, school district, and hidden gem on the Grand Strand.',
        '<b>Buy, Sell, Build, Renovate:</b> We\'re not just a sales team — we help clients at every stage of homeownership.',
        '<b>Trusted Network:</b> From local lenders to inspectors, contractors, and title companies — we connect you with the best.',
        '<b>Transparent Guidance:</b> We prioritize your interests above everything else, with clear communication at every step.',
    ]:
        story.append(Paragraph(f'• {item}', S['bullet']))

    story.append(Spacer(1, 18))
    story.append(ContactCard(CW))
    story.append(Spacer(1, 4))
    story.append(disclaimer(S))

    doc.build(story, onFirstPage=cch_footer, onLaterPages=cch_footer)
    print(f'✓ Built: {OUTPUT}')

build()
