import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace any lingering brown/burgundy hexes
# c06f59 is a reddish brown
content = content.replace('#c06f59', 'var(--accent)')
# 37, 24, 25 and 75, 35, 42 are the dark burgundy from hero-card
content = content.replace('rgba(37, 24, 25, 0.98)', 'linear-gradient(135deg, var(--bg-soft), var(--bg))')
content = content.replace('rgba(75, 35, 42, 0.94)', 'var(--surface-strong)')

# 34, 24, 25 and 67, 34, 38 are from footer-card
content = content.replace('rgba(34, 24, 25, 0.98)', 'var(--accent-deep)')
content = content.replace('rgba(67, 34, 38, 0.95)', 'var(--accent)')

# Fix the Hero Card text colors which were light for the dark bg
content = content.replace('color: #fff7ef;', 'color: var(--ink);')
content = content.replace('color: rgba(255, 247, 239, 0.76);', 'color: var(--ink-soft);')
content = content.replace('color: #fff8f2;', 'color: var(--ink);')

# Fix the Footer Card text colors
content = content.replace('color: #fff8f2;', 'color: #fff;')
content = content.replace('color: rgba(255, 248, 242, 0.78);', 'color: rgba(255, 255, 255, 0.8);')

# Fix any stray rgba(163, 76, 66) that my previous script might have left in a different format
content = re.sub(r'rgba\(163,\s*76,\s*66', 'rgba(255, 177, 196', content)
content = re.sub(r'rgba\(214,\s*171,\s*109', 'rgba(180, 124, 227', content)

with open('index.html', 'w') as f:
    f.write(content)

print("Red Eliminated!")
