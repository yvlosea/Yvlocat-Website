import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Consolidate scripts. 
# We'll find all script content between <script> and </script> and join them,
# but keeping external scripts (with src) separate.

scripts_with_src = re.findall(r'<script\s+src=".*?".*?></script>', content)
inline_scripts = re.findall(r'<script>(.*?)</script>', content, re.DOTALL)

# Remove all existing script tags (except for meta/external ones if any)
# Actually, it's safer to just target the two main blocks at the end.
# The user's index (1).html copy had a block, and then I injected another.

# Let's find the first <script> that starts around line 2500
# and the last </script> around line 3903.

# Better: Just replace the entire chunk between the first script and last script
# with a single clean block.

combined_js = "\n".join(inline_scripts)

# Change const COUPONS to window.COUPONS so it's globally accessible
combined_js = combined_js.replace('const COUPONS =', 'window.COUPONS =')

# Remove any stray close/open tags that might have been accidentally left inside
combined_js = combined_js.replace('</script>', '')
combined_js = combined_js.replace('<script>', '')

new_script_block = f"""
    <!-- Consolidated JS Logic -->
    <script>
{combined_js}
    </script>
"""

# Now replace the original blocks
# We'll strip everything from the first <script> (non-src) to the last </script>
start_marker = re.search(r'<script>', content).start()
end_marker = content.rfind('</script>') + 9

# Be careful not to delete <script src="...">
# Let's find the first <script> that DOES NOT have a src
m = re.search(r'<script>(.*)</script>', content, re.DOTALL)
if m:
    # Instead of complex regex, let's just use the markers
    # We'll preserve external scripts by keeping them in our new block
    src_tags = "\n    ".join(scripts_with_src)
    content = content[:start_marker] + src_tags + new_script_block + content[end_marker:]

# Fix common syntax errors like Double declarations
# If loadHomeReviews was defined twice, we keep the last one.
# But for now, let's just output and see.

with open('index.html', 'w') as f:
    f.write(content)

print("Scripts Consolidated and COUPONS fixed!")
