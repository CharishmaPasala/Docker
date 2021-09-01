# Docker 
1. To install docker in the ubunut machine:
	apt install docker docker.io docker-registry

2.  To write an image from scratch Need to have the following 4 files:
    • Dockerfile – it has the steps to build and run the docker
    • python script – It has the script to build the docker image
    • requirements.txt – file that is used to install the predefined packages.
3. To build the docker image the following is the command:
	docker build -t imageName pathdir
4. To run the docker image :
	docker run -p 8000:8000 imageName
After running the docker open the web browser and provide the in the new tab provide the following ip address:
	http://0.0.0.0:8000/
