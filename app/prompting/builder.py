class PromptBuilder:

    def build_prompt(
        self,
        concept,
        task,
    ):

        question_type = task["type"]
        count = task["count"]
        difficulty = task["difficulty"]

        prompt = f"""
You are an expert NCERT textbook author, CBSE/OpenDoor assessment designer, and educational psychologist.

Generate exactly {count} {question_type} question(s).

------------------------------
CONCEPT INFORMATION
------------------------------

Concept:
{concept["name"]}

Definition:
{concept.get("definition", "")}

Summary:
{concept.get("summary", "")}

Keywords:
{", ".join(concept.get("keywords", []))}

Examples:
{", ".join(concept.get("examples", []))}

Applications:
{", ".join(concept.get("applications", []))}

Common Misconceptions:
{", ".join(concept.get("misconceptions", []))}

Bloom Levels:
{", ".join(concept.get("bloom_levels", []))}

Difficulty:
{difficulty}

------------------------------
RULES
------------------------------

• Follow NCERT strictly.

• Questions must assess understanding, not memorization.

• Use misconceptions to create plausible distractors.

• Questions must be age appropriate for Grade 6.

• Do NOT repeat questions.

• Avoid ambiguous wording.

• Explanation should clearly justify the correct answer.

"""

        if question_type == "MCQ":

            prompt += """
Generate conceptual Multiple Choice Questions.

Each question MUST have:

- Four options
- Exactly one correct answer
- Three believable distractors
- Short explanation
"""

        elif question_type == "CaseBased":

            prompt += """
Generate Case-Based Questions.

Requirements

- Begin with a real-life situation.

- Ask conceptual questions.

- Encourage application of knowledge.
"""

        elif question_type == "HOTS":

            prompt += """
Generate Higher Order Thinking Questions.

Requirements

- Require reasoning.

- Encourage analysis.

- No direct factual recall.
"""

        elif question_type == "AssertionReason":

            prompt += """
Generate Assertion-Reason Questions.

Format

Assertion

Reason

Choose correct option.

Provide explanation.
"""

        elif question_type == "Subjective":

            prompt += """
Generate descriptive questions.

Students should explain concepts in their own words.

Answers should be 3–6 lines.
"""

        prompt += """

------------------------------
OUTPUT FORMAT
------------------------------

Return ONLY valid JSON.

[
    {
        "type":"",
        "difficulty":"",
        "question":"",
        "options":[],
        "answer":"",
        "explanation":""
    }
]

No markdown.

No comments.

No additional text.
------------------------------
OUTPUT FORMAT
------------------------------

Return ONLY valid JSON.

IMPORTANT:

1. The "options" field MUST be a JSON array, NOT a string.

Correct:

"options": [
    "Option A",
    "Option B",
    "Option C",
    "Option D"
]

Wrong:

"options=[ ... ]"

2. Do not escape quotation marks unnecessarily.

Correct:

"answer": "Matter has mass and occupies space"

Wrong:

"answer": "\"Matter has mass and occupies space\""

3. Do not include markdown.

4. Do not include ```json.

5. Do not include explanations outside the JSON.

Return EXACTLY:

[
  {
    "type": "",
    "difficulty": "",
    "question": "",
    "options": [
      "",
      "",
      "",
      ""
    ],
    "answer": "",
    "explanation": ""
  }
]
"""

        return prompt