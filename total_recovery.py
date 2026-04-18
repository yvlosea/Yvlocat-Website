import re
import os

# 1. Start with the aesthetic base
with open('index (1).html', 'r') as f:
    content = f.read()

# 2. Apply Purple/Pastel Variables
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
content = re.sub(r':root\s*\{[^}]*\}', ':root {' + purple_vars + '      }', content)

# 3. Clean up any dark burgundy reds from CSS
content = content.replace('rgba(37, 24, 25, 0.98)', 'var(--bg-soft)')
content = content.replace('rgba(75, 35, 42, 0.94)', 'var(--bg)')
content = content.replace('rgba(34, 24, 25, 0.98)', 'var(--accent-deep)')
content = content.replace('rgba(67, 34, 38, 0.95)', 'var(--accent)')
content = content.replace('background: linear(135deg, var(--accent-deep), var(--accent), #c06f59)', 'background: linear-gradient(135deg, var(--accent-deep), var(--accent))')
content = content.replace('#c06f59', 'var(--accent)')

# 4. Inject Supabase logic into the existing script block
# We'll add the init code at the top of the existing script
supabase_init = """
      const supabaseUrl = 'https://paaorahyaoivqqtvujxw.supabase.co';
      const supabaseKey = 'sb_publishable_6BEvMXOqzK6A7QKmdvwMQw_Lvuzcsto';
      // Load Supabase script globally
      const script = document.createElement('script');
      script.src = 'https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2';
      document.head.appendChild(script);

      async function loadDynamicCoupons() {
        if (!window.supabase) return;
        try {
          const sb = window.supabase.createClient(supabaseUrl, supabaseKey);
          const { data, error } = await sb.from('coupons').select('*').eq('active', true);
          if (data && !error) {
            data.forEach(dbCoupon => {
              if (dbCoupon.expires_at && new Date(dbCoupon.expires_at) < new Date()) { return; }
              if (window.COUPONS) {
                  window.COUPONS[dbCoupon.code] = {
                    label: dbCoupon.code,
                    type: dbCoupon.type,
                    value: dbCoupon.value,
                    minimum: dbCoupon.minimum,
                    description: `Live discount via admin system.`
                  };
              }
            });
          }
        } catch(e) {}
      }

      function initSecretAdmin() {
        const trigger = document.getElementById("secretAdminTrigger");
        if (trigger) {
          let clk = 0;
          let timr;
          trigger.addEventListener("click", () => {
            clk++;
            if (clk === 3) window.location.href = "admin.html";
            clearTimeout(timr);
            timr = setTimeout(() => { clk = 0; }, 800);
          });
        }
      }
"""
# Insert after first <script>
content = content.replace('<script>', '<script>\n' + supabase_init)

# 5. Fix COUPONS scope
content = content.replace('const COUPONS =', 'window.COUPONS =')

# 6. Ensure splash screen hides quickly even if errors occur
# We'll wrap the splash hide in a more robust way
splash_fix = """
        // Global Error Handler to ensure splash screen closes
        window.addEventListener('error', () => {
           const splash = document.getElementById('splashScreen');
           if (splash) splash.remove();
        });
        
        setTimeout(() => {
          const splash = document.getElementById('splashScreen');
          if (splash) {
            splash.style.opacity = '0';
            setTimeout(() => splash.remove(), 600);
          }
        }, 1500);
"""
# Replace existing splash timeout
content = re.sub(r'setTimeout\(\(\) => \{[^}]*splashScreen[^}]*\}, \d+\);', splash_fix, content)

# 7. Call the new functions in DOMContentLoaded
init_calls = """
        loadHomeReviews();
        initSecretAdmin();
        setTimeout(loadDynamicCoupons, 2000); // Give supabase time to load
"""
content = content.replace('loadHomeReviews();', init_calls)

# 8. Add trigger ID to brand mark
content = content.replace('<div class="brand-mark" aria-hidden="true">', '<div class="brand-mark" aria-hidden="true" id="secretAdminTrigger" style="cursor:pointer;">')

# 9. Favicon fix
content = content.replace('</head>', '    <link rel="icon" type="image/png" href="yvlocat.png">\n  </head>')

with open('index.html', 'w') as f:
    f.write(content)

print("Total Recovery Complete!")
