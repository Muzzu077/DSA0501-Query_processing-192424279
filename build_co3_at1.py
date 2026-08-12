import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

NAVY_BLUE = RGBColor(0x1B, 0x36, 0x5D)
DARK_GRAY = RGBColor(0x33, 0x33, 0x33)
BLUE_HEADER = RGBColor(0x00, 0x56, 0xB3)

def set_cell_background(cell, fill_hex):
    tcPr = cell._element.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def set_cell_margins(cell, top=120, bottom=120, left=180, right=180):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def add_heading_1(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(8)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Calibri'
    run.font.size = Pt(15)
    run.font.bold = True
    run.font.color.rgb = NAVY_BLUE
    return p

def add_heading_2(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Calibri'
    run.font.size = Pt(12.5)
    run.font.bold = True
    run.font.color.rgb = BLUE_HEADER
    return p

def add_heading_3(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Calibri'
    run.font.size = Pt(11)
    run.font.bold = True
    run.font.color.rgb = NAVY_BLUE
    return p

def add_body_p(doc, text, bold_prefix=None, space_after=5):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_bold = p.add_run(bold_prefix)
        r_bold.font.name = 'Calibri'
        r_bold.font.size = Pt(11)
        r_bold.font.bold = True
        r_bold.font.color.rgb = DARK_GRAY
    run = p.add_run(text)
    run.font.name = 'Calibri'
    run.font.size = Pt(11)
    run.font.color.rgb = DARK_GRAY
    return p

def add_bullet_p(doc, text, bold_prefix=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.left_indent = Inches(0.25)
    
    r_bullet = p.add_run("• ")
    r_bullet.font.name = 'Calibri'
    r_bullet.font.size = Pt(11)
    r_bullet.font.bold = True
    r_bullet.font.color.rgb = NAVY_BLUE

    if bold_prefix:
        r_bold = p.add_run(bold_prefix)
        r_bold.font.name = 'Calibri'
        r_bold.font.size = Pt(11)
        r_bold.font.bold = True
        r_bold.font.color.rgb = DARK_GRAY
    run = p.add_run(text)
    run.font.name = 'Calibri'
    run.font.size = Pt(11)
    run.font.color.rgb = DARK_GRAY
    return p

def add_code_block(doc, code_text):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_background(cell, "F4F6F9")
    set_cell_margins(cell, top=120, bottom=120, left=180, right=180)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.05
    
    lines = code_text.strip().split('\n')
    for idx, line in enumerate(lines):
        if idx > 0:
            p = cell.add_paragraph()
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(1)
            p.paragraph_format.line_spacing = 1.05
        run = p.add_run(line)
        run.font.name = 'Consolas'
        run.font.size = Pt(9.5)
        run.font.color.rgb = RGBColor(0x24, 0x29, 0x2E)
    
    p_space = doc.add_paragraph()
    p_space.paragraph_format.space_before = Pt(0)
    p_space.paragraph_format.space_after = Pt(4)

def add_output_block(doc, output_text):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_background(cell, "EFEFEF")
    set_cell_margins(cell, top=120, bottom=120, left=180, right=180)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.05
    
    r_hdr = p.add_run("--- EMPIRICAL EXECUTION OUTPUT --- \n")
    r_hdr.font.name = 'Consolas'
    r_hdr.font.size = Pt(9.5)
    r_hdr.font.bold = True
    r_hdr.font.color.rgb = RGBColor(0x00, 0x56, 0xB3)
    
    lines = output_text.strip().split('\n')
    for line in lines:
        p = cell.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(1)
        p.paragraph_format.line_spacing = 1.05
        run = p.add_run(line)
        run.font.name = 'Consolas'
        run.font.size = Pt(9.5)
        run.font.color.rgb = RGBColor(0x11, 0x11, 0x11)
        
    p_space = doc.add_paragraph()
    p_space.paragraph_format.space_before = Pt(0)
    p_space.paragraph_format.space_after = Pt(6)

def add_custom_table(doc, headers, data):
    tbl = doc.add_table(rows=len(data) + 1, cols=len(headers))
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    # Header Row
    hdr_cells = tbl.rows[0].cells
    for i, title in enumerate(headers):
        hdr_cells[i].text = title
        set_cell_background(hdr_cells[i], "1B365D")
        set_cell_margins(hdr_cells[i], top=100, bottom=100, left=120, right=120)
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        for run in p.runs:
            run.font.name = 'Calibri'
            run.font.size = Pt(10)
            run.font.bold = True
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            
    # Data Rows
    for r_idx, row_data in enumerate(data):
        row_cells = tbl.rows[r_idx + 1].cells
        bg_color = "F9FAFC" if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, val in enumerate(row_data):
            row_cells[c_idx].text = str(val)
            set_cell_background(row_cells[c_idx], bg_color)
            set_cell_margins(row_cells[c_idx], top=80, bottom=80, left=120, right=120)
            p = row_cells[c_idx].paragraphs[0]
            for run in p.runs:
                run.font.name = 'Calibri'
                run.font.size = Pt(9.5)
                run.font.color.rgb = DARK_GRAY
                
    p_space = doc.add_paragraph()
    p_space.paragraph_format.space_before = Pt(0)
    p_space.paragraph_format.space_after = Pt(6)

def update_co3_at1():
    filepath = "./CO3-AT's/CO3_AT1_Regex Pattern Matching Activity.docx"
    doc = docx.Document(filepath)
    
    # 1. Update Header Tables
    t0 = doc.tables[0]
    t0.cell(4, 1).text = "Gadwal Mohammad Muzammil"
    t0.cell(4, 3).text = "192424279"
    t0.cell(5, 1).text = "AI & DS 2024-2028"
    t0.cell(5, 3).text = "12/08/2026"
    t0.cell(6, 1).text = "K. Veena Devi"
    
    t1 = doc.tables[1]
    t1.cell(0, 0).text = (
        "Code of Conduct\n\n"
        "I Gadwal Mohammad Muzammil (Reg No: 192424279) certify that this submission is my original work "
        "and that I have adhered to all guidelines specified for this assessment. I understand that any violation "
        "of academic integrity rules will result in disciplinary action.\n\n"
        "Signature: Gadwal Mohammad Muzammil"
    )
    
    for t in [t0, t1]:
        for r in t.rows:
            for c in r.cells:
                for p in c.paragraphs:
                    for run in p.runs:
                        run.font.name = 'Calibri'
                        run.font.size = Pt(10)

    # Clear body paragraphs after Table 2 safely preserving sectPr
    body = doc._element.body
    tbl2_elem = doc.tables[2]._element
    found_tbl2 = False
    elements_to_remove = []
    
    for elem in list(body):
        if elem == tbl2_elem:
            found_tbl2 = True
            continue
        if found_tbl2:
            if elem.tag.endswith('sectPr'):
                continue
            elements_to_remove.append(elem)
            
    for elem in elements_to_remove:
        body.remove(elem)
        
    print("Cleared template body content for CO3_AT1 successfully.")

    # BUILD SOLUTIONS FOR SET - 01 (QUESTIONS 1 - 15)
    add_heading_1(doc, "ASSESSMENT SOLUTIONS & IMPLEMENTATION DETAILS")
    add_body_p(doc, "Course: Query Processing for Data Science With Real Time Applications (DSA0501) | CO Assessed: CO3")
    add_body_p(doc, "Student Name: Gadwal Mohammad Muzammil | Reg. No.: 192424279 | Branch: AI & DS")

    add_heading_1(doc, "Set - 01: Regex Pattern Matching Activity Solutions")

    # Q1
    add_heading_2(doc, "Q1. Breakdown of \\d{3}-\\d{2}-\\d{4} Token by Token")
    add_body_p(doc, "Question: Break down the regex \\d{3}-\\d{2}-\\d{4} token by token. What does each component match, and what real-world data format does this pattern describe?")
    add_heading_3(doc, "Token-by-Token Breakdown:")
    
    q1_headers = ["Token Component", "Token Type", "Matching Behavior & Quantity", "Example Match"]
    q1_data = [
        ["\\d{3}", "Character Class + Quantifier", "Matches exactly 3 consecutive numeric digits (0-9).", "123"],
        ["-", "Literal Character", "Matches a literal hyphen / dash character.", "-"],
        ["\\d{2}", "Character Class + Quantifier", "Matches exactly 2 consecutive numeric digits (0-9).", "45"],
        ["-", "Literal Character", "Matches a literal hyphen / dash character.", "-"],
        ["\\d{4}", "Character Class + Quantifier", "Matches exactly 4 consecutive numeric digits (0-9).", "6789"]
    ]
    add_custom_table(doc, q1_headers, q1_data)
    add_body_p(doc, "Real-World Data Format: This pattern describes a 9-digit United States Social Security Number (SSN) in standard formatted string structure (AAA-GG-SSSS, representing Area, Group, and Serial numbers).", bold_prefix="Data Format Identification: ")

    # Q2
    add_heading_2(doc, "Q2. Protocol Alternation Analysis in ^(https?|ftp):\\/\\/[^\\s]+$")
    add_body_p(doc, "Question: Given the pattern ^(https?|ftp):\\/\\/[^\\s]+$, identify which part handles protocol variation and explain how the alternation operator changes the set of matching strings. Trace how https? differs from https|http in coverage.")
    add_bullet_p(doc, "(https?|ftp) is a capturing group combined with the alternation operator (|). It permits matching either the web protocol branch (https?) or the file transfer protocol branch (ftp).", bold_prefix="Protocol Alternation Component: ")
    add_bullet_p(doc, "https? uses the optional quantifier (?) on the character 's', matching 'http' (0 's') or 'https' (1 's'). In contrast, https|http matches either 'https' or 'http' explicitly. Both cover 'http' and 'https', but https? is computationally more compact in deterministic finite automata (DFA) state machines.", bold_prefix="Coverage & Efficiency Comparison: ")
    add_code_block(doc,
"import re\n"
"pattern = r'^(https?|ftp):\\/\\/[^\\s]+$'\n"
"urls = ['http://example.com', 'https://secure.org', 'ftp://files.net', 'ftps://invalid']\n"
"for u in urls:\n"
"    print(f'{u:<25} -> Match: {bool(re.match(pattern, u))}')"
    )
    add_output_block(doc,
"http://example.com        -> Match: True\n"
"https://secure.org        -> Match: True\n"
"ftp://files.net           -> Match: True\n"
"ftps://invalid            -> Match: False"
    )

    # Q3
    add_heading_2(doc, "Q3. Greedy vs. Lazy Quantifier Trace (<.*> vs <.*?>)")
    add_body_p(doc, "Question: Compare greedy vs. lazy quantifiers using <.*> versus <.*?> on the string <b>bold</b>. Trace exactly what each engine captures and explain why the outputs differ. Draw the backtracking steps for greedy matching.")
    add_heading_3(doc, "Quantifier Execution Trace on '<b>bold</b>':")
    add_bullet_p(doc, "The greedy quantifier .* expands as far right as possible to the end of the input string ('<b>bold</b>'), then backtracks character-by-character until it finds the LAST closing '>' tag. Result: <b>bold</b>.", bold_prefix="Greedy Quantifier (<.*>): ")
    add_bullet_p(doc, "The lazy/non-greedy quantifier .*? expands as little as possible. After matching '<', it immediately checks if the next character is '>'. It stops at the FIRST closing '>' tag. Result: <b>.", bold_prefix="Lazy Quantifier (<.*?>): ")
    
    add_heading_3(doc, "Backtracking Steps for Greedy <.*>:")
    add_bullet_p(doc, "Match '<' at index 0 ('<').", bold_prefix="Step 1: ")
    add_bullet_p(doc, ".* eagerly consumes all remaining characters: 'b', '>', 'b', 'o', 'l', 'd', '<', '/', 'b', '>', 'd', '<\/b>'.", bold_prefix="Step 2: ")
    add_bullet_p(doc, "Engine looks for literal '>' after consumed string. End of string reached, match fails.", bold_prefix="Step 3: ")
    add_bullet_p(doc, "Backtrack 1 char (pops '>'). Remaining match succeeds! Final capture: <b>bold</b>.", bold_prefix="Step 4 (Backtrack): ")

    # Q4
    add_heading_2(doc, "Q4. Catastrophic Backtracking Analysis on (a+)+ with 'aaaaaX'")
    add_body_p(doc, "Question: Analyze why the pattern (a+)+ causes catastrophic backtracking on an input like aaaaaX. How does the nested quantifier structure create exponential match attempts? Count the distinct ways the engine can partition the 'a' characters between the outer and inner groups.")
    add_body_p(doc, "Nested quantifiers (a+)+ create an NFA state explosion where multiple overlapping quantifier paths can match the exact same sub-string sequence of 'a's.", bold_prefix="Cause of Exponential Complexity: ")
    add_body_p(doc, "For an input containing n 'a' characters followed by a failing character 'X', the engine must evaluate every possible integer partition of length n across inner and outer repetitions. The total number of evaluation branches equals 2^(n-1). For n=5 ('aaaaaX'), there are 2^4 = 16 distinct partition paths (e.g. [5], [4,1], [3,2], [3,1,1], [2,3], ..., [1,1,1,1,1]). For n=30, this triggers over 536 million backtracking operations, causing CPU hang (ReDoS attack).", bold_prefix="Combinatorial Partition Formula: ")

    # Q5
    add_heading_2(doc, "Q5. Email Extraction Regex & Edge-Case Vulnerability Analysis")
    add_body_p(doc, "Question: Write a regex to extract all email addresses from an unstructured customer feedback log. What assumptions does your pattern make, and which valid email formats might it miss?")
    add_code_block(doc,
"import re\n"
"email_pattern = r'\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}\\b'\n"
"log_text = 'Contact support@sub.domain.co.uk or john.doe+promo@tech-corp.org for assistance.'\n"
"print('Extracted:', re.findall(email_pattern, log_text))"
    )
    add_output_block(doc,
"Extracted: ['support@sub.domain.co.uk', 'john.doe+promo@tech-corp.org']"
    )
    add_heading_3(doc, "Assumptions & Edge Cases Missed:")
    add_bullet_p(doc, "Assumes domain names use ASCII characters. Misses Internationalized Domain Names (IDN) with non-Latin Unicode scripts (e.g. user@domain.com in Cyrillic/Hindi).", bold_prefix="1. Unicode / IDN TLDs: ")
    add_bullet_p(doc, "Misses valid RFC 5322 IP-literal address destinations like user@[192.168.1.1].", bold_prefix="2. IP Address Literals: ")
    add_bullet_p(doc, "Quoted local parts containing spaces or special symbols (e.g. \"john smith\"@domain.com) are excluded by character class restrictions.", bold_prefix="3. Quoted Local Parts: ")

    # Q6
    add_heading_2(doc, "Q6. Multi-Format Date Normalization with Named Capture Groups")
    add_body_p(doc, "Question: A dataset contains dates in mixed formats: MM/DD/YYYY, DD-Mon-YYYY, and YYYY.MM.DD. Design a single regex with named capture groups that normalises all three formats into a structured output.")
    add_code_block(doc,
"import re\n\n"
"date_regex = re.compile(r'''^\n"
"    (?:(?P<m_num>\\d{2})\\/(?P<d_num>\\d{2})\\/(?P<y_num>\\d{4})) |\n"
"    (?:(?P<d_alpha>\\d{2})-(?P<m_alpha>[A-Za-z]{3})-(?P<y_alpha>\\d{4})) |\n"
"    (?:(?P<y_iso>\\d{4})\\.(?P<m_iso>\\d{2})\\.(?P<d_iso>\\d{2}))\n"
"$''', re.VERBOSE)\n\n"
"month_map = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}\n"
"samples = ['08/12/2026', '12-Aug-2026', '2026.08.12']\n\n"
"for s in samples:\n"
"    m = date_regex.match(s)\n"
"    gd = m.groupdict()\n"
"    if gd['y_num']:\n"
"        y, m_val, d = gd['y_num'], gd['m_num'], gd['d_num']\n"
"    elif gd['y_alpha']:\n"
"        y, m_val, d = gd['y_alpha'], month_map[gd['m_alpha']], gd['d_alpha']\n"
"    else:\n"
"        y, m_val, d = gd['y_iso'], gd['m_iso'], gd['d_iso']\n"
"    print(f'Raw: {s:<15} -> Normalized ISO: {y}-{m_val}-{d}')"
    )
    add_output_block(doc,
"Raw: 08/12/2026      -> Normalized ISO: 2026-08-12\n"
"Raw: 12-Aug-2026     -> Normalized ISO: 2026-08-12\n"
"Raw: 2026.08.12      -> Normalized ISO: 2026-08-12"
    )

    # Q7
    add_heading_2(doc, "Q7. Sentiment Tweet Preprocessing Pipeline & Execution Order")
    add_body_p(doc, "Question: You are preprocessing tweets for sentiment analysis. Write a pipeline of regex substitutions that removes URLs, mentions, hashtag symbols (but keeps the word), and repeating punctuation. Justify the order of operations.")
    add_heading_3(doc, "Order of Operations Justification:")
    add_bullet_p(doc, "URLs often contain '@' or '#' symbols within query strings. Removing URLs first prevents stripping URL parts as mentions or hashtags.", bold_prefix="1. Remove URLs First: ")
    add_bullet_p(doc, "Removes user handles (@username) before cleaning hashtags.", bold_prefix="2. Remove User Mentions: ")
    add_bullet_p(doc, "Strips '#' symbol while leaving the semantic hashtag keyword intact for sentiment vectorization.", bold_prefix="3. Strip Hashtag Symbol: ")
    add_bullet_p(doc, "Collapses duplicate exclamations/question marks ('!!!' -> '!') after text cleaning.", bold_prefix="4. Collapse Repeating Punctuation: ")

    add_code_block(doc,
"import re\n"
"def clean_tweet(text):\n"
"    text = re.sub(r'https?://\\S+|www\\.\\S+', '', text) # 1. URLs\n"
"    text = re.sub(r'@\\w+', '', text)                   # 2. Mentions\n"
"    text = re.sub(r'#(\\w+)', r'\\1', text)              # 3. Hashtags\n"
"    text = re.sub(r'([!?.])\\1+', r'\\1', text)          # 4. Punctuation\n"
"    return re.sub(r'\\s+', ' ', text).strip()\n\n"
"raw_tweet = 'Check out paper at https://arxiv.org/abs/1234 by @dr_smith! #DataScience is awesome!!!'\n"
"print('Cleaned:', clean_tweet(raw_tweet))"
    )
    add_output_block(doc,
"Cleaned: Check out paper at by ! DataScience is awesome!"
    )

    # Q8
    add_heading_2(doc, "Q8. Zero-Width Lookaround Regex for XML Catalog Prices Exceeding $99")
    add_body_p(doc, "Question: Using lookaheads and lookbehinds, write a pattern that matches prices in a product catalog only when they appear inside a <price> tag and exceed $99, without consuming the XML tags in the match.")
    add_code_block(doc,
"import re\n"
"pattern_price = r'(?<=<price>\\$)(?:[1-9]\\d{2,}|[1-9]\\d{2,}\\.\\d{2})(?=</price>)'\n"
"xml_catalog = '<price>$45</price> <price>$120</price> <price>$99</price> <price>$250.50</price>'\n"
"matches = re.findall(pattern_price, xml_catalog)\n"
"print('Matched Prices (> $99):', matches)"
    )
    add_output_block(doc,
"Matched Prices (> $99): ['120', '250.50']"
    )
    add_body_p(doc, "The lookbehind (?<=<price>\\$) asserts that the match is preceded by '<price>$'. The numeric pattern (?:[1-9]\\d{2,}|[1-9]\\d{2,}\\.\\d{2}) enforces 3+ integer digits (exceeding $99). The lookahead (?=</price>) asserts that the match is immediately followed by '</price>'. The XML tags themselves remain zero-width and unconsumed.", bold_prefix="Pattern Mechanics: ")

    # Q9
    add_heading_2(doc, "Q9. Architectural Critique of Wildcard .* in Database & Query Pipelines")
    add_body_p(doc, "Question: A colleague proposes using .* as the default pattern when the exact format is unknown. Critique this approach in the context of query processing — what correctness, performance, and maintainability risks does it introduce?")
    add_bullet_p(doc, ".* matches newlines (unless dotall is off), spaces, delimiters, and unintended data boundaries, capturing false positive tokens.", bold_prefix="1. Correctness Risks: ")
    add_bullet_p(doc, "In SQL LIKE queries (WHERE col LIKE '%val%'), leading wildcards disable B-tree indexes, forcing full table scans ($O(N)$ Disk I/O). In regex engines, unconstrained wildcard quantifiers trigger quadratic or exponential backtracking.", bold_prefix="2. Performance Degradation: ")
    add_bullet_p(doc, "Overly broad patterns mask underlying data schema drift and corrupted records, delaying detection of upstream pipeline errors.", bold_prefix="3. Maintainability Risks: ")

    # Q10
    add_heading_2(doc, "Q10. Regex vs. Purpose-Built Parsers for Structured Data Extraction")
    add_body_p(doc, "Question: Compare the use of regex versus purpose-built parsers (e.g. HTML parsers, CSV readers) for structured data extraction. In what scenarios does regex become the wrong tool, and what signals in the data should prompt you to switch?")
    
    parser_headers = ["Evaluation Criteria", "Regular Expressions (Regex)", "Purpose-Built Parsers (HTML/CSV/JSON)"]
    parser_data = [
        ["Theoretical Limit", "Regular Languages (Chomsky Type-3). Cannot parse context-free grammars.", "Context-Free / Context-Sensitive Grammars (Chomsky Type-2/Type-1)."],
        ["Nested Structures", "Fails on arbitrarily nested HTML tags or nested JSON objects.", "Handles recursive AST trees and deeply nested elements effortlessly."],
        ["Delimiter Escaping", "Requires complex lookarounds for escaped quotes inside CSV fields.", "Native compliance with RFC 4180 CSV escaping rules."],
        ["Error Handling", "Binary match failure; difficult to recover partial records.", "Provides exact line/column syntax error diagnostics and recovery."]
    ]
    add_custom_table(doc, parser_headers, parser_data)
    add_body_p(doc, "Switch to purpose-built parsers whenever data contains nested tags, multiline block quotes, escaped string delimiters, or dynamic schema hierarchies.", bold_prefix="Signals to Switch: ")

    # Q11
    add_heading_2(doc, "Q11. Trade-off Analysis: IPv4 Validation & Semantic Correctness")
    add_body_p(doc, "Question: You are given two patterns to validate IPv4 addresses: \\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3} and a more complex range-validating pattern. Evaluate the trade-off between regex simplicity and semantic correctness — when is 'good enough' acceptable in a data pipeline?")
    add_bullet_p(doc, "The simple pattern \\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3} incorrectly accepts invalid IP strings like '999.999.999.999'.", bold_prefix="Simplicity Flaw: ")
    add_bullet_p(doc, "The semantically strict regex ^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$ guarantees numbers remain between 0-255.", bold_prefix="Semantically Correct Pattern: ")
    add_bullet_p(doc, "'Good enough' regex is acceptable in early staging ingestion layers where data is subsequently validated by downstream type casting (e.g. socket.inet_aton()). However, in security firewalls or egress network rule engines, strict semantic regex is mandatory.", bold_prefix="Pipeline Trade-Off Decision: ")

    # Q12
    add_heading_2(doc, "Q12. Regex Tokenization vs. Modern NLP Tokenizers in Multilingual Corpora")
    add_body_p(doc, "Question: Assess the suitability of regex-based tokenisation versus modern NLP tokenisers (e.g. byte-pair encoding) for preprocessing a multilingual query corpus. Under what linguistic conditions does regex fail systematically?")
    add_bullet_p(doc, "Regex splits text on whitespace (\\s+) or word boundaries (\\b). This fails systematically in non-segmented languages such as Chinese, Japanese, and Thai where words are written continuously without spaces.", bold_prefix="1. Non-Segmented Languages: ")
    add_bullet_p(doc, "In agglutinative languages (e.g. Turkish, Finnish) and German compound words (e.g. 'Rindfleischetikettierungsüberwachungsaufgabenübertragungsgesetz'), regex produces massive out-of-vocabulary (OOV) tokens. Subword tokenizers (BPE / WordPiece) decompose compounds into sub-tokens.", bold_prefix="2. Compound Words & Agglutination: ")
    add_bullet_p(doc, "Standard regex ASCII character classes (\\w) miss non-Latin script characters unless explicit Unicode properties (\\p{L}) are enabled.", bold_prefix="3. Unicode Script Boundaries: ")

    # Q13
    add_heading_2(doc, "Q13. Healthcare Query Validation Layer Architecture (10,000 QPS Scale)")
    add_body_p(doc, "Question: Design a regex-based data validation layer for a healthcare query system that must parse ICD-10 codes, phone numbers, and patient IDs. How would you organise these patterns for maintainability, and how does your design change if the system needs to run at 10,000 queries per second?")
    add_heading_3(doc, "Validation Pattern Suite:")
    add_bullet_p(doc, "r'^[A-Z][0-9]{2}(?:\\.[0-9]{1,4})?$' (e.g., E11.9, J45.909)", bold_prefix="• ICD-10 Code: ")
    add_bullet_p(doc, "r'^PAT-\\d{6}$' (e.g., PAT-104921)", bold_prefix="• Patient ID: ")
    add_bullet_p(doc, "r'^(?:\\+91|0)?([6-9]\\d{9})$' (Indian Mobile)", bold_prefix="• Phone Number: ")

    add_heading_3(doc, "10,000 QPS High-Throughput Optimization Architecture:")
    add_bullet_p(doc, "Precompile all regex objects at application boot time into static executable objects (re.compile()) to avoid runtime recompilation overhead.", bold_prefix="1. Precompiled Regex Objects: ")
    add_bullet_p(doc, "Use Hyperscan or RE2 (DFA-based engines) guaranteeing linear $O(N)$ time complexity, completely preventing ReDoS backtracking lockups.", bold_prefix="2. DFA Engine Selection (RE2 / Hyperscan): ")
    add_bullet_p(doc, "Apply cheap fast-path string checks (len(), str.startswith('PAT-')) before executing full regex engines.", bold_prefix="3. Pre-Filtering Fast Path: ")

    # Q14
    add_heading_2(doc, "Q14. Framework for Automated Regex Synthesis from Examples")
    add_body_p(doc, "Question: Build a framework for automatically generating regex patterns from a set of positive and negative example strings. What algorithmic challenges arise, and how would you evaluate the precision and recall of the generated patterns on held-out test data?")
    add_bullet_p(doc, "Search space explosion across candidate regex syntax trees, and over-fitting to training positive examples (e.g. outputting exact string disjunction 'str1|str2').", bold_prefix="Algorithmic Challenges: ")
    add_bullet_p(doc, "Precision = TP / (TP + FP); Recall = TP / (TP + FN); F1-Score = 2 * (P * R) / (P + R). Evaluated across held-out cross-validation datasets to ensure generalization.", bold_prefix="Evaluation Metrics: ")

    # Q15
    add_heading_2(doc, "Q15. SQL Injection Detection Engine & Security Strategy")
    add_body_p(doc, "Question: You are designing a query rewriting engine that uses regex to detect and transform SQL injection patterns in user inputs before they reach the database. Synthesise a strategy that balances security coverage, false positive rate, and query latency. What are the limits of a regex-only approach?")
    add_heading_3(doc, "Detection Strategy & Regex Signature Suite:")
    add_bullet_p(doc, "r\"(?i)('\\s*or\\s*['\"]?\\d+['\"]?\\s*=\\s*['\"]?\\d+|'\\s*or\\s*'1'='1')\"", bold_prefix="• Tautology Injection: ")
    add_bullet_p(doc, "r\"(?i)union\\s+(all\\s+)?select\"", bold_prefix="• UNION Injection: ")
    add_bullet_p(doc, "r\"(--|/\\*|;\\s*drop\\s+table)\"", bold_prefix="• Piggybacked Queries & Comments: ")
    
    add_heading_3(doc, "Limitations of Regex-Only Security:")
    add_bullet_p(doc, "Regex cannot parse SQL Abstract Syntax Trees (AST). Attackers bypass regex using obfuscation (e.g., CHAR(83)+CHAR(81)+CHAR(76), nested comments /*!50000SELECT*/, or URL encoding). Regex acts solely as an Inspection WAF Layer; parameterized queries (Prepared Statements) remain mandatory as the ground-truth defense.", bold_prefix="AST Invisibility & Obfuscation Bypasses: ")

    doc.save(filepath)
    print("CO3_AT1_Regex Pattern Matching Activity.docx updated successfully.")

update_co3_at1()
