import base64
import os

def generate_svg_banner(image_path, output_path):
    print(f"Reading image from: {image_path}")
    if not os.path.exists(image_path):
        print(f"Error: Image path '{image_path}' does not exist.")
        return False
        
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        
    mime_type = "image/jpeg"
    if image_path.lower().endswith(".png"):
        mime_type = "image/png"
        
    image_uri = f"data:{mime_type};base64,{encoded_string}"
    
    # Clean, premium Futuristic HUD SVG Layout
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 380" width="100%" height="100%" style="background:#07090e; font-family:'Fira Code', 'Courier New', monospace;">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#05070a" />
      <stop offset="100%" stop-color="#0c131d" />
    </linearGradient>

    <!-- Cyber Neon Glows -->
    <filter id="neon-glow-green" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <filter id="neon-glow-blue" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
    
    <!-- Profile Image Mask -->
    <clipPath id="avatar-clip">
      <rect x="40" y="40" width="300" height="300" rx="20" />
    </clipPath>

    <!-- Scanline Pattern for Camera Feed Look -->
    <pattern id="scanlines" width="4" height="4" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="4" y2="0" stroke="#000000" stroke-width="1.5" opacity="0.2" />
    </pattern>
  </defs>

  <!-- Background Rect with tech grid lines -->
  <rect width="1000" height="380" fill="url(#bg-grad)" />
  
  <!-- Subtle Grid Pattern -->
  <g stroke="#122538" stroke-width="0.5" opacity="0.15">
    <path d="M 0,40 L 1000,40 M 0,80 L 1000,80 M 0,120 L 1000,120 M 0,160 L 1000,160 M 0,200 L 1000,200 M 0,240 L 1000,240 M 0,280 L 1000,280 M 0,320 L 1000,320" />
    <path d="M 100,0 L 100,380 M 200,0 L 200,380 M 300,0 L 300,380 M 400,0 L 400,380 M 500,0 L 500,380 M 600,0 L 600,380 M 700,0 L 700,380 M 800,0 L 800,380 M 900,0 L 900,380" />
  </g>

  <!-- Cybernetic Border Outline for Entire Banner -->
  <rect x="5" y="5" width="990" height="370" fill="none" stroke="#00ffa3" stroke-width="1.5" opacity="0.4" rx="10" />
  
  <!-- Decorative corner sub-elements -->
  <path d="M 5,30 L 5,5 L 30,5" fill="none" stroke="#00ffa3" stroke-width="3" filter="url(#neon-glow-green)" />
  <path d="M 995,30 L 995,5 L 970,5" fill="none" stroke="#00ffa3" stroke-width="3" filter="url(#neon-glow-green)" />
  <path d="M 5,350 L 5,375 L 30,375" fill="none" stroke="#00ffa3" stroke-width="3" filter="url(#neon-glow-green)" />
  <path d="M 995,350 L 995,375 L 970,375" fill="none" stroke="#00ffa3" stroke-width="3" filter="url(#neon-glow-green)" />

  <!-- ==================== LEFT COLUMN: COMPUTER VISION HUD ==================== -->
  <g>
    <!-- Background of Image Box -->
    <rect x="40" y="40" width="300" height="300" rx="20" fill="#0b131f" stroke="#122538" stroke-width="2" />
    
    <!-- Base64 Encoded Profile Image -->
    <image x="40" y="40" width="300" height="300" href="{image_uri}" clip-path="url(#avatar-clip)" preserveAspectRatio="xMidYMid slice" />
    
    <!-- Scanline overlay -->
    <rect x="40" y="40" width="300" height="300" fill="url(#scanlines)" clip-path="url(#avatar-clip)" />
    
    <!-- MediaPipe-Style 3D Facial Keypoints & Mesh Connections Overlay -->
    <g stroke="#39ff14" stroke-width="0.8" opacity="0.6">
      <!-- Face Mesh Edges -->
      <line x1="190" y1="95" x2="160" y2="115" />
      <line x1="190" y1="95" x2="220" y2="115" />
      <line x1="190" y1="95" x2="190" y2="120" />
      <line x1="160" y1="115" x2="175" y2="125" />
      <line x1="220" y1="115" x2="205" y2="125" />
      <line x1="190" y1="120" x2="175" y2="125" />
      <line x1="190" y1="120" x2="205" y2="125" />
      <line x1="175" y1="125" x2="190" y2="145" />
      <line x1="205" y1="125" x2="190" y2="145" />
      <line x1="160" y1="115" x2="150" y2="155" />
      <line x1="220" y1="115" x2="230" y2="155" />
      <line x1="175" y1="125" x2="150" y2="155" />
      <line x1="205" y1="125" x2="230" y2="155" />
      <line x1="150" y1="155" x2="165" y2="195" />
      <line x1="230" y1="155" x2="215" y2="195" />
      <line x1="190" y1="145" x2="190" y2="175" />
      <line x1="150" y1="155" x2="190" y2="175" />
      <line x1="230" y1="155" x2="190" y2="175" />
      <line x1="165" y1="195" x2="190" y2="215" />
      <line x1="215" y1="195" x2="190" y2="215" />
      <line x1="190" y1="175" x2="190" y2="215" />
      <line x1="165" y1="195" x2="190" y2="175" />
      <line x1="215" y1="195" x2="190" y2="175" />
    </g>

    <!-- Face Mesh Vertices -->
    <g fill="#00e5ff" opacity="0.9">
      <circle cx="190" cy="95" r="2.5" />
      <circle cx="160" cy="115" r="2.5" />
      <circle cx="220" cy="115" r="2.5" />
      <circle cx="175" cy="125" r="2.5" />
      <circle cx="205" cy="125" r="2.5" />
      <circle cx="190" cy="120" r="2.5" />
      <circle cx="190" cy="145" r="2.5" />
      <circle cx="150" cy="155" r="2.5" />
      <circle cx="230" cy="155" r="2.5" />
      <circle cx="190" cy="175" r="2.5" />
      <circle cx="165" cy="195" r="2.5" />
      <circle cx="215" cy="195" r="2.5" />
      <circle cx="190" cy="215" r="2.5" />
    </g>
    
    <!-- Target Bounding Box Corners (Computer Vision Style) -->
    <!-- Top-Left Corner -->
    <path d="M 30,55 L 30,30 L 55,30" fill="none" stroke="#00FFAA" stroke-width="3.5" filter="url(#neon-glow-green)" />
    <!-- Top-Right Corner -->
    <path d="M 350,55 L 350,30 L 325,30" fill="none" stroke="#00FFAA" stroke-width="3.5" filter="url(#neon-glow-green)" />
    <!-- Bottom-Left Corner -->
    <path d="M 30,325 L 30,350 L 55,350" fill="none" stroke="#00FFAA" stroke-width="3.5" filter="url(#neon-glow-green)" />
    <!-- Bottom-Right Corner -->
    <path d="M 350,325 L 350,350 L 325,350" fill="none" stroke="#00FFAA" stroke-width="3.5" filter="url(#neon-glow-green)" />
    
    <!-- CV Bounding Box Target Label -->
    <rect x="40" y="40" width="220" height="22" rx="4" fill="#00ffa3" opacity="0.85" />
    <text x="50" y="55" font-family="'Fira Code', monospace" font-size="10" font-weight="bold" fill="#000">FACE_MESH: LOCKED // CONF: 99.85%</text>

    <!-- Bottom CV Scanning Bar (Subtle) -->
    <line x1="40" y1="300" x2="340" y2="300" stroke="#00ffa3" stroke-width="1.5" opacity="0.7" stroke-dasharray="8 4" />
    <text x="45" y="332" font-family="'Fira Code', monospace" font-size="9" fill="#00e5ff" opacity="0.8">SYS_STAT: MONITORING_ACTIVE</text>
  </g>

  <!-- ==================== RIGHT COLUMN: CYBERNETIC DETAILS ==================== -->
  
  <!-- Main Name Header -->
  <g transform="translate(390, 45)">
    <text x="0" y="40" font-size="36" font-weight="bold" fill="#ffffff" letter-spacing="1">MOKSH SHARMA</text>
    <text x="2" y="68" font-size="14" font-weight="bold" fill="#00ffa3">> AI AGENT BUILDER | CV ENGINEER | ML SYSTEMS</text>
    
    <!-- Divider HUD Line -->
    <line x1="0" y1="84" x2="570" y2="84" stroke="#1b354f" stroke-width="1.5" />
    <rect x="0" y="83" width="45" height="3" fill="#00ffa3" />
    <circle cx="565" cy="84" r="3" fill="#00e5ff" />
  </g>

  <!-- Cyber System Metadata Dashboard Panel -->
  <g transform="translate(390, 150)">
    <!-- Tech Frame -->
    <rect x="0" y="0" width="570" height="135" rx="8" fill="#0a1017" stroke="#1b354f" stroke-width="1" />
    <path d="M 0,20 L 0,0 L 20,0" fill="none" stroke="#00e5ff" stroke-width="2" />
    <path d="M 570,20 L 570,0 L 550,0" fill="none" stroke="#00e5ff" stroke-width="2" />
    <path d="M 0,115 L 0,135 L 20,135" fill="none" stroke="#00e5ff" stroke-width="2" />
    <path d="M 570,115 L 570,135 L 550,135" fill="none" stroke="#00e5ff" stroke-width="2" />

    <!-- Metadata Details -->
    <g transform="translate(20, 28)" font-size="11" fill="#8ca0b3">
      <!-- Row 1 -->
      <text x="0" y="0" font-weight="bold" fill="#00ffa3">IDENTITY:</text>
      <text x="110" y="0" fill="#ffffff">MOKSH_SHARMA // CORE_AGENT_0x07</text>

      <!-- Row 2 -->
      <text x="0" y="24" font-weight="bold" fill="#00ffa3">AFFILIATION:</text>
      <text x="110" y="24" fill="#ffffff">AI/ML LEAD @ GDG ON CAMPUS DCRUST</text>

      <!-- Row 3 -->
      <text x="0" y="48" font-weight="bold" fill="#00ffa3">ACADEMICS:</text>
      <text x="110" y="48" fill="#ffffff">B.TECH COMPUTER SCIENCE &amp; ENG (2024 - 2028)</text>

      <!-- Row 4 -->
      <text x="0" y="72" font-weight="bold" fill="#00ffa3">SYSTEM FOCUS:</text>
      <text x="110" y="72" fill="#00e5ff" font-weight="bold">AUTONOMOUS AGENTS · COMPUTER VISION · APPLIED ML</text>
      
      <!-- Row 5 -->
      <text x="0" y="96" font-weight="bold" fill="#00ffa3">STATUS LOG:</text>
      <text x="110" y="96" fill="#8ca0b3">ONLINE // PIPELINES RUNNING OPTIMAL // SECURE ✓</text>
    </g>
  </g>

  <!-- Lower Tech Stats Decors -->
  <g transform="translate(390, 310)">
    <text x="0" y="10" font-size="9" fill="#00ffa3" font-weight="bold">> ENGINE_STATUS: OPERATIONAL</text>
    <text x="260" y="10" font-size="9" fill="#8ca0b3">SYSTEM_LOAD: 12% // ACTIVE_THREADS: 48 // LATENCY: 2ms</text>
  </g>
</svg>
"""
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Banner generated successfully at: {output_path}")
    return True

if __name__ == "__main__":
    img_name = "WhatsApp Image 2026-07-16 at 10.40.02 PM.jpeg"
    workspace_dir = "d:\\New folder"
    
    img_path = os.path.join(workspace_dir, img_name)
    assets_dir = os.path.join(workspace_dir, "assets")
    if not os.path.exists(assets_dir):
        os.makedirs(assets_dir)
        print(f"Created assets directory at: {assets_dir}")
        
    output_path = os.path.join(assets_dir, "profile_banner.svg")
    
    success = generate_svg_banner(img_path, output_path)
    if success:
        print("\nSUCCESS: Custom SVG profile banner is created.")
        print(f"It is saved at: {output_path}")
        print("You can reference this SVG in your GitHub README.md using:")
        print(f'<img src="assets/profile_banner.svg" width="100%" />')
    else:
        print("\nFAILURE: Could not create profile banner.")
