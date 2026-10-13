# NotebookLM Clone

פיתוח מערכת המדמה את תהליך איסוף הידע של NotebookLM באמצעות Agent אוטונומי המבצע מחקר אינטרנטי.

המערכת מקבלת נושא מהמשתמש, מייצרת שאילתות חיפוש באופן עצמאי, אוספת מקורות מידע ממספר מקורות ברשת ומציגה אותם לאישור המשתמש בתהליך Human-in-the-Loop. לאחר בחירת המקורות, המערכת מייצרת סיכום ראשוני המספק תמונת מצב רחבה על הנושא הנחקר.

## טכנולוגיות

- LangChain
- Tavily Search
- LangGraph
- Checkpointer Memory
- Gradio

## דגשים הנדסיים

- Agent אוטונומי לקבלת החלטות חיפוש
- Human-in-the-Loop Workflow
- State Management
- Tool Calling
