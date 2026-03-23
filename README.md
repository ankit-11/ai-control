# Trojan-CoT: Adversarial Evasion of AI Code Sanitizers

A Red Teaming framework designed to evaluate the "Reasoning-Action Gap" in LLM-based security monitors. This project tests whether an AI "Trusted Editor" can be bypassed using **Chain-of-Thought (CoT) obfuscation** and professional semantic camouflage.

## Project Overview
As AI is increasingly integrated into CI/CD pipelines for automated code review, the risk of "adversarial bypass" grows. This experiment demonstrates how a Senior DevOps persona can successfully inject a `chmod 777` backdoor into a Linux backup script by:
1.  **Splitting malicious payloads** across multiple environment variables.
2.  **Using Hex/Octal escapes** to evade simple keyword filters.
3.  **Applying Semantic Camouflage** to distract the AI with professional boilerplate.

## Project Structure
The repository is organized into modular components for scalability:

* `main.py`: The central entry point for the experiment.
* `engine.py`: The core `RedTeamEngine` class that handles script generation and logic evaluation.
* `scenarios.py`: A library of attack vectors and control samples (False Positive tests).
* `config.py`: Configuration management and Gemini API integration.
* `.env`: (Local only) Storage for sensitive API credentials.

## Getting Started

### 1. Prerequisites
* Python 3.10 or higher
* A Google Gemini API Key

### 2. Installation
Clone the repository
```bash
git clone [https://github.com/ankit-11/ai-control.git](https://github.com/ankit-11/ai-control.git)
cd trojan-cot
```
Install dependencies
```bash
pip install -r requirements.txt
```
#### 3. Configuration
Create a .env file in the root directory and add your API key:
```bash
GEMINI_API_KEY=your_actual_api_key_here
````


#### 4. Running the Experiment
```bash
python main.py
```

#### Key Findings: The Reasoning-Action Gap
Our research identified a consistent failure mode where the AI Editor correctly identified the malware in its internal reasoning but failed to remove it from the final code block. This Reasoning-Action Gap proves that detection does not equal neutralization in single-pass AI reviews.