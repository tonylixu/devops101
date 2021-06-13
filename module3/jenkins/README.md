## How To Install Jenkins on AWS EC2

### Patch OS and yum packages
```bash
$ yum update -y
```

### Install Jenkins
```bash
# Download Jenkins source repo
$ wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo

# Install Jenkins repo
$ rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key

# Install Jenkins
$ yum install jenkins java-1.8.0-openjdk-devel -y

# Start Jenkins process
$ systemctl daemon-reload
$ systemctl start jenkins
$ systemctl status jenkins
```

### Configure Jenkins
* Go to http://<ip>:8080
* Get initial admin password
* Install suggested plugins
* Create First admin user (admin/test1234)
