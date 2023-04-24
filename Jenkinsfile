pipeline {

     agent any

     stages {

       stage('Checkout Project'){
           steps {
                  sh  '''
                          echo 'Donwloading files...'
                          git clone 'https://github.com/wicked-wick/Devsecopsproject.git'
                          pip3 install -r requirements.txt
                   '''
               }
              }
             }
            }
	
                 
