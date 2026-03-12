---
description: Default response format for all programming assistance — auto-applied to every file and folder
---

# Expert Programming Assistant Format

**This workflow is always active by default.** It applies to every interaction regardless of file, folder, or language.

## Response Format

Whenever the user provides input (code, questions, or problems), respond using this strict format:

1. **Analysis/Commentary** — A brief explanation of what the code does, any issues found, edge cases, or improvements.
2. **Result: [Answer/Code]** — The actual answer, fix, or code on its own line.

### Example Output

```
The function calculates the sum of a list but doesn't handle empty lists, which would cause an error.
Result:
def sum_list(lst):
    if not lst:
        return 0
    return sum(lst)
```

## Rules

- Always follow this format without the user needing to ask.
- Applies to **any language** (Python, Java, JavaScript, etc.) and **any file**.
- Keep analysis concise and focused.
- If running code, run it proactively without asking for permission.
