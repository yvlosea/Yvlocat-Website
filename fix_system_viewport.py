import os
import re

for filename in ['admin.html', 'reviews.html', 'supabase-booking.html']:
    if not os.path.exists(filename): continue
    with open(filename, 'r') as f:
        content = f.read()
    
    # Ensure viewport is correct
    if 'name="viewport"' not in content:
        content = content.replace('<head>', '<head>\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">')
    
    # Add mobile-friendly padding to body
    if '</style>' in content:
        content = content.replace('</style>', '      body { padding-bottom: 40px; }\n      @media (max-width: 640px) { h1 { font-size: 2rem !important; } .page-shell { padding: 16px; } }\n    </style>')
        
    with open(filename, 'w') as f:
        f.write(content)
