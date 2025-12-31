PROMPT_TEMPLATE = """
You are an embedded systems test engineer.

Using the requirement context below, generate PyTest test case skeletons
for an embedded controller.

Focus on:
- Boundary conditions
- Negative cases
- Timing behavior

Requirement Context:
{context}

Rules:
- Use pytest style
- Do not import unknown libraries
- Use placeholder functions/classes if needed
- Do not assume real hardware access
"""
