\#!/bin/bash

LOG\_DIR="./logs"

mkdir -p \$LOG\_DIR

\# 生成测试日志

for i in {1..5}; do echo "test log \$i" >> \$LOG\_DIR/app\$i.log; done

\# 清理1天前的日志（实际测试用1分钟前）

find \$LOG\_DIR -name "\*.log" -mmin +1 -delete

echo "清理完成"
