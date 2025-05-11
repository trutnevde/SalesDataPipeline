NAME=sales_data_pipeline

help:
    @echo "Available commands:"
    @echo "make setup    — Setup project"
    @echo "make run      — Run the full pipeline"
    @echo "make test     — Run tests"
    @echo "make clean    — Clean generated files"

setup:
    pip install -r requirements.txt

run:
    ./run_pipeline.sh

test:
    pytest tests/

clean:
    rm -rf data/processed/*.csv reports/*.png logs/*.log || true