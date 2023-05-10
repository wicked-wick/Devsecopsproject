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
      def banditExitCode = sh(returnStatus: true, script: 'bandit -r . -f txt -o result.txt')
      if (banditExitCode == 0) {
        echo 'No security issues found.'
      } else {
	echo 'Security Issues found, need to update the code.'
	sh 'cat result.txt'
	echo 'Updating the code and restarting the container'
	      sshagent(['Docker']) {
		       sh '''
		       ssh -o StrictHostKeyChecking=no ubuntu@52.66.235.57 "sudo docker start webapp && sudo docker exec webapp sh -c 'git pull' "
		       ssh -o StrictHostKeyChecking=no ubuntu@52.66.235.57 "sudo docker restart webapp "
		       '''
	      }
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
	     
	     stage('Deployment') {
		     steps {
			     script {
				     def status= sshagent(['Docker']) {
		     sh(script: "ssh -o StrictHostKeyChecking=no ubuntu@52.66.235.57 'sudo docker ps --filter name=webapp --format {{.Names}}'", returnStdout: true)
				  }
				     if (status.trim() == 'webapp') {
					     echo ' Container is already running, skipping deployment '
				     }
				     else {
					     sshagent(['Docker']){
						     sh '''
						     ssh -o StrictHostKeyChecking=no ubuntu@52.66.235.57 "sudo docker ps"
						     '''
						     echo "${status}"
					     }
				     }
			     }
		     }
	     }
}
                 
}
