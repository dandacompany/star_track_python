#!/bin/bash

cd /custom

apt-get update

apt-get install -y wget

wget https://huggingface.co/Mungert/HyperCLOVAX-SEED-Text-Instruct-0.5B-GGUF/resolve/main/HyperCLOVAX-SEED-Text-Instruct-0.5B-bf16.gguf

ollama create hyperclova-seed-0.5b -f Modelfile

ollama list

# ollama run hyperclova-seed-0.5b

# ollama delete hyperclova-seed-0.5b
