First phase: initial run 
1. Load datalab csv to S3
2. Instantiate EC2 & Configure IAM role for interaction with S3
3. Start running code:
   sudo apt update
   sudo apt install python3-venv
   python3 -m venv myenv
   source myenv/bin/activate
   pip3 install s3fs pandas scikit-learn
4. Load the NaiveBayes.py script
5. Run the code

Second phase: containerized run
1. Load dockerfile, .dockerignore, and requirements.txt
2. In the EC2 which runs NaiveBayes.py, start running code:
   sudo snap install docker
   ##Only if needed - my docker builds would ignore my dockerignore file
   sudo mv snap ../
   sudo mv .cache ../
   sudo mv .ssh ../
   ##End Optional code
   sudo docker build -t my-python-app
   sudo docker run my-python-app

Third phase: Monitoring Applications
1. Fix up the security attributes of the EC2 to allow external traffic
2. Create two additional connections, i.e. via putty
3. Start installing Prometheus and Grafana, ignoring the fact that it's best practice to run monitoring applications on a separate cluster from your analytics services
4. 
