## For development
To run the server and html interface locally:

docker build -t [image name]
docker run --rm -it -u root --name docker-deploy -p 8000:8000 -v $(pwd):/code -v $(pwd):/data [image name]

If no token is set, the default token is "sample-token".

To set a diferent token use:
docker run --rm -it -u root --name docker-deploy -p 8000:8000 -v $(pwd):/code -v $(pwd):/data [image name] -t [new token value]