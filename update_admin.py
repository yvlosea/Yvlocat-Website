import re

with open('admin.html', 'r') as f:
    content = f.read()

# Add a Reviews Management block right after the bookings list
reviews_ui = """
        <div style="margin-top: 48px; border-top: 1px solid var(--line); padding-top: 32px;">
          <h2 style="font-size:1.8rem; margin-bottom: 24px;">Reviews Channel</h2>
          <div id="reviewsList" class="bookings-grid">
             <div class="empty-state">Loading reviews...</div>
          </div>
        </div>
"""

content = content.replace('<div id="bookingsList" class="bookings-grid">\n          <div class="empty-state">Loading bookings...</div>\n        </div>', 
                        '<div id="bookingsList" class="bookings-grid">\n          <div class="empty-state">Loading bookings...</div>\n        </div>\n' + reviews_ui)

reviews_js = """
      // Filter events
      statusFilter.addEventListener("change", renderBookings);
      currencyFilter.addEventListener("change", renderBookings);
      searchInput.addEventListener("input", renderBookings);
      refreshBtn.addEventListener("click", () => { loadBookings(); loadAdminReviews(); });

      // Reviews Channel Logic
      async function loadAdminReviews() {
        const reviewsList = document.getElementById("reviewsList");
        try {
          const { data, error } = await supabase.from('reviews').select('*').order('created_at', { ascending: false });
          if (error) throw error;
          if (!data || data.length === 0) {
            reviewsList.innerHTML = `<div class="empty-state">No reviews found.</div>`;
            return;
          }
          let html = "";
          data.forEach(r => {
             const dateStr = new Date(r.created_at).toLocaleDateString();
             html += `
             <div class="booking-card">
               <div class="booking-header">
                 <div>
                   <div style="font-weight:700; color:var(--accent); font-size:1.2rem;">${r.name}</div>
                   <div class="booking-date">${dateStr} &bull; ${"🐱".repeat(r.rating || 5)}</div>
                 </div>
                 <span class="status-badge status-${r.status}">${r.status}</span>
               </div>
               <p style="margin: 8px 0; font-size: 0.95rem;">"${r.review}"</p>
               ${r.admin_comment ? `
               <div style="margin-top:12px; padding:12px; background:rgba(180,124,227,0.1); border-left:3px solid var(--accent); border-radius:0 8px 8px 0;">
                 <strong style="color:var(--accent-deep); font-size:0.8rem; text-transform:uppercase;">You Replied:</strong>
                 <p style="margin:4px 0 0 0; font-size:0.9rem;">${r.admin_comment}</p>
               </div>` : `
               <div style="margin-top:16px;">
                 <input type="text" id="replyInput_${r.id}" placeholder="Type your reply here..." style="min-height: 44px;" />
                 <button class="btn-success" style="width:auto; margin-top:8px; padding:8px 16px; min-height:0; display:inline-block;" onclick="replyToReview('${r.id}')">Submit Reply</button>
                 <button class="btn-secondary" style="width:auto; margin-top:8px; padding:8px 16px; min-height:0; display:inline-block;" onclick="deleteReview('${r.id}')">Delete Request</button>
               </div>
               `}
             </div>
             `;
          });
          reviewsList.innerHTML = html;
        } catch(err) {
          reviewsList.innerHTML = `<div class="empty-state">Error loading reviews: ${err.message}</div>`;
        }
      }

      window.replyToReview = async (id) => {
        const input = document.getElementById(`replyInput_${id}`);
        const reply = input.value.trim();
        if(!reply) return;
        try {
          const { error } = await supabase.from('reviews').update({ admin_comment: reply }).eq('id', id);
          if (error) throw error;
          loadAdminReviews();
        } catch(e) { alert("Failed to add reply."); }
      };

      window.deleteReview = async (id) => {
        if(!confirm("Are you sure you want to mark this review as deleted?")) return;
        try {
          const { error } = await supabase.from('reviews').update({ status: 'deleted' }).eq('id', id);
          if (error) throw error;
          loadAdminReviews();
        } catch(e) { alert("Failed to delete review."); }
      };
      
      // Hook up to login
      const originalLoginBtn = loginBtn.onclick;
      loginBtn.addEventListener("click", () => {
        if (isLoggedIn) {
          loadAdminReviews();
        }
      });
"""

# Replace the specific comments
content = content.replace("""      // Filter events
      statusFilter.addEventListener("change", renderBookings);
      currencyFilter.addEventListener("change", renderBookings);
      searchInput.addEventListener("input", renderBookings);
      refreshBtn.addEventListener("click", loadBookings);""", reviews_js)

with open('admin.html', 'w') as f:
    f.write(content)

print("Reviews logic integrated")
