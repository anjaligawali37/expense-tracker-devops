pipeline{
    agent any
    
    stages{
        stage("Clone Code"){
            steps{
                echo "Cloning the code"
                git url:"https://github.com/anjaligawali37/expense-tracker-devops.git", branch: "main"
            }
            
        }
        stage("build"){
            steps{
                echo "Building the image"
                sh "docker build -t expense-tracker ."
            }
            
        }
        stage("Push to Docker hub"){
            steps{
                echo "Pushing the image to Docker hub"
                withCredentials([usernamePassword(credentialsId:"dockerHub",passwordVariable:"dockerHubPass",usernameVariable:"dockerHubUser")]){
                    sh "docker tag expense-tracker ${env.dockerHubUser}/expense-tracker:latest"
                    sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}"
                    sh "docker push ${env.dockerHubUser}/expense-tracker:latest"
                }
            }
            
        }
        stage("Deploy"){
            steps{
                echo "Deploying the container"
                sh "docker compose down && docker compose up -d"
                
            }
            
        }
    }
}
