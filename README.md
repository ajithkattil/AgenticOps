---
title: AgenticOps
emoji: 🔧
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: "4.24.0"
app_file: app.py
pinned: false
---

# AgenticOps – DevOps Log Analyzer

This Gradio app uses an LLM + RAG-powered agent to analyze uploaded Jenkins/Kubernetes logs and suggest root causes and fixes based on internal KB context.

# 🤖 AgenticOps – Intelligent Agent + RAG Framework for DevOps Automation

## 🔍 Overview

**AgenticOps** is a cutting-edge DevOps assistant that brings together **Agentic AI**, **LLMs**, and **Retrieval-Augmented Generation (RAG)** to automate troubleshooting, debug CI/CD failures, and analyze logs or configurations in real time.

This POC showcases how AI agents can reason over logs, fetch knowledge from internal documents, and generate actionable responses — all while integrating with live DevOps tools like Jenkins, GitHub, and Kubernetes.

---

## 🎯 Features

- 🚀 Upload or fetch logs from Jenkins, GitHub Actions, Kubernetes, etc.
- 🤖 Autonomous multi-step decision-making using LangGraph agents
- 📚 RAG-powered context search over internal markdown or documentation
- 🛠️ Pluggable tools: CVE scanner, YAML validator, GitHub/Jenkins fetchers
- 💬 Gradio UI for interactive querying and result visualization
- 🧠 Fully local, nearly zero-cost setup with open models via Ollama

---

## ✅ Use Cases Solved

| # | Use Case | Description |
|--|----------|-------------|
| 1 | **Jenkins Failure Debugger** | Automatically fetches logs from Jenkins, analyzes failure, and suggests fixes. |
| 2 | **Kubernetes Crash Analyzer** | Fetches pod logs using `kubectl`, diagnoses CrashLoops or OOM errors, and recommends remediation. |
| 3 | **GitHub Actions YAML Fixer** | Uploads or fetches YAML config, validates, and suggests fixes using AI. |
| 4 | **Security Vulnerability Scanner** | Accepts dependency files (`requirements.txt`, `pom.xml`) and detects CVEs. |
| 5 | **Generic Log Analyzer** | Upload any custom logs, parse and extract insights using internal KB + LLMs. |

---

## 🧠 Technology Stack

| Layer               | Technology Used                                 |
|--------------------|--------------------------------------------------|
| LLM Inference       | Ollama + `mistral` or `phi3` (local, offline)   |
| Agent Framework     | LangGraph (LangChain)                           |
| Retrieval (RAG)     | FAISS + LangChain retriever                     |
| Tool Execution      | Python tool wrappers (API calls, shell commands)|
| User Interface      | Gradio                                          |
| Optional Monitoring | LangSmith                                       |

---

## 🗂️ Directory Structure

```plaintext
AgenticOps/
├── agents/
│   └── log_analyzer_agent.py        # Main agent logic using LangGraph
├── tools/
│   ├── log_parser.py                # Extracts stack traces and errors
│   ├── jenkins_fetcher.py           # Fetch Jenkins build logs via API
│   ├── github_fetcher.py            # Get GitHub Actions logs
│   ├── k8s_fetcher.py               # Retrieve Kubernetes pod logs
│   └── cve_scanner.py               # Scan dependencies for known CVEs
├── retriever/
│   └── kb_ingest.py                 # Ingest markdown/docs into FAISS vectorstore
├── data/
│   ├── sample_logs/                 # Example logs for local testing
│   └── kb_docs/                     # Internal docs/knowledge base (markdown/pdf)
├── vectorstore/
│   └── index/                       # FAISS local index storage
├── ui/
│   └── app.py                       # Gradio UI for file uploads and chat interface
├── tests/
│   ├── test_model_gpu.py           # GPU & model loading check
│   ├── test_vectorstore.py         # Vector ingestion + similarity
│   ├── test_logs_regression.py     # Known log output validation
│   └── test_artifact_hash.py       # Artifact reproducibility
├── .github/
│   └── workflows/
│       └── ci.yml                  # GitHub Actions CI config
├── requirements.txt                 # Python dependencies
└── .env                             # Environment variables (API keys, model config)
```

---

## 🔄 Product Workflow
<img width="1024" height="1536" alt="image" src="https://github.com/user-attachments/assets/12b4fac7-a8cb-4153-8d59-340d114f4673" />

### Example Input:
> “Why did my Kubernetes pod crash?”  
> or upload `jenkins_console.log`

### 🧠 Internal Steps:
1. **Input Handler**: File uploaded or log fetched from tool
2. **Agent Invokes Tools**:
   - Log parser extracts errors
   - Optional: Call `kubectl`, Jenkins API, GitHub CLI, etc.
3. **Retriever**:
   - Vector DB searches internal KB (e.g., markdown, past incidents)
4. **LLM Synthesizes**:
   - Uses Mistral/Phi-3 to generate root cause explanation and fix suggestion
5. **UI**:
   - Output displayed in Gradio interface

---

## 🔬 CI Testing Strategy

This project includes a GitHub Actions CI workflow with the following automated tests:

### 1. ✅ GPU-based LLM Validation (`test_model_gpu.py`)
- Confirms CUDA availability via `torch.cuda.is_available()`
- Loads Hugging Face model on GPU and processes a dummy input
- Verifies latency and memory usage using `nvidia-smi` or `torch.cuda` utilities

### 2. ✅ Vector Store Ingestion Test (`test_vectorstore.py`)
- Loads a sample `.txt` file and builds a FAISS vector store
- Verifies similarity search returns expected document chunks

### 3. ✅ Regression Log Tests (`test_logs_regression.py`)
- Uses known issue logs (e.g., Jenkins/K8s errors) from `tests/sample_logs/*.txt`
- Passes each log through the pipeline
- Asserts response includes specific keywords to avoid regressions

### 4. ✅ Deterministic Artifact Checks (`test_artifact_hash.py`)
- Ensures that FAISS index artifacts are consistent across runs
- Hashes the index file and compares against expected value

---

## ⚡ Quick Start

```bash
# 1. Clone repo
git clone https://github.com/YOUR_USERNAME/AgenticOps.git
cd AgenticOps

# 2. Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install and run Ollama model
brew install ollama        # (MacOS)
ollama run mistral         # or ollama run phi3

# 5. Launch the Gradio UI
python ui/app.py
```

---

## 🔮 Future Ideas

✅ Slack / CLI Bot interface

✅ GitOps triggers (e.g., auto-create JIRA tickets or PRs)

✅ Multi-agent teamwork (e.g., one explains, one validates, one fixes)

✅ Visual graphs of log similarity clusters (via embeddings)

✅ Fine-tuning on internal incident postmortems

---

## 🧠 Credits

AgenticOps is built with ❤️ using open-source AI, LangGraph, LangChain, Ollama, Gradio, and DevOps best practices.

Designed to showcase innovation in AI-powered observability, explainability, and automation for SREs and platform teams.
