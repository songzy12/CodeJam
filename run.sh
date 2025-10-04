CODE_PATH="xxx.py"

INPUT_ROOT_DIR="test_data"
TMP_OUTPUT_PATH="tmp/output.txt"

echo "Running on sample test set..."
INPUT_PATH="$INPUT_ROOT_DIR/sample_test_set_1/sample_ts1_input.txt"
EXPECTED_OUTPUT_PATH="$INPUT_ROOT_DIR/sample_test_set_1/sample_ts1_output.txt"
python3 "$CODE_PATH" < "$INPUT_PATH" > "$TMP_OUTPUT_PATH"
diff "$TMP_OUTPUT_PATH" "$EXPECTED_OUTPUT_PATH"

echo "Running on test set 1..."
INPUT_PATH="$INPUT_ROOT_DIR/test_set_1/ts1_input.txt"
EXPECTED_OUTPUT_PATH="$INPUT_ROOT_DIR/test_set_1/ts1_output.txt"
python3 "$CODE_PATH" < "$INPUT_PATH" > "$TMP_OUTPUT_PATH"
diff "$TMP_OUTPUT_PATH" "$EXPECTED_OUTPUT_PATH"

echo "Running on test set 2..."
INPUT_PATH="$INPUT_ROOT_DIR/test_set_2/ts2_input.txt"
EXPECTED_OUTPUT_PATH="$INPUT_ROOT_DIR/test_set_2/ts2_output.txt"
python3 "$CODE_PATH" < "$INPUT_PATH" > "$TMP_OUTPUT_PATH"
diff "$TMP_OUTPUT_PATH" "$EXPECTED_OUTPUT_PATH"
