import logging
from pathlib import Path
from markdown2 import markdown
from weasyprint import HTML, CSS


class MarkdownToPDFConverter:
    def __init__(self, markdown_file: Path, output_pdf: Path, css_file: Path):
        self.markdown_file = markdown_file
        self.output_pdf = output_pdf
        self.css_file = css_file

    def run(self):
        if not self.markdown_file.exists():
            logging.error(f"❌ Markdown file not found: {self.markdown_file}")
            return

        css = CSS(filename=str(self.css_file)) if self.css_file.exists() else None

        html_content = self._read_markdown_as_html()
        self._generate_pdf_from_html(html_content, css)

        logging.info(f"✅ PDF generated: {self.output_pdf.resolve()}")

    def _read_markdown_as_html(self) -> str:
        content = self.markdown_file.read_text(encoding="utf-8")
        return markdown(content)

    def _generate_pdf_from_html(self, html: str, css: CSS | None):
        HTML(string=html).write_pdf(self.output_pdf, stylesheets=[css] if css else None)


def main():
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    css_path = Path("static/style.css")

    files = [
        ("docs/pt_br.md", "docs/pt_br.pdf"),
        ("docs/en_us.md", "docs/en_us.pdf"),
    ]

    for md_file, pdf_file in files:
        converter = MarkdownToPDFConverter(
            markdown_file=Path(md_file),
            output_pdf=Path(pdf_file),
            css_file=css_path
        )
        converter.run()


if __name__ == "__main__":
    main()
