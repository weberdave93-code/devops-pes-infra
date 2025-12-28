// 声明这是一个 Pipeline 脚本
pipeline {
    // agent any 表示可以在任何可用的 Jenkins 节点上运行
    agent any
    
    // environment 块定义了整个流水线通用的环境变量
    environment {
        // AWS 区域
        AWS_REGION = 'us-east-1'
        // ECR 仓库地址（请替换为你自己的 AWS 账号 ID）
        ECR_REPO_URI = '088847613437.dkr.ecr.us-east-1.amazonaws.com/devops-pes-app' 
        // 镜像标签：使用 Jenkins 内置的构建编号（如 v-1, v-2...）
        IMAGE_TAG = "v-${BUILD_NUMBER}"
    }
    
    // stages 块包含了流水线的所有阶段
    stages {
        // 阶段1: 拉取代码
        // Jenkins 会自动从 Git 拉取代码，这里显式写出来是为了逻辑清晰
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        // 阶段2: 单元测试 (这里是模拟，实际项目中会运行 pytest 等命令)
        stage('Unit Test') {
            steps {
                echo "Running unit tests..."
            }
        }
        
        // 阶段3: 构建 Docker 镜像
        stage('Build Image') {
            steps {
                script {
                    echo "Building Docker image..."
                    // 调用宿主机的 docker build 命令
                    // -t 指定镜像名称和标签
                    // . 表示使用当前目录下的 Dockerfile
                    sh "docker build -t ${ECR_REPO_URI}:${IMAGE_TAG} ./docker"
                }
            }
        }
        
        // 阶段4: 安全扫描 (DevSecOps)
        // 扫描镜像漏洞，这里做演示，实际需安装 Trivy
        stage('Security Scan') {
            steps {
                echo "Running Trivy security scan..."
                echo "Scan passed: No critical vulnerabilities."
            }
        }
        
        // 阶段5: 推送镜像到 AWS ECR
        stage('Push to ECR') {
            steps {
                script {
                    // withAWS 是插件提供的指令，它会自动读取 Jenkins 中存的 'aws-credentials' 凭证
                    // 并将其注入到环境，让 aws 命令拥有权限
                    withAWS(credentials: 'aws-credentials', region: "${AWS_REGION}") {
                        sh """
                            # 1. 获取 ECR 登录密码并登录 Docker
                            aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ECR_REPO_URI}
                            # 2. 推送镜像
                            docker push ${ECR_REPO_URI}:${IMAGE_TAG}
                        """
                    }
                }
            }
        }

        // 阶段6: 部署到开发环境 (占位，后续第5天会用到)
        stage('Deploy to Dev') {
            when {
                branch 'dev' // 只有当 Git 分支是 dev 时才执行此步骤
            }
            steps {
                echo "Deploying to Development Environment..."
            }
        }
    }
    
    // post 块定义了构建结束后的操作（无论成功还是失败）
    post {
        success {
            echo "✅ Build and Push Successful! Image: ${ECR_REPO_URI}:${IMAGE_TAG}"
        }
        failure {
            echo "❌ Pipeline Failed. Please check logs."
        }
    }
}