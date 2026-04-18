import re

# Read current index.html
with open('index.html', 'r') as f:
    content = f.read()

# Read target design index (1).html
with open('index (1).html', 'r') as f:
    target = f.read()

# 1. Update <style> tag with enhanced mystic/mobile CSS
# Extract styles from target and merge with purple variables
mystic_styles = re.search(r'<style>(.*?)</style>', target, re.DOTALL).group(1)

# Ensure our purple variables are included in the :root
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

# Replace :root in mystic_styles
mystic_styles = re.sub(r':root\s*\{[^}]*\}', ':root {\n' + purple_vars + '      }', mystic_styles)

# Replace the style tag in content
content = re.sub(r'<style>(.*?)</style>', '<style>' + mystic_styles + '</style>', content, flags=re.DOTALL)

# 2. Add Mobile Bottom Nav and Particles to Body
body_injections = """
    <!-- Floating Particles for mobile -->
    <div class="mobile-particles" id="mobileParticles"></div>
    <div class="floating-paw" style="top: 10%; left: 5%;">🐾</div>
    <div class="floating-paw" style="top: 25%; right: 8%; animation-delay: 1s;">🐾</div>
    <div class="floating-paw" style="top: 50%; left: 3%; animation-delay: 2s;">🐾</div>
    <div class="floating-paw" style="top: 70%; right: 5%; animation-delay: 0.5s;">🐾</div>
    <div class="floating-paw" style="top: 85%; left: 10%; animation-delay: 1.5s;">🐾</div>

    <!-- Mobile Bottom Navigation -->
    <nav class="mobile-bottom-nav" id="mobileBottomNav">
      <div class="mobile-bottom-nav-inner">
        <button class="mob-nav-item is-active" data-target="hero-top" type="button">
          <span class="mob-nav-icon">🏠</span>
          <span>Home</span>
        </button>
        <button class="mob-nav-item" data-target="pricing" type="button">
          <span class="mob-nav-icon">🔮</span>
          <span>Build</span>
        </button>
        <button class="mob-nav-cta mob-nav-item" data-target="book" type="button">
          <span class="mob-nav-icon">💜</span>
          <span>Book</span>
        </button>
        <button class="mob-nav-item" data-target="experience" type="button">
          <span class="mob-nav-icon">✨</span>
          <span>Info</span>
        </button>
        <button class="mob-nav-item" data-target="reviews-section" type="button">
          <span class="mob-nav-icon">💬</span>
          <span>Reviews</span>
        </button>
      </div>
    </nav>
"""
# Insert after <body> tag
content = content.replace('<body>', '<body>' + body_injections)

# 3. Add JS enhancements from index (1).html
js_logic = """
      // Enhanced Interactives from Index (1)
      function initEnhancedInteractives() {
        const emojis = ['✨', '🌙', '⭐', '💫', '🐾', '💜', '🔮', '🌸', '♡'];
        const container = document.getElementById('mobileParticles');
        if (container) {
          for (let i = 0; i < 12; i++) {
            const p = document.createElement('div');
            p.className = 'mobile-particle';
            p.textContent = emojis[Math.floor(Math.random() * emojis.length)];
            p.style.left = Math.random() * 100 + '%';
            p.style.setProperty('--drift', (Math.random() * 80 - 40) + 'px');
            p.style.setProperty('--spin', (Math.random() * 360) + 'deg');
            p.style.animationDuration = (6 + Math.random() * 8) + 's';
            p.style.animationDelay = (Math.random() * 10) + 's';
            p.style.fontSize = (0.8 + Math.random() * 1) + 'rem';
            container.appendChild(p);
          }
          container.style.display = 'block';
        }

        // Sparkle Burst
        document.addEventListener('click', (e) => {
          const sparkles = ['✨', '⭐', '💫', '🌟', '♡'];
          const x = e.clientX;
          const y = e.clientY;
          for (let i = 0; i < 5; i++) {
            const sparkle = document.createElement('div');
            sparkle.className = 'sparkle-burst';
            sparkle.textContent = sparkles[Math.floor(Math.random() * sparkles.length)];
            sparkle.style.left = x + (Math.random() * 40 - 20) + 'px';
            sparkle.style.top = y + (Math.random() * 40 - 20) + 'px';
            sparkle.style.animationDelay = (i * 0.1) + 's';
            document.body.appendChild(sparkle);
            setTimeout(() => sparkle.remove(), 600);
          }
        });

        // Bottom Nav Logic
        const navItems = document.querySelectorAll('.mob-nav-item');
        navItems.forEach(item => {
          item.addEventListener('click', () => {
            const targetId = item.dataset.target;
            if (targetId === 'book') {
              document.getElementById('bookButton').scrollIntoView({ behavior: 'smooth', block: 'center' });
              return;
            }
            const target = document.getElementById(targetId);
            if (target) {
              target.scrollIntoView({ behavior: 'smooth' });
            }
            navItems.forEach(i => i.classList.remove('is-active'));
            item.classList.add('is-active');
          });
        });

        // Floating Emojis Interval
        setInterval(() => {
          if (document.hidden) return;
          const floats = ['💜', '✨', '🌙', '⭐', '🐾', '🔮', '🌸', '♡', '😺'];
          const el = document.createElement('div');
          el.className = 'cute-float';
          el.style.cssText = `position: fixed; bottom: -30px; left: ${Math.random()*100}%; font-size: 1.5rem; pointer-events: none; z-index: 5; animation: floatUp 10s linear;`;
          el.textContent = floats[Math.floor(Math.random() * floats.length)];
          document.body.appendChild(el);
          setTimeout(() => el.remove(), 10000);
        }, 4000);
      }
      
      // Add float animation keyframes if missing
      const style = document.createElement('style');
      style.innerHTML = `
        @keyframes floatUp {
          to { transform: translateY(-110vh) rotate(360deg); opacity: 0; }
        }
        .cute-float { transition: opacity 1s; }
      `;
      document.head.appendChild(style);

      // Initialize
      window.addEventListener('load', initEnhancedInteractives);
"""

# Insert JS before </script>
content = content.replace('    </script>', js_logic + '\n    </script>')

# 4. Patch Section IDs for navigation
content = content.replace('id="pricing"', 'id="pricing" id="hero-top"') # Ensuring top ID exists
content = content.replace('<h2>Experience</h2>', '<div id="experience"></div><h2>Experience</h2>')
content = content.replace('<h3>Published Reviews</h3>', '<div id="reviews-section"></div><h3>Published Reviews</h3>')

with open('index.html', 'w') as f:
    f.write(content)

print("Mystic Evolution Complete!")
