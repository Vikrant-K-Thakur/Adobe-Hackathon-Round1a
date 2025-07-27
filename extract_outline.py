import fitz  # PyMuPDF

def extract_outline_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")

    title = None
    title_candidates = []
    outline = []
    seen_headings = set()

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                spans = line.get("spans", [])
                if not spans:
                    continue

                line_text = " ".join(span["text"].strip() for span in spans if span["text"].strip())
                if not line_text or line_text.lower() == "overview":
                    continue

                first_span = spans[0]
                font_size = first_span["size"]
                font_name = first_span["font"]
                is_bold = "Bold" in font_name or "bold" in font_name

                if page_num == 1 and is_bold and font_size > 16 and len(line_text) >= 5:
                    title_candidates.append((font_size, line_text.strip()))

                if font_size > 16:
                    level = "H1"
                elif font_size > 13:
                    level = "H2"
                elif font_size > 11:
                    level = "H3"
                else:
                    continue

                if len(line_text.strip()) < 3 or line_text.strip() in seen_headings:
                    continue

                seen_headings.add(line_text.strip())
                outline.append({
                    "level": level,
                    "text": line_text.strip(),
                    "page": page_num
                })

    if title_candidates:
        title_candidates.sort(reverse=True)
        title = title_candidates[0][1]
    else:
        title = "Untitled Document"

    return {
        "title": title,
        "outline": outline
    }
