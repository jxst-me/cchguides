# CCH Guides Project
**Carolina Crafted Homes — Lead Generation Guides**
Frank & Tiffany Hereda · Myrtle Beach, SC

## Project Structure

```
cch-guides/
├── assets/
│   ├── cch_logo_clean.png
│   └── cch_skyline_clean.png
├── guides/
│   ├── output/
│   └── guide_01_buying_first_home.py
├── landing-pages/
│   └── buying-guide.html
├── cch_template.py
└── README.md
```

## How to Generate a PDF Guide

1. Make sure `cch_template.py` and assets are in the same directory
2. Run: `python guides/guide_01_buying_first_home.py`
3. PDF saves to `guides/output/`

## How to Add a New Guide

1. Copy an existing guide: `cp guides/guide_01_buying_first_home.py guides/guide_02_selling.py`
2. Edit the content and OUTPUT path
3. Run it

## Landing Page Setup

In `landing-pages/buying-guide.html` replace:
- `GUIDE_PDF_URL_HERE` with your Google Drive PDF share link

## Hosting on GitHub Pages

1. Push repo to GitHub
2. Settings → Pages → Source: main branch, /landing-pages folder
3. Live at: `https://yourusername.github.io/cch-guides/buying-guide.html`

## Guides Planned

| # | Title | Status |
|---|-------|--------|
| 01 | Buying Your First Home in Myrtle Beach | Done |
| 02 | Selling Your Home on the Grand Strand | Next |
| 03 | Investing in Myrtle Beach Real Estate | Planned |
| 04 | Building & Renovating on the Grand Strand | Planned |

## Contact
- Frank & Tiffany Hereda — Carolina Crafted Homes
- 4702 Oleander Dr, Suite 300 · Myrtle Beach, SC 29577
- (704) 910-9111 · info@carolinacraftedhomes.com
- carolinacraftedhomes.com
