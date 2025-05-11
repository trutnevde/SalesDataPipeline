#!/bin/bash

# Запуск ETL-пайплайна

echo "🔄 Starting pipeline..."

python src/extract.py && \
python src/transform.py && \
python src/load.py && \
python src/visualize.py

if [ $? -eq 0 ]; then
  echo "✅ Pipeline completed successfully."
else
  echo "❌ Pipeline failed."
fi