import os
import re

css_root = """:root {
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
      }"""

css_root_reviews = """:root {
        --bg: #fcfaff;
        --surface: rgba(255, 255, 255, 0.95);
        --ink: #4e355c;
        --ink-soft: #887094;
        --accent: #b47ce3;
        --accent-deep: #8f5ac0;
        --gold: #ffb1c4;
        --line: rgba(143, 90, 192, 0.14);
        --success: #6cc196;
        --warning: #ffaa85;
        --radius-xl: 34px;
        --radius-md: 18px;
        --transition: 180ms ease;
      }"""

def update_file(filepath, is_reviews=False):
    with open(filepath, 'r') as f:
        content = f.read()

    # Replace :root
    pattern = r":root\s*{[^}]*}"
    content = re.sub(pattern, css_root_reviews if is_reviews else css_root, content)
    
    # Replace background gradients
    content = re.sub(r"rgba\(214,\s*171,\s*109,", "rgba(180, 124, 227,", content)
    content = re.sub(r"rgba\(163,\s*76,\s*66,", "rgba(255, 177, 196,", content)
    
    with open(filepath, 'w') as f:
        f.write(content)


update_file('index.html')
update_file('reviews.html', True)
update_file('admin.html', True)
update_file('supabase-booking.html')

print("Colors updated across all files!")
