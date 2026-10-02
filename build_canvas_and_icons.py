import os
import subprocess

os.makedirs("icons", exist_ok=True)

# 1. Generate 5 High-Quality KPI Icons (SVGs)
icons = {
    "icons/customer_icon.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <defs>
    <linearGradient id="headGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF758C" />
      <stop offset="100%" stop-color="#FF5277" />
    </linearGradient>
    <linearGradient id="bodyGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3B82F6" />
      <stop offset="100%" stop-color="#1E3A8A" />
    </linearGradient>
    <filter id="iconShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="4" stdDeviation="3" flood-opacity="0.3"/>
    </filter>
  </defs>
  <g filter="url(#iconShadow)">
    <!-- Head -->
    <circle cx="50" cy="35" r="22" fill="url(#headGrad)" stroke="#FFFFFF" stroke-width="2"/>
    <!-- Shoulders/Body -->
    <path d="M 18 85 C 18 64, 32 58, 50 58 C 68 58, 82 64, 82 85 Z" fill="url(#bodyGrad)" stroke="#FFFFFF" stroke-width="2"/>
  </g>
</svg>""",

    "icons/cart_icon.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <defs>
    <linearGradient id="cartGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284C7" />
      <stop offset="100%" stop-color="#0369A1" />
    </linearGradient>
    <filter id="cartShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="2.5" flood-opacity="0.25"/>
    </filter>
  </defs>
  <g filter="url(#cartShadow)">
    <path d="M 15 22 L 26 22 L 38 62 L 78 62 L 88 32 L 29 32" fill="none" stroke="url(#cartGrad)" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>
    <!-- Grid inside basket -->
    <line x1="33" y1="42" x2="84" y2="42" stroke="#EF4444" stroke-width="2.5"/>
    <line x1="36" y1="52" x2="80" y2="52" stroke="#EF4444" stroke-width="2.5"/>
    <line x1="48" y1="32" x2="44" y2="62" stroke="#EF4444" stroke-width="2.5"/>
    <line x1="62" y1="32" x2="58" y2="62" stroke="#EF4444" stroke-width="2.5"/>
    <line x1="76" y1="32" x2="72" y2="62" stroke="#EF4444" stroke-width="2.5"/>
    <!-- Wheels -->
    <circle cx="42" cy="74" r="6.5" fill="#EF4444" stroke="#7F1D1D" stroke-width="2"/>
    <circle cx="74" cy="74" r="6.5" fill="#EF4444" stroke="#7F1D1D" stroke-width="2"/>
    <circle cx="42" cy="74" r="2.5" fill="#FFFFFF"/>
    <circle cx="74" cy="74" r="2.5" fill="#FFFFFF"/>
  </g>
</svg>""",

    "icons/box_icon.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <defs>
    <filter id="boxShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="4" stdDeviation="3" flood-opacity="0.3"/>
    </filter>
  </defs>
  <g filter="url(#boxShadow)" stroke="#273C75" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" fill="none">
    <!-- Isometric Box -->
    <polygon points="50,20 86,38 50,56 14,38" fill="#F8FAFC" fill-opacity="0.9"/>
    <polygon points="14,38 50,56 50,86 14,68" fill="#E2E8F0" fill-opacity="0.9"/>
    <polygon points="50,56 86,38 86,68 50,86" fill="#CBD5E1" fill-opacity="0.9"/>
    <!-- Flap seam -->
    <line x1="50" y1="20" x2="50" y2="56" stroke="#273C75" stroke-width="3"/>
    <line x1="32" y1="29" x2="68" y2="47" stroke="#3B82F6" stroke-width="2"/>
  </g>
</svg>""",

    "icons/sales_coins_icon.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <defs>
    <linearGradient id="goldCoin" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FDE047" />
      <stop offset="50%" stop-color="#EAB308" />
      <stop offset="100%" stop-color="#CA8A04" />
    </linearGradient>
    <filter id="coinShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="4" stdDeviation="3" flood-opacity="0.3"/>
    </filter>
  </defs>
  <g filter="url(#coinShadow)">
    <!-- Small figurine pushing/holding the stack -->
    <circle cx="30" cy="48" r="7" fill="#E2E8F0" stroke="#64748B" stroke-width="1.5"/>
    <path d="M 30 55 L 26 72 L 20 86" stroke="#64748B" stroke-width="3" stroke-linecap="round"/>
    <path d="M 30 58 L 48 50" stroke="#64748B" stroke-width="3" stroke-linecap="round"/>
    <!-- Stack of Gold Coins -->
    <ellipse cx="68" cy="84" rx="18" ry="6" fill="url(#goldCoin)" stroke="#A16207" stroke-width="1.5"/>
    <rect x="50" y="78" width="36" height="6" fill="url(#goldCoin)" stroke="#A16207" stroke-width="1.5"/>
    <ellipse cx="68" cy="78" rx="18" ry="6" fill="url(#goldCoin)" stroke="#A16207" stroke-width="1.5"/>
    <rect x="50" y="71" width="36" height="7" fill="url(#goldCoin)" stroke="#A16207" stroke-width="1.5"/>
    <ellipse cx="68" cy="71" rx="18" ry="6" fill="url(#goldCoin)" stroke="#A16207" stroke-width="1.5"/>
    <rect x="50" y="64" width="36" height="7" fill="url(#goldCoin)" stroke="#A16207" stroke-width="1.5"/>
    <ellipse cx="68" cy="64" rx="18" ry="6" fill="url(#goldCoin)" stroke="#A16207" stroke-width="1.5"/>
    <rect x="50" y="57" width="36" height="7" fill="url(#goldCoin)" stroke="#A16207" stroke-width="1.5"/>
    <ellipse cx="68" cy="57" rx="18" ry="6" fill="url(#goldCoin)" stroke="#A16207" stroke-width="1.5"/>
    <rect x="50" y="50" width="36" height="7" fill="url(#goldCoin)" stroke="#A16207" stroke-width="1.5"/>
    <ellipse cx="68" cy="50" rx="18" ry="6" fill="url(#goldCoin)" stroke="#A16207" stroke-width="1.5"/>
  </g>
</svg>""",

    "icons/profit_hand_icon.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <defs>
    <linearGradient id="handGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E3A8A" />
      <stop offset="100%" stop-color="#0F172A" />
    </linearGradient>
    <filter id="handShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="4" stdDeviation="3" flood-opacity="0.3"/>
    </filter>
  </defs>
  <g filter="url(#handShadow)">
    <!-- Cuff/Suit -->
    <path d="M 12 78 L 28 66 L 36 76 L 20 88 Z" fill="#DC2626"/>
    <path d="M 28 66 L 34 62 L 40 70 L 34 74 Z" fill="#FFFFFF"/>
    <!-- Hand holding upward -->
    <path d="M 33 67 C 45 56, 56 60, 68 62 C 78 63, 86 61, 88 56 C 88 52, 82 50, 72 52 L 56 50 C 48 48, 42 52, 36 56 Z" fill="url(#handGrad)" stroke="#38BDF8" stroke-width="1.5"/>
    <!-- Coins floating above hand -->
    <circle cx="68" cy="38" r="6" fill="#FBBF24" stroke="#D97706" stroke-width="1.5"/>
    <circle cx="80" cy="34" r="5" fill="#F59E0B" stroke="#B45309" stroke-width="1.5"/>
    <circle cx="62" cy="27" r="4.5" fill="#FBBF24" stroke="#D97706" stroke-width="1.5"/>
  </g>
</svg>"""
}

for filepath, svg_content in icons.items():
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg_content.strip())
print(f"Generated {len(icons)} KPI icons.")

# 2. Build 1920x1080 Canvas Background Template (SVG)
svg_canvas = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="1920" height="1080">
  <defs>
    <!-- Background Canvas Gradient: Coral/Peach Sunset to Rich Slate Navy -->
    <linearGradient id="bgGrad" x1="100%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#E28679" />
      <stop offset="35%" stop-color="#DA7B70" />
      <stop offset="70%" stop-color="#34486D" />
      <stop offset="100%" stop-color="#141E33" />
    </linearGradient>

    <!-- Metallic Embossed Card Gradient Fill -->
    <linearGradient id="cardFill" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#F5F9FC" />
      <stop offset="45%" stop-color="#E9F1F7" />
      <stop offset="100%" stop-color="#CDDCE8" />
    </linearGradient>

    <!-- Card Metallic Beveled Border Gradient -->
    <linearGradient id="cardBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#B8D0E5" />
      <stop offset="50%" stop-color="#6A8DAF" />
      <stop offset="100%" stop-color="#3C5B7C" />
    </linearGradient>

    <!-- Active Tab Fill -->
    <linearGradient id="activeTab" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FFF5F2" />
      <stop offset="100%" stop-color="#FCD5CF" />
    </linearGradient>

    <!-- Drop Shadow Filter for 3D Bevel Cards -->
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="8" stdDeviation="10" flood-color="#070D18" flood-opacity="0.45"/>
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#000000" flood-opacity="0.25"/>
    </filter>

    <!-- Text Shadow for Title -->
    <filter id="textGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="4" stdDeviation="4" flood-color="#0A1120" flood-opacity="0.7"/>
    </filter>
  </defs>

  <!-- Canvas Background -->
  <rect x="0" y="0" width="1920" height="1080" fill="url(#bgGrad)"/>

  <!-- ==================== HEADER BAR ==================== -->
  <!-- Brand Logo Text -->
  <text x="50" y="65" font-family="'Brush Script MT', 'Lucida Calligraphy', cursive, serif" font-size="34" font-weight="bold" fill="#FCD34D" filter="url(#textGlow)" letter-spacing="1">
    K.m.s BI Vizs
  </text>

  <!-- Report Title -->
  <text x="960" y="70" font-family="'Georgia', 'Times New Roman', serif" font-size="46" font-weight="bold" font-style="italic" fill="#FFFFFF" text-anchor="middle" filter="url(#textGlow)" letter-spacing="2">
    Sales Analysis Report 2020
  </text>

  <!-- ==================== LEFT SIDEBAR: 5 KPI CARDS ==================== -->
  <!-- Card 1: Total Customers -->
  <g filter="url(#cardShadow)">
    <rect x="50" y="110" width="330" height="165" rx="16" ry="16" fill="url(#cardFill)" stroke="url(#cardBorder)" stroke-width="3"/>
  </g>

  <!-- Card 2: Total Orders -->
  <g filter="url(#cardShadow)">
    <rect x="50" y="295" width="330" height="165" rx="16" ry="16" fill="url(#cardFill)" stroke="url(#cardBorder)" stroke-width="3"/>
  </g>

  <!-- Card 3: Total Quantity -->
  <g filter="url(#cardShadow)">
    <rect x="50" y="480" width="330" height="165" rx="16" ry="16" fill="url(#cardFill)" stroke="url(#cardBorder)" stroke-width="3"/>
  </g>

  <!-- Card 4: Total Sales -->
  <g filter="url(#cardShadow)">
    <rect x="50" y="665" width="330" height="165" rx="16" ry="16" fill="url(#cardFill)" stroke="url(#cardBorder)" stroke-width="3"/>
  </g>

  <!-- Card 5: Total Profit -->
  <g filter="url(#cardShadow)">
    <rect x="50" y="850" width="330" height="165" rx="16" ry="16" fill="url(#cardFill)" stroke="url(#cardBorder)" stroke-width="3"/>
  </g>

  <!-- ==================== CENTER SECTION ==================== -->
  <!-- Top Center: Donut / Segment Slicer Container -->
  <g filter="url(#cardShadow)">
    <rect x="410" y="110" width="860" height="390" rx="16" ry="16" fill="url(#cardFill)" stroke="url(#cardBorder)" stroke-width="3"/>
    
    <!-- Navigation Pill Tabs Container Bar -->
    <rect x="425" y="120" width="830" height="48" rx="8" ry="8" fill="#F0F4F8" fill-opacity="0.8" stroke="#B8CADB" stroke-width="1.5"/>
    
    <!-- Tab 1: Sales by Month (Active) -->
    <rect x="430" y="124" width="270" height="40" rx="6" ry="6" fill="url(#activeTab)" stroke="#E07A5F" stroke-width="2" stroke-dasharray="4,3"/>
    <text x="565" y="150" font-family="'Segoe UI', sans-serif" font-size="16" font-weight="bold" fill="#334155" text-anchor="middle">Sales by Month</text>

    <!-- Tab 2: Sales by Category -->
    <rect x="710" y="124" width="265" height="40" rx="6" ry="6" fill="#E2EBF2" stroke="#CBD5E1" stroke-width="1"/>
    <text x="842" y="150" font-family="'Segoe UI', sans-serif" font-size="16" font-weight="600" fill="#475569" text-anchor="middle">Sales by Category</text>

    <!-- Tab 3: Sales by Segment -->
    <rect x="985" y="124" width="265" height="40" rx="6" ry="6" fill="#E2EBF2" stroke="#CBD5E1" stroke-width="1"/>
    <text x="1117" y="150" font-family="'Segoe UI', sans-serif" font-size="16" font-weight="600" fill="#475569" text-anchor="middle">Sales by Segment</text>
  </g>

  <!-- Bottom Center Left: Top 5 Products by Sales -->
  <g filter="url(#cardShadow)">
    <rect x="410" y="525" width="420" height="490" rx="16" ry="16" fill="url(#cardFill)" stroke="url(#cardBorder)" stroke-width="3"/>
  </g>

  <!-- Bottom Center Right: Top 5 Customers by sales -->
  <g filter="url(#cardShadow)">
    <rect x="850" y="525" width="420" height="490" rx="16" ry="16" fill="url(#cardFill)" stroke="url(#cardBorder)" stroke-width="3"/>
  </g>

  <!-- ==================== RIGHT SIDEBAR ==================== -->
  <!-- Top Right: Sales Vs Profit by City -->
  <g filter="url(#cardShadow)">
    <rect x="1295" y="110" width="575" height="305" rx="16" ry="16" fill="url(#cardFill)" stroke="url(#cardBorder)" stroke-width="3"/>
  </g>

  <!-- Middle Right: Sales Monthly Trend -->
  <g filter="url(#cardShadow)">
    <rect x="1295" y="435" width="575" height="280" rx="16" ry="16" fill="url(#cardFill)" stroke="url(#cardBorder)" stroke-width="3"/>
  </g>

  <!-- Bottom Right: Profit Percentage by Segment -->
  <g filter="url(#cardShadow)">
    <rect x="1295" y="735" width="575" height="280" rx="16" ry="16" fill="url(#cardFill)" stroke="url(#cardBorder)" stroke-width="3"/>
  </g>

</svg>"""

with open("canvas_background.svg", "w", encoding="utf-8") as f:
    f.write(svg_canvas.strip())
print("Created canvas_background.svg successfully!")

# 3. Convert SVG to PNG using Headless Chrome for immediate 1080p Power BI import
chrome_paths = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
]

chrome_bin = None
for p in chrome_paths:
    if os.path.exists(p):
        chrome_bin = p
        break

if chrome_bin:
    svg_abs = os.path.abspath("canvas_background.svg")
    png_abs = os.path.abspath("canvas_background.png")
    cmd = [
        chrome_bin,
        "--headless",
        "--disable-gpu",
        f"--screenshot={png_abs}",
        "--window-size=1920,1080",
        "--hide-scrollbars",
        f"file:///{svg_abs}"
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
        if os.path.exists("canvas_background.png"):
            size_kb = os.path.getsize("canvas_background.png") / 1024
            print(f"Generated 1920x1080 canvas_background.png ({size_kb:.1f} KB) via Headless Chrome!")
        else:
            print("Chrome command executed, checking PNG generation...")
    except Exception as e:
        print(f"Notice: PNG render via Chrome had exception: {e}")
