import re

supabase_js = """
    <!-- Supabase Integration -->
    <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
    <script>
      const supabaseUrl = 'https://paaorahyaoivqqtvujxw.supabase.co';
      const supabaseKey = 'sb_publishable_6BEvMXOqzK6A7QKmdvwMQw_Lvuzcsto';
      const supabase = supabase.createClient(supabaseUrl, supabaseKey);

      async function loadDynamicCoupons() {
        try {
          const { data, error } = await supabase.from('coupons').select('*').eq('active', true);
          if (data && !error) {
            data.forEach(dbCoupon => {
              if (dbCoupon.expires_at && new Date(dbCoupon.expires_at) < new Date()) { return; }
              COUPONS[dbCoupon.code] = {
                label: dbCoupon.code,
                type: dbCoupon.type,
                value: dbCoupon.value,
                minimum: dbCoupon.minimum,
                description: `Live discount via admin system.`
              };
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

      window.addEventListener('load', () => {
        loadDynamicCoupons();
        initSecretAdmin();
      });
    </script>
"""

with open('index.html', 'r') as f:
    content = f.read()

# Add Supabase scripts before final </script>
content = content.replace('  </body>', supabase_js + '\n  </body>')

# Add trigger ID to brand mark
content = content.replace('<div class="brand-mark" aria-hidden="true">', '<div class="brand-mark" aria-hidden="true" id="secretAdminTrigger" style="cursor:pointer;">')

with open('index.html', 'w') as f:
    f.write(content)

print("Logic Injected!")
