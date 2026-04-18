import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace old gold/brown colors with purple/pink ones
content = content.replace('rgba(214, 171, 109,', 'rgba(180, 124, 227,')
content = content.replace('rgba(163, 76, 66,', 'rgba(255, 177, 196,')
content = content.replace('rgba(106, 46, 53,', 'rgba(143, 90, 192,')
content = content.replace('rgba(43, 27, 29,', 'rgba(78, 53, 92,')

# Update admin-comment specifically
content = content.replace('background: rgba(214, 171, 109, 0.15);', 'background: var(--bg-soft);')
content = content.replace('border-left: 3px solid var(--gold);', 'border-left: 3px solid var(--accent);')

# Ensure loadHomeReviews is called
if 'loadHomeReviews()' not in content.split('document.addEventListener')[1]:
    content = content.replace("document.addEventListener('DOMContentLoaded', () => {", 
                              "document.addEventListener('DOMContentLoaded', () => {\n        loadHomeReviews();")

with open('index.html', 'w') as f:
    f.write(content)

print("Final Polish Applied!")
