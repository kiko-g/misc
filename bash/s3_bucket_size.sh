#!/bin/bash

# List your S3 buckets
buckets=("vsports" "finishershub" "finishershub.mw2019" "finishershub.mw2022")
total_size=0

# Iterate through the buckets and calculate the total size in GB
for bucket in "${buckets[@]}"; do
    bucket_size=$(aws s3api list-objects --bucket "$bucket" --output json --query "sum(Contents[].Size)" | awk 'BEGIN { FS = "," } ; {if ($1 ~ /^[0-9]+$/) { sum += $1 } } END { print sum / (1024 ^ 3) }')
    echo "Size of $bucket: $bucket_size GB"
    total_size=$(echo "$total_size + $bucket_size" | bc)
done

# Print the total size in GB
echo "Total size of all buckets: $total_size GB"
