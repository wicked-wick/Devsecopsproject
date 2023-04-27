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
                          git clone 'https://github.com/wicked-wick/Devsecopsproject.git
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
	     stage('Check-Git-secrets'){
		     steps {
		     sh '''
		     echo 'Checking secrets.....'
		     rm trufflehog || true
		     trufflehog --json https://github.com/wicked-wick/Devsecopsproject.git > trufflehog
		     cat trufflehog
		     '''
		     }
	     }
     }
}
                 
