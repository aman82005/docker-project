Cat vs Dog Voting App

deploying  simple Flask + Redis web app  manually on docker where users can vote for Cats or Dogs.  
This app demonstrates using Flask for the web interface and Redis for storing votes.

##Features
- Vote for either Cats or Dogs 🐱🐶  
- Stores vote counts in Redis  
- Displays live voting results  
- Fully containerized using Docker  

##How It Works
- Flask runs a simple web interface on port `5000`.
- Votes are stored in Redis keys:  
- `cat` → number of cat votes  
- `dog` → number of dog votes
- The app connects to Redis using the `REDIS_HOST` environment variable.

## Step 1: Install Docker and Docker Compose

1.Update the server's packages and install Docker:
  - sudo yum update -y
  - sudo yum install docker docker-compose-plugin -y
2.Start the Docker service:
  -sudo service docker start
3.Add your user to the docker group. This lets you run Docker commands without typing sudo every time.
  -sudo usermod -a -G docker ec2-user

## Step 2: Create the Project Files

1.Create a directory for your project:
 -mkdir vote-app && cd vote-app
2.Create the Python application file:
 -Run nano app.py This will open a text editor. Copy and paste the Python code below into the terminal.Press Ctrl+O (Write Out), press Enter to save, and then press Ctrl+X to exit.
 -write python code
3.create dockerfile (instructions to build python image)

### Step 3: Create a Docker Network By default, containers are isolated. For our webapp and redis containers to talk to each other, they must be on the same virtual network.
 -docker network create vote-net

### Step 4: Start the Data Tier (Redis)
 -docker run -d --name redis-db --network vote-net redis:alpine

### Step 5: Build and Start the Application Tier (Python)
  This is a two-part process
  A. Build the Docker Image:
   -docker build -t vote-app .
  B. Run the Application Container:
   -docker run -d -p 8000:5000 --network vote-net -e REDIS_HOST=redis-db --name vote-app-container vote-app

  ### Step 6: Verify It Works!
Open your browser to http://localhost:8000. The voting app should load and work perfectly.
