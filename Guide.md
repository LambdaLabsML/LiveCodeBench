# Produce LiveCodeBench Results


## Results

| Method       | Qwen3-30B | Qwen3-235B |
|--------------|----------:|-----------:|
| Reference    |      62.6 |       70.7 |
| Reproduction |      62.0 |       70.9 |


## Setup
```
git clone https://github.com/LambdaLabsML/LiveCodeBench.git

sudo docker run --rm -it  --gpus all   \
-v ~/.cache/huggingface:/root/.cache/huggingface   \
-v ./LiveCodeBench:/LiveCodeBench   \
--shm-size=512g --ipc=host   \
--entrypoint /bin/bash   \
vllm/vllm-openai:latest

cd /LiveCodeBench
pip install -e .
```

## Qwen3

```
python3 -m lcb_runner.runner.main \
--model Qwen/Qwen3-30B-A3B --scenario codegeneration \
--evaluate --release_version release_v5 --n 1 \
--max_tokens 32768 --stop '<|im_end|>' \
--start_date 2024-10-01 --end_date 2025-02-01

python3 -m lcb_runner.evaluation.compute_scores \
--eval_all_file output/Qwen3-30B-A3B/Scenario.codegeneration_1_0.2_eval_all.json \
--start_date 2024-10-01 --end_date 2025-02-01

python3 -m lcb_runner.runner.main \
--model Qwen/Qwen3-235B-A22B --scenario codegeneration \
--evaluate --release_version release_v5 --n 1 \
--max_tokens 32768 --stop '<|im_end|>' \
--start_date 2024-10-01 --end_date 2025-02-01

python3 -m lcb_runner.evaluation.compute_scores \
--eval_all_file output/Qwen3-235B-A22B/Scenario.codegeneration_1_0.2_eval_all.json \
--start_date 2024-10-01 --end_date 2025-02-01
```