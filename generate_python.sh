python3 -m grpc_tools.protoc -I./proto \
        --python_out=./grpc_rep_python/scrapper \
        --pyi_out=./grpc_rep_python/scrapper \
        --grpc_python_out=./grpc_rep_python/scrapper \
        ./proto/scrapper.proto


# Specify the directory to crawl
directory="grpc_rep_python/scrapper"

# Check if the directory exists
if [ ! -d "$directory" ]; then
    echo "Directory $directory not found."
    exit 1
fi

# Iterate over files in the directory
for file in "$directory"/*_pb2_grpc.py; do
    # Check if the file exists
    if [ -f "$file" ]; then
        # Use temporary file for intermediate processing
        temp_file=$(mktemp)

        # Replace line using sed with a capture group for identifier
        sed 's/import \(.*\)_pb2 as \1__pb2/from . import \1_pb2 as \1__pb2/' "$file" > "$temp_file"

        # Move the temporary file content back to the original file
        mv "$temp_file" "$file"
    fi
done