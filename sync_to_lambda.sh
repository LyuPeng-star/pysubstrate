#!/bin/bash
LAMBDA_IP="${1:-YOUR_LAMBDA_IP}"

if [ "$LAMBDA_IP" = "YOUR_LAMBDA_IP" ]; then
    echo "❌ Please provide Lambda IP: ./scripts/sync_to_lambda.sh 1.2.3.4"
    exit 1
fi

echo "🚀 Syncing code to Lambda Labs: $LAMBDA_IP"

# 只同步代码，不包含虚拟环境
rsync -avz \
    --exclude='__pycache__/' \
    --exclude='*.pyc' \
    --exclude='data/local/' \
    --exclude='logs/' \
    --exclude='results/' \
    --exclude='.git/' \
    --exclude='.DS_Store' \
    ./ ubuntu@${LAMBDA_IP}:/home/ubuntu/pysubstrate/

echo "✅ Code synced successfully!"
