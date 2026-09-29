from fastapi import FastAPI
from qna import ask_question
from explanation_module import explain_concept
from quiz_module import generate_quiz 
from summary_module import summarize_text

app=FastAPI(title="EduGenie")