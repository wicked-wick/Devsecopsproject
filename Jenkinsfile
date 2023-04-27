pipeline {

     agent any

     stages {

       stage('Checkout Project'){
	          when { 
			   expression { !fileExists('/var/lib/jenkins/workspace/Devsecops project/Devsecopsproject/BUILD_STATUS') }
		   }
           steps {
		   script{
		   if (fileExists('Devsecopsproject')) {
			   
			   sh ''' echo 'pulling files..'
			          cd Devsecopsproject && git pull 
			   '''
		   }
		   else {
			   
                  sh  '''
                          echo 'Downloading files...'
                          git clone 'https://github.com/wicked-wick/Devsecopsproject.git'
                   '''
		   }
			   sh ''' 
			   echo 'installing pip'
			   sudo apt-get -y install python3-pip
			   cd Devsecopsproject
			   pip3 install -r requirements.txt
			   echo "Build Ready" > BUILD_STATUS
			   '''
	   }
	   }	   
       }
	     stage ('Check-Git-secrets') {
		     steps {
		     sh '''
		     rm trufflehog || true
		     echo 'Checking Git Secrets....'
		     trufflehog --json https://github.com/wicked-wick/Devsecopsproject.git > trufflehog
		     cat trufflehog
		     '''
		     }
	     }
	     stage('SAST') {
		     steps {
			     sh '''
			     rm result.json || true
			     echo 'Doing Static Scanning...'
			     bandit -r . -f json -o result.json || true
			     cat result.json
			     '''
		     }
	     }
     }
}
                 
