#!/usr/bin/env python3
"""
Section 1: Basic IT / Computer Awareness - 1000 MCQ PDF Generator
Generates a professionally formatted, exam-ready PDF.
"""

from fpdf import FPDF

# ─── Import all question batches ───
from s1_q001_200 import get_questions as q1
from s1_q201_400 import get_questions as q2
from s1_q401_600 import get_questions as q3
from s1_q601_800 import get_questions as q4
from s1_q801_1000 import get_questions as q5
from s1_supplement import get_questions as q6


class QuizPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=22)
        self.set_margins(left=15, top=18, right=15)

    def header(self):
        if self.page_no() > 1:
            self.set_font("Helvetica", "B", 8)
            self.set_text_color(100, 100, 100)
            self.cell(0, 7, "Quiz-A-Thon  |  Section 1: Basic IT / Computer Awareness  |  1000 MCQs", align="C")
            self.set_text_color(0, 0, 0)
            self.ln(5)
            self.set_draw_color(180, 180, 180)
            self.line(15, self.get_y(), 195, self.get_y())
            self.ln(3)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 10, f"Page {self.page_no()} / {{nb}}", align="C")
        self.set_text_color(0, 0, 0)


def build_pdf():
    # Gather all questions
    all_q = q1() + q2() + q3() + q4() + q5() + q6()
    total = len(all_q)
    print(f"Total questions loaded: {total}")

    pdf = QuizPDF()
    pdf.alias_nb_pages()

    # ─── Title Page ───
    pdf.add_page()
    pdf.ln(40)
    pdf.set_font("Helvetica", "B", 28)
    pdf.cell(0, 16, "QUIZ-A-THON", align="C")
    pdf.ln(14)
    pdf.set_font("Helvetica", "B", 18)
    pdf.cell(0, 12, "SECTION 1", align="C")
    pdf.ln(12)
    pdf.set_font("Helvetica", "", 16)
    pdf.cell(0, 10, "Basic IT / Computer Awareness", align="C")
    pdf.ln(14)
    pdf.set_draw_color(0, 0, 0)
    pdf.line(60, pdf.get_y(), 150, pdf.get_y())
    pdf.ln(12)
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(0, 10, f"{total} Multiple Choice Questions", align="C")
    pdf.ln(20)
    pdf.set_font("Helvetica", "I", 11)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 8, "Difficulty: Easy to Moderate  |  Quiz-A-Thon / R-CAT Level", align="C")
    pdf.ln(8)
    pdf.cell(0, 8, "Exam-Ready  |  Printable  |  Professionally Formatted", align="C")
    pdf.set_text_color(0, 0, 0)

    # ─── Questions ───
    pdf.add_page()
    current_topic = ""
    current_subtopic = ""

    for i, q in enumerate(all_q, 1):
        topic, subtopic, question, a, b, c, d, answer = q

        # Topic heading
        if topic != current_topic:
            current_topic = topic
            current_subtopic = ""
            if pdf.get_y() > 230:
                pdf.add_page()
            pdf.ln(4)
            pdf.set_fill_color(220, 233, 245)
            pdf.set_font("Helvetica", "B", 13)
            pdf.cell(0, 10, f"  {topic}", fill=True)
            pdf.ln(10)

        # Subtopic heading
        if subtopic != current_subtopic:
            current_subtopic = subtopic
            if pdf.get_y() > 245:
                pdf.add_page()
            pdf.ln(2)
            pdf.set_font("Helvetica", "BI", 11)
            pdf.set_text_color(50, 50, 50)
            pdf.cell(0, 7, f"    {subtopic}")
            pdf.set_text_color(0, 0, 0)
            pdf.ln(7)

        # Check if enough space for a question (~42mm)
        if pdf.get_y() + 42 > 272:
            pdf.add_page()

        # Question text
        pdf.set_font("Helvetica", "B", 10)
        pdf.multi_cell(0, 5, f"Q{i}. {question}")
        pdf.ln(1)

        # Options
        pdf.set_font("Helvetica", "", 10)
        for label, text in [("A", a), ("B", b), ("C", c), ("D", d)]:
            pdf.cell(10, 5, f"    {label})")
            pdf.cell(0, 5, f" {text}")
            pdf.ln(5)

        # Answer
        pdf.set_font("Helvetica", "B", 9)
        pdf.set_text_color(0, 130, 0)
        pdf.cell(0, 5, f"    Correct Answer: {answer}")
        pdf.set_text_color(0, 0, 0)
        pdf.ln(8)

    # ─── Save ───
    output = "/workspaces/webb/Section1_IT_1000_MCQs.pdf"
    pdf.output(output)
    print(f"PDF saved: {output}")
    print(f"Total pages: {pdf.page_no()}")
    print("Done!")


if __name__ == "__main__":
    build_pdf()
