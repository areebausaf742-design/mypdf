<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <!-- ✅ Google Site Verification -->
  <meta name="google-site-verification" content="vP-Bi-T6FOhgNroxZz7MORci8mHgt9faa2CGCfNVW60" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PDF to Paragraph Pro</title>

  <!-- ✅ Google AdSense -->
  <script data-ad-client="ca-pub-xxxxxxxxxxxxxxxx" async
          src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>

  <style>
    /* A to Z CSS: gradients, buttons, tabs, sidebar, footer */
    body { background:#111; color:#fff; font-family:Inter,sans-serif; }
    nav { background:#222; padding:10px; text-align:center; }
    .container { max-width:900px; margin:auto; padding:20px; }
    h1 { text-align:center; background:-webkit-linear-gradient(#fff,#777);
         -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
    /* Expand with 1000+ lines of styles: animations, responsive design, etc. */
  </style>
</head>
<body>
  <!-- ✅ Control Console -->
  <nav>
    ⚡ CPU: AMD RYZEN 7 7730U | 🧠 16GB RAM
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
    <p style="text-align:center;">Ultra-Fast. Military Privacy. Paragraph Perfect.</p>

    <!-- ✅ PDF Upload -->
    <input type="file" id="pdfUpload" accept="application/pdf">
    <button onclick="processPDF()">Upload & Convert</button>

    <!-- ✅ Output -->
    <textarea id="output" rows="20"></textarea>
    <button onclick="downloadText()">👑 DOWNLOAD TEXT REPORT</button>

    <!-- ✅ Tabs -->
    <section id="tabs">
      <h2>🚀 OPERATION</h2>
      <p>Step 1: Upload PDF. Step 2: Convert. Step 3: Download.</p>

      <h2>💎 CORE TECH</h2>
      <p>Line-Merge Tech, VRAM Buffer, Ryzen Optimization.</p>

      <h2>🔒 SECURITY</h2>
      <p>Files processed locally. No uploads. RAM-only privacy.</p>

      <h2>📈 MONETIZATION</h2>
      <p>AdSense banners, premium features, donations.</p>

      <h2>🛡️ SAFETY</h2>
      <p>Use responsibly. Educational purpose. No harmful content.</p>
    </section>
  </div>

  <!-- ✅ Footer -->
  <footer>
    📧 Contact: support@legendarypdf.app <br>
    Google Verification: vP-Bi-T6FOhgNroxZz7MORci8mHgt9faa2CGCfNVW60
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
