#!/usr/bin/env python3
"""
Loraks TravelTech - Bütünleşik Proje Okuyucu Üreteci (Single Page Reader Generator)
Bu betik docs, src, tests, database ve anayasa dosyalarını tek bir scrollable HTML
ve tek bir birleşik Markdown dosyası haline getirir.
"""

import os
import json
import html

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML_OUTPUT = os.path.join(WORKSPACE_DIR, "LORAKS_PROJE_KUTUPHANESI.html")
MD_OUTPUT = os.path.join(WORKSPACE_DIR, "LORAKS_TUM_PROJE_TEK_DOSYA.md")

FILE_GROUPS = [
    {
        "category": "🏛️ Proje Anayasası & Genel Bakış",
        "badge": "Yönetişim",
        "badge_color": "bg-purple-100 text-purple-800",
        "files": [
            ("AGENTS.md", "markdown"),
            ("README.md", "markdown"),
        ]
    },
    {
        "category": "📑 Resmi Dokümanlar & Blueprintler (docs/)",
        "badge": "Dokümantasyon",
        "badge_color": "bg-blue-100 text-blue-800",
        "files": [
            ("docs/01_master_plan_v5_1.md", "markdown"),
            ("docs/02_yonetim_kurulu_ve_ortaklar_sunum_notu.md", "markdown"),
            ("docs/03_kuresel_iyi_ornekler_ve_buyume_kanallari.md", "markdown"),
            ("docs/04_marka_kimligi_ve_gorsel_rehber.md", "markdown"),
            ("docs/05_smmm_ve_acente_gorusme_dosyasi.md", "markdown"),
            ("docs/06_host_os_ve_yan_gelirler.md", "markdown"),
            ("docs/07_lovable_ve_ai_studio_kurulum_workflow.md", "markdown"),
            ("docs/08_one_pager_yatirimci_ozeti.md", "markdown"),
            ("docs/09_yazilim_ve_vergi_test_otomasyonu_dokumani_v3.md", "markdown"),
            ("docs/10_loraks_preview_master_prompt.md", "markdown"),
            ("docs/11_creator_academy_ve_kokartli_rehber_agi_raporu.md", "markdown"),
            ("docs/12_loraks_traveltech_final_master_blueprint_v5_3.md", "markdown"),
            ("docs/13_denetim_simulasyonu_ve_stratejik_kiyaslama.md", "markdown"),
            ("docs/14_loraks_traveltech_uc_uc_analiz_raporu.md", "markdown"),
            ("docs/15_canliya_gecis_master_yapilacaklar_listesi.md", "markdown"),
            ("docs/16_surum_evrimi_ve_eksiklik_analiz_raporu.md", "markdown"),
            ("docs/17_loraks_traveltech_nihai_birlesik_master_blueprint_v5_4.md", "markdown"),
        ]
    },
    {
        "category": "💻 Kaynak Kodlar & Motorlar (src/)",
        "badge": "Yazılım Motoru",
        "badge_color": "bg-emerald-100 text-emerald-800",
        "files": [
            ("src/tax_engine.py", "python"),
            ("src/payment_engine.py", "python"),
            ("src/payout_engine.py", "python"),
            ("src/pathway_engine.py", "python"),
            ("src/safe_harbor_filters.py", "python"),
            ("src/wallet_ledger.py", "python"),
            ("src/intercompany_billing.py", "python"),
            ("src/refund_engine.py", "python"),
            ("src/ai_audit_agent.py", "python"),
            ("src/server.py", "python"),
            ("src/exceptions.py", "python"),
        ]
    },
    {
        "category": "🧪 Test Senaryoları & Otomasyon (tests/)",
        "badge": "Kalite & Test",
        "badge_color": "bg-amber-100 text-amber-800",
        "files": [
            ("tests/run_all_tests.py", "python"),
            ("tests/test_integration.py", "python"),
            ("tests/test_compliance_automation.py", "python"),
            ("tests/test_payment_engine.py", "python"),
            ("tests/test_pathway_engine.py", "python"),
            ("tests/test_wallet_ledger.py", "python"),
        ]
    },
    {
        "category": "🗄️ Veritabanı Mimarisi (database/)",
        "badge": "Veritabanı",
        "badge_color": "bg-rose-100 text-rose-800",
        "files": [
            ("database/schema.sql", "sql"),
            ("database/seed.sql", "sql"),
        ]
    }
]

def make_id(filepath):
    return "sec_" + filepath.replace("/", "_").replace(".", "_")

def generate_markdown():
    lines = []
    lines.append("# LORAKS TRAVELTECH — BÜTÜNLEŞİK PROJE KÜTÜPHANESİ")
    lines.append("> **Tüm Dokümanlar, Yazılım Motorları (src), Testler ve Veritabanı Şemaları Tek Sayfada**\n")
    lines.append("## 📌 İçindekiler Tablosu\n")
    
    for group in FILE_GROUPS:
        lines.append(f"### {group['category']}")
        for fpath, ftype in group['files']:
            title = os.path.basename(fpath)
            anchor = make_id(fpath)
            lines.append(f"- [{title} (`{fpath}`)](\#{anchor})")
        lines.append("")

    lines.append("\n---\n")

    for group in FILE_GROUPS:
        lines.append(f"\n# {group['category']}\n")
        for fpath, ftype in group['files']:
            full_path = os.path.join(WORKSPACE_DIR, fpath)
            anchor = make_id(fpath)
            title = os.path.basename(fpath)
            if not os.path.exists(full_path):
                continue
            with open(full_path, "r", encoding="utf-8") as f:
                content = f.read()

            lines.append(f"\n<a id='{anchor}'></a>")
            lines.append(f"## 📄 {title} (`{fpath}`)")
            lines.append(f"*{group['badge']}* | Dosya Yolu: `{fpath}`\n")
            
            if ftype == "markdown":
                lines.append(content)
            else:
                lines.append(f"```{ftype}\n{content}\n```")
            lines.append("\n---\n")

    with open(MD_OUTPUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Markdown dosyası oluşturuldu: {MD_OUTPUT}")

def generate_html():
    sections_json = []

    for group in FILE_GROUPS:
        g_data = {
            "category": group["category"],
            "badge": group["badge"],
            "badge_color": group["badge_color"],
            "items": []
        }
        for fpath, ftype in group["files"]:
            full_path = os.path.join(WORKSPACE_DIR, fpath)
            if not os.path.exists(full_path):
                continue
            with open(full_path, "r", encoding="utf-8") as f:
                content = f.read()
            g_data["items"].append({
                "id": make_id(fpath),
                "path": fpath,
                "filename": os.path.basename(fpath),
                "type": ftype,
                "content": content
            })
        sections_json.append(g_data)

    data_payload = json.dumps(sections_json, ensure_ascii=False)

    html_template = f"""<!DOCTYPE html>
<html lang="tr" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>LORAKS TRAVELTECH — Bütünleşik Proje Kütüphanesi</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <!-- Marked.js for Markdown -->
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <!-- Highlight.js for Syntax Highlighting -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/python.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/sql.min.js"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400&display=swap');
    
    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }}
    .font-mono {{
      font-family: 'JetBrains Mono', monospace;
    }}
    .prose-custom h1 {{ font-size: 1.875rem; font-weight: 800; margin-top: 1.75rem; margin-bottom: 0.75rem; color: #0f172a; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.5rem; }}
    .prose-custom h2 {{ font-size: 1.5rem; font-weight: 700; margin-top: 1.5rem; margin-bottom: 0.5rem; color: #1e293b; }}
    .prose-custom h3 {{ font-size: 1.25rem; font-weight: 600; margin-top: 1.25rem; margin-bottom: 0.5rem; color: #334155; }}
    .prose-custom p {{ margin-bottom: 0.875rem; line-height: 1.7; color: #334155; }}
    .prose-custom ul, .prose-custom ol {{ margin-left: 1.5rem; margin-bottom: 1rem; color: #334155; }}
    .prose-custom ul {{ list-style-type: disc; }}
    .prose-custom ol {{ list-style-type: decimal; }}
    .prose-custom li {{ margin-bottom: 0.25rem; }}
    .prose-custom blockquote {{ border-left: 4px solid #6366f1; padding-left: 1rem; margin-top: 1rem; margin-bottom: 1rem; color: #475569; background-color: #f8fafc; padding-top: 0.5rem; padding-bottom: 0.5rem; border-radius: 0 0.375rem 0.375rem 0; }}
    .prose-custom table {{ width: 100%; border-collapse: collapse; margin-top: 1rem; margin-bottom: 1rem; font-size: 0.875rem; }}
    .prose-custom th, .prose-custom td {{ border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem; text-align: left; }}
    .prose-custom th {{ background-color: #f1f5f9; font-weight: 600; color: #1e293b; }}
    .prose-custom tr:nth-child(even) {{ background-color: #f8fafc; }}
    .prose-custom code:not(pre code) {{ background-color: #e2e8f0; color: #0f172a; padding: 0.15rem 0.35rem; border-radius: 0.25rem; font-size: 0.85em; font-family: 'JetBrains Mono', monospace; }}
    .prose-custom hr {{ margin-top: 2rem; margin-bottom: 2rem; border-color: #cbd5e1; }}
    
    /* Dark mode classes */
    .dark .prose-custom h1 {{ color: #f8fafc; border-bottom-color: #334155; }}
    .dark .prose-custom h2 {{ color: #f1f5f9; }}
    .dark .prose-custom h3 {{ color: #e2e8f0; }}
    .dark .prose-custom p, .dark .prose-custom li {{ color: #cbd5e1; }}
    .dark .prose-custom blockquote {{ border-left-color: #818cf8; background-color: #1e293b; color: #94a3b8; }}
    .dark .prose-custom th, .dark .prose-custom td {{ border-color: #334155; }}
    .dark .prose-custom th {{ background-color: #1e293b; color: #f8fafc; }}
    .dark .prose-custom tr:nth-child(even) {{ background-color: #0f172a; }}
    .dark .prose-custom code:not(pre code) {{ background-color: #334155; color: #38bdf8; }}
  </style>
</head>
<body class="bg-slate-50 text-slate-900 transition-colors duration-200">

  <!-- Top Sticky Bar -->
  <header class="sticky top-0 z-50 bg-white/90 backdrop-blur-md border-b border-slate-200 px-6 py-3 flex items-center justify-between shadow-xs">
    <div class="flex items-center gap-3">
      <div class="w-8 h-8 rounded-lg bg-indigo-600 flex items-center justify-center text-white font-black text-lg shadow-sm">
        L
      </div>
      <div>
        <h1 class="text-base font-bold text-slate-900 leading-tight">LORAKS TRAVELTECH — Bütünleşik Proje Kütüphanesi</h1>
        <p class="text-xs text-slate-500">Tüm Belgeler (docs), Motorlar (src), Testler ve Veritabanı • Tek Sayfada Kesintisiz Kaydırma</p>
      </div>
    </div>
    
    <div class="flex items-center gap-3">
      <div class="relative">
        <input id="searchInput" type="text" placeholder="Dosyalarda ara... (Cmd+K)" 
          class="text-xs bg-slate-100 hover:bg-slate-200/70 focus:bg-white border border-slate-300 rounded-full pl-8 pr-4 py-1.5 focus:outline-none focus:ring-2 focus:ring-indigo-500 w-48 sm:w-64 transition-all">
        <svg class="w-3.5 h-3.5 text-slate-400 absolute left-2.5 top-2.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
        </svg>
      </div>

      <button id="themeToggle" class="p-2 text-slate-500 hover:text-slate-800 rounded-lg hover:bg-slate-100 text-xs font-semibold flex items-center gap-1">
        <span id="themeIcon">🌙</span>
      </button>

      <button onclick="window.print()" class="hidden md:flex items-center gap-1.5 px-3 py-1.5 text-xs font-medium text-slate-700 bg-slate-100 hover:bg-slate-200 rounded-lg border border-slate-300">
        🖨️ PDF / Yazdır
      </button>
    </div>
  </header>

  <div class="flex max-w-[1700px] mx-auto">
    <!-- Sidebar Navigation -->
    <aside id="sidebar" class="w-72 lg:w-80 shrink-0 h-[calc(100vh-57px)] sticky top-[57px] border-r border-slate-200 bg-white/70 overflow-y-auto p-4 space-y-6">
      <div class="text-[11px] font-bold text-slate-400 uppercase tracking-wider px-2">Kütüphane İndeksi</div>
      <nav id="navTree" class="space-y-5 text-xs"></nav>
    </aside>

    <!-- Main Content Area -->
    <main id="mainContainer" class="flex-1 min-w-0 p-6 lg:p-10 space-y-16">
      <!-- Welcome Hero Banner -->
      <section class="bg-gradient-to-br from-indigo-900 via-indigo-800 to-slate-900 text-white rounded-2xl p-8 shadow-xl relative overflow-hidden">
        <div class="max-w-3xl space-y-3 relative z-10">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/10 text-indigo-200 text-xs font-medium">
            <span>✨ Loraks Unified Project Viewer</span>
            <span>•</span>
            <span>Master Edition v5.4</span>
          </div>
          <h2 class="text-3xl font-extrabold tracking-tight">Tüm Proje Tek Ekranda, Kesintisiz Kaydırılabilir</h2>
          <p class="text-indigo-200 text-sm leading-relaxed">
            Bu sayfa; <strong>docs/</strong> altındaki 17 stratejik ve yasal belgeyi, <strong>src/</strong> içerisindeki tüm yazılım motorlarını, 
            <strong>tests/</strong> senaryolarını ve <strong>database/</strong> şemalarını tek bir akışta sunar. 
            Sol menüden istediğiniz belgeye atlayabilir veya aşağı doğru kaydırarak baştan sona inceleyebilirsiniz.
          </p>
          <div class="pt-2 flex flex-wrap gap-2 text-xs">
            <span class="px-2.5 py-1 bg-white/10 rounded-md">📄 17 Doküman</span>
            <span class="px-2.5 py-1 bg-white/10 rounded-md">💻 11 Python Motoru</span>
            <span class="px-2.5 py-1 bg-white/10 rounded-md">🧪 6 Test Dosyası</span>
            <span class="px-2.5 py-1 bg-white/10 rounded-md">🗄️ SQL Şemaları</span>
          </div>
        </div>
      </section>

      <!-- Dynamic File Sections -->
      <div id="contentSections" class="space-y-16"></div>
    </main>
  </div>

  <!-- Floating Back to Top Button -->
  <button id="backToTop" class="fixed bottom-6 right-6 w-11 h-11 bg-indigo-600 text-white rounded-full shadow-lg flex items-center justify-center opacity-0 pointer-events-none transition-all duration-300 hover:bg-indigo-700 hover:scale-105 z-50">
    ↑
  </button>

  <script>
    const PROJECT_DATA = {data_payload};

    // Render Navigation and Content
    const navTree = document.getElementById('navTree');
    const contentSections = document.getElementById('contentSections');

    PROJECT_DATA.forEach((group, gIndex) => {{
      // Sidebar Group
      const groupDiv = document.createElement('div');
      groupDiv.className = 'space-y-1.5';
      
      const groupHeader = document.createElement('div');
      groupHeader.className = 'font-semibold text-slate-800 text-[13px] flex items-center justify-between px-2 py-1';
      groupHeader.innerHTML = `<span>${{group.category}}</span><span class="text-[10px] ${{group.badge_color}} px-1.5 py-0.5 rounded font-mono">${{group.items.length}}</span>`;
      groupDiv.appendChild(groupHeader);

      const ul = document.createElement('ul');
      ul.className = 'space-y-0.5 border-l-2 border-slate-100 ml-3 pl-2';

      group.items.forEach(item => {{
        const li = document.createElement('li');
        li.innerHTML = `
          <a href="#${{item.id}}" id="nav-link-${{item.id}}" 
             class="nav-item block py-1 px-2 rounded text-slate-600 hover:text-indigo-600 hover:bg-indigo-50/50 transition-colors truncate">
            ${{item.filename}}
          </a>
        `;
        ul.appendChild(li);

        // Content Section
        const sec = document.createElement('section');
        sec.id = item.id;
        sec.className = 'scroll-mt-20 bg-white rounded-xl border border-slate-200/80 shadow-xs p-6 lg:p-8 space-y-4';

        // Header for section
        sec.innerHTML = `
          <div class="flex flex-wrap items-center justify-between gap-3 border-b border-slate-100 pb-4">
            <div class="flex items-center gap-2">
              <span class="text-xs font-mono font-medium ${{group.badge_color}} px-2.5 py-1 rounded-md">
                ${{group.badge}}
              </span>
              <h2 class="text-xl font-bold text-slate-900 font-mono">${{item.filename}}</h2>
              <span class="text-xs text-slate-400 font-mono">(${{item.path}})</span>
            </div>
            <div class="flex items-center gap-2">
              <button onclick="copyToClipboard('${{item.id}}')" class="text-xs px-2.5 py-1 bg-slate-100 hover:bg-slate-200 text-slate-600 rounded font-medium flex items-center gap-1 transition-colors">
                📋 Kopyala
              </button>
              <a href="#${{item.id}}" class="text-xs px-2.5 py-1 bg-slate-100 hover:bg-slate-200 text-slate-600 rounded font-medium">
                🔗 Bağlantı
              </a>
            </div>
          </div>
          <div id="body-${{item.id}}" class="min-w-0"></div>
        `;
        contentSections.appendChild(sec);

        // Render Markdown or Code
        const bodyContainer = sec.querySelector(`#body-${{item.id}}`);
        if (item.type === 'markdown') {{
          bodyContainer.className = 'prose-custom';
          try {{
            bodyContainer.innerHTML = marked.parse(item.content);
          }} catch(e) {{
            bodyContainer.textContent = item.content;
          }}
        }} else {{
          const pre = document.createElement('pre');
          pre.className = 'rounded-xl overflow-x-auto bg-[#0d1117] p-4 text-xs font-mono text-slate-100 border border-slate-800 shadow-inner';
          const code = document.createElement('code');
          code.className = `language-${{item.type}}`;
          code.textContent = item.content;
          pre.appendChild(code);
          bodyContainer.appendChild(pre);
          hljs.highlightElement(code);
        }}
      }});

      groupDiv.appendChild(ul);
      navTree.appendChild(groupDiv);
    }});

    // Copy Content Function
    window.copyToClipboard = function(itemId) {{
      for (const group of PROJECT_DATA) {{
        for (const item of group.items) {{
          if (item.id === itemId) {{
            navigator.clipboard.writeText(item.content);
            alert(`"${{item.filename}}" içeriği panoya kopyalandı!`);
            return;
          }}
        }}
      }}
    }};

    // Search Filter
    const searchInput = document.getElementById('searchInput');
    searchInput.addEventListener('input', (e) => {{
      const query = e.target.value.toLowerCase().trim();
      document.querySelectorAll('.nav-item').forEach(link => {{
        const text = link.textContent.toLowerCase();
        const li = link.closest('li');
        if (!query || text.includes(query)) {{
          li.style.display = 'block';
        }} else {{
          li.style.display = 'none';
        }}
      }});
    }});

    // Active Scrollspy
    const sections = document.querySelectorAll('main section[id]');
    window.addEventListener('scroll', () => {{
      let current = '';
      const scrollY = window.pageYOffset;
      sections.forEach(section => {{
        const sectionTop = section.offsetTop - 120;
        if (scrollY >= sectionTop) {{
          current = section.getAttribute('id');
        }}
      }});

      document.querySelectorAll('.nav-item').forEach(a => {{
        a.classList.remove('text-indigo-600', 'bg-indigo-50', 'font-bold');
        if (a.getAttribute('href') === `#${{current}}`) {{
          a.classList.add('text-indigo-600', 'bg-indigo-50', 'font-bold');
        }}
      }});

      // Back to top button visibility
      const btt = document.getElementById('backToTop');
      if (scrollY > 500) {{
        btt.classList.remove('opacity-0', 'pointer-events-none');
        btt.classList.add('opacity-100');
      }} else {{
        btt.classList.add('opacity-0', 'pointer-events-none');
        btt.classList.remove('opacity-100');
      }}
    }});

    document.getElementById('backToTop').addEventListener('click', () => {{
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }});

    // Dark Mode Toggle
    const themeToggle = document.getElementById('themeToggle');
    const themeIcon = document.getElementById('themeIcon');
    let isDark = false;
    themeToggle.addEventListener('click', () => {{
      isDark = !isDark;
      if (isDark) {{
        document.documentElement.classList.add('dark');
        document.body.classList.replace('bg-slate-50', 'bg-slate-950');
        document.body.classList.replace('text-slate-900', 'text-slate-100');
        document.getElementById('sidebar').classList.replace('bg-white/70', 'bg-slate-900/80');
        themeIcon.textContent = '☀️';
      }} else {{
        document.documentElement.classList.remove('dark');
        document.body.classList.replace('bg-slate-950', 'bg-slate-50');
        document.body.classList.replace('text-slate-100', 'text-slate-900');
        document.getElementById('sidebar').classList.replace('bg-slate-900/80', 'bg-white/70');
        themeIcon.textContent = '🌙';
      }}
    }});
  </script>
</body>
</html>
"""

    with open(HTML_OUTPUT, "w", encoding="utf-8") as f:
        f.write(html_template)
    print(f"HTML kütüphane dosyası oluşturuldu: {HTML_OUTPUT}")

if __name__ == "__main__":
    generate_markdown()
    generate_html()
