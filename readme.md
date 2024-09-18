Here's the README formatted for GitHub:

# Customizable Quiz Application

A flexible quiz application with two versions: a basic version (alpha) and an advanced version using Google's Generative AI (omni).

## Features

### Alpha Version
- Load predefined questions from JSON
- Randomly select questions
- Multiple-choice questions
- Customizable quiz length
- Basic scoring system

### Omni Version
- Google's Generative AI for dynamic questions
- Multiple question types (MCQ, Short Answer, One Word)
- Customizable topics, difficulty, and length
- Adjustable grading strictness
- Configurable bot personality
- Explanations for incorrect answers

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/quiz-application.git
   cd quiz-application
   ```

2. Install dependencies:
   ```
   pip install google-generativeai
   ```

3. For omni version, set up Google API key:
   ```python:omni/main.py
   api_key = "your_api_key_here"
   ```

## Usage

### Alpha Version

```bash
cd alpha
python main.py
```

### Omni Version

```bash
cd omni
python main.py
```

Follow the prompts to customize your quiz.

## Customization

### Alpha Version
Edit `alpha/questions.json`:

```json:alpha/questions.json
[
    {
        "question": "What is the time complexity of a binary search algorithm?",
        "options": [
            "O(n)",
            "O(log n)",
            "O(n^2)",
            "O(1)"
        ],
        "correct_answer": "O(log n)"
    },
    // Add more questions...
]
```

### Omni Version
Modify `get_user_preferences()` in `omni/main.py` for more options.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - [@not_ekalabya](https://twitter.com/your_twitter) - ekalabya2010@example.com