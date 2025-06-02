First phase
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

Second phase
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
