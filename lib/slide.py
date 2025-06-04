from IPython.display import display, HTML

def show_html_slides(slides_data):
    """
    slides_data: 각 슬라이드의 제목과 내용 리스트를 담은 딕셔너리의 리스트.
                 예: [{'title': '슬라이드 제목', 'items': ['항목 1', '항목 2', ...]}]
    """
    totalSlides = len(slides_data)
    slides_html_content = ""
    for idx, slide_data in enumerate(slides_data):
        active = "active" if idx == 0 else ""
        title = slide_data.get('title', '')
        items = slide_data.get('items', [])

        content_html = f'<h1 class="slide-header-title">{title}</h1>'
        if items:
            content_html += '<ul class="slide-list-content">'
            for item in items:
                content_html += f'<li>{item}</li>'
            content_html += '</ul>'
        
        slides_html_content += f'''
        <div class="slide-content {active}" id="slide-{idx+1}">
            {content_html}
        </div>
        '''
    
    slide_html = f"""
    <style>
    .slide-container {{
        width: 100%;
        max-width: 960px;
        aspect-ratio: 16 / 9;
        height: auto;
        min-height: 540px; /* Increased min-height for better readability */
        border: 1px solid #ddd; /* Lighter border */
        border-radius: 12px; /* Softer corners */
        background: #ffffff; /* Clean white background */
        box-shadow: 0 4px 12px rgba(0,0,0,0.05); /* Subtle shadow */
        position: relative;
        overflow: hidden;
        margin: 20px auto; /* Added margin for better page integration */
        display: flex;
        align-items: center;
        justify-content: center;
    }}
    .slide-content {{
        width: 100%;
        height: 100%;
        display: none;
        justify-content: flex-start; /* Align content to the top */
        align-items: center; /* Center content horizontally */
        flex-direction: column;
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        text-align: left; /* Default text align to left for lists */
        padding: 50px; /* Generous padding */
        box-sizing: border-box; /* Include padding in width/height */
    }}
    .slide-content.active {{
        display: flex;
    }}
    .slide-header-title {{
        font-size: 2.8em; /* Larger title */
        color: #2c3e50; /* Dark, modern blue */
        margin-bottom: 30px;
        font-weight: 600; /* Slightly bolder */
        width: 100%; /* Ensure title takes full width for centering if needed */
        text-align: center; /* Center the title */
    }}
    .slide-list-content {{
        font-size: 1.3em; /* Adjusted for readability */
        color: #34495e; /* Softer black */
        line-height: 1.8; /* Increased line height */
        list-style-type: disc; /* Standard bullets */
        padding-left: 40px; /* Indent list items */
        align-self: flex-start; /* Align list to the left within the content area */
        width: 100%; /* Allow list to use available width */
        max-width: 800px; /* Optional: constrain list width for very wide slides */
    }}
    .slide-list-content li {{
        margin-bottom: 12px; /* Space between list items */
    }}
    .navigation {{
        position: absolute;
        bottom: 20px; /* Positioned slightly higher */
        left: 50%;
        transform: translateX(-50%);
        z-index: 10;
        display: flex;
        justify-content: center;
    }}
    .nav-btn {{
        background: #3498db; /* Brighter blue */
        color: white;
        border: none;
        padding: 12px 20px; /* Larger buttons */
        margin: 0 10px;
        border-radius: 6px; /* Softer button corners */
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.3s ease; /* Smooth hover effect */
    }}
    .nav-btn:hover {{
        background: #2980b9; /* Darker blue on hover */
    }}
    </style>

    <div class="slide-container" id="slideContainer">
        {slides_html_content}
        <div class="navigation">
            <button class="nav-btn" onclick="prevSlide()">이전</button>
            <button class="nav-btn" onclick="nextSlide()">다음</button>
        </div>
    </div>
    <script>
    MathJax = {{
      tex: {{
        inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
        displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
        processEscapes: true
      }},
      svg: {{
        fontCache: 'global'
      }}
    }};
    </script>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <script>
    var currentSlide = 1;
    var totalSlides = {totalSlides};

    function showSlide(n) {{
        for (var i = 1; i <= totalSlides; i++) {{
            var slide = document.getElementById('slide-' + i);
            if (slide) {{
                slide.classList.remove('active');
                if (i === n) {{
                    slide.classList.add('active');
                }}
            }}
        }}
        // Trigger MathJax typesetting for the new active slide
        if (window.MathJax && typeof window.MathJax.typesetPromise === 'function') {{
            setTimeout(() => {{ // Delay to ensure DOM is updated
                try {{
                    const elementToTypeset = document.getElementById('slide-' + n);
                    if (elementToTypeset) {{
                        window.MathJax.typesetPromise([elementToTypeset]);
                    }} else {{
                        // console.warn("MathJax: Element slide-" + n + " not found for typesetting.");
                    }}
                }} catch (e) {{
                    console.error("MathJax typesetting error:", e);
                }}
            }}, 0);
        }}
    }}

    function prevSlide() {{
        currentSlide = currentSlide - 1;
        if (currentSlide < 1) currentSlide = totalSlides;
        showSlide(currentSlide);
    }}

    function nextSlide() {{
        currentSlide = currentSlide + 1;
        if (currentSlide > totalSlides) currentSlide = 1;
        showSlide(currentSlide);
    }}

    document.addEventListener("DOMContentLoaded", function() {{
        showSlide(currentSlide);
    }});
    </script>
    """
    display(HTML(slide_html))