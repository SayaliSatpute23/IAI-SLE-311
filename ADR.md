# ADR 1: Selection of Tech Stack for Basic AI Agent

## Status

Accepted

## Date

02 September 2026

## Context

The objective of this project is to develop a basic AI Agent as part of the
AI-Augmented Workflow course.

The agent will be developed as a simple application that accepts input from
the user, sends the input to an AI model, receives the generated response,
and displays the response to the user.

The project also focuses on using AI-assisted coding tools during development.
Therefore, the selected technology should be simple for a student to learn,
easy to test, and suitable for AI-assisted development.

## Decision

The following technology stack has been selected:

- **Programming Language:** Python
- **AI Service:** OpenAI API
- **API Interface:** OpenAI Responses API
- **Development Environment:** Visual Studio Code
- **Version Control:** Git
- **Repository Hosting:** GitHub
- **AI-Assisted Coding Tool:** GitHub Copilot
- **Documentation Format:** Markdown

Python was selected because it provides a simple and readable syntax and has
libraries that support communication with AI APIs.

The OpenAI API was selected to provide the AI model capability for the basic
agent. The agent will send user input to the API and display the generated
response.

Visual Studio Code will be used to write and test the Python code. Git and
GitHub will be used to track and store project changes.

GitHub Copilot may be used during development to assist with code generation,
explanations, and improvements.

Markdown files will be used for project documentation, including this ADR and
the Contribution Log.

## Consequences

### Advantages

- Python is relatively easy to read and learn for a beginner.
- The project can be developed using a small amount of code.
- The OpenAI API provides access to an AI model for the basic agent.
- Visual Studio Code provides an environment for writing and testing code.
- Git provides version control for project changes.
- GitHub provides online storage and project sharing.
- AI-assisted coding can help with generating code, explaining errors, and
  improving development speed.
- Markdown makes project documentation simple and readable.

### Limitations

- The OpenAI API requires an API key.
- The API key must be protected and must not be uploaded to GitHub.
- API usage may involve cost depending on the account and usage.
- The agent requires an internet connection when using the OpenAI API.
- AI-generated code may contain errors and must be reviewed and tested.
- Relying too heavily on AI-generated code can reduce understanding of the
  implementation.

## AI-Assisted Coding Considerations

AI-assisted coding tools will be used as development aids rather than as a
replacement for the student's understanding.

Any AI-generated code used in the project will be reviewed, tested, and
documented in the Contribution Log.

The student remains responsible for understanding the code, checking its
correctness, making required modifications, and testing the final program.

## Alternatives Considered

### Ollama

Ollama could be used as an open-source/local alternative for running AI models.
It was considered because it can support local model execution. However, the
OpenAI API was selected for this basic implementation because it provides a
straightforward API-based approach for connecting the Python application to
an AI model.

### Other Programming Languages

Languages such as JavaScript could also be used to develop an AI Agent.
Python was selected because of its readability and suitability for a
beginner-level AI project.

## Conclusion

Python with the OpenAI API has been selected as the technology stack for the
basic AI Agent.

The project will use Git, GitHub, Visual Studio Code, and GitHub Copilot to
support an AI-assisted software development workflow. AI-generated
contributions will be reviewed and recorded in the Contribution Log.