#!/bin/bash
# 快速激活pysubstrate开发环境
echo "🚀 Activating PySubstrate environment..."
# 激活虚拟环境
source /Users/lyupaif/pysubstrate-env/bin/activate
# 进入项目目录
cd /Users/lyupaif/pysubstrate
echo "✅ Environment activated!"
echo "Python: $(which python)"
echo "Location: $(pwd)"
