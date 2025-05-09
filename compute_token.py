#!/usr/bin/env python3
import json
import sys
from transformers import AutoTokenizer

def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <input.json> <model_name>")
        sys.exit(1)

    input_path = sys.argv[1]
    model_name = sys.argv[2]

    # load your tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)

    # load the entire JSON array
    with open(input_path, "r", encoding="utf-8") as f:
        records = json.load(f)

    total_tokens = 0
    total_strings = 0

    for rec in records:
        outputs = rec.get("output_list", [])
        for txt in outputs:
            # count tokens in each string
            n = len(tokenizer.encode(txt, add_special_tokens=False))
            total_tokens += n
            total_strings += 1

    if total_strings == 0:
        print("No strings found in any 'output_list'.")
        sys.exit(1)

    avg = total_tokens / total_strings
    print(f"Processed {len(records)} records, {total_strings} strings total.")
    print(f"Average tokens per string: {avg:.2f}")

if __name__ == "__main__":
    main()
