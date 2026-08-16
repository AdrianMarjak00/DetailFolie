import re

def fix_phones(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The existing block starts with <a href="tel:+421947969264" class="contact-item">
    # and ends with </a>.
    # I need to target the whole phone block and replace it.
    
    old_phone_pattern = r'<a href="tel:\+421947969264" class="contact-item">.*?<span class="c-lbl">Telefón</span>\s*<span class="c-val"[^>]*>\+421 947 969 264</span>\s*<span class="c-val"[^>]*>\+421 944 105 831</span>\s*</div>\s*</a>'
    
    new_phone_block = '''<div class="contact-item" style="align-items: flex-start;">
            <div class="c-ico" style="background:rgba(37,99,235,.1); border-color:rgba(37,99,235,.2); color:var(--blue-h); margin-top: 2px;">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </div>
            <div style="display: flex; flex-direction: column; gap: 6px;">
              <span class="c-lbl">Telefón</span>
              <a href="tel:+421947969264" class="phone-link c-val">
                +421 947 969 264
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" style="opacity: 0.5; margin-left: 4px;"><path d="M5 12h14M12 5l7 7-7 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
              </a>
              <a href="tel:+421944105831" class="phone-link c-val">
                +421 944 105 831
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" style="opacity: 0.5; margin-left: 4px;"><path d="M5 12h14M12 5l7 7-7 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
              </a>
            </div>
          </div>'''

    if re.search(old_phone_pattern, content, re.DOTALL):
        content = re.sub(old_phone_pattern, new_phone_block, content, flags=re.DOTALL)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated phones in {filepath}')
    else:
        print(f'Phone block not found in {filepath}')

fix_phones('index.html')
fix_phones('budovy.html')

def append_css():
    filepath = 'style.css'
    css = '''
/* DUAL PHONE LINKS */
.phone-link {
  display: inline-flex;
  align-items: center;
  text-decoration: none;
  transition: all 0.3s ease;
  position: relative;
}
.phone-link svg {
  transition: transform 0.3s ease, opacity 0.3s ease;
}
.phone-link:hover {
  color: var(--blue-h);
}
.phone-link:hover svg {
  transform: translateX(4px);
  opacity: 1 !important;
}
.contact-item { transition: all 0.3s ease; }
.contact-item:hover { border-color:rgba(37,99,235,.2); box-shadow:var(--shadow-a); }
'''
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(css)
    print('Appended CSS')

append_css()
