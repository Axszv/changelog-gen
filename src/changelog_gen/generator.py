import datetime

def generate_changelog(commits_by_type, output_file):
    """Generate or update CHANGELOG.md from grouped commits."""
    date_str = datetime.date.today().isoformat()
    header = f"## [{date_str}]\n\n"
    sections = []
    for typ, msgs in commits_by_type.items():
        if not msgs:
            continue
        section_title = typ.capitalize()
        sections.append(f"### {section_title}\n")
        for m in msgs:
            sections.append(f"- {m}\n")
        sections.append("\n")
    new_content = header + "".join(sections)

    # 读原文件内容
    try:
        with open(output_file, 'r', encoding='utf-8') as f:
            old = f.read()
    except FileNotFoundError:
        old = ""
    # 写回：新内容在前，旧内容在后
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(new_content + old)

