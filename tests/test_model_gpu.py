import os
import torch
import time
from transformers import AutoTokenizer, AutoModelForCausalLM

def test_llm_gpu():
    print("🟡 Starting test_llm_gpu...")
    os.makedirs("tests/output_logs", exist_ok=True)

    try:
        print("🔍 Checking for GPU...")
        assert torch.cuda.is_available(), "❌ GPU is not available."

        model_name = "mistralai/Mistral-7B-Instruct-v0.2"
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

        prompt = "What is DevOps?"
        inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

        start = time.time()
        with torch.no_grad():
            outputs = model.generate(**inputs, max_new_tokens=20)
        duration = time.time() - start

        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(f"✅ Inference done in {duration:.2f} seconds.")
        print(f"🧠 Response: {response}")

        with open("tests/output_logs/gpu_test_success.log", "w") as f:
            f.write(f"✅ Test Passed\nPrompt: {prompt}\nResponse: {response}\nInference Time: {duration:.2f}s")

    except Exception as e:
        print(f"❌ Exception: {str(e)}")
        with open("tests/output_logs/gpu_test_error.log", "w") as f:
            f.write("❌ GPU LLM Test Failed\n")
            f.write(str(e))
        raise

# ✅ Run this when executed directly
if __name__ == "__main__":
    test_llm_gpu()
