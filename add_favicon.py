import os
import re

favicon_tag = '<link rel="icon" type="image/png" href="yvlocat.png">'

for filename in ['index.html', 'admin.html', 'reviews.html', 'supabase-booking.html']:
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            content = f.read()
        
        # Check if already exists
        if 'rel="icon"' in content:
            content = re.sub(r'<link rel="icon".*?>', favicon_tag, content)
        else:
            # Insert before </head> or after title
            if '</head>' in content:
                content = content.replace('</head>', f'    {favicon_tag}\n  </head>')
            else:
                # Fallback for small files
                content = content.replace('<head>', f'<head>\n    {favicon_tag}')
        
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Favicon added to {filename}")

