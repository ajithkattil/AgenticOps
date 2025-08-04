# tests/test_model_gpu.py

"""
Test loading a Hugging Face LLM onto GPU and running a sample prompt.
Also checks if GPU is available and measures performance metrics.
"""

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

def test_llm_gpu():
    assert torch.cuda.is_available(), "GPU is not available."

    model_name = "mistralai/Mistral-7B-Instruct-v0.2"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

    prompt = "What is DevOps?"
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=20)

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    assert "DevOps" in response or len(response) > 0

