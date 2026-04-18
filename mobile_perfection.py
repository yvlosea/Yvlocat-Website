import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Update Modal Styles for Mobile (Bottom Sheets)
modal_css_fix = """
      /* Mobile Bottom Sheet Modals */
      @media (max-width: 640px) {
        .modal-shell {
          align-items: flex-end; /* Stick to bottom */
          padding: 0;
        }
        .modal-panel {
          width: 100% !important;
          max-width: none !important;
          border-radius: 32px 32px 0 0 !important; /* Rounded top only */
          padding-bottom: env(safe-area-inset-bottom) !important;
          animation: slideUpSheet 0.4s cubic-bezier(0.23, 1, 0.32, 1);
        }
        @keyframes slideUpSheet {
          from { transform: translateY(100%); }
          to { transform: translateY(0); }
        }
        
        /* Hide redundant sticky CTA */
        .mobile-sticky-cta { display: none !important; }
        
        /* Ensure text is a bit larger on mobile */
        body { font-size: 16px; }
        h2 { font-size: 1.8rem !important; }
        
        .page-shell { padding-bottom: 120px; } /* Space for bottom nav */
      }
      
      /* Active Nav Item Styling */
      .mob-nav-item.is-active {
        color: var(--accent) !important;
        transform: translateY(-4px);
      }
      .mob-nav-item.is-active .mob-nav-icon {
        filter: drop-shadow(0 0 8px var(--accent));
      }
"""
# Append to style tag
content = content.replace('</style>', modal_css_fix + '\n    </style>')

# 2. Fix the "Book" button in Bottom Nav to actually open the modal
# We'll update the JS logic for bottom nav
nav_logic_fix = """
              if (targetId === 'book') {
                const bookBtn = document.getElementById('bookButton');
                if (bookBtn) bookBtn.click();
                return;
              }
"""
content = content.replace("if (targetId === 'book') {", nav_logic_fix + "              if (targetId === 'book_DISABLED_OLD_LOGIC') {")

# 3. Add Intersection Observer for automatic nav switching
auto_nav_js = """
      // Automatic Mobile Nav Highlight on Scroll
      function initAutoNavHighlight() {
        const sections = ['hero-top', 'pricing', 'experience', 'reviews'];
        const navItems = document.querySelectorAll('.mob-nav-item');
        
        const observerOptions = {
          root: null,
          rootMargin: '-20% 0px -60% 0px',
          threshold: 0
        };
        
        const observer = new IntersectionObserver((entries) => {
          entries.forEach(entry => {
            if (entry.isIntersecting) {
              const id = entry.target.id;
              navItems.forEach(item => {
                if (item.dataset.target === id) {
                  item.classList.add('is-active');
                } else if (item.dataset.target !== 'book') {
                  item.classList.remove('is-active');
                }
              });
            }
          });
        }, observerOptions);
        
        sections.forEach(id => {
          const el = document.getElementById(id);
          if (el) observer.observe(el);
        });
      }
      window.addEventListener('load', initAutoNavHighlight);
"""
content = content.replace('      window.addEventListener(\'load\', () => {', auto_nav_js + '\n      window.addEventListener(\'load\', () => {')

with open('index.html', 'w') as f:
    f.write(content)

print("Mobile UI Perfected!")
