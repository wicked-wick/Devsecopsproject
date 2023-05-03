pipeline {

     agent any

     stages {

       stage('Checkout Project'){
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
			   rm /Devsecopsproject/BUILD_STATUS || true
			   echo 'installing pip'
			   sudo apt-get -y install python3-pip
			   cd Devsecopsproject
			   pip3 install -r requirements.txt
			   echo "Build Ready" > BUILD_STATUS
			   '''
	   }
	   }	   
       }
	     stage('SAST') {
		     steps {
			     sh 'rm result.txt || true'
			      script {
      sh '''echo "Doing static Scanning"			      
         bandit -r . -f txt -o result.txt'''
      if (sh(script: 'echo $?', returnStdout: true).trim() == '0') {
        sh 'echo "No security issues found by Bandit."
      } else {
         sh '''
	 echo "Bandit security issues found. Pipeline failed."
         cat result.txt
	 '''
         error "Bandit found security issues. Pipeline failed."
      }
			      }
		     }
	     }
	     
	     stage('Software-Composition-Analysis') {
		     steps {
			     sh '''
			     rm sca.txt || true
			     echo 'Software Composition Analysis..'
			     safety check -r requirements.txt -o text > sca.txt
			     cat sca.txt
			     '''
		     }
	     }
			     
     }
}
                 
