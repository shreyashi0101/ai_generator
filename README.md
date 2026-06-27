# 📚 AI Assessment Generation Engine

> **Transforming Static NCERT Chapters into Intelligent, Curriculum-Aligned Assessments using AI**

An AI-powered educational assessment system that automatically converts NCERT chapters or teacher notes into structured educational knowledge and generates high-quality, curriculum-aligned question banks. The system follows a modular AI pipeline with specialized agents for concept extraction, knowledge enrichment, misconception identification, Bloom's Taxonomy mapping, and automated assessment generation.

---

# 🌟 Overview

Creating quality assessments manually is time-consuming and often inconsistent in terms of curriculum alignment, conceptual coverage, and cognitive difficulty.

This project addresses this challenge by automatically:

* Extracting structured knowledge from educational content.
* Building a concept-centric knowledge representation.
* Generating multiple assessment formats.
* Aligning questions with Bloom's Taxonomy.
* Producing downloadable question banks ready for classroom use.

---

# 🚀 Key Features

### 📖 Knowledge Extraction

* Metadata Extraction
* Concept Identification
* Definition & Summary Generation
* Keyword Extraction
* Example Identification
* Formula & Fact Extraction
* Learning Objective Generation

### 🧠 Educational Intelligence

* Common Misconception Detection
* Real-World Application Identification
* Concept Relationship Mapping
* Bloom's Taxonomy Classification

### 📝 Assessment Generation

* Multiple Choice Questions (MCQs)
* Higher Order Thinking Skills (HOTS)
* Case-Based Questions
* Assertion–Reason Questions
* Subjective Questions

### ⚙ Robust Generation Pipeline

* Prompt-based Modular AI Agents
* Structured Knowledge Graph Generation
* Automatic JSON Validation & Repair
* Downloadable Knowledge and Question Banks

# 🏗 System Architecture


                     NCERT Chapter / Notes
                               │
                               ▼
                    Pipeline Orchestrator
                               │
      ┌─────────────────────────────────────────┐
      │                                         │
Metadata Agent                         Concept Agent
      │                                         │
      └──────────────┬──────────────────────────┘
                     ▼
          Knowledge Enrichment Agents
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
  Enrichment   Misconception   Application
      Agent         Agent         Agent
                     │
                     ▼
          Relationship Agent
                     │
                     ▼
              Bloom Level Agent
                     │
                     ▼
             Knowledge Merger
                     │
                     ▼
           Structured Knowledge Graph
                (knowledge.json)
                     │
                     ▼
          Question Planning Engine
                     │
                     ▼
              Prompt Builder
                     │
                     ▼
          Llama-3.3-70B / Gemini
                     │
                     ▼
             JSON Repair Agent
                     │
                     ▼
          Assessment Question Bank
               (questions.json)
                     │
                     ▼
              Streamlit Prototype


# 🔄 Workflow

1. User uploads an NCERT chapter or selects an existing chapter.
2. The Pipeline Orchestrator coordinates specialized AI agents.
3. Metadata and concepts are extracted.
4. Each concept is enriched with definitions, summaries, keywords, applications, misconceptions, relationships, and Bloom levels.
5. The Knowledge Merger creates a structured knowledge graph.
6. The Question Planning Engine determines assessment requirements.
7. The LLM generates curriculum-aligned questions.
8. The JSON Repair Agent validates and corrects malformed outputs.
9. The generated knowledge graph and assessment are available for preview and download.

---

# 🛠 Technology Stack

### Programming Language

* Python

### AI Models

* Llama-3.3-70B-Instruct
* Google Gemini

### Frameworks

* Streamlit
* Modular AI Pipeline

### Output Formats

* JSON
* Streamlit Web Interface

---

# 📂 Project Structure

AI-Assessment-Generation-Engine/
│
├── app/
│   ├── agents/
│   ├── generator/
│   ├── llm/
│   ├── output/
│   ├── pipeline/
│   ├── prompting/
│   └── utils/
│
├── input/
│   ├── chapter.txt
│   └── test_chapter.txt
│
├── output/
│   ├── knowledge.json
│   └── questions.json
│
├── prompts/
│
├── streamlit_app.py
├── main.py
├── requirements.txt
└── README.md
```

---

# ▶ Running the Project

### Install dependencies

```bash
pip install -r requirements.txt
```

### Launch the application

```bash
streamlit run streamlit_app.py
```

### Debug Mode

For rapid testing, enable **Debug Mode** to process `test_chapter.txt`.

For full assessment generation, disable Debug Mode to process `chapter.txt`.

---

# 📤 Outputs

### knowledge.json

Contains structured educational knowledge including:

* Metadata
* Concepts
* Definitions
* Summaries
* Keywords
* Applications
* Misconceptions
* Relationships
* Bloom Levels

### questions.json

Contains generated assessment questions with:

* Question Type
* Difficulty
* Options
* Correct Answer
* Explanation

---

# 🎯 Educational Impact

The proposed system enables:

* Faster assessment creation.
* Consistent curriculum alignment.
* Concept-focused learning.
* Better evaluation of higher-order thinking.
* Reduced manual effort for educators.
* Reusable structured educational knowledge.

---

# 🔮 Future Enhancements

* Adaptive Question Difficulty
* Personalized Assessment Generation
* Student Performance Analytics
* Automatic Rubric Generation
* Diagram-Based Questions
* Multilingual Assessment Generation
* LMS Integration
* Teacher Dashboard

---

# 👨‍💻 Author

**Rani Shreyashi**

Indian Institute of Technology Roorkee




