import re

def update_contacts(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_contacts = '''<div class="contact-items">
          <a href="tel:+421947969264" class="contact-item">
            <div class="c-ico" style="background:rgba(37,99,235,.1); border-color:rgba(37,99,235,.2); color:var(--blue-h);"><svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
            <div>
              <span class="c-lbl">Telefón</span>
              <span class="c-val" style="display:block;">+421 947 969 264</span>
              <span class="c-val" style="display:block; margin-top:4px;">+421 944 105 831</span>
            </div>
          </a>
          <a href="mailto:mbazger85@gmail.com" class="contact-item">
            <div class="c-ico" style="background:rgba(37,99,235,.1); border-color:rgba(37,99,235,.2); color:var(--blue-h);"><svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
            <div>
              <span class="c-lbl">Email</span>
              <span class="c-val">mbazger85@gmail.com</span>
            </div>
          </a>
          <div class="contact-item">
            <div class="c-ico" style="background:rgba(37,99,235,.1); border-color:rgba(37,99,235,.2); color:var(--blue-h);"><svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M17.657 16.657L13.414 20.9a2 2 0 01-2.827 0l-4.243-4.243a8 8 0 1111.314 0z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
            <div>
              <span class="c-lbl">Lokácia</span>
              <span class="c-val">Podvysoká</span>
            </div>
          </div>
        </div>
        
        <div style="margin-bottom: 30px; border-radius: var(--r-md); overflow: hidden; border: 1px solid var(--border);">
          <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d20775.297424683057!2d18.6543!3d49.4042!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x471465d3d4b68dd1%3A0x400f7d1c6978ac0!2zUG9kdnlzb2vDoQ!5e0!3m2!1ssk!2ssk!4v1700000000000!5m2!1ssk!2ssk" width="100%" height="220" style="border:0; display:block;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
        
        <div class="social-row">'''

    pattern = re.compile(r'<div class="contact-items">.*?<div class="social-row">', re.DOTALL)
    
    if pattern.search(content):
        content = pattern.sub(new_contacts, content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated {filepath}')
    else:
        print(f'Pattern not found in {filepath}')

update_contacts('index.html')
update_contacts('budovy.html')
