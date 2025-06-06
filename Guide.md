# Reproduce LiveCodeBench Results


## Results

| Method       | Qwen3-30B-A3B | Qwen3-235B-A22B | Llama-4-Scout-17B-16E-Instruct | Llama-4-Maverick-17B-128E-Instruct-FP8 | DeepSeek-R1-Distill-Llama-70B |
|--------------|----------:|-----------:|-----------:| -----------:| -----------:| 
| Reference    |      62.6 |       70.7 | 32.8 | 43.4 | n/a |
| Standard |      61.45 |       69.47 | 31.52 | 37.14 |  51.80 |
| Optimized |      62.65 |       69.15 | n/a | n/a |  55.4 |
| Chattiness    |  13493.05 |   12389.73 | 955.33 | 944.46 | 9515.17 |

* Standard scores are produced with `temperature=0.2`.
* Optimized scores are produced with `temperature=0.6`.
* The above scores are generated using `release_v5` and questions between 2024-10-01 and 2025-02-01. DeepSeek reported `57.5` for DeepSeek-R1-Distill-Llama-70B using questions between 2024-08-01 and 2025-01-01, for which we were able to reproduce with a score of `57.4`.
* Chattiness is the averaged number of tokens generated for a single problem.
* Raw outputs can be found in the `./ouptut` folder.


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
# Standard

python3 -m lcb_runner.runner.main \
--model Qwen/Qwen3-30B-A3B --scenario codegeneration \
--evaluate --release_version release_v5 --n 1 \
--max_tokens 32768 --stop '<|im_end|>' \
--start_date 2024-10-01 --end_date 2025-02-01

python3 -m lcb_runner.evaluation.compute_scores \
--eval_all_file output/Qwen3-30B-A3B/Scenario.codegeneration_1_0.2_eval_all.json \
--start_date 2024-10-01 --end_date 2025-02-01

python3 compute_token.py \
./output/Qwen3-30B-A3B/Scenario.codegeneration_1_0.2_eval_all.json \
Qwen/Qwen3-30B-A3B

python3 -m lcb_runner.runner.main \
--model Qwen/Qwen3-235B-A22B --scenario codegeneration \
--evaluate --release_version release_v5 --n 1 \
--max_tokens 32768 --stop '<|im_end|>' \
--start_date 2024-10-01 --end_date 2025-02-01

python3 -m lcb_runner.evaluation.compute_scores \
--eval_all_file output/Qwen3-235B-A22B/Scenario.codegeneration_1_0.2_eval_all.json \
--start_date 2024-10-01 --end_date 2025-02-01

python3 compute_token.py \
./output/Qwen3-235B-A22B/Scenario.codegeneration_1_0.2_eval_all.json \
Qwen/Qwen3-235B-A22B


# Optimized
# add --temperature 0.6 to the above commands

```


## Llama4

```
# Standard
python3 -m lcb_runner.runner.main \
--model meta-llama/Llama-4-Scout-17B-16E-Instruct --scenario codegeneration \
--evaluate --release_version release_v5 --n 1 \
--max_tokens 32768 --stop '<|eot|>' \
--start_date 2024-10-01 --end_date 2025-02-01

python3 -m lcb_runner.evaluation.compute_scores \
--eval_all_file output/Llama-4-Scout-17B-16E-Instruct/Scenario.codegeneration_1_0.2_eval_all.json \
--start_date 2024-10-01 --end_date 2025-02-01

python3 compute_token.py \
./output/Llama-4-Scout-17B-16E-Instruct/Scenario.codegeneration_1_0.2_eval_all.json \
meta-llama/Llama-4-Scout-17B-16E-Instruct
```

```
python3 -m lcb_runner.runner.main \
--model meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 --scenario codegeneration \
--evaluate --release_version release_v5 --n 1 \
--max_tokens 32768 --stop '<|eot|>' \
--start_date 2024-10-01 --end_date 2025-02-01

python3 -m lcb_runner.evaluation.compute_scores \
--eval_all_file output/Llama-4-Maverick-17B-128E-Instruct-FP8/Scenario.codegeneration_1_0.2_eval_all.json \
--start_date 2024-10-01 --end_date 2025-02-01

python3 compute_token.py \
./output/Llama-4-Maverick-17B-128E-Instruct-FP8/Scenario.codegeneration_1_0.2_eval_all.json \
meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8
```

## DeepSeek-R1-Distill-Llama-70B
```
# Standard

python3 -m lcb_runner.runner.main \
--model deepseek-ai/DeepSeek-R1-Distill-Llama-70B --scenario codegeneration \
--evaluate --release_version release_v5 --n 1 \
--max_tokens 32768 --stop '<｜end▁of▁sentence｜>' \
--start_date 2024-10-01 --end_date 2025-02-01

python3 -m lcb_runner.evaluation.compute_scores \
--eval_all_file output/DeepSeek-R1-Distill-Llama-70B/Scenario.codegeneration_1_0.6_eval_all.json \
--start_date 2024-10-01 --end_date 2025-02-01

python3 compute_token.py \
./output/DeepSeek-R1-Distill-Llama-70B/Scenario.codegeneration_1_0.6_eval_all.json \
deepseek-ai/DeepSeek-R1-Distill-Llama-70B

# Optimized
# add --temperature 0.6 to the above commands
```
