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
                          echo 'Donwloading files...'
                          git clone 'https://github.com/wicked-wick/Devsecopsproject.git
                   '''
		   }
			   sh ''' 
			   echo 'installing pip'
			   apt-get -y install python3-pip
			   cd Devsecopsproject
			   pip3 install -r requirements.txt
			   '''
	   }
	   }	   
       }
     }
}
                 
