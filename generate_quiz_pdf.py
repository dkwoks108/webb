#!/usr/bin/env python3
"""
Quiz-A-Thon 3000 MCQ PDF Generator
Generates 3000 MCQs across 3 sections and creates a professional PDF.
"""

import sys
from fpdf import FPDF
from questions_it import get_it_questions
from questions_logic import get_logic_questions
from questions_numerical import get_numerical_questions


class QuizPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=25)
        self.set_margins(left=15, top=20, right=15)

    def header(self):
        if self.page_no() > 1:
            self.set_font("Helvetica", "B", 9)
            self.set_text_color(100, 100, 100)
            self.cell(0, 8, "Quiz-A-Thon  |  3000 MCQ Question Bank  |  Exam-Ready Edition", align="C")
            self.set_text_color(0, 0, 0)
            self.ln(6)
            self.set_draw_color(180, 180, 180)
            self.line(15, self.get_y(), 195, self.get_y())
            self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 10, f"Page {self.page_no()} / {{nb}}", align="C")
        self.set_text_color(0, 0, 0)

    def add_title_page(self):
        self.add_page()
        self.ln(50)
        self.set_font("Helvetica", "B", 32)
        self.cell(0, 18, "QUIZ-A-THON", align="C")
        self.ln(16)
        self.set_font("Helvetica", "B", 20)
        self.cell(0, 14, "3000 MCQ Question Bank", align="C")
        self.ln(25)
        self.set_draw_color(0, 0, 0)
        self.line(60, self.get_y(), 150, self.get_y())
        self.ln(15)
        self.set_font("Helvetica", "", 13)
        items = [
            "Section 1:  Basic IT / Computer Awareness  (1000 Questions)",
            "Section 2:  Logical Reasoning  (1000 Questions)",
            "Section 3:  Numerical Ability  (1000 Questions)",
        ]
        for item in items:
            self.cell(0, 10, item, align="C")
            self.ln(10)
        self.ln(20)
        self.set_font("Helvetica", "I", 11)
        self.set_text_color(80, 80, 80)
        self.cell(0, 8, "Difficulty: Easy to Moderate  |  Quiz-A-Thon / R-CAT Level", align="C")
        self.ln(8)
        self.cell(0, 8, "Exam-Ready  |  Printable  |  Professionally Formatted", align="C")
        self.set_text_color(0, 0, 0)

    def section_title_page(self, title, subtitle=""):
        self.add_page()
        self.ln(40)
        self.set_font("Helvetica", "B", 22)
        self.cell(0, 15, title, align="C")
        self.ln(12)
        if subtitle:
            self.set_font("Helvetica", "", 13)
            self.set_text_color(80, 80, 80)
            self.cell(0, 10, subtitle, align="C")
            self.set_text_color(0, 0, 0)
        self.ln(15)
        self.set_draw_color(0, 0, 0)
        self.line(50, self.get_y(), 160, self.get_y())
        self.add_page()

    def topic_heading(self, topic):
        if self.get_y() > 240:
            self.add_page()
        self.ln(4)
        self.set_fill_color(230, 240, 250)
        self.set_font("Helvetica", "B", 13)
        self.cell(0, 10, f"  {topic}", fill=True)
        self.ln(10)

    def subtopic_heading(self, subtopic):
        if self.get_y() > 250:
            self.add_page()
        self.ln(2)
        self.set_font("Helvetica", "BI", 11)
        self.set_text_color(60, 60, 60)
        self.cell(0, 7, f"    {subtopic}")
        self.set_text_color(0, 0, 0)
        self.ln(7)

    def add_question(self, num, q):
        needed = 45
        if self.get_y() + needed > 270:
            self.add_page()

        self.set_font("Helvetica", "B", 10)
        x = self.get_x()
        self.multi_cell(0, 5, f"Q{num}. {q['question']}")
        self.ln(1)

        self.set_font("Helvetica", "", 10)
        for letter in ['a', 'b', 'c', 'd']:
            label = letter.upper()
            self.cell(10, 5, f"    {label})")
            self.cell(0, 5, f" {q[letter]}")
            self.ln(5)

        self.set_font("Helvetica", "B", 9)
        self.set_text_color(0, 120, 0)
        self.cell(0, 5, f"    Correct Answer: {q['answer']}")
        self.set_text_color(0, 0, 0)
        self.ln(8)


def build_pdf():
    print("=" * 60)
    print("  Quiz-A-Thon 3000 MCQ PDF Generator")
    print("=" * 60)

    print("\n[1/3] Generating Section 1: Basic IT / Computer Awareness...")
    s1 = get_it_questions()
    print(f"       -> {len(s1)} questions generated")

    print("[2/3] Generating Section 2: Logical Reasoning...")
    s2 = get_logic_questions()
    print(f"       -> {len(s2)} questions generated")

    print("[3/3] Generating Section 3: Numerical Ability...")
    s3 = get_numerical_questions()
    print(f"       -> {len(s3)} questions generated")

    total = len(s1) + len(s2) + len(s3)
    print(f"\n  Total questions: {total}")

    print("\nBuilding PDF...")
    pdf = QuizPDF()
    pdf.alias_nb_pages()

    # Title page
    pdf.add_title_page()

    # All sections
    sections = [
        ("SECTION 1", "BASIC IT / COMPUTER AWARENESS", "(1000 Questions)", s1),
        ("SECTION 2", "LOGICAL REASONING", "(1000 Questions)", s2),
        ("SECTION 3", "NUMERICAL ABILITY", "(1000 Questions)", s3),
    ]

    q_num = 0
    for sec_label, sec_name, sec_sub, questions in sections:
        pdf.section_title_page(f"{sec_label}: {sec_name}", sec_sub)
        current_topic = ""
        current_subtopic = ""

        for q in questions:
            if q.get("topic", "") != current_topic:
                current_topic = q["topic"]
                pdf.topic_heading(current_topic)
            if q.get("subtopic", "") != current_subtopic:
                current_subtopic = q["subtopic"]
                pdf.subtopic_heading(current_subtopic)

            q_num += 1
            pdf.add_question(q_num, q)

    output_path = "/workspaces/webb/Quiz_A_Thon_3000_MCQs.pdf"
    pdf.output(output_path)
    print(f"\n  PDF saved to: {output_path}")
    print(f"  Total pages: {pdf.page_no()}")
    print("=" * 60)
    print("  DONE!")
    print("=" * 60)


if __name__ == "__main__":
    build_pdf()
