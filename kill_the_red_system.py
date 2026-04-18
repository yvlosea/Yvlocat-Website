import re
import os

def clean_colors(content):
    content = content.replace('#a34c42', 'var(--accent)')
    content = content.replace('#6a2e35', 'var(--accent-deep)')
    content = content.replace('#c06f59', 'var(--accent)')
    content = re.sub(r'rgba\(163,\s*76,\s*66', 'rgba(255, 177, 196', content)
    content = re.sub(r'rgba\(214,\s*171,\s*109', 'rgba(180, 124, 227', content)
    content = re.sub(r'rgba\(106,\s*46,\s*53', 'rgba(143, 90, 192', content)
    
    # Hero/Footer card dark burgundy handling
    content = content.replace('rgba(37, 24, 25, 0.98)', 'var(--bg-soft)')
    content = content.replace('rgba(75, 35, 42, 0.94)', 'var(--bg)')
    content = content.replace('rgba(34, 24, 25, 0.98)', 'var(--accent-deep)')
    content = content.replace('rgba(67, 34, 38, 0.95)', 'var(--accent)')
    return content

for filename in ['index.html', 'admin.html', 'reviews.html', 'supabase-booking.html']:
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            content = f.read()
        content = clean_colors(content)
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Cleaned {filename}")

