## HAProxy-Flask
1. Docker version should be 19.03.0+</br></br>
2. Enter your subnets in .env file. Add IP addresses of the flask containers in the</br>
   haproxy/hosts file. Please use the same map in haproxy/haproxy.cfg file.</br></br>
3. If you want to run code from github or other sources in the flask container add that in the Dockerfile.</br></br>
4. To change port or other configuration edit compose.yaml file.</br></br>
5. To build the docker image of the flask container run ```docker build --tag flask:v1 .```</br>
   If you change the --tag please use the same tag in compose.yaml file.</br></br>
6. Run
   ```docker compose up -d```</br>
