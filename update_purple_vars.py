import re

purple_vars = """
        --bg: #fcfaff;
        --bg-soft: #f4ebff;
        --surface: rgba(255, 255, 255, 0.90);
        --surface-strong: rgba(255, 255, 255, 0.98);
        --surface-dark: #3a2b42;
        --ink: #4e355c;
        --ink-soft: #887094;
        --accent: #b47ce3;
        --accent-deep: #8f5ac0;
        --gold: #ffb1c4;
        --gold-soft: rgba(255, 177, 196, 0.22);
        --rose: #e6c5f7;
        --line: rgba(143, 90, 192, 0.15);
        --line-strong: rgba(143, 90, 192, 0.3);
        --success: #6cc196;
        --warning: #ffaa85;
        --shadow: 0 24px 70px rgba(143, 90, 192, 0.12);
        --shadow-soft: 0 14px 34px rgba(143, 90, 192, 0.08);
        --radius-xl: 40px;
        --radius-lg: 30px;
        --radius-md: 22px;
        --radius-sm: 16px;
        --transition: 180ms ease;
"""

with open('index.html', 'r') as f:
    content = f.read()

content = re.sub(r':root\s*\{[^}]*\}', ':root {' + purple_vars + '      }', content)

with open('index.html', 'w') as f:
    f.write(content)

print("Purple Vars Applied!")
