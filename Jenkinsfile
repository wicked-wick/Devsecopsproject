pipeline {

     agent any

     stages {

       stage('Checkout Project'){
           steps {
		   script{
		   if (fileExists('Devsecopsproject')) {
			   sh ' cd Devsecopsproject && git pull '
		   }
		   else {
			   
                  sh  '''
                          echo 'Donwloading files...'
                          git clone 'https://github.com/wicked-wick/Devsecopsproject.git'
			  sudo apt-get install python3-pip
                          pip3 install -r requirements.txt
                   '''
		   }
	   }
	   }	   
       }
     }
}
                 
