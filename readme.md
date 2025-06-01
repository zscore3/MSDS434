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
1. 
