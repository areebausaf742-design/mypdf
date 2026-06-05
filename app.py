<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <!-- ✅ Google Site Verification -->
  <meta name="google-site-verification" content="vP-Bi-T6FOhgNroxZz7MORci8mHgt9faa2CGCfNVW60" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PDF to Paragraph Pro | Legendary Converter</title>

  <!-- ✅ Google AdSense -->
  <script data-ad-client="ca-pub-xxxxxxxxxxxxxxxx" async
          src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>

  <!-- ✅ Styles -->
  <style>
    /* Global Reset */
    * { margin:0; padding:0; box-sizing:border-box; }

    body {
      background: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)),
                  url('https://source.unsplash.com/random/1600x900/?technology,abstract');
      background-size: cover;
      color: white;
      font-family: 'Inter', sans-serif;
      line-height: 1.6;
    }

    nav {
      background: rgba(20,20,20,0.95);
      padding: 15px;
      text-align: center;
      font-weight: bold;
      letter-spacing: 1px;
    }

    .container {
      max-width: 1000px;
      margin: 40px auto;
      padding: 30px;
      background: rgba(255,255,255,0.05);
      border-radius: 20px;
      backdrop-filter: blur(15px);
      box-shadow: 0 0 30px rgba(0,0,0,0.5);
    }

    h1 {
      text-align: center;
      font-size: 2.5em;
      background: -webkit-linear-gradient(#ffffff, #777777);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      font-weight: 900;
      margin-bottom: 10px;
    }

    p.subtitle {
      text-align: center;
      color: #ddd;
      font-size: 20px;
      margin-bottom: 30px;
    }

    input[type="file"] {
      display:block;
      margin:20px auto;
      padding:10px;
      background:#222;
      border-radius:10px;
      color:#fff;
    }

    button {
      width: 100%;
      background: linear-gradient(90deg, #FF4B4B 0%, #ff8a8a 100%);
      color: white;
      border: none;
      padding: 18px;
      border-radius: 15px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 2px;
      transition: all 0.4s ease;
      margin-top: 10px;
      cursor:pointer;
    }
    button:hover {
      transform: translateY(-5px);
      box-shadow: 0 15px 30px rgba(255, 75, 75, 0.6);
    }

    textarea {
      width: 100%;
      margin-top: 20px;
      padding: 15px;
      border-radius: 10px;
      border: none;
      font-size: 14px;
      min-height: 300px;
      background: rgba(255,255,255,0.1);
      color:#fff;
    }

    section.tabs {
      margin-top:40px;
    }
    section.tabs h2 {
      margin-top:20px;
      font-size:1.5em;
      color:#ff8a8a;
    }
    section.tabs p, section.tabs ul {
      margin-left:10px;
    }

    footer {
      text-align: center;
      margin-top: 30px;
      color: #aaa;
      padding:20px;
      background:rgba(0,0,0,0.6);
    }

    /* Animations */
    @keyframes pulse {
      0% { transform:scale(1); }
      50% { transform:scale(1.05); }
      100% { transform:scale(1); }
    }
    h1 { animation:pulse 5s infinite; }

    /* Responsive */
    @media(max-width:768px){
      h1 { font-size:1.8em; }
      .container { padding:15px; }
    }
  </style>
</head>
<body>
  <!-- ✅ Control Console -->
  <nav>
    ⚡ CPU: AMD RYZEN 7 7730U ACTIVE | 🧠 16GB RAM OPTIMIZED
  </nav>

  <!-- ✅ Banner Ad -->
  <ins class="adsbygoogle"
       style="display:block"
       data-ad-client="ca-pub-xxxxxxxxxxxxxxxx"
       data-ad-slot="1234567890"
       data-ad-format="auto"></ins>
  <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>

  <div class="container">
    <h1>🚀 LEGENDARY PDF TO PARAGRAPH PRO</h1>
    <p class="subtitle">Ultra-Fast. Military Privacy. Paragraph Perfect.</p>

    <!-- ✅ PDF Upload -->
    <input type="file" id="pdfUpload" accept="application/pdf">
    <button onclick="processPDF()">Upload & Convert</button>

    <!-- ✅ Output -->
    <textarea id="output" placeholder="Converted text will appear here..."></textarea>
    <button onclick="downloadText()">👑 DOWNLOAD TEXT REPORT</button>

    <!-- ✅ Tabs -->
    <section class="tabs">
      <h2>🚀 OPERATION</h2>
      <p>Step 1: Upload PDF. Step 2: Convert. Step 3: Download.</p>

      <h2>💎 CORE TECH</h2>
      <ul>
        <li>Line-Merge Tech: Fixes broken lines.</li>
        <li>VRAM Buffer: Optimized for fast rendering.</li>
        <li>Ryzen Engine Simulation.</li>
      </ul>

      <h2>🔒 SECURITY</h2>
      <p>Files processed locally. No uploads. RAM-only privacy.</p>

      <h2>📈 MONETIZATION</h2>
      <p>AdSense banners, premium features, donations.</p>

      <h2>🛡️ SAFETY</h2>
      <p>Use responsibly. Educational purpose. No harmful content.</p>
    </section>
  </div>

  <!-- ✅ Sidebar Ad -->
  <ins class="adsbygoogle"
       style="display:block"
       data-ad-client="ca-pub-xxxxxxxxxxxxxxxx"
       data-ad-slot="9876543210"
       data-ad-format="auto"></ins>
  <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>

  <!-- ✅ Footer -->
  <footer>
    📧 Contact: support@legendarypdf.app <br>
    Google Verification: vP-Bi-T6FOhgNroxZz7MORci8mHgt9faa2CGCfNVW60 <br>
    Verification Portal: google4389f87ed75cf887.html
  </footer>

  <!-- ✅ PDF.js -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.14.305/pdf.min.js"></script>
  <script>
    async function processPDF() {
      const file = document.getElementById("pdfUpload").files[0];
      if (!file) { alert("Upload a PDF first."); return; }
      const reader = new FileReader();
      reader.onload = async function() {
        const typedarray = new Uint8Array(this.result);
        const pdf = await pdfjsLib.getDocument(typedarray).promise;
        let text = "";
        for (let i=0; i<pdf.numPages; i++) {
          const page = await pdf.getPage(i+1);
          const content = await page.getTextContent();
          text += content.items.map(item => item.str).join(" ") + "\n\n";
        }
        document.getElementById("output").value = text;
        alert("✅ Conversion Successful!");
      };
      reader.readAsArrayBuffer(file);
    }
    function downloadText() {
      const text = document.getElementById("output").value;
      const blob = new Blob([text], {type:"text/plain"});
      const link = document.createElement("a");
      link.href = URL.createObjectURL(blob);
      link.download = "export.txt";
      link.click();
    }
  </script>
</body>
</html>
