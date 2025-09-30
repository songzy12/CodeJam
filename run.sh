CODE_PATH="xxx.py"

OUTPUT_PATH="tmp/output.txt"

INPUT_PATH="tmp/ts1_input.txt"
EXPECTED_OUTPUT_PATH="tmp/ts1_output.txt"
python3 "$CODE_PATH" < "$INPUT_PATH" > "$OUTPUT_PATH"
diff "$OUTPUT_PATH" "$EXPECTED_OUTPUT_PATH"

INPUT_PATH="tmp/ts2_input.txt"
EXPECTED_OUTPUT_PATH="tmp/ts2_output.txt"
python3 "$CODE_PATH" < "$INPUT_PATH" > "$OUTPUT_PATH"
diff "$OUTPUT_PATH" "$EXPECTED_OUTPUT_PATH"
