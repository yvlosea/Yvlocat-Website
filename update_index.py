import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Splash screen and CSS animations
splash_css = """
      @keyframes pulse {
        0% { box-shadow: 0 0 10px rgba(214,171,109,0.2); transform: scale(0.98); }
        100% { box-shadow: 0 0 40px rgba(214,171,109,0.6); transform: scale(1.02); }
      }

      .mobile-sticky-cta {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 16px;
        background: linear-gradient(180deg, transparent, rgba(255,251,246,1) 40%);
        z-index: 30;
      }
      
      @media (min-width: 900px) {
        .hidden-desktop { display: none !important; }
      }
"""

content = content.replace("      @media (max-width: 899px) {", splash_css + "\n      @media (max-width: 899px) {\n        .page-shell { padding-bottom: 90px; }\n        .brand-lockup { flex-direction: column; justify-content: center; width: 100%; text-align: center; }\n        .brand-mark { width: 64px; height: 64px; border-radius: 20px; box-shadow: 0 0 24px rgba(214,171,109,0.5); }\n")

# 2. Bottom sheet modal on mobile
bottom_sheet_css = """
      @media (max-width: 759px) {
        .modal-shell {
          align-items: flex-end;
          padding: 0;
        }
        .modal-panel {
          border-radius: 32px 32px 0 0;
          max-height: 88vh;
          width: 100%;
        }
"""
content = content.replace("      @media (max-width: 759px) {", bottom_sheet_css)

# 3. Watermark background
watermark_css = """      body {
        margin: 0;
        min-height: 100vh;
        font-family: "Manrope", sans-serif;
        color: var(--ink);
        background:
          url('kittylogo.png') center/120px repeat,
          radial-gradient(circle at top left, rgba(214, 171, 109, 0.3), transparent 24%),
          radial-gradient(circle at 80% 10%, rgba(163, 76, 66, 0.14), transparent 22%),
          linear-gradient(180deg, #f6f2eb 0%, var(--bg) 38%, #f0e7dc 100%);
        background-blend-mode: overlay, normal, normal, normal;
      }
      
      body::before {
        content: "";
        position: fixed;
        inset: 0;
        background: rgba(244, 239, 231, 0.94);
        z-index: 0;
        pointer-events: none;
      }
"""
# Need to replace the current body definition.
content = re.sub(r'      body \{\s*margin: 0;\s*min-height: 100vh;.*?\n      \}', watermark_css.strip(), content, flags=re.DOTALL)

# But wait, body::before and body::after already exist.
# I will just replace the existing body::before and body::after definition with new ones.
# Or better, just add a div.watermark-bg.
# Let's revert that and just use a div for watermark to avoid breaking existing ::before blobbing.
