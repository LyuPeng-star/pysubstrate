#!/usr/bin/env python3
"""环境测试脚本"""

import sys
import os
import torch
import cma
import numpy as np

def test_environment():
    print("🧪 Testing PySubstrate Environment")
    print("="*50)
    
    # 基础信息
    print(f"Python version: {sys.version}")
    print(f"Working directory: {os.getcwd()}")
    print(f"Python executable: {sys.executable}")
    
    # PyTorch测试
    print(f"\n🔥 PyTorch version: {torch.__version__}")
    print(f"MPS available: {torch.backends.mps.is_available()}")
    
    # 创建测试张量
    x = torch.randn(5, 5)
    if torch.backends.mps.is_available():
        x = x.to('mps')
        print(f"✅ MPS device test passed")
    
    # CMA-ES测试
    print(f"\n🎯 CMA-ES version: {cma.__version__}")
    
    def simple_objective(x):
        return sum(x**2)
    
    es = cma.CMAEvolutionStrategy([0]*3, 0.5, {'maxiter': 5, 'verbose': -1})
    while not es.stop():
        solutions = es.ask()
        es.tell(solutions, [simple_objective(x) for x in solutions])
    
    print(f"✅ CMA-ES test passed, best: {es.result.fbest:.4f}")
    
    print("\n🎉 All tests passed! Environment is ready.")

if __name__ == "__main__":
    test_environment()
